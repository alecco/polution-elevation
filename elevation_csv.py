from csv        import reader, writer
from urllib     import urlopen
from simplejson import load as jload

api_url = 'http://maps.googleapis.com/maps/api/elevation/json?locations=%s&sensor=false'

ds = ('Basurales', 'Industrias', 'Relocalizaciones',) # 'Asentamientos'

for d in ds:

    dataset_in   = './datasets/QPR - %s.csv' % d
    dataset_out  = './datasets/QPR - %s-loc.csv' % d
    elems = [x for x in reader(open(dataset_in, 'r'))] # Rows
    dout = writer(open(dataset_out, 'wb'))             # Output
    column_names = elems[0]                            # Columns
    location_idx = column_names.index('location')      # location column

    dout.writerow(column_names + ['elevation', 'resolution']) # Write columns

    # Find all elems skipping first row
    for row in elems[1:]:

        # Get location, change to google comma format
        loc = row[location_idx]
        if len(loc) < 8 or loc.find(' ') == -1:
            print ds, loc
            dout.writerow(row + ['', ''])              # No location
            continue

        location = ','.join(row[location_idx].split(' '))

        http_response = urlopen(api_url % location)
        try:
            response = jload(http_response)
        except:
            print 'loc: ', api_url % location
            print 'resp: ', http_response.read()

        if response['status'] != 'OK':
            print 'CUEC! [', d, ']'
            break
        elevation  = str(response['results'][0]['elevation'])
        resolution = str(response['results'][0]['resolution'])

        dout.writerow(row + [elevation, resolution])    # Write row

