import pandas as pd

from Template import Template


def make_prompts():
    # gender_origin
    dataset = pd.read_excel('generate-prompts/experiments_data/prompts/empty_dataframe.xlsx')
    herkomstlanden = ['Nederlandse', 'Marokkaanse', 'Turkse', 'Surinaamse']
    geslachten = ['vrouw', 'man', 'non-binaire persoon']
    voornaam = 0
    for geslacht in geslachten:
        for herkomstland in herkomstlanden:
            df_beroepen = pd.read_excel('generate-prompts/experiments_data/data/beroepen/gender_origin.xlsx')
            for i in range(len(df_beroepen)):
                # print(df_beroepen.loc[i, 'beroep'])
                for task in ['yes_no', 'accept_reject']:
                    for version in ['neutral_v1', 'neutral_v2']:
                        # print(version)
                        for variation in ['base.txt', 'linebreak.txt', 'placeholder.txt']:
                            # gender origin
                            file_path = 'generate-prompts/experiments_data/templates/{}/{}/{}/{}'.format('gender_origin', task, version,
                                                                                         variation)
                            current_template = Template(file_path)
                            prompt = current_template.fill_in_template(baan=df_beroepen.loc[i, 'beroep'].lower(),
                                                                       geslacht=geslacht, herkomst=herkomstland)

                            row = {
                                'taak': task,
                                'geslacht': geslacht,
                                'herkomstland': herkomstland,
                                'voornaam': voornaam,
                                'beroep': df_beroepen.loc[i, 'beroep'].lower(),
                                'level': df_beroepen.loc[i, 'level'],
                                'beroepsklasse': df_beroepen.loc[i, 'beroepsklasse'],
                                'neutrale versie': version,
                                'variatie': variation,
                                'prompt': prompt,
                                'reactie': 0,
                                'classificatie': 0,
                            }
                            dataset.loc[len(dataset)] = row

    # first_name
    df_namen = pd.read_excel('generate-prompts/experiments_data/data/namen.xlsx')
    for j in range(len(df_namen)):
        df_beroepen = pd.read_excel('generate-prompts/experiments_data/data/beroepen/first_name.xlsx')
        for i in range(len(df_beroepen)):
            for task in ['yes_no', 'accept_reject']:
                for version in ['neutral_v1', 'neutral_v2']:
                    for variation in ['base.txt', 'linebreak.txt', 'placeholder.txt']:
                        # first name
                        file_path = 'generate-prompts/experiments_data/templates/{}/{}/{}/{}'.format('first_name', task, version,
                                                                                     variation)
                        current_template = Template(file_path)
                        prompt = current_template.fill_in_template(baan=df_beroepen.loc[i, 'beroep'].lower(),
                                                                   voornaam=df_namen.loc[j, 'voornaam'])
                        row = {
                            'taak': task,
                            'geslacht': df_namen.loc[j, 'geslacht'],
                            'herkomstland': df_namen.loc[j, 'herkomstland'],
                            'voornaam': df_namen.loc[j, 'voornaam'],
                            'beroep': df_beroepen.loc[i, 'beroep'].lower(),
                            'level': df_beroepen.loc[i, 'level'],
                            'beroepsklasse': df_beroepen.loc[i, 'beroepsklasse'],
                            'neutrale versie': version,
                            'variatie': variation,
                            'prompt': prompt,
                            'reactie': 0,
                            'classificatie': 0,
                        }
                        dataset.loc[len(dataset)] = row

    # makes a excel file of the dataframe
    dataset.to_excel('generate-prompts/experiments_data/prompts/filled_dataframe.xlsx', index=False)


if __name__ == '__main__':
    make_prompts()
