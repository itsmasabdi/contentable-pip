# Contentable

Contentable is an end-to-end testing platform designed for large language models (LLMs). With Contentable, users can easily add testing to their LLMs to ensure performance and reliability.

## Installation

To install Contentable, simply run the following command:

```bash
pip install contentable
```

Make sure you have the following dependencies installed:

- openai
- requests

These dependencies should be handled automatically by the installation process.

## Usage

Contentable simplifies the process of adding end-to-end testing to your LLMs. To use Contentable, replace your standard OpenAI API interaction code with Contentable's interface, as shown in the examples below:

### Non-Streaming Example

Instead of using the OpenAI API directly:

```python
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
  stream=False
)
```

Use Contentable like this:

```python
import os
import contentable

contentable.api_key = os.getenv("OPENAI_API_KEY")

completion = contentable.OpenAI.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
  datasetId="your dataset id",
  conversationId="your conversation id",  # optional
  stream=False
)
```

### Streaming Example

For streaming responses, simply set the `stream` parameter to `True`:

```python
import os
import contentable

contentable.api_key = os.getenv("OPENAI_API_KEY")

streaming_completion = contentable.OpenAI.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me a joke!"}
  ],
  datasetId="your dataset id",
  conversationId="your conversation id",  # optional
  stream=True
)
```

Remember to replace `"your dataset id"` with the actual dataset ID you want to use for testing, and `"your conversation id"` (if provided) with the appropriate conversation identifier.

## Contributing

We welcome contributions from the community. If you'd like to contribute, please fork the repository and create a pull request with your changes.

## License

Contentable is released under the MIT License. See the bundled LICENSE file for details.

## Contact

If you have any questions or feedback, please contact Mas Abdi at mas@contentable.ai.