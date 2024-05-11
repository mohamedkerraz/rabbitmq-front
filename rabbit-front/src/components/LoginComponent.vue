<template>
  <div>
    <ul>
      <li v-for="message in messages" :key="message">{{ message }}</li>
    </ul>
  </div>
</template>

<script>
import io from 'socket.io-client';

export default {
  data() {
    return {
      messages: [],
      events:[],
      queue_name: 'd118b99a-9e74-44bd-b1c0-f7a7e017e1fd'
    };
  },
  created() {
    // Se connecter au serveur Flask via WebSocket en passant par /consumer
    this.socket = io('http://localhost:5000', { path: '/socket.io' });

    // Écouter les messages envoyés par le serveur Flask
    this.socket.on('message', (message) => {
      this.messages.push(message);
      console.log(message)
    });
    // Demander au serveur Flask d'envoyer les messages
    this.socket.emit('get_messages', this.queue_name);
  }
};
</script>