<!-- Login.vue -->
<template>
  <div class="auth-container">
    <h2>Войти</h2>
    <form @submit.prevent="handleLogin">
      <div>
        <label for="username">Имя пользователя</label>
        <input v-model="username" id="username" type="text" required />
      </div>
      <div>
        <label for="password">Пароль</label>
        <input v-model="password" id="password" type="password" required />
      </div>
      <button type="submit">Войти</button>
    </form>
    <p>
      Нет аккаунта?
      <router-link to="/register">Зарегистрироваться</router-link>
    </p>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import api from '@/axios'

export default {
  name: 'LoginForm',
  data() {
    return {
      username: '',
      password: '',
      error: null,
    }
  },
  methods: {
    async handleLogin() {
      this.error = null
      try {
        const { data } = await api.post('/api/token/', {
          username: this.username,
          password: this.password,
        })
        localStorage.setItem('access_token', data.access)
        localStorage.setItem('refresh_token', data.refresh)
        this.$router.push('/')
      } catch (e) {
        this.error = 'Неверный логин или пароль.'
      }
    }
  }
}
</script>

<style scoped>
.auth-container { max-width: 400px; margin: auto; padding: 2rem; }
.error { color: red; margin-top: 1rem; }
</style>