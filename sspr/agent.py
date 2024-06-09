import os
from typing import Dict

from loguru import logger
import litellm
import mdformat

from sspr import config
from sspr import prompt


def get_llm_call_options() -> Dict[str, str]:
    """Prepares the options dict for the LLM call from the global config."""
    global_config = config.get_config()
    options = {
        "model": (global_config.model if global_config.provider == 'openai'
                  else f'{global_config.provider}/{global_config.model}'),
    }
    if global_config.provider == 'openai':
        os.environ["OPENAI_API_KEY"] = global_config.api_key
    if global_config.provider == 'ollama':
        options['api_base'] = global_config.api_base_url
        if global_config.api_base_url.endswith('/'):
            logger.warning('API base URL should probably not end with a '
                           'slash ("/"). Consider removing it if you get '
                           'connection errors')

    return options


def parse_response(response: str) -> str:
    """Parses the response from the LLM API."""
    response = response.split('<review>')[1].split('</review>')[0]
    try:
        return mdformat.text(response)
    except Exception as e:
        logger.warning("Could not aply markdown formatting. Response might be "
                       f"invalid markdown: {e}")
        return response


def get_review(diff: str) -> str:
    """Get the review from the diff."""
    messages = [{"role": "system:", "content": prompt.load_prompt()},
                {"role": "user:", "content": diff}]
    logger.debug(f"Prompt: {messages}")

    try:
        logger.info('Calling LLM API...')
        response = litellm.completion(
            messages=messages,
            stream=True,
            **get_llm_call_options()
        )
        for message in response:
            print(message)
    #         text_response = message['choices'][0]['message']['content']
    #     logger.info(f"Raw response: {text_response}")
    #     return parse_response(text_response)
    except Exception as e:
        logger.error(f"Error in LLM call: {e}")
        raise e
