#!../venv/bin/python3
"""sample script"""

from inference.engine import Model

en2indic_exp_dir = "../en-indic"
en2indic_model = Model(expdir=en2indic_exp_dir)

sents = ["Jai Jagannath!"]
# en2indic_model.batch_translate(sents, "en", "hi")
odia_splits = en2indic_model.batch_translate(sents, "en", "or")
response = "\n".join(odia_splits)
print(response)
