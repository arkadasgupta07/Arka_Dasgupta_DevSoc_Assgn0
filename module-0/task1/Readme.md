# 3D Image Gallery Project

An interactive 3D image gallery that responds to hover events with depth perception effects. This project demonstrates advanced CSS techniques including 3D transforms, sibling selectors, and the `:has()` pseudo-class.

## Preview

The gallery displays a row of images that initially appear darkened. When you hover over an image:

- The hovered image moves forward (z-axis) and becomes fully visible
- The next three images to the right move forward with decreasing intensity and rotate slightly
- The previous three images to the left also move forward with decreasing intensity and rotate in the opposite direction
- This creates an immersive 3D effect that responds to user interaction

## File Structure

```bash
project-folder/
│
├── index.html
├── styles.css
├── 1.jpg
├── 2.jpg
├── ... (all your image files)
└── README.md
```

---

## Step-by-Step Implementation Guide

### 1. HTML Structure

Create an `index.html` file and add the following code:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="styles.css" />
    <title>3D Image Gallery</title>
  </head>
  <body>
    <main>
      <div class="list">
        <div class="item"><img src="1.jpg" alt="Image 1" /></div>
        <div class="item"><img src="2.jpg" alt="Image 2" /></div>
        <div class="item"><img src="3.jpg" alt="Image 3" /></div>
        <div class="item"><img src="4.jpg" alt="Image 4" /></div>
        <div class="item"><img src="5.jpg" alt="Image 5" /></div>
        <div class="item"><img src="6.jpg" alt="Image 6" /></div>
        <div class="item"><img src="7.jpg" alt="Image 7" /></div>
        <div class="item"><img src="8.jpg" alt="Image 8" /></div>
        <div class="item"><img src="9.jpg" alt="Image 9" /></div>
        <div class="item"><img src="10.jpg" alt="Image 10" /></div>
      </div>
    </main>
  </body>
</html>
```

Explanation:

- The basic HTML structure with viewport meta tag for responsive design
- A `<main>` container to hold our gallery
- A `<div>` with class "list" that will become our 3D container
- Multiple `<div>` elements with class "item", each containing an image

---

### 2. Basic CSS Setup

Create a `styles.css` file and start with these foundational styles:

```css
body {
  background-color: black;
  margin: 0;
  padding: 0;
}

.list {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  min-height: 100vh;
}

.list img {
  width: 130px;
  height: auto;
  border-radius: 6px;
}
```

Explanation:

- Sets a black background for dramatic contrast
- Removes default margin and padding from the body
- Makes the list a flex container to arrange images horizontally
- Centers the gallery both vertically and horizontally
- Adds spacing between images with the gap property
- Ensures the gallery takes the full viewport height
- Styles the images with consistent width and rounded corners

---

### 3. 3D Transformation Setup

Add these styles to enable 3D transformations:

```css
.list {
  transform-style: preserve-3d;
  transform: perspective(1000px);
}
```

Explanation:

- `transform-style: preserve-3d` ensures child elements maintain their 3D position
- `transform: perspective(1000px)` creates a 3D space with a specific depth perspective
- A lower perspective value would create a more dramatic 3D effect

---

### 4. Initial State for Images

Add the initial state for all gallery items:

```css
.list .item {
  transition: 0.5s;
  filter: brightness(0);
}
```

Explanation:

- `transition: .5s` creates smooth animations for all transform and filter changes
- `filter: brightness(0)` makes all images completely black initially

---

### 5. Hover Effects for the Target Image

Add styles for when an image is directly hovered:

```css
.list .item:hover {
  transform: translateZ(200px);
  filter: brightness(1);
}
```

Explanation:

- When hovering over an image, it moves 200px forward on the z-axis
- The brightness filter is removed, making the image fully visible

---

### 6. Sibling Selector Effects

Add styles for the siblings following the hovered image:

```css
.list .item:hover + * {
  transform: translateZ(150px) rotateY(40deg);
  filter: brightness(0.6);
}

.list .item:hover + * + * {
  transform: translateZ(70px) rotateY(20deg);
  filter: brightness(0.4);
}

.list .item:hover + * + * + * {
  transform: translateZ(30px) rotateY(10deg);
  filter: brightness(0.2);
}
```

Explanation:

- `+ *` selects the immediate next sibling
- `+ * + *` selects the sibling after the next one (2nd sibling)
- `+ * + * + *` selects the third sibling
- Each subsequent sibling moves forward less and rotates less
- Each has decreasing brightness to create a depth fade effect

---

### 7. Preceding Sibling Effects with :has() Selector

Add styles for the siblings preceding the hovered image:

```css
.list .item:has(+ *:hover) {
  transform: translateZ(150px) rotateY(-40deg);
  filter: brightness(0.6);
}

.list .item:has(+ * + *:hover) {
  transform: translateZ(70px) rotateY(-20deg);
  filter: brightness(0.4);
}

.list .item:has(+ * + * + *:hover) {
  transform: translateZ(30px) rotateY(-10deg);
  filter: brightness(0.2);
}
```

Explanation:

- `:has(+ *:hover)` selects an element that has an immediate next sibling being hovered
- `:has(+ * + *:hover)` selects an element that has a second next sibling being hovered
- The preceding siblings rotate in the opposite direction (negative values)
- This creates a symmetrical effect around the hovered image

---

### Key Concepts Explored

#### 1. CSS 3D Transforms

- `perspective()`: Creates a 3D space
- `translateZ()`: Moves elements along the z-axis (depth)
- `rotateY()`: Rotates elements around the y-axis (vertical rotation)

#### 2. Advanced CSS Selectors

- Sibling selectors (+) for targeting adjacent elements
- The `:has()` pseudo-class for selecting elements based on their descendants

#### 3. CSS Filters

- `brightness()`: Adjusts the brightness of elements
- Used creatively to enhance the depth perception effect

#### 4. CSS Transitions

- Smoothly animates changes in transform and filter properties

### Customization Ideas

- Adjust the 3D intensity: Change the perspective value and translateZ values
- Modify the animation speed: Adjust the transition duration
- Change the image size: Modify the width of the images
- Experiment with different filters: Try sepia, contrast, or blur filters
- Add borders or shadows: Enhance the visual design with additional effects

---

### Conclusion

This 3D image gallery demonstrates how advanced CSS selectors and 3D transforms can create immersive, interactive experiences without JavaScript. The techniques shown here can be applied to various UI components like menus, carousels, and interactive product displays.
