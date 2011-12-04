from csv   import reader
from dist  import km_dist

ofile = open('datasets/places.kml', 'w')

# Print header
ofile.write('<?xml version="1.0" encoding="UTF-8"?>')
ofile.write('<kml xmlns="http://www.opengis.net/kml/2.2">')

placemark = (
   '<Placemark>\n'
   '    <name>%s</name>\n'
   '    <description>%s</description>\n'
   '    <Point>\n'
   '        <coordinates>%s</coordinates>\n'
   '    </Point>\n'
   '</Placemark>\n'
   )

ofile.write('Content-Type: application/vnd.google-earth.kml+xml\n')

#
ds = (('Basurales', 'denominacion'), ('Industrias', 'razon_social'),
        ('Relocalizaciones', 'asentamiento')) # 'Asentamientos'

for fname, name in ds:

    dataset_in   = './datasets/QPR - %s-loc.csv' % fname
    elems = [x for x in reader(open(dataset_in, 'r'))] # Rows
    column_names = elems[0]                            # Columns
    location_idx = column_names.index('location')      # location column
    elevation_idx = column_names.index('elevation')    # elevation column
    name_idx      = column_names.index(name)           # pos name

    # Find all elems skipping first row
    for row in elems[1:]:

        # Get location, change to google comma format
        loc       = row[location_idx]
        elevation = row[elevation_idx]
        name      = row[name_idx]

        if len(loc) < 8 or loc.find(' ') == -1:
            continue # Skip missing data

        loc = ','.join(loc.split(' '))

        ofile.write(placemark % (name, fname, loc))

#ds = ('Relocalizaciones',) # 'Asentamientos'

#
# Now process risky relations
#

ds = ('Basurales', 'Industrias', 'Relocalizaciones') # Again...
places = []

# Process relations
asentamientos   = './datasets/QPR - Relocalizaciones-loc.csv'
basurales       = './datasets/QPR - Basurales-loc.csv'
industrias      = './datasets/QPR - Industrias-loc.csv'
elems_a = [x for x in reader(open(asentamientos, 'r'))] # Rows
elems_b = [x for x in reader(open(basurales, 'r'))] # Rows
elems_i = [x for x in reader(open(industrias, 'r'))] # Rows
column_names_a = elems_a[0]  # Columns
column_names_b = elems_b[0]  # Columns
column_names_i = elems_i[0]  # Columns


# For all asentamientos find relations within 5km
# skip header
column_names_a    = elems_a[0]   # Columns
location_idx_a    = column_names_a.index('location')      # location column
elevation_idx_a   = column_names_a.index('elevation')    # elevation column
name_idx_a        = column_names_a.index('asentamiento')           # pos name

location_idx_b    = column_names_b.index('location')     # location column
elevation_idx_b   = column_names_b.index('elevation')    # elevation column
name_idx_b        = column_names_b.index('denominacion') # pos name

location_idx_i    = column_names_i.index('location')     # location column
elevation_idx_i   = column_names_i.index('elevation')    # elevation column
name_idx_i        = column_names_i.index('razon_social') # pos name

riesgo_basura     = [] # risk relations indexed
riesgo_industrias = [] # risk relations indexed

for i in range(1, len(elems_a[1:])):

    row_a       = elems_a[i]
    loc_a       = row_a[location_idx_a]
    elevation_a = row_a[elevation_idx_a]
    name_a      = row_a[name_idx_a]

    if len(loc_a) < 8 or loc_a.find(' ') == -1:
        continue # Skip missing data

    lat_a, lon_a = loc_a.split(' ')

    print 'Asentamiento: ', name_a

    for j in range(1, len(elems_b[1:])):
        # Compare with basurales

        row_b       = elems_b[j]
        loc_b       = row_b[location_idx_b]
        elevation_b = row_b[elevation_idx_b]
        name_b      = row_b[name_idx_b]

        if len(loc_b) < 8 or loc_b.find(' ') == -1:
            continue # Skip missing data (basurales...)

        lat_b, lon_b = loc_b.split(' ')

        distance_km = km_dist(float(lat_a), float(lon_a), float(lat_b),
                float(lon_b))

        distance_m = int(distance_km * 1000) # meters

        if distance_m < 2000:
            elevation_dif = int(float(elevation_b) - float(elevation_a))
            if elevation_dif + 1 > 0:
                riesgo_basura.append((i, j, distance_m, elevation_dif))
                print '    basura riesgo: ', riesgo_basura[-1]

    for j in range(1, len(elems_i[1:])):
        # Compare with basurales

        row_i       = elems_i[j]
        loc_i       = row_i[location_idx_i]
        elevation_i = row_i[elevation_idx_i]
        name_i      = row_i[name_idx_i]

        if len(loc_i) < 8 or loc_i.find(' ') == -1:
            continue # Skip missing data (basurales...)

        lat_i, lon_i = loc_i.split(' ')

        distance_km = km_dist(float(lat_a), float(lon_a), float(lat_i),
                float(lon_i))

        distance_m = int(distance_km * 1000) # meters

        if distance_m < 2000:
            elevation_dif = int(float(elevation_i) - float(elevation_a))
            if elevation_dif + 1 > 0:
                riesgo_industrias.append((i, j, distance_m, elevation_dif))
                print '    industria riesgo: ', riesgo_industrias[-1]

ofile.write('</kml>')
