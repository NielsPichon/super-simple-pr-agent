# super-simple-pr-agent
A super simple PR review bot, inspired by Codium PR-agent.


To use locally

```
pip install -e .

sspr --diff diff_text_file.txt --out review.md
```

Otherwise you can use the github action.

Review parameters can be set using environment variables. Check sspr/conf.py:Config  to see the available parameters. They can be overwrittent by setting the name of the parameter in all uppercase as a parameter:

* `MODEL`: model to use
* `PROVIDER`: model api provider (`openai` or `ollama`)
* `API_BASE_URL`: ollama api base url with no ending `/`
* `API_KEY`: openai api auth key
* `GITHUB_TOKEN`: github auth token if using the github action
* `GITHUB_EVENT_NAME`: github event name if using the github action.
* `GITHUB_EVENT_PATH`: github event name if using the github action.
* `LOG_LEVEL`: log level. 'DEBUG', 'INFO', 'WARNING', 'ERROR'
* `MAX_MODEL_TOKENS`: Max number of tokens the model supports. Currently does nothing but ultimately will be used to split the diff.


**TODO**
* add automatic GitHub diff pull and comment publishing
* add diff split if too long
