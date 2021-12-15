
import { createRouter, createWebHistory } from 'vue-router'
import Timezone from '../components/Timezone.vue';

export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Timezone',
      component: Timezone,
    }
  ],
});
