<template>
    <div>
      <input type="text" v-model="login" placeholder="Login">
      <input type="mdp" v-model="mdp" placeholder="Mot de passe">
      <button @click="handleLogin">Connexion</button>
    </div>
  </template>
  
  <script>
  import sqlite3 from 'sqlite3';
  
  export default {
    data() {
      return {
        login: '',
        mdp: ''
      };
    },
    methods: {
      handleLogin() {
        const db = new sqlite3.Database('../bdd/user.db');
        db.serialize(() => {
          db.get(`SELECT * FROM user WHERE login = ? AND mdp = ?`, [this.login, this.mdp], (err, row) => {
            if (err) {
              console.error(err.message);
            } else if (!row) {
              console.log("Nom d'utilisateur ou mot de passe incorrect");
            } else {
              console.log("Connecté avec succès !");
            }
          });
        });
        db.close();
      }
    }
  }
  </script>
  