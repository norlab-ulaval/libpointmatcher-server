<template>
  <div id="app">
    <Navbar v-if="$route.name !== 'auth'" />
    <router-view></router-view>
  </div>
</template>

<script>
import Navbar from '@/components/layout/Navbar.vue';

export default {
  components: {
    Navbar,
  }
};
</script>