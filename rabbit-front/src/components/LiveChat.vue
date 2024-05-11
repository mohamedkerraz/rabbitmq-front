<template>
  <section style="background-color: #eee;">
    <div class="container py-5">

      <div v-if="loggedIn">
      
        <div class="row">

          <div class="col-md-6 col-lg-5 col-xl-4 mb-4 mb-md-0">

            <h5 class="font-weight-bold mb-3 text-center text-lg-start">Amis</h5>

            <div class="card">
              <div class="card-body">
                <ul class="list-unstyled mb-0">
                  <li class="p-2 border-bottom" style="background-color: #eee;">
                    <a href="#!" class="d-flex justify-content-between">
                      <div class="d-flex flex-row">

                        <div class="pt-1">
                          <p class="fw-bold mb-0">John Doe</p>
                          <p class="small text-muted">Hello, Are you there?</p>
                        </div>
                      </div>
                      <div class="pt-1">
                        <p class="small text-muted mb-1">Just now</p>
                        <span class="badge bg-danger float-end">1</span>
                      </div>
                    </a>
                  </li>

                  <li class="p-2 border-bottom">
                    <a href="#!" class="d-flex justify-content-between">
                      <div class="d-flex flex-row">

                        <div class="pt-1">
                          <p class="fw-bold mb-0">Danny Smith</p>
                          <p class="small text-muted">Lorem ipsum dolor sit.</p>
                        </div>
                      </div>
                      <div class="pt-1">
                        <p class="small text-muted mb-1">5 mins ago</p>
                      </div>
                    </a>
                  </li>


                  <li class="p-2 border-bottom">
                    <a href="#!" class="d-flex justify-content-between">
                      <div class="d-flex flex-row">

                        <div class="pt-1">
                          <p class="fw-bold mb-0">Alex Steward</p>
                          <p class="small text-muted">Lorem ipsum dolor sit.</p>
                        </div>
                      </div>
                      <div class="pt-1">
                        <p class="small text-muted mb-1">Yesterday</p>
                      </div>
                    </a>
                  </li>


                  <li class="p-2 border-bottom">
                    <a href="#!" class="d-flex justify-content-between">
                      <div class="d-flex flex-row">
                        <div class="pt-1">
                          <p class="fw-bold mb-0">Ashley Olsen</p>
                          <p class="small text-muted">Lorem ipsum dolor sit.</p>
                        </div>
                      </div>
                      <div class="pt-1">
                        <p class="small text-muted mb-1">Yesterday</p>
                      </div>
                    </a>
                  </li>


                  <li class="p-2 border-bottom">
                    <a href="#!" class="d-flex justify-content-between">
                      <div class="d-flex flex-row">
                        <div class="pt-1">
                          <p class="fw-bold mb-0">Kate Moss</p>
                          <p class="small text-muted">Lorem ipsum dolor sit.</p>
                        </div>
                      </div>
                      <div class="pt-1">
                        <p class="small text-muted mb-1">Yesterday</p>
                      </div>
                    </a>
                  </li>
                  <li class="p-2 border-bottom">
                    <a href="#!" class="d-flex justify-content-between">
                      <div class="d-flex flex-row">
                        <div class="pt-1">
                          <p class="fw-bold mb-0">Lara Croft</p>
                          <p class="small text-muted">Lorem ipsum dolor sit.</p>
                        </div>
                      </div>
                      <div class="pt-1">
                        <p class="small text-muted mb-1">Yesterday</p>
                      </div>
                    </a>
                  </li>
                  <li class="p-2">
                    <a href="#!" class="d-flex justify-content-between">
                      <div class="d-flex flex-row">
                        <div class="pt-1">
                          <p class="fw-bold mb-0">Brad Pitt</p>
                          <p class="small text-muted">Lorem ipsum dolor sit.</p>
                        </div>
                      </div>
                      <div class="pt-1">
                        <p class="small text-muted mb-1">5 mins ago</p>
                        <span class="text-muted float-end"><i class="fas fa-check" aria-hidden="true"></i></span>
                      </div>
                    </a>
                  </li>
                </ul>

              </div>
            </div>

          </div>

          <div class="col-md-6 col-lg-7 col-xl-8">
            <h5 class="font-weight-bold mb-3 text-center text-lg-start">Chat Géneral</h5>
            <ul class="list-unstyled">

              <li class="d-flex justify-content-between mb-4">
                <div class="card">
                  <div class="card-header d-flex justify-content-between p-3">
                    <p class="fw-bold mb-0">Brad Pitt</p>
                    <p class="text-muted small mb-0"><i class="far fa-clock"></i> 12 mins ago</p>
                  </div>
                  <div class="card-body">
                    <p class="mb-0">
                      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
                      labore et dolore magna aliqua.
                    </p>
                  </div>
                </div>
              </li>

              <li class="d-flex justify-content-between mb-4">
                <div class="card w-100">
                  <div class="card-header d-flex justify-content-between p-3">
                    <p class="fw-bold mb-0">Lara Croft</p>
                    <p class="text-muted small mb-0"><i class="far fa-clock"></i> 13 mins ago</p>
                  </div>
                  <div class="card-body">
                    <p class="mb-0">
                      Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque
                      laudantium.
                    </p>
                  </div>
                </div>
              </li>

              <li class="d-flex justify-content-between mb-4">
                <div class="card">
                  <div class="card-header d-flex justify-content-between p-3">
                    <p class="fw-bold mb-0">Brad Pitt</p>
                    <p class="text-muted small mb-0"><i class="far fa-clock"></i> 10 mins ago</p>
                  </div>
                  <div class="card-body">
                    <p class="mb-0">
                      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
                      labore et dolore magna aliqua.
                    </p>
                  </div>
                </div>
              </li>
              <!-- Affichez les détails du message ici -->
              <li v-for="message in messages" :key="message.id" class="d-flex justify-content-between mb-4">
              
                <div class="card">
                  <div class="card-header d-flex justify-content-between p-3">
                    <p class="fw-bold mb-0">{{ message.sender }}</p>
                    <p class="text-muted small mb-0"><i class="far fa-clock"></i> {{ message.timestamp }}</p>
                  </div>
                  <div class="card-body">
                    <p class="mb-0">{{ message.content }}</p>
                  </div>
                </div>
              </li>

              <li class="bg-white mb-3">
                <div data-mdb-input-init class="form-outline">
                  <textarea v-model="message_send" class="form-control" id="textAreaExample2" rows="4"></textarea>
                  <label class="form-label" for="textAreaExample2">Votre message</label>
                </div>
              </li>
              <button type="button" data-mdb-button-init data-mdb-ripple-init class="btn btn-info btn-rounded float-end"
                @click="send_message">Envoyer</button>
            </ul>

          </div>

        </div>

      </div>

      <div v-else>
        <LoginComponent @login-success="handleLoginSuccess" @close-modal="closeModal" />
      </div>


    </div>
  </section>
