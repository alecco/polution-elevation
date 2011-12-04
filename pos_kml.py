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

location_idx_a  = column_names_a.index('location')      # location column
elevation_idx_a = column_names_a.index('elevation')    # elevation column
name_idx_a      = column_names_a.index(name)           # pos name

for fname, name in ds:
    def km_dist(lat1, long1, lat2, long2):
        loc       = row[location_idx]
        elevation = row[elevation_idx]
        name      = row[name_idx]
    pass

ofile.write('</kml>')

