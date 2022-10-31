# Stereo Camera Depth
_Computational Robotics Computer Vision Project_ - Krishna Suresh and Allyson Hur

## Goal

## Method


### Design Decision


## Results


### Images Rectification

<p float="left">
    <img src="images/mac126/left.png" width = 360px >
    <img src="images/mac126/right.png" width = 360px >
</p>
<p float="left">
    <img src="images/mac126/rect_left.png" width = 360px >
    <img src="images/mac126/rect_right.png" width = 360px >
</p>

### Comparison of different kernels
<p float="left">
3x3:
    <img src="images/mac126/dispk3o80.png"  alt="3" width = 240px >
6x6:
    <img src="images/mac126/dispk6o80.png" alt="6" width = 240px >
10x10:
    <img src="images/mac126/dispk10o80.png" alt="10" width = 240px >
30x30:
    <img src="images/mac126/dispk30o80.png" alt="30" width = 240px >
</p>

### Different Correspondence Search Ranges
Fix kernel size to 10x10px
<p float="left">
10px:
    <img src="images/mac126/dispk10o10.png"  alt="3" width = 180px >
30px:
    <img src="images/mac126/dispk10o30.png"  alt="3" width = 180px >
80px:
    <img src="images/mac126/dispk10o80.png" alt="6" width = 180px >
200px:
    <img src="images/mac126/dispk10o200.png" alt="10" width = 180px >
480px:
    <img src="images/mac126/dispk10o480.png" alt="30" width = 180px >
</p>

### Other Tests
Raw left image | 15x15 kernel SSD | OAK-D DepthAI
<p float="left">
    <img src="images/case/left.png" width = 360px >
    <img src="images/case/dispk15o80.png" width = 360px >
    <img src="images/case/dai.png" width = 360px >
</p>
<p float="left">
    <img src="images/proto/left.png" width = 360px >
    <img src="images/proto/dispk15o80.png" width = 360px >
    <img src="images/proto/dai.png" width = 360px >
</p>
<p float="left">
    <img src="images/wood/left.png" width = 360px >
    <img src="images/wood/dispk15o80.png" width = 360px >
    <img src="images/wood/dai.png" width = 360px >
</p>

### Challenges
### Improvements

### Lessons


## Resources