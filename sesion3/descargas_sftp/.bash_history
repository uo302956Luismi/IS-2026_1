sudo apt update 
sudo apt upgrade 
sudo addgroup --system docker
sudo adduser $USER docker
sudo snap install docker
docker version
sudo addgroup --system docker
sudo adduser $USER docker
docker version
exit
ipa
ip a
sudo shutdown now
pwd
mkdir IS-2026
cd IS-2026/
ls -la
ll
/usr/bin/python3
ls
cd IS-2026/
ls
cd IS-2026/
ls
git config --global user.name "Luis Miguel"
git config --global user.email uo302956@uniovi.es
ll
cd ..
ll
cd ..
sudo rm -rf IS-2026/
ll
pwd
ll
ls
ll
mkdir IS-2026
cd IS-2026/
ls
cd IS-2026/
ls
/usr/bin/python3 /home/uo302956/IS-2026/udp_cliente1.py
/usr/bin/python3 /home/uo302956/IS-2026/udp_cliente1.py localhost 8080
/usr/bin/python3 /home/uo302956/IS-2026/udp_servidor1.py
/usr/bin/python3 /home/uo302956/IS-2026/udp_servidor1.py 8080
/usr/bin/python3 /home/uo302956/IS-2026/udp_servidor2_simula_perdidas.py 8080
ip a
sudo shutdown now
nano udp_servidor1.py
ls
nano udp_servidor1.py
ls
ip a
docker network create pruebas
docker ps
ls -la 
chmod 777 lanza_docker_ser_udp_broad.sh 
./lanza_docker_ser_udp_broad.sh 
docker ps
chmod 777 udp_docker_lanzar_cliente.sh 
./udp_docker_lanzar_cliente.sh 
docker network inspect pruebas
./udp_docker_lanzar_cliente.sh 172.18.255.255
sudo reboot now
rm -rf sesion2-2/
mkdir -p ~/02-2
cd ~/02-2
mkdir basedatos
mkdir amigos

