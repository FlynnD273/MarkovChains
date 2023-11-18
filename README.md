# Markov Chains

This is a simple script to generate Markov chains from Discord messages. To get the data for it, use [Discord Chat Exporter](https://github.com/Tyrrrz/DiscordChatExporter/tree/master) to export messages to JSON files. Put the JSON files in a folder, and run `python createModel.py -p <path/to/json/files> -o <path/to/export/model/to>`

To generate text from the model, run `python runModel.py "starting text"`
