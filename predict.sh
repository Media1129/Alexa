python3 run_predict.py \
  --model_name_or_path bert-base-uncased \
  --dataset_name recipe_dataset.py \
  --output_dir ./result2/ \
  --do_train \
  --do_predict \
  --overwrite_output_dir \
  --num_train_epochs 1
