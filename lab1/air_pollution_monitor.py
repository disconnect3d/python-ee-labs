"""Air pollution monitor."""
import sys
import requests
from BeautifulSoup import BeautifulSoup


class AirPollutionMonitor(object):
    def __init__(self, url):
        self.url = url
        self._get_page()

    def _get_page(self):
        r = requests.get(self.url)

        if r.status_code != 200:
            print "Error: can't connect to `{}` (status code: {})".format(self.url, r.status_code)
            sys.exit()

        self.html_doc = r.text

    def parse_indicators(self):
        try:
            soup = BeautifulSoup(self.html_doc)

            find_class = lambda find_in, class_name: find_in.find(**{'class': class_name})

            for indicator_name in ('current_pm10', 'current_pm25', 'current_no2', 'current_so2'):
                current_div = soup.find(id=indicator_name)

                #print current_div
                particle = find_class(current_div, 'particle_label').text
                value = find_class(current_div, 'value_label').text
                norm = current_div.find(**{'class': 'norm_label'}).text

                print "Particle:", particle
                print "Value:", value
                print "Norm:", norm, '\n'

        except Exception as e:
            print "Parse error at `{}` - {}".format(self.url, e)

apm = AirPollutionMonitor(url='http://powietrze.krakow.pl')
apm.parse_indicators()

# it seems that values are not in the 'value_label' as inspected on the page...