</template>

<script>
import axios from 'axios';
import RabbitMQClient from '@/rabbitmq.js';
import LoginComponent from './LoginComponent.vue';

export default {

  name: 'LiveChat',
  components: {
    LoginComponent
  },
  props: {
    msg: String
  },
  data() {
    return {
      message_send: null,
      messages: [],
      error: null,
      loggedIn: false,
    };
  },
  mounted() {
    // Appel de l'API lorsque le composant est monté
    RabbitMQClient.onMessage((message) => {
      this.messages.push(message);
    });
    this.subscribe();
  },
  methods: {
    handleLoginSuccess() {
      this.loggedIn = true;
    },
    subscribe() {
      axios.get('http://api.example.com/subscribe/')
        .then(response => {
          // Succès de l'appel API, mettre à jour les données
          this.message_send = response.data;
          console.log(this.message_send);
        })
        .catch(error => {
          // Gestion des erreurs de l'appel API
          this.error = error;
        });

      // Utilisation de `this.$socket` pour la connexion WebSocket
      this.$socket.onmessage = (message) => {
        const parsedMessage = JSON.parse(message.data);
        this.messages.push(parsedMessage);
      };
    },
    send_message() {
      console.log("message envoyé : " + this.message_send);
      RabbitMQClient.sendMessage(this.message_send);
      this.message_send = '';
      axios.post('http://api.example.com/send_message/', { message: this.message_send })
        .then(response => {
          // Succès de l'appel API, mettre à jour les données
          this.message_send = response.data;
          console.log(this.message_send);
        })
        .catch(error => {
          // Gestion des erreurs de l'appel API
          this.error = error;
        });
    }
  }
}

</script>


<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
