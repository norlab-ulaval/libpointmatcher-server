<template>
    <ProfileInfo :loading-data="loadingData" />
</template>

<script>
import ProfileInfo from '../components/profile/ProfileInfo.vue';
import { loadFiles } from '../components/3d/dataLoader';

export default {
    components: {
        ProfileInfo
    },
    data() {
      return {
        loadingData: false,
      };
    },
    async mounted() {
        this.loadingData = true;
        await loadFiles();
        this.loadingData = false;
    }
}
</script>