mkdir sesion2-2
cd ..
cd IS-2026/
mkdir sesion2-2
cd sesion2-2/
mkdir basedatos
mkdir amigos
mkdir sitios_nginx
docker ps
chmod 777 lanzar_docker_basedatos.sh 
./lanzar_docker_basedatos.sh 
docker ps
docker run -it --rm --network pruebas mariadb bash
source ~/flaskenv/bin/activate
sudo add-apt-repository universe
sudo apt install python3-venv
python3 -m venv ~/flaskenv
source ~/flaskenv/bin/activate
pip install wheel
pip install flask
pip install gunicorn
source ~/flaskenv/bin/activate
pip install flask-sqlalchemy pymysql flask-migrate
pip install httpie
cd amigos/
mkdir app
mkdir app/templates
mkdir instance
touch app/__init__.py
touch app/models.py
touch app/views.py
touch config.py
touch instance/config.py
touch lanzar.py
docker inspect basedatos
FLASK_APP=lanzar.py flask run -h 0.0.0.0
FLASK_APP=lanzar.py flask db migrate
FLASK_APP=lanzar.py flask db init
FLASK_APP=lanzar.py flask db migrate
FLASK_APP=lanzar.py flask db upgrade
docker run -it --rm --network pruebas mariadb bash
FLASK_APP=lanzar.py flask shell
FLASK_APP=lanzar.py flask run -h 0.0.0.0
mkdir app/html
mkdir app/api
touch app/html/__init__.py
touch app/html/views.py
touch app/api/__init__.py
touch app/api/views.py
FLASK_APP=lanzar.py flask run -h 0.0.0.0
find . -maxdepth 3 -type f
FLASK_APP=lanzar.py flask db upgrade
FLASK_APP=lanzar.py flask run -h 0.0.0.0
cat instance/config.py
app.config.from_pyfile('config.py')
FLASK_APP=lanzar.py flask db current
FLASK_APP=lanzar.py flask db upgrade
FLASK_APP=lanzar.py flask run -h 0.0.0.0
FLASK_APP=lanzar.py flask shell
FLASK_APP=lanzar.py flask db upgrade
FLASK_APP=lanzar.py flask shell
http GET localhost:5000/api/amigos
FLASK_APP=lanzar.py flask run -h 0.0.0.0
source ~/flaskenv/bin/activate
http GET localhost:5000/api/amigo/1
http GET localhost:5000/api/amigo/0
http GET localhost:5000/api/amigo/byName/Luis
http GET localhost:5000/api/amigo/2
http GET localhost:5000/api/amigo/3
http GET localhost:5000/api/amigos
http --json POST localhost:5000/api/amigos name=Javier
http --json POST localhost:5000/api/amigos name=Ana lati=43.53 longi=-5.66
cd sesion2-2/
cd amigos/
export DEPLOYMENT_MODE=development
export DATABASE_URI=mysql+pymysql://amigosuser:amigospass@IP_DE_MARIADB/amigosdb
export DATABASE_URI=mysql+pymysql://amigosuser:amigospass@172.18.0.2/amigosdb
export DEPLOYMENT_MODE=development
export DATABASE_URI=mysql+pymysql://amigosuser:amigospass@172.18.0.2/amigosdb
touch Dockerfile
docker build -t amigos:1.0 .
docker images
cd ..
chmod 777 lanzar_contenedor_flask.sh 
./lanzar_contenedor_flask.sh 
docker ps
chmod 777 lanza_contenedor_nginx.sh 
./lanza_contenedor_nginx.sh 
docker ps
cd amigos/
FLASK_APP=lanzar.py flask db migrate
FLASK_APP=lanzar.py flask db upgrade
docker run -it --rm --network pruebas mariadb bash
source ~/flaskenv/bin/activate
export DEPLOYMENT_MODE=development
export DATABASE_URI=mysql+pymysql://amigosuser:amigospass@172.18.0.2/amigosdb
FLASK_APP=lanzar.py flask run -h 0.0.0.0
http GET localhost:5000/api/amigos
http --json PUT localhost:5000/api/amigo/1 device="Mi movil"
http GET localhost:5000/api/amigos
cat app/models.py
cat app/__init__.py
cat config.py
cat migrations/versions/*.py
http GET localhost:5000/api/amigos
http --json PUT localhost:5000/api/amigo/1 device="Mi movil"
http --json PUT localhost:5000/api/amigo/4 device="Mi movil"
http --json PUT localhost:5000/api/amigo/3 device="Mi movil"
http GET localhost:5000/api/amigos
http --json PUT localhost:5000/api/amigo/1 device="Mi movil"
FLASK_APP=lanzar.py flask shell
http GET localhost:5000/api/amigos
FLASK_APP=lanzar.py flask shell
ps aux | grep flask
sudo lsof -i :5000
ss -ltnp | grep 5000
ps -p 41994 -o pid,lstart,args
readlink /proc/41994/cwd
tr '\0' '\n' < /proc/41994/environ | grep -E '^(DATABASE_URI|DEPLOYMENT_MODE|FLASK_APP)='
docker ps
http GET localhost:5000/api/amigos
http GET localhost/api/amigos
http --json PUT localhost/api/amigo/7 device="Mi movil nuevo"
ls -la
docker images
docker inspect amigos --format 'Imagen: {{.Config.Image}} | Montajes: {{json .Mounts}}'
cat Dockerfile
docker build -t amigos:2.0 .
docker images
docker inspect nginx --format '{{json .NetworkSettings.Networks}}'
docker inspect amigos --format '{{json .NetworkSettings.Networks}}'
docker inspect amigos --format 'Entorno: {{json .Config.Env}} | Comando: {{json .Config.Cmd}} | Política: {{json .HostConfig.RestartPolicy}}'
docker inspect basedatos --format '{{json .NetworkSettings.Networks}}'
docker stop amigos
docker rename amigos amigos-v1-backup
docker ps -a
docker images amigos
docker run -d   --name amigos   --network pruebas   -e DEPLOYMENT_MODE=production   -e DATABASE_URI="mysql+pymysql://amigosuser:amigospass@basedatos/amigosdb"   amigos:2.0
docker ps
http GET localhost/api/amigos
http GET localhost/api/devices
docker stop nginx
docker stop amigos
docker stop basedatos
cd ..
./lanzar_docker_basedatos.sh 
./lanzar_contenedor_flask_2.sh 
docker ps
./lanzar_contenedor_flask_2.sh 
./lanza_contenedor_nginx.sh 
docker ps
./lanza_contenedor_nginx.sh 
docker ps
./lanza_contenedor_nginx.sh 
docker ps
docker ps -a
docker logs nginx
ls -l sitios_nginx
cat sitios_nginx/*
./lanza_contenedor_nginx.sh 
docker ps
