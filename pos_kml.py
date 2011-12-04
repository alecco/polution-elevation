from csv        import reader

kml = (
   '<?xml version="1.0" encoding="UTF-8"?>\n'
   '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
   '<Placemark>\n'
   '<name>Random Placemark</name>\n'
   '<Point>\n'
   '<coordinates>%d,%d</coordinates>\n'
   '</Point>\n'
   '</Placemark>\n'
   '</kml>'
   )
print 'Content-Type: application/vnd.google-earth.kml+xml\n'
print kml

ds = ('Basurales', 'Industrias', 'Relocalizaciones',) # 'Asentamientos'

for d in ds:

    dataset_in   = './datasets/QPR - %s.csv' % d
    elems = [x for x in reader(open(dataset_in, 'r'))] # Rows
    column_names = elems[0]                            # Columns
    location_idx = column_names.index('location')      # location column
    # Find all elems skipping first row
    for row in elems[1:]:

        # Get location, change to google comma format
        loc = row[location_idx]

#ds = ('Relocalizaciones',) # 'Asentamientos'
