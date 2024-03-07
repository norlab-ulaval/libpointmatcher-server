<template>
    <nav class="bg-white shadow">
        <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">

            <div>
                <img src="/public/norlab_logo_acronym_light.png" alt="logo" class="h-24 w-24">
            </div>

            <div class="flex">
                <a class="text-gray-700 hover:text-blue-500 mx-4" href="#">Home</a>
                <a class="text-gray-700 hover:text-blue-500 mx-4" href="#">Uploads</a>
                <a class="text-gray-700 hover:text-blue-500 mx-4" href="#">Profile</a>
            </div>

            <div>
                <a class="text-gray-700 hover:text-blue-500 mx-4" href="#">Log out</a>
            </div>
        </div>
    </nav>
</template>
  
  <script>
  export default {
    name: 'Navbar',
  };
  </script>
  