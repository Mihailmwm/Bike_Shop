import { createRouter, createWebHistory } from 'vue-router';
// import HomePage from '../pages/HomePage.vue';
import AboutPage from '../pages/About.vue';
import ProcessPage from '../pages/Process.vue';
import ContactPage from '@/components/contact/Contact.vue';
import ShopPage from '../pages/Shop.vue';
import AppMain from '@/components/AppMain/AppMain.vue';

import ProductPage from "@/components/ShopPage/ProductPage.vue"; 

const routes = [
  { path: '/home', name: 'HomePage', component: AppMain },
  { path: '/about', name: 'AboutPage', component: AboutPage },
  { path: '/process', name: 'ProcessPage', component: ProcessPage },
  { path: '/contact', name: 'ContactPage', component: ContactPage },
  { path: '/shop', name: 'ShopPage', component: ShopPage },

  // {path: "/product/:id", name: "ProductDetail", component: ProductPage, props: true},
  {path: '/product/:id', name: 'ProductPage', component: ProductPage, props: true },

];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
