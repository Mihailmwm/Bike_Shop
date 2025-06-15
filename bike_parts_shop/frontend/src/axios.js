// src/axios.js
import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000',  // когда devServer.proxy настроен, можно оставить '/'; но для надёжности указываем полный URL
  withCredentials: true,             // если планируете работать с cookie
})

export default api
