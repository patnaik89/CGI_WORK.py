#importing maya commands
import maya.cmds as cmds;

#creating bezier curve
cmds.curve(
    bez = True, d = 3,
    p = [ (0, 0, 0),
          (0, 1, 0),
          (1, 1, 0),
          (1, 0, 0) ],
    k = [ 0, 0, 0, 1, 1, 1 ]
);

#get arc length of a Bezier curve
length = cmds.arclen( 'bezier1' );
print length;

#get a list of control point of a Bezier curve; 
cvs = cmds.getAttr ('bezier1.cv[*]');
print cvs;

#scale the curve with factor 2
for i in range(0, 4):
    cvs[i] = (cvs[i][0]*2, cvs[i][1]*2, cvs[i][2]*2) ;

cmds.curve (
    bez = True, d = 3,
    p = cvs,
    k = [ 0, 0, 0, 1, 1, 1 ]
);

#create (1-t)^3, etc…
t = 0.3;
tt = 1-t;
BezFun = (tt*tt*tt, 3*t*tt*tt, 3*t*t*tt, t*t*t);

#draw a sphere at a given location
position = (
    BezFun[0]*cvs[0][0]+BezFun[1]*cvs[1][0]+BezFun[2]*cvs[2][0]+BezFun[3]*cvs[3][0],
    BezFun[0]*cvs[0][1]+BezFun[1]*cvs[1][1]+BezFun[2]*cvs[2][1]+BezFun[3]*cvs[3][1],
    BezFun[0]*cvs[0][2]+BezFun[1]*cvs[1][2]+BezFun[2]*cvs[2][2]+BezFun[3]*cvs[3][2],
);

cmds.sphere (p = position, r=0.1);

#
cmds.sphere (r = 0.1);
for ourtime in range(0, 100):
    cmds.currentTime(ourtime);

t = ourtime/(100.0-1.0);
tt= 1-t;
BezFun = (tt*tt*tt, 3*t*tt*tt, 3*t*t*tt, t*t*t);
position = (
    BezFun[0]*cvs[0][0]+BezFun[1]*cvs[1][0]+BezFun[2]*cvs[2][0]+BezFun[3]*cvs[3][0],
    BezFun[0]*cvs[0][1]+BezFun[1]*cvs[1][1]+BezFun[2]*cvs[2][1]+BezFun[3]*cvs[3][1],
    BezFun[0]*cvs[0][2]+BezFun[1]*cvs[1][2]+BezFun[2]*cvs[2][2]+BezFun[3]*cvs[3][2],
);

cmds.move(position[0], position[1], position[2]);
