FROM nginx

# remove nginx default html page
RUN rm -rf /usr/share/nginx/html/*

# Add the nginx configuration file
ADD ./nginx/nginx.conf /etc/nginx/nginx.conf

# Copy over static assets from the frontend
# COPY ./frontend/dist /usr/share/nginx/html
