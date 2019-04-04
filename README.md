# opencv-python-docker
Projeto com scripts para uso de visão computacional utilizando a biblioteca Opencv do Python

#INICIANDO#

1. `docker pull allangsilva/opencv:latest`
2. `make build` para criar imagem Docker
3. `make run` para executar o container Docker
4. Libere conexões na sua máquina executando `xhost +`
5. `make in` para entrar no container Docker

* Será criado um volume mapeando a pasta `src/`.

- Execute os arquivos `.py` dentro do container

