import simplejson
import urllib

ELEVATION_BASE_URL = 'http://maps.googleapis.com/maps/api/elevation/json'
CHART_BASE_URL = 'http://chart.apis.google.com/chart'

def getChart(chartData, chartDataScaling="-500,5000", chartType="lc",
        chartLabel="Elevation in Meters", chartSize="500x160",
        chartColor="orange", **chart_args):
    chart_args.update({
      'cht': chartType,
      'chs': chartSize,
      'chl': chartLabel,
      'chco': chartColor,
      'chds': chartDataScaling,
      'chxt': 'x,y',
      'chxr': '1,-500,5000'
    })

    dataString = 't:' + ','.join(str(x) for x in chartData)
    chart_args['chd'] = dataString.strip(',')

    chartUrl = CHART_BASE_URL + '?' + urllib.urlencode(chart_args)

    print chartUrl

    def getElevation(path="36.578581,-118.291994|36.23998,-116.83171",samples="100",sensor="false", **elvtn_args):
      elvtn_args.update({
        'path': path,
        'samples': samples,
        'sensor': sensor
      })

      url = ELEVATION_BASE_URL + '?' + urllib.urlencode(elvtn_args)
      response = simplejson.load(urllib.urlopen(url))

      # Create a dictionary for each results[] object
      elevationArray = []

      for resultset in response['results']:
        elevationArray.append(resultset['elevation'])

      # Create the chart passing the array of elevation data
      getChart(chartData=elevationArray)

if __name__ == '__main__':
    # Mt. Whitney
    startStr = "36.578581,-118.291994"
    # Death Valley
    endStr = "36.23998,-116.83171"

    pathStr = startStr + "|" + endStr

    getElevation(pathStr)

