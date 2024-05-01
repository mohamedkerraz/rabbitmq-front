import { Injectable } from '@nestjs/common';
import { ClientProxy, ClientProxyFactory, Transport } from '@nestjs/microservices';

@Injectable()
export class RabbitMQService {
  private client: ClientProxy;

  constructor() {
    this.client = ClientProxyFactory.create({
      transport: Transport.RMQ,
      options: {
        urls: ['amqp://localhost:5672'],
        queue: 'main_queue',
      },
    });
  }

  async createChannel(channelName: string) {
  }

  async subscribeToChannel(channelName: string) {
  }

  async unsubscribeFromChannel(channelName: string) {
  }

  async sendMessage(channelName: string, message: any) {
  }
}