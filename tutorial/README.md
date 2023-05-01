## Generative AI and LLM Tutorial

<p align="center">
  <img src="https://user-images.githubusercontent.com/33823853/235499795-303e9dcb-36a2-45e7-96c5-f9b6f42557da.png" width="350" height="350">
</p>

## Table of Contents

* [Generative AI](generative_ai)
* [LLM](llm)
* [Prompt Engineering](prompt_engineering)
* [Pre-Training](pre-training)
* [Fine-Tuning](fine-tuning)
* [Useful Links](useful_links)
* [References](references)


## Generative AI
### What is Generative AI?
Generative AI (GenAI) is a type of artificial intelligence technology that can produce various types of content including text, imagery, audio and synthetic data[[1]](https://www.techtarget.com/searchenterpriseai/definition/generative-AI). Generative models learn the patterns and structure of the input data, and then generate new content that is similar to the training data but with some degree of novelty (rather than only classifying or predicting data). Generative AI can be either unimodal or multimodal; unimodal systems take only one type of input (for example, text) whereas multimodal systems can take more than one type of input (for example, text and images)[[2]](https://en.wikipedia.org/wiki/Generative_artificial_intelligence). 

The most prominent frameworks for approaching generative AI include generative adversarial networks (GANs) and generative pre-trained transformers (GPTs). GANs consist of two parts: a generator network that creates new data samples, and a discriminator network that evaluates whether the samples are real or fake. The two networks are trained together in a competitive process, with the generator network continually trying to produce better and more realistic samples, while the discriminator network tries to accurately identify the fake ones. GPTs are artificial neural networks that are based on the transformer architecture, pre-trained on large datasets of unlabelled text, and able to generate novel human-like text. They use large language models to produce data based on the training data set that was used to create them [[2]](https://en.wikipedia.org/wiki/Generative_artificial_intelligence).

### What are the applications of Generative AI?
Generative AI has many potential applications, including in creative fields such as art, music, and writing, as well as in fields such as healthcare, finance, and gaming. However, there are also concerns about the potential misuse of generative AI, such as in creating fake news or deepfakes, which can be used to deceive or manipulate people. Notable generative AI systems include ChatGPT, a chatbot built by OpenAI using their GPT-3 and GPT-4 founational large language models, and Bard, a chatbot built by Google using their LaMDA foundation model. Other generative AI models include artificial intelligence art systems such as Stable Diffusion, Midjourney, and DALL-E. Generative AI has potential applications across a wide range of industries, including software development, marketing, and fashion. Investment in generative AI surged during the early 2020s, with large companies such as Microsoft, Google, and Baidu as well as numerous smaller firms developing generative AI models [[2]](https://en.wikipedia.org/wiki/Generative_artificial_intelligence).

### How Does Generative AI Works?
Generative AI models use neural networks to identify the patterns and structures within existing data to generate new and original content. One of the breakthroughs with generative AI models is the ability to leverage different learning approaches, including unsupervised or semi-supervised learning for training. This has given organizations the ability to more easily and quickly leverage a large amount of unlabeled data to create foundation models. As the name suggests, foundation models can be used as a base for AI systems that can perform multiple tasks. 

Examples of foundation models include GPT-3 and Stable Diffusion, which allow users to leverage the power of language. For example, popular applications like ChatGPT, which draws from GPT-3, allow users to generate an essay based on a short text request. On the other hand, Stable Diffusion allows users to generate photorealistic images given a text input [[3]](https://www.nvidia.com/en-us/glossary/data-science/generative-ai/#:~:text=Generative%20AI%20models%20use%20neural,semi%2Dsupervised%20learning%20for%20training.).

### What are the capabilities of Generative AI?
The capabilities of a generative AI system depend on the modality or type of the data set used [[2]](https://en.wikipedia.org/wiki/Generative_artificial_intelligence).

**Text:** Generative AI systems trained on words or word tokens include GPT-3, LaMDA, LLaMA, BLOOM, GPT-4, and others (see List of large language models). They are capable of natural language processing, machine translation, and natural language generation and can be used as foundation models for other tasks. Data sets include BookCorpus, Wikipedia, and others (see List of text corpora).\
**Code:** In addition to natural language text, large language models can be trained on programming language text, allowing them to generate source code for new computer programs. Examples include OpenAI Codex.\
**Images:** Generative AI systems trained on sets of images with text captions include such as Imagen, DALL-E, Midjourney, Stable Diffusion and others (see Artificial intelligence art, Generative art, Synthetic media). They are commonly used for text-to-image generation and neural style transfer. Datasets include LAION-5B and others (See Datasets in computer vision).\
**Molecules:** Generative AI systems can be trained on sequences of amino acids or molecular representations such as SMILES representing DNA or proteins. These systems, such as AlphaFold, are used for protein structure prediction and drug discovery.[20] Datasets include various biological datasets.\
**Music:** Generative AI systems such as MusicLM can be trained on the audio waveforms of recorded music along with text annotations, in order to generate new musical samples based on text descriptions such as "a calming violin melody backed by a distorted guitar riff".\
**Video:** Generative AI trained on annotated video can generate temporally-coherent video clips. Examples include Gen1 by RunwayML and Make-A-Video by Meta Platforms.\
**Multimodal:** A generative AI system can be built from multiple generative models, or one model trained on multiple types of data. For example, one version of OpenAI's GPT-4 accepts both text and image inputs.\

### What are the advantages of Generative AI?
Some of the advantages of generative AI are [[4]](https://speakai.co/advantages-of-generative-ai/):

**Increased Efficiency:** Generative AI can be used to automate tasks that would otherwise require manual labor. This can help businesses save time and money, as well as increase efficiency. For example, generative AI can be used to generate images and videos quickly and accurately, which can be used in marketing campaigns or other projects.\
**Improved Quality:** Generative AI can help improve the quality of content generated. It can be used to create high-quality images and videos that are more visually appealing than those created manually. Additionally, generative AI can be used to generate text that is more accurate and relevant than text created by humans.\
**Faster Results:** Generative AI can help businesses get results faster than they would with manual labor. For example, generative AI can be used to generate images and videos in a fraction of the time it would take a human to do the same task. This can help businesses get their projects done faster and more efficiently.\
**Cost Savings:** Generative AI can help businesses save money. By automating tasks, businesses can reduce their labor costs and save money. Additionally, generative AI can help businesses reduce costs associated with creating content, such as images and videos.
**Improved Decision Making:** Generative AI can help businesses make better decisions. By using generative AI, businesses can generate data that can be used to make better decisions. For example, generative AI can be used to generate data that can be used to make decisions about marketing campaigns or product development.\
**Increased Creativity:** Generative AI can help businesses be more creative. By using generative AI, businesses can generate new ideas and concepts that can be used to create new products or services. Additionally, generative AI can be used to generate images and videos that are more visually appealing than those created manually.\
**Improved Customer Experience:** Generative AI can help businesses improve their customer experience. By using generative AI, businesses can generate content that is more accurate and relevant to their customers. This can help businesses create a better customer experience and increase customer satisfaction.

### What are the limitations of Generative AI?
Some of the advantages of generative AI are [[5]](https://fact.technology/learn/generative-ai-advantages-limitations-and-challenges/):

**Quality of Generated Outputs:** Generative AI systems may not always produce high-quality outputs, and the generated outputs may contain errors or artifacts. This can be due to a variety of factors, such as a lack of data, poor training, or an overly complex model.\
**Control Over the Generated Outputs:** Generative AI systems are typically trained on a dataset and can generate new outputs that are similar to, but not identical to, the input data. However, it can be difficult to control the specific characteristics of the generated outputs.\
**Computational Requirements:** Generative AI systems typically require large amounts of data and computational resources to train. This can be expensive and time-consuming, which can be a barrier to entry for some organizations.\
**Bias and Fairness:** Generative AI systems can inadvertently replicate biases present in the training data. This can lead to unfair or discriminatory results, particularly if the training data contains biased information.\
**Explainability and Interpretability:** Generative AI models can be complex and opaque, making it difficult to understand how they are making their predictions. This can be a challenge when trying to ensure that the model is making fair and unbiased decisions.\
**Safety and Security:** Generative AI systems can be used to generate realistic and convincing fake images, videos, and text, which can be used to spread misinformation or propaganda. This highlights the importance of developing safety and security measures to prevent the malicious use of generative AI.







## LLM

## Prompt Engineering

## Pre-Training

## Fine-Tuning

## Useful Links

[1] [Large Language Models from scratch: Part 1](https://www.youtube.com/watch?v=lnA9DMvHtfI&t=264s)\
[2] [Large Language Models: Part 2](https://www.youtube.com/watch?v=YDiSFS-yHwk&t=87s)\
[3] [5 Tips and Misconceptions about Finetuning GPT-3](https://www.youtube.com/watch?v=VfAsu_dxw0g)\
[4] [How to fine-tune GPT-3 without code](https://www.youtube.com/watch?v=VfAsu_dxw0g)\
[5] [How to Fine Tune GPT3 | Beginner's Guide to Building Businesses w/ GPT-3](https://www.youtube.com/watch?v=PB3JY89SxM0)\
[6] [GPT-3 Fine Tuning Prompts & Code](https://docs.google.com/document/d/1jJbk61grxYZV2qbBNtNnVaeEFsqMskWY5Uh6ELlqiB4/edit)\
[7] [awesome-ChatGPT|LLaMA(instruction)-dataset](https://github.com/yaodongC/awesome-instruction-dataset)\
[8] [How To Fine-Tune the Alpaca Model For Any Language | ChatGPT Alternative](https://medium.com/@martin-thissen/how-to-fine-tune-the-alpaca-model-for-any-language-chatgpt-alternative-370f63753f94))\
[9] [Prompt Engineering Guide](https://www.promptingguide.ai/)\
[10] [ChatGPT Use Cases](https://research.aimultiple.com/chatgpt-use-cases/)\
[11] [Introducing IGEL an instruction-tuned German large Language Model](https://www.philschmid.de/introducing-igel)\
[12] [Using ChatGPT for Question Answering on Your Own Data](https://medium.com/mlearning-ai/using-chatgpt-for-question-answering-on-your-own-data-afa33d82fbd0)\
[13] [ChatGPT: Beginner to Expert in 8 Minutes!](https://www.youtube.com/watch?v=pyGeTck5xRk)\
[14] [10 Question-Answering Datasets To Build Robust Chatbot Systems](https://analyticsindiamag.com/10-question-answering-datasets-to-build-robust-chatbot-systems/)\
[15] [Mastering GPT-3: A Comprehensive Guide to Fine-Tuning with OpenAI, Complete with Examples](https://medium.com/@kapildevkhatik2/mastering-gpt-3-a-comprehensive-guide-to-fine-tuning-with-openai-complete-with-examples-e28515c22d92)\
[16] [Hello Dolly: Democratizing the magic of ChatGPT with open models](https://www.databricks.com/blog/2023/03/24/hello-dolly-democratizing-magic-chatgpt-open-models.html)\
[17] [A snapshot of today's open-source LLMs space every builder should know.](https://www.linkedin.com/posts/sahar-mor_artificialintelligence-machinelearning-activity-7049789761728770049-QLsv?utm_source=share&utm_medium=member_desktop)\
[18] [GPT-4 Tutorial: How to Chat With Multiple PDF Files (~1000 pages of Tesla's 10-K Annual Reports)](https://www.youtube.com/watch?v=Ix9WIZpArm0)\
[19] [AWS, Surge, Scale, Self-instruct Instruction Dataset](https://huggingface.co/spaces/HuggingFaceH4/SSS)\
[20] [New Scaling Laws for Large Language Models](https://www.lesswrong.com/posts/midXmMb2Xg37F2Kgn/new-scaling-laws-for-large-language-models)\
[21] [Getting started with LangChain — A powerful tool for working with Large Language Models](https://medium.com/@avra42/getting-started-with-langchain-a-powerful-tool-for-working-with-large-language-models-286419ba0842)\
[22] [AI talks: ChatGPT assistant via Streamlit](https://blog.streamlit.io/ai-talks-chatgpt-assistant-via-streamlit/))\
[23] [Meet MiniGPT-4: An Open-Source AI Model That Performs Complex Vision-Language Tasks Like GPT-4](https://www.linkedin.com/posts/asifrazzaq_gpt4-ai-largelanguagemodels-ugcPost-7054175482832949248-qQGh)\
[24] [How to train your own Large Language Models](https://blog.replit.com/llm-training)\
[25] [Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374)\
[26] [Train and Deploy BLOOM with Amazon SageMaker and PEFT](https://www.philschmid.de/bloom-sagemaker-peft)\
[27] [Tools of the AI engineer](https://www.linkedin.com/posts/mikkolehtimaki_github-softlandia-ltdapplied-ai-engineering-activity-7055259676703109120-9WVc/?utm_source=share&utm_medium=member_android)\
[28] [MiniGPT-4: Enhancing Vision-language Understanding with Advanced Large Language Models](https://github.com/Vision-CAIR/MiniGPT-4)\
[29] [LangChain Chat](https://blog.langchain.dev/langchain-chat/)\
[30] [PEFT: Parameter-Efficient Fine-Tuning of Billion-Scale Models on Low-Resource Hardware](https://huggingface.co/blog/peft)\
[31] [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)\
[32] [PEFT LoRA Explained in Detail - Fine-Tune your LLM on your local GPU](https://www.youtube.com/watch?v=YVU5wAA6Txo)\
[33] [Finetuning Large Language Models](https://magazine.sebastianraschka.com/p/finetuning-large-language-models)\
[34] [The ALPACA Code explained: Self-instruct fine-tuning of LLMs](https://www.youtube.com/watch?v=jQL0ZeHtXFc)\
[35] [A brief history of LLaMA models](https://agi-sphere.com/llama-models/)


## References
[1] [What is generative AI? Everything you need to know](https://www.techtarget.com/searchenterpriseai/definition/generative-AI)\
[2] [Generative artificial intelligence](https://en.wikipedia.org/wiki/Generative_artificial_intelligence)\
[3] [What is Generative AI?](https://www.nvidia.com/en-us/glossary/data-science/generative-ai/#:~:text=Generative%20AI%20models%20use%20neural,semi%2Dsupervised%20learning%20for%20training.)\
[4] [Advantages Of Generative AI](https://speakai.co/advantages-of-generative-ai/)\
[5] [Generative AI: Advantages, Disadvantages, Limitations, and Challenges](https://fact.technology/learn/generative-ai-advantages-limitations-and-challenges/)\





