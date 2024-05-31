FROM node:lts-slim

WORKDIR /app/


COPY package.json package-lock.json /app/

RUN npm install --only=prod


COPY . /app/

EXPOSE 3000


CMD ["npm", "start"]
