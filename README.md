# kpref
A reference project. We like to have a dedicated K8s cluster for each major application.


## Moving parts

- *py-api*: A python API using Quart via Hypercorn ASGI, and pytest via Tox
  - [Quart](https://pgjones.gitlab.io/quart/)
  - [Hypercorn](https://pgjones.gitlab.io/hypercorn/)
- *jenkins*: to orchestrate the CICD with github webhooks and auto build
  - [Jenkins](https://www.jenkins.io/)
