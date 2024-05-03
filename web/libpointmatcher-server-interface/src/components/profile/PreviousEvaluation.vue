<template>
    <div>
        <div :class="[this.collapsed ? 'rounded-md': 'rounded-t-md', 'mx-auto px-4 py-2 border-2 border-black dark:border dark:text-gray-200 dark:border-gray-200 overflow-hidden']">
            <div class="flex mx-auto px-4 py-2">
                <button type="button" @click="toggleCollapsed" value="Show evaluation">
                    <i v-if="collapsed">
                        <svg class="w-6 h-6 text-gray-800 dark:text-gray-100" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 8">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="m1 1 5.326 5.7a.909.909 0 0 0 1.348 0L13 1"/>
                        </svg>
                    </i>
                    <i v-else>
                        <svg class="w-6 h-6 text-gray-800 dark:text-gray-100" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 8">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M13 7 7.674 1.3a.91.91 0 0 0-1.348 0L1 7"/>
                        </svg>
                    </i>
                </button>
                <div class="flex grow justify-between mx-auto px-4 py-2 text-lg dark:text-gray-100">
                    <div>{{ this.singleRun.evaluation_name }}</div>
                    <div>{{ formatDate() }}</div>                  
                </div>
            </div>          
        </div>
        <div v-if="!collapsed" class="border-x-2 border-b-2 border-black rounded-b-md dark:border dark:text-gray-200">
          <div class="flex mx-auto px-4 py-2">   
              <div>
                <div class="flex justify-between">
                  <div class="flex me-2 pe-2 py-2">
                    <p class="flex me-2 my-auto">
                      Score :
                    </p>
                    <select class="border-2 border-gray-300 bg-white h-10 rounded-lg text-gray-700 w-44 text-center dark:bg-neutral-800 dark:text-gray-200 dark:border" v-model="selectedRun">
                      <option :value="null" disabled selected hidden>Select Score...</option>                             
                      <option v-for="run in getOrderedRuns()" :value="run">{{ getFormattedRunName(run) }}</option>                              
                    </select>  
                  </div>
                  
                  <div v-if="selectedRun" class="flex ms-2 ps-2 py-2">
                    <p class="flex me-2 my-auto">
                      Iterations :
                    </p> 
                    <select class="border-2 border-gray-300 bg-white h-10 rounded-lg text-gray-700 w-44 text-center dark:bg-neutral-800 dark:text-gray-200 dark:border" v-model="selectedIteration">
                      <option :value="null" disabled selected hidden>Select Iteration...</option>          
                      <option v-for="(iteration, index) in selectedRun.iterations" :value="index">{{ index }}</option>
                    </select>                
                  </div>
                </div>
                <div v-if="getBothSelected()">                          
                  <PointsVisualizer :width="600" :height="400" :data="getSelectedData()" :transform="getSelectedIteration().transformation" :key="this.selectedIteration" />
                </div>
                <div v-else>
                  <PointsVisualizer :width="600" :height="400" :data="[]" />
                </div>                
              </div>
              
              <div class="grow justify-center" v-if="getBothSelected()">
                <div class="flex flex-col h-full justify-center text-3xl">
                  <div class="py-2">{{ "Rotation error : " + formatScore(getSelectedIteration().rotation_error) }}</div>
                  <div class="py-2">{{ "Translation error : " + formatScore(getSelectedIteration().translation_error) }}</div>
                </div>
              </div>                         
          </div>
        </div>
    </div>
</template>

<script>
import PointsVisualizer from '../3d/PointsVisualizer.vue';
import { files } from '@/components/3d/dataLoader'

export default {
  name: 'PreviousEvaluation',
  components: {
    PointsVisualizer,
  },
  props: {
    runs: {
      type: Object,
      required: true,
    },  
  },
  data() {
    return {
      collapsed: true,
      singleRun: null,
      selectedRun: null,
      selectedIteration: null,
    };
  },
  async created() {
    this.singleRun = this.runs[0];  
  },
  methods: {
    toggleCollapsed() {
      this.collapsed = !this.collapsed;
    },
    formatDate() {
      return this.singleRun.date.split('T')[0];
    },
    getAverageScore() {
      return (this.singleRun.iterations[0].rotation_error + this.singleRun.iterations[0].translation_error) / 2;
    },
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    formatScore(score) {
      return score.toFixed(2);
    },
    getOrderedRuns() {  
      return this.runs.sort((a, b) => a.type.localeCompare(b.type));
    },
    getFormattedRunName(run) {
      return this.capitalizeFirstLetter(run.type) + " - " + run.file_name;
    },
    getBothSelected() {
      return this.selectedRun != null && this.selectedIteration != null;
    },
    getSelectedIteration() {
      return this.selectedRun.iterations[this.selectedIteration];
    },
    getSelectedData() {
      return files[this.selectedRun.type][this.selectedRun.file_name]
    }
  },  
  watch: {
    selectedRun: function() {      
      this.selectedIteration = null;
    },    
  },
};
</script>

<style scoped>
.slide-fade-enter-active {
  transition: all 0.3s ease-in;
}

.slide-fade-leave-active {
  transition: all 0.3s ease-in
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateY(-10px);
  opacity: 0;
}
</style>