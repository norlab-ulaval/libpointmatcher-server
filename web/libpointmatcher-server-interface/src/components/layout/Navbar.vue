<template>
    <nav class="shadow w-full" style="background-color: #515151;">
        <div class="flex items-center justify-between px-10 py-2 mx-auto">

            <div class="pl-8">
                <img src="/public/norlab_logo_acronym_light.png" alt="logo" class="h-auto" style="width: 11rem;">
            </div>

            <div class="flex items-center mr-auto ml-8"> 
                <a class="text-white hover:text-blue-500 text-xl mr-8 font-mono" href="#">HOME</a>
                <a class="text-white hover:text-blue-500 text-xl mr-8 font-mono" href="#">UPLOADS</a>
                <a class="text-white hover:text-blue-500 text-xl font-mono" href="#">PROFILE</a>
            </div>

            <div class="pr-8">
                <a class="text-white hover:text-blue-500 text-xl font-mono" href="#">LOG OUT</a>
            </div>
        </div>
    </nav>
</template>
  
  <script>
  export default {
    name: 'Navbar',
  };
  </script>
  