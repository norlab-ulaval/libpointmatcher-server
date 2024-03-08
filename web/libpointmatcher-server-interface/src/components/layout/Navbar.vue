<template>
    <nav class="shadow w-full" style="background-color: #515151;">
        <div class="flex items-center justify-between px-10 py-2 mx-auto">

            <div class="pl-8">
                <router-link to="/home">
                    <img src="/public/norlab_logo_acronym_light.png" alt="logo" class="h-auto" style="width: 11rem;">
                </router-link>                
            </div>

            <div class="flex items-center mr-auto ml-8">
                <router-link
                    class="text-white border-b-3 border-transparent hover:border-white custom-text-size mr-8 pb-2 font-sans"
                    to="/home"
                    active-class="border-white"
                >
                    Home
                </router-link>
                <router-link
                    class="text-white border-b-3 border-transparent hover:border-white custom-text-size mr-8 pb-2 font-sans"
                    to="/uploads"
                    active-class="border-white"
                >
                    Uploads
                </router-link>
                <router-link
                    class="text-white border-b-3 border-transparent hover:border-white custom-text-size pb-2 font-sans"
                    to="/profile"
                    active-class="border-white"
                >
                    Profile
                </router-link> 
            </div>

            <div class="pr-8">
                <a class="text-white border-b-3 border-transparent hover:border-white custom-text-size font-sans pb-2" @click="handleLogout">Log out</a>
            </div>
        </div>
    </nav>
</template>
  
  <script>
  import { logout } from '@/api';

  export default {
    name: 'Navbar',
    methods: {
        async handleLogout() {
            const result = await logout();
            if (result.success) {
                this.$router.push('/');
            } else {
                console.error(result.error);
            }
        }
    }
  };
  </script>

<style>
.custom-text-size {
    font-size: 1.5rem;
}
</style>
  