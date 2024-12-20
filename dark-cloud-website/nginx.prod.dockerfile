##### Stage 1
FROM node:latest as node
LABEL author="Russell Boley"
WORKDIR /app
COPY package.json package.json
RUN npm install
COPY . .
RUN npm run build -- --prod

##### Stage 2
FROM nginx:alpine
VOLUME /var/cache/nginx
COPY ./config/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=node /app/dist/APM /usr/share/nginx/html
WORKDIR /usr/share/nginx/html


# docker build -t nginx-angular-gettingstarted-prod -f nginx.prod.dockerfile .
# docker run -p 8080:80 nginx-angular-gettingstarted-prod