
# Vertex Light Blender Add-on

## Description
The Vertex Light add-on is a custom script for Blender that allows you to apply different lighting effects to the vertices of a mesh. It provides options for clearing previous colors, applying light based on angles, adding random noise, and smoothing vertex colors.

# Installation
- Paste the file vertex_light.py into your blender addons folder (../Blender/2.7x/scripts/addons)
- In Blender, go to File -> User Preferences, go to the addon tab and search for "Vertex Light", then check the box on the results.

## Usage
1. Install the add-on in Blender.
2. Select the object you want to apply the vertex lighting effects to.
3. Open the "Object" menu in the 3D Viewport.
4. Click on the "Cursor Array" option.
5. Adjust the available settings in the operator panel to customize the effects:
   - **Selected faces only**: Apply changes only to selected faces.
   - **Clear Previous Color**: Remove existing vertex colors.
   - **Base Color Factor**: How much of the base color to be added.
   - **Base color**: Specify the base color to be added to the vertexes.
   - **Enable Light**: Enable light effects.
   - **Horizontal angle**: Set the horizontal axis angle for the light.
   - **Vertical angle**: Set the vertical axis angle for the light.
   - **Light color**: Specify the color of the light.
   - **Light Amount**: How much of the light will be applied.
   - **Light Angle Allowance**: How much of the angle is allowed for the light.
   - **Enable Noise**: Enable random noise effects.
   - **Black and white noise**: Make the noise black and white.
   - **Noise color**: Specify the color of the noise.
   - **Noise to selected only**: Apply noise only to selected vertices.
   - **Noise intensity**: How much noise will be applied.
   - **Enable Color Smoothing**: Make edges less apparent by smoothing vertex colors.
   - **Only selected vertices**: Apply color smoothing only to selected vertices.
   - **Smooth Amount**: How smooth the colors will be.
6. Click the "Execute" button to apply the vertex lighting effects to the selected object.

## Keymap
The add-on includes a keymap for quick access:
- Press **Ctrl + Shift + Space** in Object Mode to open the operator panel and apply the vertex lighting effects.

# BlenderVertexShingAddon
Blender addon to easily simulate simple light as vertex color.

# Demo
![](demo.gif)

# Links
- Another demo: https://www.youtube.com/watch?v=tOw-9daXfas&t=11s&ab_channel=Zbcrowbarg
- Repository: https://github.com/CristovaoBG/blender-vertex-shading-addon

Developed by Cristóvão B. Gomes
cristovao@live.com
