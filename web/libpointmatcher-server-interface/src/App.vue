<template>
  <div id="app" class="flex flex-col h-screen">
    <Navbar v-if="$route.name !== 'auth'" />
    <main class="flex-grow w-full">
      <router-view></router-view>
    </main>
    <Footer v-if="$route.name !== 'auth'" />
  </div>
</template>

<script>
import Navbar from '@/components/layout/Navbar.vue';
import Footer from '@/components/layout/Footer.vue';
import Cookies from 'js-cookie';

export default {
  name: "app",
  components: {
    Navbar,
    Footer,
  },
  // created() {
  //   Cookies.remove('token');
  // }
};
</script>