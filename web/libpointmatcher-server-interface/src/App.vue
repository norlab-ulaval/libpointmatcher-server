<template>
  <div id="app" class="flex flex-col h-screen">
    <Navbar v-if="$route.name !== 'auth'" />
    <main class="flex-grow w-full">
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
import Navbar from '@/components/layout/Navbar.vue';

export default {
  name: "app",
  components: {
    Navbar,
  }
};
</script>