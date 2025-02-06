MODEL_FLAGS="--image_size 64 --num_channels 32 --num_res_blocks 3"
DIFFUSION_FLAGS="--diffusion_steps 2000 --noise_schedule linear"

python scripts/image_sample.py --model_path xxxx $MODEL_FLAGS $DIFFUSION_FLAGS