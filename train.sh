MODEL_FLAGS="--image_size 128 --num_channels 32 --num_res_blocks 3"
DIFFUSION_FLAGS="--diffusion_steps 2000 --noise_schedule linear"
TRAIN_FLAGS="--lr 1e-4 --batch_size 100"

python scripts/image_train.py --data_dir xxxx $MODEL_FLAGS $DIFFUSION_FLAGS $TRAIN_FLAGS