# EmojiFood

This small game is a demostration of PyGame and OpenCV.

## Developed by

[Jorge I. Meza](https://www.github.com/jimezam/) (jimezam at autonoma.edu.co)  
Semillero Programación Web y Móvil  
[Universidad Autónoma de Manizales](https://www.autonoma.edu.co/)

## How to install

```
$ git clone https://github.com/jimezam/EmojiFood.git

$ cd EmojiFood

$ python -m venv env

$ source env/bin/activate  #*

$ pip install -r requirements.txt -v
```

`#*` The environment activation command depends on the *shell* type used as follows.

| Sistema operativo | Comando |
| --- | --- |
| Linux & MacOs | `$ source env/bin/activate` |
| Windows (cmd) | `$ env\Scripts\activate.bat` |
| Powershell Core | `$ env/bin/Activate.ps1` |

## How to run

To run the application the correspondent environment must be already activated (see below).

```
$ python game.py
```

## Technical tips

### MP3 file could not be opened.  

Sometimes .mp3 files cannot be opened by PyGame library due its format.  This can be easily solved using `ffmpeg` as follows.

```
$ ffmpeg -i original.mp3 newname.mp3
```
## Resources

- PyGame  
  https://www.pygame.org/news
- OpenCV  
  https://opencv.org/
- Cascade Classifier  
  [https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)
- Face Detection using Haar Cascades  
  https://docs.opencv.org/3.4/d2/d99/tutorial_js_face_detection.html
