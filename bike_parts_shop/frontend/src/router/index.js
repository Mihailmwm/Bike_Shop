import { createRouter, createWebHistory } from 'vue-router';
// import HomePage from '../pages/HomePage.vue';
import AboutPage from '../pages/About.vue';
import ProcessPage from '../pages/Process.vue';
import ContactPage from '../pages/Contact.vue';
import ShopPage from '../pages/Shop.vue';
import AppMain from '@/components/AppMain/AppMain.vue';
// import ItemFilters from '@/components/ShopPage/ItemFilters.vue';
// import ItemCard from '@/components/ShopPage/ItemCard.vue';
// import ProductList from "@/components/ProductList.vue";

const routes = [
  { path: '/home', name: 'HomePage', component: AppMain },
  { path: '/about', name: 'AboutPage', component: AboutPage },
  { path: '/process', name: 'ProcessPage', component: ProcessPage },
  { path: '/contact', name: 'ContactPage', component: ContactPage },
  { path: '/shop', name: 'ShopPage', component: ShopPage },
  // { path: '/shop', name: 'ShopPage', component: ItemCard },
  // { path: '/shop', name: 'ShopPage', component: ItemFilters },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
