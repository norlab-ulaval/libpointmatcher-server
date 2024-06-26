<template>
  <WarningToast :show="showWarningToast" :message="warningMessage" />
  <h1 class="text-3xl font-bold text-center mb-4 mt-8 dark:text-gray-100">Configuration Upload</h1>

  <div class="w-full px-96 pt-4">
    <label
      for="dropzone-file"
      :class="[
        'flex flex-col items-center justify-center w-full h-64 border-2 border-dashed rounded-lg cursor-pointer',
        isDragOver ? 'bg-gray-400' : 'bg-gray-50 border-gray-300 dark:border-gray-400',
        'hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-800'
      ]"
      @dragover.prevent="isDragOver = true"
      @dragleave.prevent="isDragOver = false"
      @drop.prevent="handleDrop"
    >
      <div class="flex flex-col items-center justify-center pt-5 pb-6">
        <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
        </svg>
        <p class="mb-2 text-sm text-gray-500 dark:text-gray-200"><span class="font-semibold">Click to upload</span> or drag and drop</p>
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
    <div class="px-4 py-2 min-h-24 pt-4">
      <div class="text-lg font-semibold mb-2 dark:text-gray-100">Files:</div>
      <ul>
        <li v-for="(file, index) in uploadedFiles" :key="index" class="flex items-center p-2 bg-gray-100 rounded-lg mb-2 shadow dark:bg-neutral-800">
          <svg class="w-6 h-6 text-gray-800 dark:text-white mr-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 3v4a1 1 0 0 1-1 1H5m4 8h6m-6-4h6m4-8v16a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V7.914a1 1 0 0 1 .293-.707l3.914-3.914A1 1 0 0 1 9.914 3H18a1 1 0 0 1 1 1Z"/>
          </svg>
          <div class="flex-grow">
            <div class="font-medium text-base/7 dark:text-gray-100">{{ file.name }}</div>
            <div class="text-sm text-gray-600 dark:text-gray-100">{{ (file.size / 1024).toFixed(2) }} KB</div>
          </div>
          <button @click="removeFile(index)" class="ml-2">
            <svg class="w-6 h-6 text-gray-800 hover:text-red-600 dark:text-gray-100" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </li>
      </ul>
    </div>
    <div class="flex justify-between items-center my-4 px-4">
      <div class="flex items-center">
        <input 
        id="anonymous" 
        type="checkbox" 
        class="w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-800 dark:border-gray-700"
        :disabled="uploadedFiles.length === 0"
        >
        <label for="anonymous" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Anonymous</label>
      </div>
      <button @click="runConfigurations" :disabled="uploadedFiles.length === 0 || isRunning" class="inline-flex items-center px-4 py-2 bg-blue-600 border border-transparent rounded-md font-semibold text-xs text-white uppercase tracking-widest hover:bg-blue-700 active:bg-blue-900 focus:outline-none focus:border-blue-900 focus:ring ring-blue-300 disabled:opacity-75 transition ease-in-out duration-150 dark:bg-gray-700 dark:hover:bg-gray-600">
        <template v-if="isRunning">
          <div class="animate-spin inline-block size-4 border-[3px] border-current border-t-transparent text-white rounded-full" role="status" aria-label="loading"></div>
          <span class="ms-3">Loading</span>
        </template>
        <template v-else>Run</template>
      </button>
    </div>
  </div>
</template>

<script>
import WarningToast from '@/components/ui/WarningToast.vue';
import { transferFile } from '@/api';
export default {
  components: {
      WarningToast,
  },
  data() {
    return {
      uploadedFiles: [ ],
      isDragOver: false,
      showWarningToast: false,
      warningMessage: '',
      isRunning: false,
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

      event.target.value = null;
    },
    processFiles(files) {
      const fileList = Array.from(files);
      const yamlFiles = fileList.filter(file => file.name.endsWith('.yml') || file.name.endsWith('.yaml'));   

      yamlFiles.forEach(async file => {
        const fileExists = this.uploadedFiles.some(existingFile => existingFile.name === file.name);
        if (fileExists) {
          this.displayToast(`A file named "${file.name}" has already been uploaded.`);
        } else {
          this.uploadedFiles.push(file);
        }

      });
    },
    removeFile(index) {
      this.uploadedFiles.splice(index, 1);
    },
    async runConfigurations() {
      this.isRunning = true;
      try {
        for (const file of this.uploadedFiles) {
          await this.convertAndTransferFile(file);
        }
        this.$router.push({ name: 'profile'});
      } catch(error) {
        this.displayToast(`Failed to process files`);
        console.error('Failed to process files:', error);
      } finally {
        this.isRunning = false;
      }
    },

    async convertAndTransferFile(file) {
      try {
        const base64Data = await this.readFileAsBase64(file);
        transferFile(base64Data, document.getElementById('anonymous').checked, file.name);
        console.log(document.getElementById('anonymous').checked)
        
      } catch (error) {
        this.displayToast(`Failed to process files`);
        console.error('Error reading file:', error);
        throw error;
      }
    },

    readFileAsBase64(file) {
      return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(btoa(reader.result));
        reader.onerror = error => reject(error);
        reader.readAsBinaryString(file);
      });
    },
    displayToast(message) {
      this.warningMessage = message;
      this.showWarningToast = true;
      setTimeout(() => {
      this.showWarningToast = false;
      }, 3000);
    },
  }
};
</script>

<style>
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s;
  }
  .fade-enter-from, .fade-leave-to {
    opacity: 0;
  }
  </style>  