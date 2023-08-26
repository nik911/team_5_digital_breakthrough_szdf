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
    use_auth_token=True
).to("cuda")

prompt = "a photo of an astronaut riding a horse on mars"
with autocast("cuda"):
    image = pipe(prompt)["images"][0]

image.save("astronaut_rides_horse.png")


