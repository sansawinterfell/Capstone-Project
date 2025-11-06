FROM ubuntu 


RUN apt update 
RUN apt install python3-pip -y
RUN pip3 install Flask


WORKDIR /usr/src/

COPY .. dest

CMD [ "python3", "-m" , "Flask" , "RUN" , "--host=0.0.0.0"]