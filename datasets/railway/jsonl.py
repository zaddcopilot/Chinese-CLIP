# -*- coding: utf-8 -*-
import json

def replace_fullwidth_commas_and_convert_to_jsonl(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    with open(output_file, 'w', encoding='utf-8') as file:
        for line in lines:
            # Replace fullwidth commas with halfwidth commas
            processed_line = line.replace('，', ',')
            print(processed_line)
            json_line =json.dumps(processed_line.strip(), ensure_ascii=False)
            
            # Write the JSON object as a line to the output file
            file.write(json_line + '\n')
    

# Usage
input_file = 'ori.txt'  
output_file = 'output.jsonl'
replace_fullwidth_commas_and_convert_to_jsonl(input_file, output_file)
