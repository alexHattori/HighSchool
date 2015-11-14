

#include "Arduino.h"
#include "KiwiDrive.h"

KiwiDrive::KiwiDrive(int ld[], int rd[], int fd[]){
	
	leftDirs = ld;
	rightDirs = rd;
	frontDirs = fd;
	
	leftWheelSpeed = leftDirs[1];
	rightWheelSpeed = rightDirs[1];
	frontWheelSpeed = frontDirs[1];
}

/* void KiwiDrive::drive(double xcomp, double ycomp, double yaw){
	
	rightWheelSpeed = ((xcomp/3.0)+(0.57735*ycomp)+(8.0*yaw/93.0));
	leftWheelSpeed = ((xcomp/3.0)-(0.57735*ycomp)+(8.0*yaw/93.0));
	frontWheelSpeed = ((-2.0*xcomp/3.0)+(8.0*yaw/93.0));
	
	leftServo.writeMicroseconds(convertSpeed(leftWheelSpeed,leftDirs));
	rightServo.writeMicroseconds(convertSpeed(rightWheelSpeed,rightDirs));
	frontServo.writeMicroseconds(convertSpeed(frontWheelSpeed,frontDirs));

} */
int KiwiDrive::getLeft(double xcomp, double ycomp, double yaw){
	leftWheelSpeed = ((xcomp/3.0)-(0.57735*ycomp)+(8.0*yaw/93.0));
	return convertSpeed(leftWheelSpeed,leftDirs);
}
int KiwiDrive::getRight(double xcomp, double ycomp, double yaw){
	rightWheelSpeed = ((xcomp/3.0)+(0.57735*ycomp)+(8.0*yaw/93.0));
	return convertSpeed(rightWheelSpeed,rightDirs);
}
int KiwiDrive::getFront(double xcomp, double ycomp, double yaw){
	frontWheelSpeed = ((-2.0*xcomp/3.0)+(8.0*yaw/93.0));
	return convertSpeed(frontWheelSpeed,frontDirs);
}
int KiwiDrive::convertSpeed(double speed, int dirs[]){
	if(speed>0){
		return int(((dirs[2]-dirs[1])*abs(speed))+dirs[1]);
	}
	else if(speed<0){
		return int(dirs[1]-((dirs[1]-dirs[0])*abs(speed)));
	}
	else{
		return dirs[1];
		
	}
}