# develop stage
FROM node:lts-alpine as develop-stage

WORKDIR /app

COPY package*.json ./

RUN npm install
COPY . .

# build stage
FROM develop-stage as build-stage
RUN npm run build


# production stage
FROM nginx:latest as production-stage

# remove nginx default html page
RUN rm -rf /usr/share/nginx/html/*

RUN mkdir /app

COPY --from=build-stage /app/dist /app

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

# CMD ["nginx", "-g", "daemon off;"]











# # production stage
# FROM build-stage as production-stage

# # RUN rm -rf /usr/share/nginx/html/* # remove nginx default html page

# COPY --from=build-stage /app/dist /usr/share/nginx/html
# # EXPOSE 8080
# # CMD ["nginx", "-g", "daemon off;"]