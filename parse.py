#!/Library/Frameworks/EPD64.framework/Versions/Current/bin/python
import profileParser
import os
import sys

if __name__ == "__main__":


	profile = os.path.join(os.path.split(os.path.realpath(__file__))[0],'CTPAnonimizationProfile.xml')

	parse = profileParser.ctpparser(profile)
	print parse._printParameters()
	dicom = sys.argv[1]
	
	targetDicom = sys.argv[2]
	parse.anonymizeDicom(dicom,targetDicom)
	#parse._printParameters()

	
