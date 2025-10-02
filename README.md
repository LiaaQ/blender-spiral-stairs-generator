# Spiral Staircase Generator – Blender Add-on

A simple Blender plugin for generating customizable spiral staircases.  

![Preview](./media/3d.png)  
![Demo Video](./media/3d.mp4)  

---

## User Documentation

This Blender add-on allows you to generate a spiral staircase made of cuboid steps.  
You can customize parameters such as step count, width, depth, height, and spiral radius.  

### Installation
1. Place the downloaded folder into the Blender addons directory: ``..../Blender/version/scripts/addons``
2. In Blender, go to **Edit > Preferences > Add-ons** and enable **Spiral Staircase Generator**.  

### Usage
1. In the 3D Viewport, press **N** to open the right panel.  
2. Switch to the **Staircase** tab.  
3. Adjust the parameters as desired.  
4. Click **Generate Spiral Staircase** to create your staircase.  

#### Parameters
- **Step Count** – number of steps  
- **Step Width** – width of a step  
- **Step Depth** – depth of a step  
- **Step Height** – height of a step  
- **Radius** – staircase curvature radius  

---

## Development Notes
- This add-on was created as a small Blender project.  
- It uses Python, Blender’s operator system, and a custom UI panel for parameter input.
