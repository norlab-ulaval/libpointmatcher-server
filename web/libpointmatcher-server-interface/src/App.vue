<template>
  <div id="app" class="flex flex-col h-screen ">
    <Navbar/>
    <main class="flex-grow w-full dark:bg-neutral-900">
      <router-view></router-view>
    </main>
    <Footer v-if="$route.name !== 'auth'" />
  </div>
</template>

<script>
import Navbar from '@/components/layout/Navbar.vue';
import Footer from '@/components/layout/Footer.vue';

export default {
  name: "app",
  components: {
    Navbar,
    Footer,
  },
};
</script>