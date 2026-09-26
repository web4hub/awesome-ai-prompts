import * as THREE from 'three';
import { RGBELoader } from 'three/examples/jsm/loaders/RGBELoader.js';

// 1. Scene & Renderer Setup with proper tone mapping
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 100);
camera.position.set(0, 0, 5);

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.2;
document.body.appendChild(renderer.domElement);

// 2. Load Studio HDR Environment (Crucial for luxury reflections)
new RGBELoader()
    .load('https://dl.polyhaven.org/file/ph-assets/HDRIs/hdr/1k/studio_small_03_1k.hdr', function (texture) {
        texture.mapping = THREE.EquirectangularReflectionMapping;
        scene.environment = texture;
    });

// 3. Create Watch Components Group
const watchGroup = new THREE.Group();
scene.add(watchGroup);

// --- MATERIAL 1: Brushed Luxury Gold Bezel/Case ---
const bezelMaterial = new THREE.MeshPhysicalMaterial({
    color: 0xd4af37,            // Luxury Gold tone
    metalness: 1.0,
    roughness: 0.25,
    anisotropy: 0.85,           // Stretches highlights circularly
    anisotropyRotation: Math.PI / 2,
    clearcoat: 0.4,
    clearcoatRoughness: 0.1
});

const bezelGeometry = new THREE.CylinderGeometry(1.2, 1.2, 0.2, 64);
const bezelMesh = new THREE.Mesh(bezelGeometry, bezelMaterial);
watchGroup.add(bezelMesh);


// --- MATERIAL 2: Custom Sunburst Dial (Procedural Shader) ---
const sunburstMaterial = new THREE.ShaderMaterial({
    uniforms: {
        uBaseColor: { value: new THREE.Color(0x051c24) },      // Deep midnight blue dial
        uHighlightColor: { value: new THREE.Color(0x40a9ff) }   // Bright sun-ray flash
    },
    vertexShader: `
        varying vec2 vUv;
        void main() {
            vUv = uv;
            gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
        }
    `,
    fragmentShader: `
        varying vec2 vUv;
        uniform vec3 uBaseColor;
        uniform vec3 uHighlightColor;

        void main() {
            vec2 centeredUv = vUv - 0.5;
            float angle = atan(centeredUv.y, centeredUv.x);
            
            // Generate fine micro-grooves that mimic a rayé sunburst dial
            float sunburst = sin(angle * 180.0) * 0.5 + 0.5;
            
            vec3 color = mix(uBaseColor, uHighlightColor, sunburst * 0.25);
            gl_FragColor = vec4(color, 1.0);
        }
    `
});

const dialGeometry = new THREE.CylinderGeometry(1.0, 1.0, 0.02, 64);
const dialMesh = new THREE.Mesh(dialGeometry, sunburstMaterial);
dialMesh.position.y = 0.11;
watchGroup.add(dialMesh);


// --- MATERIAL 3: Sapphire Crystal Glass ---
const crystalMaterial = new THREE.MeshPhysicalMaterial({
    metalness: 0.0,
    roughness: 0.0,
    transmission: 0.98,       // True glass transparency
    thickness: 1.0,           // Optical refraction depth
    ior: 1.77,                // Synthetic sapphire index of refraction
    chromaticAberration: 0.04,// Splits light at edges
    transparent: true,
    opacity: 1.0
});

const crystalGeometry = new THREE.CylinderGeometry(1.18, 1.18, 0.05, 64);
const crystalMesh = new THREE.Mesh(crystalGeometry, crystalMaterial);
crystalMesh.position.y = 0.15;
watchGroup.add(crystalMesh);


// 4. Animation Loop (Rotates the watch to showcase metallic highlights)
function animate() {
    requestAnimationFrame(animate);
    
    watchGroup.rotation.x = 0.3;
    watchGroup.rotation.y += 0.005; // Slow spin to catch studio reflections
    
    renderer.render(scene, camera);
}
animate();

// Handle window resizing
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});
