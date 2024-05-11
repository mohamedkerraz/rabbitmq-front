<template>
    <div>
      <input type="text" v-model="login" placeholder="Login">
      <input type="mdp" v-model="mdp" placeholder="Mot de passe">
      <button @click="handleLogin">Connexion</button>
    </div>
  </template>
  