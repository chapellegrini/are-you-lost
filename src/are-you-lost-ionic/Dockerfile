FROM node:8 as ionicbuilder
WORKDIR /app
RUN npm install -g ionic
RUN npm install -g cordova
COPY package*.json ./
RUN npm install
COPY . .
RUN rm -rf /app/www
RUN npm install
RUN ionic build --prod # --prod minify js, css, and optimize js

FROM nginx:alpine
RUN rm -rf /var/www/*
COPY --from=ionicbuilder /app/www/ /var/www
EXPOSE 80
