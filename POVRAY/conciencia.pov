// PoVRay 3.7 Scene File " ... .pov"
// author:  ...
// date:    ...
//--------------------------------------------------------------------------
#version 3.7;
global_settings{ assumed_gamma 1.0 }
#default{ finish{ ambient 0.1 diffuse 0.9 }} 
//--------------------------------------------------------------------------
#include "colors.inc"
#include "textures.inc"
#include "glass.inc"
#include "metals.inc"
#include "golds.inc"
#include "stones.inc"
#include "woods.inc"
#include "shapes.inc"
#include "shapes2.inc"
#include "functions.inc"
#include "math.inc"
#include "transforms.inc"
//--------------------------------------------------------------------------
// camera ------------------------------------------------------------------
#declare Camera_0 = camera {/*ultra_wide_angle*/ angle 75      // front view
                            location  <0.0 , 1.0 ,-3.0>
                            right     x*image_width/image_height
                            look_at   <0.0 , 1.0 , 0.0>}
#declare Camera_1 = camera {/*ultra_wide_angle*/ angle 90   // diagonal view
                            location  <2.0 , 2.5 ,-3.0>
                            right     x*image_width/image_height
                            look_at   <0.0 , 1.0 , 0.0>}
#declare Camera_2 = camera {/*ultra_wide_angle*/ angle 90 // right side view
                            location  <3.0 , 1.0 , 0.0>
                            right     x*image_width/image_height
                            look_at   <0.0 , 1.0 , 0.0>}
#declare Camera_3 = camera {/*ultra_wide_angle*/ angle 90        // top view
                            location  <0.0 , 3.0 ,-0.001>
                            right     x*image_width/image_height
                            look_at   <0.0 , 1.0 , 0.0>}
camera{Camera_0}
// sun ---------------------------------------------------------------------
light_source{<1500,2500,-2500> color White}
// sky ---------------------------------------------------------------------
plane{<0,1,0>,1 hollow  
       texture{ pigment{ bozo turbulence 0.76
                         color_map { [0.5 rgb <0.20, 0.20, 1.0>]
                                     [0.6 rgb <1,1,1>]
                                     [1.0 rgb <0.5,0.5,0.5>]}
                       }
                finish {ambient 1 diffuse 0} }      
       scale 10000}
// fog ---------------------------------------------------------------------
fog{fog_type   2
    distance   50
    color      White
    fog_offset 0.1
    fog_alt    2.0
    turbulence 0.8}
// ground ------------------------------------------------------------------
plane { <0,1,0>, 0 
        texture{ pigment{ color rgb<0.35,0.65,0.0>*0.9 }
	         normal { bumps 0.75 scale 0.015 }
                 finish { phong 0.1 }
               } // end of texture
      } // end of plane
//--------------------------------------------------------------------------
//---------------------------- objects in scene ----------------------------
//--------------------------------------------------------------------------  
sphere { <0,0,0>, 0.5 

        texture { pigment{ color rgb<1.00, 0.55, 0.00>}
                  finish { phong 1.0 reflection 0.00}
                } // end of texture

          scale<1,1,1>  rotate<0,0,0>  translate<0,0.5,5>  
       }  // end of sphere ----------------------------------- 

box { <-1.00, 0.00, -1.00>,< 1.00, 2.00, 1.00>   

      texture { pigment{ color rgb<1.00, 1.00, 1.00>}  
                finish { phong 1 reflection{ 0.00 metallic 0.00} } 
              } // end of texture

      scale <1,1,1> rotate<0,0,0> translate<3,0,5> 
    } // end of box --------------------------------------

box { <-1.00, 0.00, -1.00>,< 1.00, 2.00, 1.00>   

      texture { pigment{ color rgb<0.00, 0.50, 0.20>}  
                finish { phong 1 reflection{ 0.00 metallic 1.00} } 
              } // end of texture

      scale <0.5,0.5,0.5> rotate<0,0,0> translate<-4,0,9> 
    } // end of box --------------------------------------
/*
cylinder { <0,0,0>,<0,2.00,0>, 0.30 

           texture { pigment { color rgb<1,1,1> }
                   //normal  { bumps 0.5 scale <0.005,0.25,0.005>}
                     finish  { phong 0.5 reflection{ 0.00 metallic 0.00} } 
                   } // end of texture

           scale <3,0.01,3> rotate<0,0,0> translate<0,0,0>
         } // end of cylinder -------------------------------------
cylinder { <0,0,0>,<0,2.00,0>, 0.30 

           texture { pigment { color rgb<1,1,1> }
                   //normal  { bumps 0.5 scale <0.005,0.25,0.005>}
                     finish  { phong 0.5 reflection{ 0.00 metallic 0.00} } 
                   } // end of texture

           scale <0.1,0.01,0.1> rotate<0,0,0> translate<0,0,0>
         } // end of cylinder -------------------------------------
         */
// CSG difference, subtract intersections of shapes 2...N from Shape1


