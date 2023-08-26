# make sure you're logged in with `huggingface-cli login`
import huggingface
from openai import cli
from torch import autocast
from diffusers import StableDiffusionPipeline
from huggingface_hub import login


access_token_read = "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"
access_token_write = "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"
login(token = access_token_read)

pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    use_auth_token=False
).to("cpu")

prompt = "a photo of an astronaut riding a horse on mars"
with autocast("cpu"):
    image = pipe(prompt)["sample"][0]

image.save("astronaut_rides_horse.png")
