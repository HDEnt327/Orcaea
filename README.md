# Orcaea

Local-based Arcaea score database

## Intro

As we all may know, Lowiro recently closed/limited their official API, rendering applications such as bots completely unusable. The current solution for many of Arcaea players are to either wait for the slow official API, or using Excel to organize their play data. 

As a solution to this, I present **Orcaea**, a local-based database that can store your play data easily, through either manual-input or screenshot recognition, and display your play data and organize them in different catagories, and also show and output the classic b30 images.

The main focus of this project is to make play data input **SIMPLE**, application based manual input can be faster than Excel, but is still annoying to do. Thus, the focus of Orcaea has been to optimize the visual recognition of play data, including the song, the difficulty, and the score.

Orcaea wants to make the data input methods as easy as possible, however, the screenshot recognition part currently is still limited to a small number of devices, however this can be solved through contribution, see the *Contribution* section below.

## Usage

Download either the latest release or download the code as a ZIP

- If you downloaded as a ZIP:
  
  Unzip the code to any directory, install the requirements by running `pip install -r requirements.txt` in the directory that you Unzipped the code in, and run main.py.
  
- If you downloaded the release:
  
  Simply download the version for your operating system and directly run it.
  
## Contributing

Orcaea could use a lot of contribution (well, if anyone even cares about this stupid little project), the main issue currently would be the screenshot recognition modules. Orcaea currently uses a list of device screens and the positions of various data present in the result screen. Though many have been added, more can be covered. If you find out that your device does not work with the current program, please use screentests.py and add to the json your screen ratio and the positions of data just like all the others.

Alternatively, it is also welcome to develop new techniques to identify which data are needed about the need of copping the original image, this is still to be investgated.

Otherwise, any sorts of contribution is welcome!

## License

MIT License
