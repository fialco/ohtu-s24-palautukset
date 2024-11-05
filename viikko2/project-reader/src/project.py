class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.license = license
        self.authors = authors
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def _listify(self, list):
        list_string = "\n"
        for i in list:
            list_string += "- " + i + "\n"
        return list_string
    
    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors: {self._listify(self.authors)}\n"
            f"\nDependencies: {self._listify(self.dependencies)}\n"
            f"\nDevelopment dependencies: {self._listify(self.dev_dependencies)}"
        )
