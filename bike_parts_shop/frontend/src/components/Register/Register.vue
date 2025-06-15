<!-- Register.vue  -->
<template>
  <div class="auth-container">
    <h2>Регистрация</h2>
    <form @submit.prevent="handleRegister">
      <div>
        <label for="username">Имя пользователя</label>
        <input v-model="username" id="username" type="text" required />
      </div>
      <div>
        <label for="email">Email</label>
        <input v-model="email" id="email" type="email" required />
      </div>
      <div>
        <label for="password">Пароль</label>
        <input v-model="password" id="password" type="password" required />
      </div>
      <button type="submit">Зарегистрироваться</button>
    </form>
    <p>
      Уже есть аккаунт?
      <router-link to="/login">Войти</router-link>
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
.auth-container { max-width: 400px; margin: auto; padding: 2rem; }
.error { color: red; margin-top: 1rem; }
</style>
