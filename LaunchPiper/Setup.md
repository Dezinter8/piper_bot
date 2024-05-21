# PiPER STARTUP SERVICE

1. Tworzenie pliku serwisu:
```
sudo nano /etc/systemd/system/ros2_launch.service
```

2. Plik `ros2_launch.service`:

```
[Unit]
Description=Uruchamia skrypt ROS 2 launch przy starcie systemu

[Service]
Type=simple
ExecStart=/bin/bash -c '. /opt/ros/humble/setup.bash; ros2 launch /home/bot/piper_ws/src/piper_bot/LaunchPiper/MasterLaunch.py'


[Install]
WantedBy=multi-user.target
```

Ten plik zawiera definicję usługi, która uruchamia skrypt ROS 2 launch MasterLaunch.py po starcie systemu. Upewnij się, że ścieżki są poprawne i odpowiadają Twojej konfiguracji.

3. Włączanie usługi uruchomieniowej dla PiPER:

```
sudo systemctl daemon-reload
```
* To polecenie przeprowadza ponowne wczytanie konfiguracji systemd, co jest potrzebne po dodaniu nowego pliku serwisu.

```
sudo systemctl enable ros2_launch.service
```
* To polecenie włącza usługę ros2_launch tak, aby uruchamiała się automatycznie po starcie systemu.

```
sudo systemctl start ros2_launch.service
```
* To polecenie natychmiastowo uruchamia usługę ros2_launch, bez konieczności restartowania systemu.

```
journalctl -u ros2_launch.service
```
* To polecenie wyświetli wszystkie wpisy związane z usługą `ros2_launch.service`. 
