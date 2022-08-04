function UsersCode(up)

	Methods

	for index = TopDepth()+1:BottomDepth()
		% Enter user code here
		% Check for curve equal to zero
		if numCrv(index)-numCrv(index-1) == 0.0
			Save_DiffCrv(index, -999);
		elseif denCrv(index)-denCrv(index-1) == 0.0
			Save_DiffCrv(index, -999);
		else
			% Calculate the first derivative
			Save_DiffCrv(index, (numCrv(index)-numCrv(index-1)) / (denCrv(index)-denCrv(index-1)));
		end;
	end;

	Save_DiffCrv_Comments('Curve Written by User Program');
end