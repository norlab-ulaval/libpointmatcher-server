
<template>
  <div class="flex items-center justify-center">
    <div>
      <h1> Welcome page </h1>
      <PointsVisualizer />
    </div>
  </div>
</template>

<script>
import PointsVisualizer from '@/components/3d/PointsVisualizer.vue';

export default {
  name: 'HomeView',
  components: {
    PointsVisualizer
  }
};
</script>