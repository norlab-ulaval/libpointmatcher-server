<template>
    <nav id="navbar" class="shadow w-full bg-neutral-600 dark:bg-neutral-900">
        <div class="flex items-center justify-between px-10 py-2 mx-auto">

            <div class="pl-8">
                <router-link to="/home" class="inline-block p-0 m-0 align-middle">
                    <img src="/public/norlab_logo_acronym_light.png" alt="logo" class="h-auto" style="width: 11rem;">
                </router-link>                    
            </div>

            <div class="flex items-center mr-auto ml-8">
                <router-link
                    class="text-white border-b-2 border-transparent hover:border-white custom-text-size mr-8 pb-2 font-sans font-light"
                    to="/"
                    active-class="border-white"
                >
                    Home
                </router-link>
                <router-link
                    v-if="authStore.isLoggedIn"
                    class="text-white border-b-2 border-transparent hover:border-white custom-text-size mr-8 pb-2 font-sans font-light"
                    to="/uploads"
                    active-class="border-white"
                >
                    Uploads
                </router-link>
                <router-link
                    v-if="authStore.isLoggedIn"
                    class="text-white border-b-2 border-transparent hover:border-white custom-text-size pb-2 font-sans font-light"
                    to="/profile"
                    active-class="border-white"
                >
                    Profile
                </router-link> 
            </div>

            <div class="pr-8">
                <a v-if="authStore.isLoggedIn" class="text-white border-b-2 border-transparent hover:border-white custom-text-size font-sans pb-2 cursor-pointer font-light" @click="handleLogout">Log out</a>
                <router-link
                    v-if="!authStore.isLoggedIn"
                    class="text-white border-b-2 border-transparent hover:border-white custom-text-size pb-2 font-sans font-light"
                    to="/auth"
                    active-class="border-white"
                >
                    Log in
                </router-link>
            </div>
        </div>
    </nav>
</template>
  
  <script setup>
    import { onMounted } from 'vue';
    import { logout } from '@/api';
    import { useAuthStore } from '@/stores/authStore';
    import router from '@/router'

    const authStore = useAuthStore();

    const handleLogout = async () => {
        const result = await logout();
        if (result.success) {
            authStore.logout();
            router.push({ name: 'auth' });
        } else {
            console.error(result.error);
        }
    }
    onMounted(() => {
        authStore.checkAuth();
    });
  </script>
<style>
.custom-text-size {
    font-size: 1.65rem;
}
</style>
  