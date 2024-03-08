<template>
  <div class="flex flex-col items-center justify-center w-full px-72 pt-12">
    <label
      for="dropzone-file"
      :class="[
        'flex flex-col items-center justify-center w-full h-64 border-2 border-dashed rounded-lg cursor-pointer',
        isDragOver ? 'bg-gray-400' : 'bg-gray-50 border-gray-300',
        'hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-600'
      ]"
      @dragover.prevent="isDragOver = true"
      @dragleave.prevent="isDragOver = false"
      @drop.prevent="handleDrop"
    >
      <div class="flex flex-col items-center justify-center pt-5 pb-6">
        <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
        </svg>
        <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload</span> or drag and drop</p>
        <p class="text-xs text-gray-500 dark:text-gray-400">YAML files only</p>
      </div>
      <input
        id="dropzone-file"
        type="file"
        class="hidden"
        @change="handleFiles"
        multiple
        accept=".yml, .yaml"
      />
    </label>
    <div class="text-md text-center mt-4">Files uploaded</div>
    <div class="mt-2 w-40">    
      <ul>
        <li v-for="(file, index) in uploadedFiles" :key="index" class="bg-white w-full text-center mt-2 p-2 rounded-md shadow-md">
          {{ file.name }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      uploadedFiles: [],
      isDragOver: false,
    };
  },
  methods: {
    handleDragOver(event) {
      event.preventDefault();
    },
    handleDrop(event) {
      this.isDragOver = false;
      const files = event.dataTransfer.files;
      this.processFiles(files);
    },
    handleFiles(event) {
      this.processFiles(event.target.files);
    },
    processFiles(files) {
      const fileList = Array.from(files);
      const yamlFiles = fileList.filter(file => file.name.endsWith('.yml') || file.name.endsWith('.yaml'));
      this.uploadedFiles.push(...yamlFiles);

      // TODO: ajouter la logique pour uploader les fichiers
    }
  }
};
</script>

  