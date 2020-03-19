#!/bin/bash
sudo systemctl stop ChilliGUni.service
sudo cp "/var/lib/jenkins/workspace/FlaskApp Example Pipeline/service/ChilliGUni.service" /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable ChilliGUni.service
sudo systemctl start ChilliGUni.service