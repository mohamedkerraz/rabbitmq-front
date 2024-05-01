import { Controller, Post, Body } from '@nestjs/common';
import { RabbitMQService } from './rabbitmq.service';

@Controller('rabbitmq')
export class RabbitMQController {
  constructor(private readonly rabbitMQService: RabbitMQService) {}

  @Post('channel')
  async createChannel(@Body('channelName') channelName: string) {
    return this.rabbitMQService.createChannel(channelName);
  }

  @Post('subscribe')
  async subscribeToChannel(@Body('channelName') channelName: string) {
    return this.rabbitMQService.subscribeToChannel(channelName);
  }

  @Post('unsubscribe')
  async unsubscribeFromChannel(@Body('channelName') channelName: string) {
    return this.rabbitMQService.unsubscribeFromChannel(channelName);
  }

  @Post('message')
  async sendMessage(@Body() message: any) {
    const { channelName, content } = message;
    return this.rabbitMQService.sendMessage(channelName, content);
  }
}
