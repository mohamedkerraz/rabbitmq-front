
FROM rabbitmq:3.8-management


COPY rabbitmq.config /etc/rabbitmq/rabbitmq.config

EXPOSE 15672

EXPOSE 5672

CMD ["rabbitmq-server", "--config", "/etc/rabbitmq/rabbitmq.config"]