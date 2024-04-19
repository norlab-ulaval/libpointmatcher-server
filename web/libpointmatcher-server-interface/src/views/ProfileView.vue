<template>
    <ProfileInfo />
</template>

<script>
import ProfileInfo from '../components/profile/ProfileInfo.vue';
import { loadFiles } from '../components/3d/dataLoader';

export default {
    components: {
        ProfileInfo
    },
    async mounted() {
        console.log("loading files...(ajouter un toast ici probablement)")
        await loadFiles();
        console.log("files loaded")
    }
}
</script>