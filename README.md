# mrshudson

 In the models and world folder, you will see the urdf and sdf files respectively. In both files, update the path of the meshes according to their locations in your system.

For Sherlocks using docker as per our instructions, You all will have a same directory address given by "file:///home/ubuntu/erc_ws/src/mrs_hudson/meshes/".
So You don't need to change any path. To be safer, crosscheck the address of one of your stl files.

For those using any other way of running linux or Any other folders as their workspace:

Use a simple find and replace, eg:

find = "file:///home/ubuntu/erc_ws/src/mrs_hudson/meshes/"

replace with repective addresses of base_link.stl , left_wheel.stl and right_wheel.stl in your system (Easy way to know: just go to the mrs_hudson folder you cloned, then meshes folder, copy the address of stl files). Make sure to not mess up with these, also do check if it was previously right_wheel.stl address then the new address which you are updating should be of right_wheel.stl and not any other stl file. else you get a error :)

Do these replacements in both urdf and sdf files, crosscheck all when you are done. 

