import pandas as pd
import sys
import time
import os

script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# os.environ['HF_HOME'] = '{}/hug_models'.format(script_dir)
# os.environ['HF_HUB_OFFLINE'] = '1'
from transformers import pipeline


def run_experiment(start_range, end_range, model, prompt_csv):
    start_time = time.time()
    pipe = pipeline("text-generation", model=model, max_new_tokens=500, temperature=0.001, do_sample=True, device=0)

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
        prompt = subset_index_res.loc[i, 'prompt']

        messages = [
            {"role": "user", "content": prompt},
        ]
        total_response = pipe(messages)
        response_llm = total_response[0]["generated_text"][1]["content"]
        # save response in dataframe
        subset_index_res.loc[i, 'reactie'] = response_llm

        # save dataframe every 150 responses
        if i % 150 == 0:
            subset_index_res.to_csv(
                '{}/reactions/{}_{}_{}_{}_during.csv'.format(script_dir, model_save, prompts_save, start_range,
                                                             end_range), sep='\t', index=False)

    subset_index_res.to_csv(
        '{}/reactions/{}_{}_{}_{}.csv'.format(script_dir, model_save, prompts_save, start_range, end_range), sep='\t',
        index=False)
    print('Time needed is {}'.format(time.time() - start_time))


if __name__ == "__main__":
    sys_start_range = int(sys.argv[1])
    sys_end_range = int(sys.argv[2])
    sys_model = str(sys.argv[3])
    sys_prompt_csv = str(sys.argv[4])
    run_experiment(start_range=sys_start_range, end_range=sys_end_range, model=sys_model, prompt_csv=sys_prompt_csv)
