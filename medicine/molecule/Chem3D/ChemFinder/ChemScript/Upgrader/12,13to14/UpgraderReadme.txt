***********************************************************************************************
*                     CambridgeSoft ChemScript/Python Version 14                              *
*                               Migration from v12/13 to v14                                  *
*                                                                                             *
*© 2005-2014 CambridgeSoft Corporation, a subsidiary of PerkinElmer, Inc. All rights reserved.*
***********************************************************************************************

In this file you will find:

   1.  A reference to the set of API changes between v12 and v13, which is under: ..\11to12\UpgraderReadme.txt
   2.  If you want to migrate a script from v11 to v14, please use Upgrader12.py to upgrade it from v11 to v12.
       Then use this tool to migrate it to v14.
   3.  A description of the ChemScript v14 migration tool:

	ChemScript 14 includes a migration tool "UpgradeWizard". which is installed by default in the folder:

	C:\Program Files\CambridgeSoft\ChemOffice2014\ChemScript\Upgrader\12,13to14\
		on 32-bit windows systems, or ;
	C:\Program Files (x86)\CambridgeSoft\ChemOffice2014\ChemScript\Upgrader\12,13to14\
		on 64-bit windows systems.

	This tool can assist you in migrating your script from the ChemScript 12 or 13 API to the
	ChemScript 14 API.  Please note that this tool is not expected or intended to work
	perfectly, rather it is intended as an aid to doing a large portion of the renaming work
	that will need to be done when migrating code from ChemScript 12/13 to ChemScript 14.

	The script creates a new "_14.py"(or corresponding cs) file, renaming any ChemScript function 
	calls that were changed between version 12.0/13.0 and version 14.0.
	
	The steps are:
	1)	Choose all the scripts (*.py|*.cs) that are required to be migrated by the migration wizard.
	2)	Click "Execute" to migrate.
	3)	Migrated files will be generated in the same folder where your original file lives.

	The migration tool is a first step that will do most of the work, but there may be
	additional work that needs to be done in order for the migrated script to function
	correctly.

	Additional notes may be included in the migrated scripts in order to warn about special
	cases such as ambiguous names or deprecated classes or methods.  Be sure to look at the
	migrated scripts to find these comments and address them.

	****************************************************************************************
	*      Please review your script against the "API Reference" pages,                    *
	*      which is available from the "ChemScript 14.0" menu in windows.                  *
	****************************************************************************************
