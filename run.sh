python3 run_ner.py \
  --model_name_or_path result/checkpoint-1000 \
  --dataset_name recipe_dataset.py \
  --output_dir ./result2/ \
  --do_predict \
  --overwrite_output_dir \
  --num_train_epochs 1
