function UsersCode(up)

	Methods

	% Enter user code here
	% Find max and min values in array data
	valMax = -0.0000001;
	valMin = 9999999999999.9;

	for index = TopDepth():BottomDepth()
		arrayValues = Array_InCrv_Chunk(index, 1, 1, Array_InCrv_MaxX(), Array_InCrv_MaxY());
		valMin = min(arrayValues(:));
		valMax = max(arrayValues(:));		
	end

	% Calculate the gain and shift to normalize
	gain = 1.0 / (valMax - valMin);
	shift = -gain * valMin;

	% Output new array with normalized values
	for index = TopDepth():BottomDepth()
		arrayValues = Array_InCrv_Chunk(index, 1, 1, Array_InCrv_MaxX(), Array_InCrv_MaxY()) * gain + shift;
		Save_Array_OutCrv_Chunk(index, 1, 1, arrayValues, size(arrayValues, 1), size(arrayValues, 2));
	end

	Save_OutCrv_Comments('Updated by Normalize Array User Prog');
end