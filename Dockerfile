FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements2.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp build-base python3 gcc libc-dev python3-dev linux-headers openssl bash git py3-pip libffi-dev openssl-dev
RUN apk add libxml2 libxslt libxml2-dev libxslt-dev
RUN pip3 install setuptools
RUN pip3 install -r /requirements.txt
RUN apk del .tmp

RUN mkdir app/

# Create a group and user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

RUN chown -R appuser:appgroup app



# Copy existing application directory permissions
COPY --chown=appuser:appgroup iCrawler/ app/

WORKDIR /app
COPY ./scripts /scripts

# Tell docker that all future commands should run as the appuser user
USER appuser

#RUN chmod +x /scripts/*


CMD ["entrypoint.sh"]