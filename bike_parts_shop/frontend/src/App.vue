<template>
  <div>
    <Header />
    <router-view />
    <Footer />
  </div>
</template>

<script setup lang="js">
import Header from './components/Header/AppHeader.vue';
import Footer from './components/Footer/AppFooter.vue';
// import Main from './components/Main/AppMain.vue'

</script>

<!-- <script>
import AppHeader from '@/components/Header/AppHeader.vue'
import AppFooter from '@/components/Footer/AppFooter.vue'

export default {
  name: 'App',
  components: {
    AppHeader,
    AppFooter
  }
}
</script> -->