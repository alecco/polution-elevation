from csv        import reader

# Print header
print '<?xml version="1.0" encoding="UTF-8"?>'
print '<kml xmlns="http://www.opengis.net/kml/2.2">'

placemark = (
   '<Placemark>\n'
   '    <name>%s</name>\n'
   '    <Point>\n'
   '        <coordinates>%d,%d</coordinates>\n'
   '    </Point>\n'
   '</Placemark>\n'
   )

print 'Content-Type: application/vnd.google-earth.kml+xml\n'

#
ds = (('Basurales', 'denaminacion'), ('Industrias', 'razon_social'),
        ('Relocalizaciones', 'asentamiento')) # 'Asentamientos'

for fname, name in ds:

    dataset_in   = './datasets/QPR - %s-loc.csv' % fname
    elems = [x for x in reader(open(dataset_in, 'r'))] # Rows
    column_names = elems[0]                            # Columns
    location_idx = column_names.index('location')      # location column
    elevation_idx = column_names.index('elevation')    # elevation column

    # Find all elems skipping first row
    for row in elems[1:]:

        # Get location, change to google comma format
        loc = row[location_idx]
        elevation = row[elevation_idx]
        if len(loc) < 8 or loc.find(' ') == -1:
            continue # Skip

        print placemark % (loc)

#ds = ('Relocalizaciones',) # 'Asentamientos'

print '</kml>' # Print end

