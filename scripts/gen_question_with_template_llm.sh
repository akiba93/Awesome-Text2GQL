#!/bin/bash

MODE=400
INPUT_DIR_OR_FILE='./input_examples/gen_question_llm.txt'
OUTPUT_DIR="./output"
SUFFIX='_t'
MODEL_PATH='../Qwen__Qwen2.5-Coder-14B-Instruct'

echo "----------------Running generalize_llm.py to GEN_PROMPT_WITH_TEMPLATE----------------"
python3 generalize_llm.py "$MODE" "$INPUT_DIR_OR_FILE" "$OUTPUT_DIR" "$SUFFIX" "$MODEL_PATH"
