from csv        import reader

ds = ('Basurales', 'Industrias', 'Relocalizaciones',) # 'Asentamientos'

# Print header
print '<?xml version="1.0" encoding="UTF-8"?>\n'
print '<kml xmlns="http://www.opengis.net/kml/2.2">\n'

placemark = (
   '<Placemark>\n'
   '    <name>%s</name>\n'
   '    <Point>\n'
   '        <coordinates>%d,%d</coordinates>\n'
   '    </Point>\n'
   '</Placemark>\n'
   )

print 'Content-Type: application/vnd.google-earth.kml+xml\n'

for d in ds:

    dataset_in   = './datasets/QPR - %s-loc.csv' % d
    elems = [x for x in reader(open(dataset_in, 'r'))] # Rows
    column_names = elems[0]                            # Columns
    location_idx = column_names.index('location')      # location column
    elevation_idx = column_names.index('elevation')    # elevation column

    # Find all elems skipping first row
    for row in elems[1:]:

        # Get location, change to google comma format
        loc = row[location_idx]
        print placemark % (loc)

#ds = ('Relocalizaciones',) # 'Asentamientos'

print '</kml>' # Print end

