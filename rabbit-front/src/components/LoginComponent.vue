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
    this.socket.onAny((eventName, ...args) => {
      console.log(args)
      console.log(eventName)
      this.events.push(eventName);
    });
    // Demander au serveur Flask d'envoyer les messages
    this.socket.emit('get_messages');
  }
};
</script>