#!/bin/bash
# outputディレクトリ内のファイルをrsync over SSHで転送
rsync -acvz --delete docker-compose.yml ryo@34.83.27.41
