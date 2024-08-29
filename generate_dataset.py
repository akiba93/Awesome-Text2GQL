import json
from base.Schema import Schema
from base.Config import Config
import sys
import os


def generate(config, input_path, output_path):
    with open(input_path, "rb") as file:
        for line in file:
            db_id = line.decode("utf-8")
            db_id = db_id.strip()
            break
    schema_path = config.get_schema_path(db_id)
    if db_id == "common":
        schema_desc = ""
    else:
        schema = Schema(db_id, schema_path)
        schema_desc = schema.gen_desc()
    instruction_beginning = '我希望你像一个Tugraph数据库前端一样工作，你只需要返回给我cypher语句。下面是一条描述任务的指令，写一条正确的response来完成这个请求.\n"\n##Instruction:\n'
    instruction_end = "\n\n"
    instruction = instruction_beginning + schema_desc + instruction_end
    data_size = 0
    with open(input_path, "r") as file:
        data_size = sum(1 for line in file) / 2

    data_list = [
        {
            "db_id": db_id,
            "instruction": instruction,
            "input": "",
            "output": "",
            "history": [],
        }
        for i in range(int(data_size))
    ]

    with open(input_path, "rb") as file:
        for i, line in enumerate(file, start=0):
            if i != 0:
                index = i - 1
                line = line.strip()
                if index % 2 == 0:
                    data_temp = {"output": line.decode("utf-8")}
                    data_list[int(index / 2)].update(data_temp)
                else:
                    data_temp = {"input": str(line.decode("utf-8"))}
                    data_list[int(index / 2)].update(data_temp)
    json_data = json.dumps(data_list, ensure_ascii=False, indent=4)
    with open(output_path, "a") as file:
        file.write(json_data)
    print("prompt and query have been written into JSON file: ",output_path)


if __name__ == "__main__":
    current_working_directory = os.getcwd()
    config_path = "config.json"
    if len(sys.argv) > 1:
        config_path = sys.argv[1]
        config = Config(config_path)
    else:
        config = Config(config_path)

    input_path_list = config.get_input_corpus_list()
    output_path = config.get_output_corpus()

    for input_path in input_path_list:
        generate(config, input_path, output_path)