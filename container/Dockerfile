FROM python:3.11-slim-bookworm

RUN apt-get update && apt-get install -y fortune-mod cowsay --no-install-recommends && apt-get clean autoclean && apt-get autoremove --yes && rm -rf /var/lib/{apt,dpkg,cache,log}/

RUN groupadd fortune && useradd fortune -g fortune -d /fortune

COPY --chown=fortune:fortune --chmod=640 scripts /fortune

ENV PATH=$PATH:/usr/games/

USER fortune
WORKDIR /fortune
RUN pip install --upgrade pip && pip install -r requirements.txt --user

ENTRYPOINT ["python", "./fortune.py"]