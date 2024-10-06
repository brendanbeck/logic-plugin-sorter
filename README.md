# logic-scripter-cc-controller

### Overview
This is a quick Python script I whipped up which automatically sorts your audio units in Logic Pro according to categories you provide. This is done by simply asking ChatGPT what category best describes a given plugin.

No manual intervention inside Logic's Plug-In Manager is required; this is done by reading from your audio units' plist metadata and writing directly to Logic Pro's Plug-In Manager tagging settings located in `user/Music/Audio Music Apps/Databases/Tags/`. 

![Screenshot 2024-10-06 at 3 05 14 PM](https://github.com/user-attachments/assets/24a3352d-5ba5-4728-ab53-4e855a30251a)
![Screenshot 2024-10-06 at 3 04 40 PM](https://github.com/user-attachments/assets/85953443-a68b-4d9d-b410-24afd4a2a66a)

### Limitations
- Requires the use of OpenAI's API which is not free. However, be rest assured that this script uses very little tokens in the request and response. By sorting 1000+ plugins on my Mac, I used a couple of cents worth of credits at most. 
  - I did consider to have OpenAI sort the plugins in an entire batch to save tokens, but this introduces more possibility for error on the response. The cost is negligible, especially considering the risk of giving a malformed response.
  - At the time of creating this, I did try open source LLMs that could be embedded (such as Meta's Llama 3.2), but unfortunately they did not perform well on the responses unless the audio unit in question was very widely known. Even then, it even misclassified some Native Instruments audio units. With OpenAI's `gpt-4o` model, it was correctly classifying virtually all plugins.
- Audio units which are very new or not known have a chance of being misclassified (although this possibility is very, very small with `gpt-4o` in my experience).
- Audio units whose `.plist` file that does not define `<AudioComponents>` cannot be sorted; At this time I have no way of deriving the tagset title of an audio unit (at least, not a simple way that does not require other languages) without this information.
  - Of the 1000+ audio units I have installed, only eight of them did not have this defined.
- Plugins provided by Apple (whether the manufacturer is labeled "Apple" or "Logic") are not handled by this script. I'm not sure where to find `plist` information for these plugins (or if you even can).
  - In theory you could make a dictionary of the known tagsets for these plugins and then include these in the script, but that requires a lot of manual work and its unknown to me if the tagset titles change over time.
    - E.g., move an Apple-provided plugin into a category in Logic's Plug-In Manager. The tagset file that is most recently modified in `user/Music/Audio Music Apps/Databases/Tags/` corresponds to that plugin.

### Setup

#### Requirements
1. Logic Pro
2. Some third party audio units installed
3. A ChatGPT API key
4. Python 3.12

#### Run Procedure
1. Install the requirements given in `requirements.txt` using pip. (E.g., `pip install -r /path/to/requirements.txt`)
2. Set your ChatGPT API key as an environment variable to `OPENAI_API_KEY`.
3. Change the settings in `config.json`. Ideally you will just need to change the `tags_directory` path and then provide your categories as an array of strings in `categories`.
4. Ensure that Logic Pro is not running
5. Execute the script (`python LogicPluginSorter.py`)

Before making any changes, the script will create a backup copy of your current `Tags` folder in the case that something goes wrong at `./backup`. Application logs and sorting results will be written to a log file in `./logs`.


