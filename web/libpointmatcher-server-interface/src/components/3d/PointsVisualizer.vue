<template>
  <div>
    <Dataloader @csv-data="loadPointsData"/>
    <div v-on:mouseenter="entering" v-on:mouseleave="leaving" v-on:mousemove="tryUpdateRender" ref="visualizer"></div>
  </div>
</template>

<script>
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import Dataloader from '@/components/3d/Dataloader.vue';

export default {
  name: 'ThreeJSPoints',
  data() {
    return {
      pointsData: [],
      controls: null,
      holding: false,
      over: false,
    };
  },
  components: {
    Dataloader,
  },
  methods: {
    async loadPointsData(data) {
      if (data != undefined && data != null) {
        this.pointsData = data;
        this.initThree();
      }
    },
    initThree() {    
      //Initialisation de la scène, de la caméra et du rendu  
      this.scene = new THREE.Scene();
      this.camera = new THREE.PerspectiveCamera(70, window.innerWidth / window.innerHeight, 1, 6000);
      this.camera.up.set( 0, 0, 1 );
      this.renderer = new THREE.WebGLRenderer();
      this.renderer.setSize(window.innerWidth, window.innerHeight);
      this.$refs.visualizer.appendChild(this.renderer.domElement);
      
      //Initialisation des contrôles
      this.controls = new OrbitControls(this.camera, this.renderer.domElement)
      this.controls.enableDamping = true;
      this.controls.dampingFactor = 0.25;
      this.controls.enableZoom = true;
      this.controls.rotateSpeed = 0.35;
    
      this.renderPoints();

      this.camera.position.z = 5;
    },
    renderPoints() {    
      const material = new THREE.PointsMaterial({ color: 0xff0000, size: 0.1 });
      const geometry = new THREE.BufferGeometry();
      
      const positions = new Float32Array(this.pointsData.length * 3);

      for (let i = 0; i < this.pointsData.length; i++) {
        positions[i * 3] = this.pointsData[i].x;
        positions[i * 3 + 1] = this.pointsData[i].y;
        positions[i * 3 + 2] = this.pointsData[i].z;
      }

      geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

      const points = new THREE.Points(geometry, material)

      this.scene.add(points);

      this.updateRender();
    },
    updateRender() {
      this.camera.aspect = window.innerWidth / window.innerHeight;
      this.camera.updateProjectionMatrix();
      this.renderer.setSize(window.innerWidth, window.innerHeight);
      this.renderer.render(this.scene, this.camera);
      this.controls.update();
    },
    entering() {
      this.over = true;
    },
    leaving() {
      this.over = false;
    },
    tryUpdateRender() {
      if (this.holding) {
        this.overUpdateRender();
      }
    },
    overUpdateRender() {
      if (this.over) {
        this.updateRender();
      }
    },
  },
  mounted() {
    window.addEventListener('resize', () => {
      this.updateRender();
    });
    window.addEventListener('mousedown', () => {
      this.holding = true;
    });
    window.addEventListener('mouseup', () => {
      this.holding = false;
    });
    window.addEventListener('wheel', () => {
      this.overUpdateRender();
    });
  },
};
</script>
