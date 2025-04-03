import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './assets/styles/style.css'
import './components/Footer/s.scss'
import './components/Header/h.scss'
import './components/Header/nav.js'
import './components/Header/burger.js'
import './components/AppMain/m.scss'

const app = createApp(App);
app.use(router);
app.mount('#app');


