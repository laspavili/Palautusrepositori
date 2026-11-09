class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        lista = []
        for sana in dependencies:
            siivottu = "".join(kirjain for kirjain in sana if kirjain.isalpha())
            lista.append(siivottu)

        return "\n-".join(lista)
        
    
    def _authors_siistitty(self, authors):
        return "\n-".join(authors)

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense:\n-{self.license or '-'}\n"
            f"\nAuthors:\n-{self._authors_siistitty(self.authors)}\n"
            f"\nDependencies:\n-{self._stringify_dependencies(self.dependencies)}\n"
            f"\nDevelopment dependencies:\n-{self._stringify_dependencies(self.dev_dependencies)}"
        )
