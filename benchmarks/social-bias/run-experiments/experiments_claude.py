import pandas as pd
import sys
import os
import anthropic
import time


def run_experiment(start_range, end_range, model, prompt_csv):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    start_time = time.time()

    # call the client
    client = anthropic.Anthropic()

    # load csv file (tsv)
    dataframe = pd.read_csv('{}/prompts/{}'.format(script_dir, prompt_csv), sep='\t')

    # change name for saving
    model_save = model.replace('/', '_')
    prompts_save = prompt_csv.replace('.csv', '')

    subset = dataframe.loc[start_range:end_range]
    subset_index_res = subset.reset_index(drop=True)
    # set to None otherwise it might generate errors
    subset_index_res['reactie'] = None

    for i in range(len(subset_index_res)):
        prompt = subset_index_res.loc[i,'prompt']
        # make a message
        message = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=500,
            temperature=0.0,
            system="You are a helpful assistant.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ]
        )
        response_llm = message.content[0].text
        #save response in dataframe
        subset_index_res.loc[i,'reactie'] = response_llm

        #save dataframe every 150 responses
        if i % 150 == 0:
            subset_index_res.to_csv('{}/reactions/{}_{}_{}_{}_during.csv'.format(script_dir, model_save, prompts_save, start_range, end_range), sep='\t', index=False)

    subset_index_res.to_csv('{}/reactions/{}_{}_{}_{}.csv'.format(script_dir, model_save, prompts_save, start_range, end_range), sep ='\t', index=False)
    print('Time needed is {}'.format(time.time() - start_time))


if __name__ == "__main__":
    sys_start_range = int(sys.argv[1])
    sys_end_range = int(sys.argv[2])
    sys_model = str(sys.argv[3])
    sys_prompt_csv = str(sys.argv[4])
    run_experiment(start_range=sys_start_range, end_range=sys_end_range, model=sys_model, prompt_csv=sys_prompt_csv)
