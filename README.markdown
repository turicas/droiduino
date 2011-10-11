Droiduino = Android + Arduino + Python
======================================

Introduction
------------

This is a project in which you can control a cooler velocity via Internet. But
with this code-base __you can control any machine you have using your Android
phone, via Internet__.

The code is splitted in 3 parts:

- __Android__: runs on top of [Scripting Layer for
Android](http://code.google.com/p/android-scripting/) (aka SL4A), using Python,
  HTML, CSS and JavaScript to communicate with an Web application (the Django
  Web application cited below).
- __Arduino__: control the relays and other things you want based on the
  requests you made using your phone. Arduino get the status will want to your
  machines from the Django Web application (the same Android uses to *change*
  the status of the machines, cited above).
- __Django__: the Web application in which Android will post the new statuses
  you want to your machines and in which Arduino will get these statuses.

See the next section to know how to install and use it.

Installation
------------

### Android

To do.


### Arduino

Arduino needs to get information about which should be the statuses of the
machines you are controlling. It can be made in two methods:

#### USB

You need to have a computer connected via USB with Arduino and run
permanently the script `arduino/update_status.py`, so the computer will get
the information in the Django website and pass it through USB to Arduino.

To run this method you need to:

- Configure the URL of Django app and Arduino USB port in
  `arduino/update_status.py`;
- Configure the ports you are using in the Arduino at `arduino/droiduino.ino`;
- Upload `arduino/droiduino.ino` to your Arduino;
- Plug your Arduino in one USB port;
- Run `arduino/update_status.py` (it was tested on GNU/Linux only, but is
  supposed to work in Windows and Mac OS with little changes. You need
  [Python](http://www.python.org/) and
  [PySerial](http://pyserial.sourceforge.net/) installed to run this script.

Obviously, you need also the Django Web application running in the configured
URL.


#### [Ethernet Shield](http://www.arduino.cc/en/Main/ArduinoEthernetShield)

With this method Arduino talks directly with the Django Web application and
gets the statuses. Note: Arduino code for this method __is not finished yet__
since my Ethernet Shield is not working. Sorry :-(


Django
------

To run the Web application you need to install
[Django](http://djangoproject.com). The code available here (at `django/`) is
for a *Django app* (not a Django project).


#### Using virtualenv

You can use [virtualenv](http://pypi.python.org/pypi/virtualenv) and
[virtualenvwrapper](http://pypi.python.org/pypi/virtualenvwrapper) if don't
need to install Django in your system:

    mkvirtualenv droiduino
    cdvirtualenv 
    pip install django
    django-admin.py startproject the-project-name
    cd project/
    ln -s /path/to/this/repository/django/droiduino .


#### Running the Web application

To run this Web application you need to create a Django project, configure
`urls.py` and host it within a Web server that supports WSGI. I'm using
[WebFaction](http://bit.ly/host-python) and happy with it.


Talks about this project
------------------------

This project was presented by [Tatiana Al-Chueyr](http://tatialchueyr.com/) and
[Álvaro Justen](http://blog.justen.eng.br/) at
[PythonBrasil\[7\]](http://www.pythonbrasil.org.br/) in the talk "[Controlando
de LEDs a eletrodomésticos com Python, Android e
Arduino](http://www.pythonbrasil.org.br/2011/programacao/diaria/grade-do-evento/mobilidade-e-sistemas-embarcados/controlando-de-leds-a-eletrodomesticos-com-python-android-e-arduino)"
(Portuguese for "Controlling from LEDs to appliances with Python, Android and
Arduino").


License
-------

This project is licensed under the [GNU General Public
License](http://www.gnu.org/copyleft/gpl.html) (aka GPL).

Copyright &copy; [Tatiana Al-Chueyr](http://tatialchueyr.com/) and
[Álvaro Justen](http://blog.justen.eng.br/) 2011.
