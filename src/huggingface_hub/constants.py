import os


# Possible values for env variables

ENV_VARS_TRUE_VALUES = {"1", "ON", "YES", "TRUE"}
ENV_VARS_TRUE_AND_AUTO_VALUES = ENV_VARS_TRUE_VALUES.union({"AUTO"})

# Constants for file downloads

PYTORCH_WEIGHTS_NAME = "pytorch_model.bin"
TF2_WEIGHTS_NAME = "tf_model.h5"
TF_WEIGHTS_NAME = "model.ckpt"
TF_SAVED_MODEL_NAME = "saved_model"
FLAX_WEIGHTS_NAME = "flax_model.msgpack"
CONFIG_NAME = "config.json"

HUGGINGFACE_CO_URL_HOME = "https://huggingface.co/"

HUGGINGFACE_CO_URL_TEMPLATE = (
    "https://huggingface.co/{repo_id}/resolve/{revision}/{filename}"
)

REPO_TYPE_DATASET = "dataset"
REPO_TYPE_SPACE = "space"
REPO_TYPES = [None, REPO_TYPE_DATASET, REPO_TYPE_SPACE]

REPO_TYPES_URL_PREFIXES = {
    REPO_TYPE_DATASET: "datasets/",
    REPO_TYPE_SPACE: "spaces/",
}


# default cache
hf_cache_home = os.path.expanduser(
    os.getenv(
        "HF_HOME", os.path.join(os.getenv("XDG_CACHE_HOME", "~/.cache"), "huggingface")
    )
)
default_cache_path = os.path.join(hf_cache_home, "hub")

HUGGINGFACE_HUB_CACHE = os.getenv("HUGGINGFACE_HUB_CACHE", default_cache_path)

HF_HUB_OFFLINE = os.environ.get("HF_HUB_OFFLINE", "AUTO").upper()
if HF_HUB_OFFLINE in ENV_VARS_TRUE_VALUES:
    HF_HUB_OFFLINE = True
else:
    HF_HUB_OFFLINE = False
