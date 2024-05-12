# Download

Na początku należy zainstalować wymagane programy (Ros2 humble itd.).

Następnie należy pobrać repozytorium:

```
cd Desktop/

git clone https://github.com/Dezinter8/Piper_Gui.git
```

Aby zainstalować aplikację, najlepiej stworzyć środowisko wirtualne (venv) przy użyciu programów takich jak pycharm lub bezpośrednio z konsoli powershell przy pomocy komendy:

```
cd Piper_Gui/

virtualenv venv

source venv/bin/activate
```

Aby Pobrać wymagane biblioteki należy użyć komendy:

```
pip install PyQt5 vtk opencv-python-headless
```

Aby uruchomić program należy użyć komendy:

```
python main.py
```

# Building Ui

mainwindow ui - Można go odpalić w Qt Designerze i edytować bezpośrednio w nim. Po edycji należy wykonać komendę:

```
pyuic5 mainwindow.ui -o MainWindow.py
```

resources qrc - Jest to plik zawierający zasoby takie jak ikony czy zdjęcia. Aby go przekonwertować na plik py należy użyć komendy:

```
pyrcc5 resources.qrc -o resources_rc.py
```
