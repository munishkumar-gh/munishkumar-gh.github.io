unit UsersCode;

interface

uses Functions, Math;

Procedure UserCode; stdcall;

implementation

{User Code}
Procedure UserCode; stdcall;
Var
   index, Ix, IY : Integer;
   gain, shift, R, valmin, valmax : Single;
begin
   {enter user code here}
   {find max and min values in array data}
      ValMax := -0.0000001;
      ValMin := 9999999999999.9;        
      for index := Topdepth to BottomDepth do begin
         for IX := 1 to Array_InCrv_MaxX do begin
            for IY := 1 to Array_InCrv_MaxY do begin
               R := Array_InCrv(Index,Ix,Iy);
               if (R < ValMin) and (R <> -999.0) then
                  ValMin := R;
               if (R > ValMax) and (R <> -999.0) then
                  ValMax := R;
            end;
         end; 
      end;
   {calculate the gain and shift to normalize}
      gain := 1.0 / (Valmax - Valmin);
      shift := - gain * Valmin; 
   {output new array with normalized values}
      for index := Topdepth to BottomDepth do begin
         for IX := 1 to Array_InCrv_MaxX do begin
            for IY := 1 to Array_InCrv_MaxY do begin
               R := Array_InCrv(Index,Ix,Iy) * Gain + shift;
               Save_array_OutCrv(Index,Ix,Iy,R);
            end;
         end;
      end;
   Save_OutCrv_Comments('Updated by Normalize Array User Prog');
end;

end.
