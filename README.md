# scrape_yt
**This is a simple Youtube video and playlist downloader.**

## Installation
* run ``` git clone https://github.com/pranayteaches/scrape_yt ```
* than run ``` cd scrape_yt ```
* check whether setuptools and wheel are installed ``` python -m pip install --upgrade pip setuptools wheel ```
* Just run the setup.py by ``` pip install --user scrape_yt ```
* Cngratulations your youtube video downloader is installed.

## Checking
* after you have done the installation process. Just check it by import it.
* To import the package open cmd and type ``` python ```. after that type ``` import scrape_yt ```.

## Using
after the above process is completed. 
* You may import scrape_yt in your project by ``` import scrape_yt ```.
* than describe the path. For ex. ``` path = "Downloads" ```.
* To download a youtube video in the best quality you may run the following command.
``` scrape_yt.best_q_single_vid(path) ```.
* To download a youtube playlist in best available quality, you may run the following command.
``` best_q_playlist(path) ```
* An example of the full code
```
import scrape_yt
path = "downloads"
a = scrape_yt.best_q_single_vid(path)
b = scrape_yt.best_q_playlist(path)
```
### Feel free to post an issue or pull request.
Thank You,


