FROM node:8
WORKDIR /usr/src/app
RUN npm install -g ionic
COPY package*.json ./
RUN npm install
COPY . ./
#RUN npm install @ionic/app-scripts@latest --save-dev
CMD ionic serve
