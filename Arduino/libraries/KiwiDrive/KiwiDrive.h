#ifndef KiwiDrive_h
#define KiwiDrive_h

#include "Arduino.h"

class KiwiDrive
{
public: 
	KiwiDrive(int ld[], int rd[], int fd[]);
	
//	void drive(double xcomp, double ycomp, double yaw);             //-1<=xcomp,ycomp<=1  -11.625<=yaw<=11.625
	int convertSpeed(double speed, int dirs[]);
	int getLeft(double xcomp, double ycomp, double yaw);
	int getRight(double xcomp, double ycomp, double yaw);
	int getFront(double xcomp, double ycomp, double yaw);
	
private:
	int * leftDirs;
	int * rightDirs;
	int * frontDirs;
	
	double leftWheelSpeed;
	double rightWheelSpeed;
	double frontWheelSpeed;
};

#endif