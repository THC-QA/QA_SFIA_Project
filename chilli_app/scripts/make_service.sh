sudo systemctl stop ChilliApp.service
sudo cp "/var/lib/jenkins/workspace/FlaskApp Example Pipeline/service/ChilliApp.service" /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable ChilliApp.service
sudo systemctl start ChilliApp.service