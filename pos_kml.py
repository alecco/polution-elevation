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
   ) %(longitude, latitude)
print 'Content-Type: application/vnd.google-earth.kml+xml\n'
print kml

ds = ('Basurales', 'Industrias', 'Relocalizaciones',) # 'Asentamientos'

for d in ds:

    dataset_in   = './datasets/QPR - %s.csv' % d
    elems = [x for x in reader(open(dataset_in, 'r'))] # Rows
    column_names = elems[0]                            # Columns
    location_idx = column_names.index('location')      # location column
#ds = ('Relocalizaciones',) # 'Asentamientos'
# villa 21-24,cba-02,,-34.659268 -58.401239,CABA,840,Iguazú Nº 1835 en el ex predio de Mundo Grúa,-34.659012 -58.402306,,15-01-13,,,,6.54063367844,610.812927246
