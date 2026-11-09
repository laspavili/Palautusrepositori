import toml
from urllib import request
from project import Project



class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")


        parsetoml = toml.loads(content)

        tiedot = parsetoml["project"]
        tiedot2 = parsetoml["dependency-groups"]
        parse_authors = parsetoml["project"]["authors"]

        name = tiedot["name"]
        description = tiedot["description"]
        lisenssi = tiedot["license"]

        authors = []
        for author in parse_authors:
            authors.append(author["name"])

        riippuvuudet = tiedot["dependencies"]
        kehitys_riippuvuudet = tiedot2["dev"]
        



        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, lisenssi, authors, riippuvuudet, kehitys_riippuvuudet)
