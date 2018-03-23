import requests
import urllib.parse

BASE_URL = 'http://api.dbpedia-spotlight.org/en/annotate?text={text}&confidence={confidence}&support={support}'
TEXT = 'First documented in the 13th century, Berlin was the capital of the Kingdom of Prussia (1701–1918), the German Empire (1871–1918), the Weimar Republic (1919–33) and the Third Reich (1933–45). Berlin in the 1920s was the third largest municipality in the world. After World War II, the city became divided into East Berlin -- the capital of East Germany -- and West Berlin, a West German exclave surrounded by the Berlin Wall from 1961–89. Following German reunification in 1990, the city regained its status as the capital of Germany, hosting 147 foreign embassies.'
CONFIDENCE = '0.5'
SUPPORT = '120'
REQUEST = BASE_URL.format(
    text=urllib.parse.quote_plus(TEXT), 
    confidence=CONFIDENCE, 
    support=SUPPORT
)
HEADERS = {'Accept': 'application/json'}

r = requests.get(url=REQUEST, headers=HEADERS)
response = r.json()
resources = response['Resources']

print(len(resources))
for res in resources:
    print(res['@surfaceForm'] + ' - ' + res['@URI']) 