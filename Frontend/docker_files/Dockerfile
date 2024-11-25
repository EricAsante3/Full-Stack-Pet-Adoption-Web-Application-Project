FROM node:16-alpine
WORKDIR /app



COPY Frontend/furrr_everr_Friends ./furrr_everr_Friends
WORKDIR /app/furrr_everr_Friends


RUN npm install

EXPOSE 5173
CMD ["npm", "run", "dev"]