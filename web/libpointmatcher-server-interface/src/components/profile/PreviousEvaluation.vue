<template>
    <div>
        <div :class="this.headerClass">
            <div class="flex mx-auto px-4 py-2">
                <button type="button" @click="toggleCollapsed" value="Show evaluation">
                    <i v-if="collapsed">
                        <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 8">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="m1 1 5.326 5.7a.909.909 0 0 0 1.348 0L13 1"/>
                        </svg>
                    </i>
                    <i v-else>
                        <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 8">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M13 7 7.674 1.3a.91.91 0 0 0-1.348 0L1 7"/>
                        </svg>
                    </i>
                </button>
                <div class="flex grow justify-between mx-auto px-4 py-2">
                    <div>{{ this.singleRun.evaluation_name }}</div>
                    <div>{{ formatDate() }}</div>                  
                </div>
            </div>          
        </div>
        <div v-if="!collapsed" class="border-x-2 border-b-2 border-black rounded-b-md">
          <div class="flex mx-auto px-4 py-2">   
              <div>
                <select class="border-2 border-gray-300 bg-white h-10 rounded-lg text-gray-700 w-44 text-center" v-model="selectedRun">
                  <option value="" disabled>Score type</option>         
                  <option v-for="run in getOrderedRuns()" :value="run">{{ getFormattedRunName(run) }}</option>                              
                </select>  
                
                Iterations
                <select v-if="selectedRun" class="border-2 border-gray-300 bg-white h-10 rounded-lg text-gray-700 w-44 text-center" v-model="selectedIteration">
                  <option value="" disabled>Run</option>         
                  <option v-for="(iteration, index) in selectedRun.iterations" :value="index">{{ index }}</option>
                </select>                
                <div v-if="getBothSelected()">                          
                  <PointsVisualizer :width="600" :height="400" :data="csvData" :transform="getSelectedIteration().transformation" />
                </div>
                <div v-else>
                  <PointsVisualizer :width="600" :height="400" :data="csvData" />
                </div>
                
              </div>
              
              <div class="grow justify-center" v-if="getBothSelected()">
                <div class="flex flex-col h-full justify-center">
                  <div>{{ "Rotation error : " + getSelectedIteration().rotation_error }}</div>
                  <div>{{ "Translation error : " + getSelectedIteration().translation_error }}</div>
                </div>
              </div>                         
          </div>
        </div>
    </div>
</template>

<script>
import PointsVisualizer from '../3d/PointsVisualizer.vue';

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
    csvData: {
      type: Array,
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
    //await this.fetchData();
    console.log("Evalutation in sub-componenent...");
    console.log(this.runs)
    this.singleRun = this.runs[0];  
  },
  mounted() {
    //console.log("Evalutation in sub-componenent...");
    //console.log(this.runs);
    console.log("Mounted")
    

  },
  methods: {
    async fetchData() {
      /*const response = await getEvaluations();
      if (response.success) {
        this.evaluations = response.evaluations;
      } else {
        console.error(response.error);
      }*/
    },
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
      return (score * 100).toFixed(2);
    },
    getOrderedRuns() {
      console.log("getting ordered runs...")
      return this.runs.sort((a, b) => a.type.localeCompare(b.type));
    },
    getFormattedRunName(run) {
      return this.capitalizeFirstLetter(run.type) + " - " + run.file_name;
    },
    getBothSelected() {
      return this.selectedRun != null && this.selectedIteration != null;
    },
    getSelectedIteration() {
      console.log("Getting selected transformation...")
      console.log("Selected run")
      console.log(this.selectedRun)
      console.log("Selected iteration")
      console.log(this.selectedIteration)
      console.log("Selected iteration in run")
      console.log(this.selectedRun.iterations[this.selectedIteration])
      console.log("Transformation")
      console.log(this.selectedRun.iterations[this.selectedIteration].transformation)

      return this.selectedRun.iterations[this.selectedIteration];
    }
  },
  computed: {
    headerClass() {
      if (this.collapsed) {
        return 'mx-auto px-4 py-2 border-2 border-black rounded-md';
      }
      return 'mx-auto px-4 py-2 border-2 border-black rounded-t-md';
    },
  },
  watch: {
    selectedRun: function() {
      console.log("Selected run changed")
      console.log(this.selectedRun)
      this.selectedIteration = null;
    },
    selectedIteration: function() {
      console.log("Selected iteration changed")
      console.log(this.selectedIteration)
    }
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