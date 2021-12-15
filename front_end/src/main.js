import App from './App.vue';
import { createApp } from 'vue';
import router from './router';

const  app = createApp(App);
app.use(router);
// await router.isReady();
app.mount('#app');
