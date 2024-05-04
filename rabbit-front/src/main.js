import { createApp } from 'vue';
import App from './App.vue';
// import VueSocketIO from 'vue-socket.io';
// import SocketIO from 'socket.io-client';
import 'bootstrap/dist/css/bootstrap.min.css';

const app = createApp(App);

// app.use(
//   new VueSocketIO({
//     debug: true,
//     connection: SocketIO('ws://api.example.com/'),
//   })
// );

app.mount('#app');
