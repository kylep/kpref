#/bin/bash
docker build --no-cache -t kpericak/kpref-py-api .
docker run  --rm kpericak/kpref-py-api bash -c "cd /app && tox"
