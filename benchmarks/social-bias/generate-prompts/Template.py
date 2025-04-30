from langchain.prompts import PromptTemplate

class Template:
    # def __init__(self, foldername, filename):
    def __init__(self, file_path):
        # self.filename = filename
        # self.foldername = foldername
        self.file_path = file_path
        # an object made when calling this class is a template that can be filled in (filled in template = prompt)
        self.template = self.load_template()

    def load_template(self):
        #open txt file
        with open(self.file_path) as template:
            contents = template.read()
        # with open('templates/{}/{}'.format(self.foldername,self.filename)) as template:
        #     contents = template.read()

        #make it a template
        template = PromptTemplate(
            template=contents,
            input_variables=["voornaam", "baan", "geslacht", "herkomst"]
        )
        return template

    def fill_in_template(self, herkomst = None, naam=None, baan=None, geslacht=None, voornaam=None):
        # a prompt is a filled in template
        prompt = self.template.format(naam=naam, baan=baan, geslacht=geslacht, herkomst=herkomst, voornaam=voornaam)

        return prompt
