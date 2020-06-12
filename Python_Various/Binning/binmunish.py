###########################################################################
#    Copyright (C) 2008 by Peter Wood                                      
#    <pjw110@grenache.anu.edu.au>                                                             
#
# Copyright: See COPYING file that comes with this distribution
#
###########################################################################
from math import log10, floor


def ReadTSV(filename, ignorefirstline = True): 
  """
  Function to read a 6 column TSV (tab separated value) file.
  """
  xdata = []
  y0data = []
  y1data = []
  y2data = []
  y3data = []
  y4data = []
  file = open( filename, 'r' )
  try:
    lines = file.readlines()
    for step in range(len(lines)):
      if step == 0 and ignorefirstline:
        continue
      line = lines[step]
      linesplit = line.split('\t')
      assert len(linesplit) == 6
      #print linesplit[0]
      #print linesplit[1]
      xdata.append( float(linesplit[0]) )
      y0data.append( float(linesplit[1]) )
      y1data.append( float(linesplit[2]) )
      y2data.append( float(linesplit[3]) )
      y3data.append( float(linesplit[4]) )
      y4data.append( float(linesplit[5]) )
  finally:
    file.close()
  return (xdata, y0data, y1data, y2data, y3data, y4data)

def LogBinFile(filename, numbins, ignorefirstline = True): 
  """
  Function to logbin a 2 column TSV (tab separated value) file.
  
  bin_value = floor( num_bins * log10(xvalue)/log10(highestvalue) )
  """
  (xdata, y0data, y1data, y2data, y3data, y4data) = ReadTSV(filename, ignorefirstline)
  ylist = [y0data, y1data, y2data, y3data, y4data]
  outputlist = []
  for ydata in ylist:
    output, binstep = Run_log_bin( xdata, ydata, numbins)
    outputlist.append( output )
  return ( outputlist, binstep )

def Run_log_bin( xdata, ydata, numbins, countvalue = 1 ):
  output = range(numbins+1)
  for step in range(len(output)):
    output[step] = 0
  highestvalue = 10**( floor(log10(xdata[-1])+1) ) #assume xdata sorted, increasing
  for step in range(len(xdata)):
    xval = xdata[step]
    yval = ydata[step]
    binvalue = int(floor( numbins * log10(xval)/log10(highestvalue) ))
    if ydata[step] == countvalue:
      output[binvalue] += 1
  binstep = highestvalue**(1./numbins)
  return output, binstep


def SaveOutput( output, binstep, filename ):
  """
  saves output to filename
  """
  file = open( filename, 'w' )
  try:
    for step in range(len(output)):
      file.write("%10g \t %10g\n"%(binstep**step, output[step]))
  finally:
    file.close()

def ProcessFile( inputfilename, outputfilename, numbins, ignorefirstline = True ):
  """
  reads file, bins its, saves outputted data
  """
  (outputlist, binstep) = LogBinFile( inputfilename, numbins, ignorefirstline )
  filenamelist = [outputfilename+"1.txt", outputfilename+"2.txt", outputfilename+"3.txt", outputfilename+"4.txt",  outputfilename+"5.txt" ]
  #print output
  for step in range(len(outputlist)):
    output = outputlist[step]
    outputfilename = filenamelist[step]
    SaveOutput( output, binstep, outputfilename )

if __name__ == '__main__':
  ProcessFile( '184_US.txt', '184_US_b.txt', 50 )
