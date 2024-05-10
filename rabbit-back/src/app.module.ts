import { Module, NestModule, MiddlewareConsumer } from '@nestjs/common';
import { AppService } from './app.service';
import { RabbitMQModule } from './rabbitmq/rabbitmq';
import { RabbitMQController } from './rabbitmq/rabbitmq.controller';
import { RacineController } from './app.controller';
import { HaikuMiddleware } from './middleware/middleware';

@Module({
  imports: [ RabbitMQModule],
  controllers: [RacineController],
  providers: [AppService],
})
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer
      .apply(HaikuMiddleware)
      .forRoutes(RabbitMQController);
  }
}
