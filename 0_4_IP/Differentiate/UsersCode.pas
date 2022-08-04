unit UsersCode;

interface

uses Functions, Math;

Procedure UserCode; stdcall;

implementation

{User Code}
Procedure UserCode; stdcall;
Var
   index : Integer; 
   num1,num2,den1,den2: Real;
begin
   for index := Topdepth+1 to BottomDepth do begin
   {enter user code here}
	{ assign curve values to variables}
	num1 := numCrv(index);
	num2 := numCrv(index-1);
	den1 := denCrv(index);
	den2 := denCrv(index-1);
      {check for curve equal to zero}
      if num1 - num2 = 0.0 then 
         Save_DiffCrv(index,-999)
	  else if den1 - den2 = 0.0 then 
         Save_DiffCrv(index,-999)
      else
      {Calculate the first derivative}
         Save_DiffCrv(index,(num1-num2)/(den1-den2));

      end;
    Save_DiffCrv_Comments('Curve Written by User Program');
end;

end.
