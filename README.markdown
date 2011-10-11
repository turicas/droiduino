Droiduino = Android + Arduino + Python
======================================

Introduction
------------

This is a project in which you can control a cooler velocity via Internet. With
this code-base __you can control any machine you have using your Android phone,
via Internet__.

The code is splitted in 3 parts:

- __Android__: runs on top of SL4A, using Python, HTML, CSS and JavaScript to
  communicate with an Web application.
- __Arduino__: control the relays and other thigs you want based on the
  requests. Your Arduino needs the circuits to control things and an [Ethernet
  Shield](http://www.arduino.cc/en/Main/ArduinoEthernetShield).
- __Django__: the Web application in which Android will post the new status you
  want to the machine and in wichi Arduino will get this status.


License
-------

This project is licensed under the [GNU General Public
License](http://www.gnu.org/copyleft/gpl.html) (aka GPL).

Copyright &copy; [Tatiana Al-Chueyr](http://tatialchueyr.com/) and
[Álvaro Justen](http://blog.justen.eng.br/) 2011.


Preparing the environment (Django)
----------------------------------

    mkvirtualenv pybr7
    cdvirtualenv 
    ./bin/pip-2.7 install django
    django-admin.py startproject project
    cd project/
    ln -s /path/to/this/project/code/django/pybr7 .


Talks about this project
------------------------

This project was presented by [Tatiana Al-Chueyr](http://tatialchueyr.com/) and
[Álvaro Justen](http://blog.justen.eng.br/) at
[PythonBrasil\[7\]](http://www.pythonbrasil.org.br/) in the talk "[Controlando
de LEDs a eletrodomésticos com Python, Android e
Arduino](http://www.pythonbrasil.org.br/2011/programacao/diaria/grade-do-evento/mobilidade-e-sistemas-embarcados/controlando-de-leds-a-eletrodomesticos-com-python-android-e-arduino)"
(Portuguese for "Controlling from LEDs to appliances with Python, Android and
Arduino").
