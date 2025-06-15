<!-- Register.vue  -->
<template>
  <div class="auth-container">
    <!-- <h2>Регистрация</h2> -->
    <form @submit.prevent="handleRegister">
      <div class="section">
        <label for="username" class="section-title">Имя пользователя</label>
        <input v-model="username" id="username" type="text" required />
      </div>

          <div class="sectionL"></div>

      <div class="section">
        <label for="email" class="section-title">Email</label>
        <input v-model="email" id="email" type="email" required />
      </div>
          <div class="sectionL"></div>
      <div class="section">
        <label for="password" class="section-title">Пароль</label>
        <input v-model="password" id="password" type="password" required />
      </div>
      <button type="submit" class="keep">Зарегистрироваться</button>
    </form>
    <p>
      Уже есть аккаунт?
      <router-link to="/login" style=" text-decoration: none;">Войти</router-link>
    </p>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import api from '@/axios'

export default {
  name: 'RegisterForm',
  data() {
    return {
      username: '',
      email: '',
      password: '',
      error: null,
    }
  },
  methods: {
    async handleRegister() {
      this.error = null
      try {
        await api.post('/api/register/', {
          username: this.username,
          email: this.email,
          password: this.password,
        })
        // После успешной регистрации — редирект на страницу логина
        this.$router.push('/login')
      } catch (e) {
        this.error = 'Ошибка при регистрации.'
      }
    }
  }
}
</script>

<style scoped>

input:-webkit-autofill {
  -webkit-box-shadow: 0 0 0px 1000px #ffffff00 inset !important; 
  -webkit-text-fill-color: rgb(51, 119, 182) !important;        
  transition: background-color 9999s ease-out, color 9999s ease-out;
}


input {
    font-size: 20px;
    border: 2px solid white;
    background-color: #ffffff00;
    color: rgb(51, 119, 182);
}
input p {
    color: white;
}

.keep:hover {
  background: #0056b3;
}

.keep {
        margin-top: 2vw;
    padding: 1em 2em;
    /* font-size: 1em; */
    background: transparent;
    border: 2px solid white;
    color: white;
    cursor: pointer;
    max-width: -moz-fit-content;
    max-width: fit-content;
    min-width: -moz-fit-content;
    min-width: fit-content;
    text-decoration: none;
}

.section {
    border-top: 2px solid white;
    border-right: 2px solid white;
    border-bottom: 2px solid white;
}

.sectionL {
    border-left: 2px solid white;
    padding: 40px 0;
}
.section-title {
    font-weight: bold;
    font-size: 18px;
    text-transform: uppercase;
    position: absolute;
    top: -15px;
    left: 20px;
    background: black;
    padding: 5px;
    color: white;
}

.auth-container { 
    max-width: 400px; 
    margin: auto; 
    /* padding: 2rem; */
    padding-top: 10em;
    height: 100vh;
 }

 .auth-container p{ 
color: white;


}


.error { color: red; margin-top: 1rem; }
</style>
