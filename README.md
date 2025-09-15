# fluxo-cidcd-devops
# Atividade CI/CD – Disciplina DevOps

## Objetivo
- Criar um fluxo de CI/CD completo.
- Criar pelo menos um branch, 5 commits e pelo menos um Pull Request para fazer marge de um branch pelo main.

## Como rodar via Docker

### Build da imagem
```bash
docker build -t fluxo-cicd-devops:latest .

## Testes 
http://localhost:8000/

http://localhost:8000/soma?a=2&b=3

http://localhost:8000/media?valores=2,4,6
