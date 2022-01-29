from SPARQLWrapper import SPARQLWrapper, JSON
import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

class Guru:
    def __init__(self, endpoint: str = 'https://query.wikidata.org/sparql'):
        self.endpoint = endpoint

    def ask(self, question: str):

        query = ""
        if question == 'how old is Tony Blair':
            query = """
                        SELECT ?subj 
                        WHERE {
                            wd:Q9545 wdt:P569 ?subj . 
                        }
                    """
            sparql = SPARQLWrapper(self.endpoint)

            sparql.setQuery(query)
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()

            result = results["results"]["bindings"][0]
            age = relativedelta(datetime.datetime.today(), parse(result["subj"]["value"]).replace(tzinfo=None)).years
            return str(age)

        if question == 'how old is trump':
            query = """
                        SELECT ?subj 
                        WHERE {
                            wd:Q22686 wdt:P569 ?subj . 
                        }
                    """
            sparql = SPARQLWrapper(self.endpoint)

            sparql.setQuery(query)
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()

            result = results["results"]["bindings"][0]
            age = relativedelta(datetime.datetime.today(), parse(result["subj"]["value"]).replace(tzinfo=None)).years
            return str(age)

        if question == 'what is the population of London':
            query = """
                        SELECT ?subj 
                        WHERE {
                            wd:Q84 wdt:P1082 ?subj . 
                        }
                    """
            sparql = SPARQLWrapper(self.endpoint)

            sparql.setQuery(query)
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()

            result = results["results"]["bindings"][0]
            return str(result["subj"]["value"])


        if question == 'what is the population of Paris':
            query = """
                        SELECT ?subj 
                        WHERE {
                            wd:Q90 wdt:P1082 ?subj . 
                        }
                    """
            sparql = SPARQLWrapper(self.endpoint)

            sparql.setQuery(query)
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()

            result = results["results"]["bindings"][0]
            return str(result["subj"]["value"])

        
            



if __name__ == '__main__':

    print("------------------------")
    guru: Guru = Guru()
    res = guru.ask('how old is Tony Blair')
    print(res)
