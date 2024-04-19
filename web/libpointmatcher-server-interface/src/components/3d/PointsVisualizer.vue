<template>
  <div>
    <div v-on:mouseenter="entering" v-on:mouseleave="leaving" v-on:mousemove="tryUpdateRender" ref="visualizer"></div>    
  </div>
</template>

<script>
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';

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
  props: {
    width: {
      type: Number,
      required: true,
    },
    height: {
      type: Number,
      required: true,
    },
    data: {
      type: Array,
      required: true,
    },
    transform: {
      type: Array,
      required: false,
      default: [],
    }
  },  
  methods: {    
    initThree() {    
      //Initialisation de la scène, de la caméra et du rendu  
      this.scene = new THREE.Scene();
      this.camera = new THREE.PerspectiveCamera(70, this.width / this.height, 1, 6000);
      this.camera.up.set( 0, 0, 1 );
      this.renderer = new THREE.WebGLRenderer();
      this.renderer.setSize(this.width, this.height);
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
    renderPoints(color = 0xff0000) {    
      const material = new THREE.PointsMaterial({ color: color, size: 0.1 });
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
      this.camera.aspect = this.width / this.height;
      this.camera.updateProjectionMatrix();
      this.renderer.setSize(this.width, this.height);
      this.renderer.render(this.scene, this.camera);
      this.controls.update();
    },
    applyTransform() {      
      this.pointsData.forEach((point) => {
        const x = (point.x * this.transform[0][0]) + (point.y * this.transform[0][1]) + (point.z * this.transform[0][2]) +  this.transform[0][3];
        const y = (point.x * this.transform[1][0]) + (point.y * this.transform[1][1]) + (point.z * this.transform[1][2]) +  this.transform[1][3];
        const z = (point.x * this.transform[2][0]) + (point.y * this.transform[2][1]) + (point.z * this.transform[2][2]) +  this.transform[2][3];
        const w = (point.x * this.transform[3][0]) + (point.y * this.transform[3][1]) + (point.z * this.transform[3][2]) +  this.transform[3][3];

        point.x = x/w;
        point.y = y/w;
        point.z = z/w;
      });

      this.renderPoints(0x3884ff);
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

    if (this.data != undefined && this.data != null) {
      this.pointsData = JSON.parse(JSON.stringify(this.data));
      this.initThree();
      this.updateRender();
      this.applyTransform();
    }
  },
  watch: {
    data: function() {
      this.pointsData = JSON.parse(JSON.stringify(this.data));
      this.renderPoints();
    },    
  },
};
</script>
