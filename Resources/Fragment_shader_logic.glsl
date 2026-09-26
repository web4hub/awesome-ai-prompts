varying vec2 vUv;
uniform vec3 uBaseColor;
uniform vec3 uHighlightColor;

void main() {
    // Center coordinates from -0.5 to 0.5
    vec2 centeredUv = vUv - 0.5;
    
    // Calculate angle for radial rays
    float angle = atan(centeredUv.y, centeredUv.x);
    
    // Create high-frequency fine lines rotating around the center
    float sunburst = sin(angle * 120.0) * 0.5 + 0.5;
    
    // Mix base dial tone with sharp light specular reflections
    vec3 color = mix(uBaseColor, uHighlightColor, sunburst * 0.3);
    
    gl_FragColor = vec4(color, 1.0);
}
