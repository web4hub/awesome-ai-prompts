# Prompt: Three.js Luxury Watch Procedural Shader & Material Suite

## Category
Computer Graphics / WebGL / Three.js Shading

## Description
Generates a complete, high-end production setup for rendering luxury watch components (brushed gold bezels with anisotropic highlights, synthetic sapphire crystal with physical refraction and chromatic aberration, and custom polar sunburst dials) using plain Three.js.

---

## The Prompt

```aprompt
Act as an expert WebGL and Three.js graphics engineer specializing in high-end product configurators and physically based rendering (PBR). 

Write a complete, optimized implementation in plain Three.js (ES module syntax) that renders a luxury watch head setup containing the following three precise material and geometry layers:

1. Brushed Luxury Gold Bezel/Case:
   - Use THREE.MeshPhysicalMaterial.
   - Configure a luxury gold color tone.
   - Set full metalness, optimized roughness, and configure high anisotropy with rotation aligned circularly along the tangent plane to mimic a radial brushed metal finish.
   - Add controlled clearcoat parameters for polished edges.

2. Custom Procedural Sunburst Dial:
   - Use a custom THREE.ShaderMaterial.
   - Implement polar coordinate conversion in the fragment shader to compute radial angles from centered UVs (`atan(centeredUv.y, centeredUv.x)`).
   - Generate fine high-frequency repeating micro-grooves using sine waves (`sin(angle * frequency)`) to create the characteristic light-scattering rayé / sunburst effect.
   - Expose uniforms for base dial color and specular highlight color.

3. Synthetic Sapphire Crystal Glass:
   - Use THREE.MeshPhysicalMaterial with high transmission (near 1.0) and optical thickness.
   - Set the index of refraction (IOR) to precisely match synthetic sapphire (~1.77).
   - Enable chromatic aberration to handle physical dispersion splitting on the edges.

4. Scene Environment & Renderer Setup:
   - Configure a WebGLRenderer with ACESFilmicToneMapping and appropriate exposure.
   - Load an HDRI studio environment map asynchronously using RGBELoader for realistic reflections.
   - Implement a continuous animation loop showcasing smooth rotational movement to emphasize metallic anisotropy and refraction highlights.
