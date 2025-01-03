#!/bin/bash

MODE=200
INPUT_DIR_OR_FILE='./input_examples/corpus.txt'
OUTPUT_DIR="./output"
SUFFIX='_general_directly'
#For online model service calling
MODEL_PATH=''
#For local model calling
#Using relative model path or HuggingFace model id
#MODEL_PATH='../Qwen/Qwen2.5-Coder-7B-Instruct'

echo "----------------Running generalize_llm.py to GENERAL_PROMPT_DIRECTLY----------------"
python3 generalize_llm.py "$MODE" "$INPUT_DIR_OR_FILE" "$OUTPUT_DIR" "$SUFFIX" "$MODEL_PATH"
