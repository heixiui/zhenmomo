docker swarm init --advertise-addr 192.168.100.11

worker01:docker swarm join --token ****

worker02:docker swarm join --token ****

docker nodels

1 mkdir /data

2 mv /var/lib/docker /data

3 ln -s /data/docker /var/lib/docker

4 systemctl start docker 

5 docker info | grep "Dir"

6 ls -l /var/lib/docker

7  docker info | grep "Storage Drive"

8 systemctl stop docker

9 cd /etc/systemd/system/multi-user.target.wants/

10 vi docker.service 

  ExecStart=/usr/bin/dockerd --graph=/data/docker --storage-driver=overlay2

 11  systemctl daemon-reload

 12 systemctl start docker

13  docker info | grep "Dir"

14  docker info | grep "Storage Drive"

15 cd

16 docker network create --driver overlay portainer_agent_network

17 docker network create --driver overlay my_network



18 docker service create --name portainer_agent --network portainer_agent_network --publish mode=host,target=9001,published=9001 -e AGENT_CLUSTER_ADDR=tasks.portainer_agent --mode global --mount type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock portainer/agent



19 

 docker service create --name portainer --network portainer_agent_network --publish 9000:9000 --replicas=1 --constraint 'node.role==manager' portainer/portainer -H "tcp://tasks.portainer_agent:9001" --tlsskipverify