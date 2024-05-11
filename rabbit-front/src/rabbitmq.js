// const amqp = require('amqplib/callback_api');

// async function connect() {
//   try {
//     const connection = await amqp.connect('amqp://localhost:15672'); // Remplacez "localhost" par l'URL de RabbitMQ si nécessaire
//     const channel = await connection.createChannel();
//     const queue = 'test'; // Remplacez "chat_queue" par le nom de votre file d'attente

//     await channel.assertQueue(queue);

//     channel.consume(queue, (message) => {
//       if (message !== null) {
//         const content = message.content.toString();
//         console.log('Nouveau message reçu :', content);
//         channel.ack(message);
//       }
//     });
//   } catch (error) {
//     console.error('Erreur de connexion à RabbitMQ :', error);
//   }
// }

// connect();