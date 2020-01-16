***********************************************************************************************
*                     CambridgeSoft ChemScript/Python Version 12                              *
*                               Migration from v11 to v12                                     *
*                                                                                             *
*                   © 2005-2009 CambridgeSoft Corp., All Rights Reserved.                     *
***********************************************************************************************

In this file you will find:

   1.  A summary of the main changes between version 11 and version 12.
   2.  Instructions describing how to use the provided migration tool: "Upgrader12.py"


1. --------------------------------------------------------------------------------------------

	The main aspects of the migration from ChemScript11 to ChemScript12 are:

	* ‘import’ versionless ChemScript is no longer supported from ChemScript 12.
	  All “import ChemScript” statements must be replaced with “import ChemScript12”.

	* All the method names were capitalized.

	* The “Molecule” class and "Mol" nickname were renamed to “StructureData”.

	* The “Reaction” class and “Rxn” nickname were renamed to “ReactionData”.

	* SDFileWriter’s methods “writeMol” and “writeMols” were renamed to “WriteStructure”
	   and “WriteStructures” respectively.

	* RDFileWriter’s methods “writeMol” and “writeMols” were renamed to “WriteReaction”
	   and “WriteReactions” respectively.

	* "LargestCommonSubstructure"’s property “mol” was renamed to “CommonSubstructure”.

	* The following classes from ChemScript 11.5 have been removed for this release:
	   Chain, Color, DocProp, Document, ExcelWriter, Font, Group, MacroMol and SuperAtom.

	* The following methods and properties from ChemScript 11.5 have been removed for
           this release:
	     *    Atom --> getParent()
	     *    Molecule --> aminoAcids()
	     *    Molecule --> bases()
	     *    Molecule --> getAminoAcid()
	     *    Molecule --> getBase()
	     *    Reaction --> units()
	     *    SearchOptions --> ignoreImplicitH
	     *    SearchOptions --> similar
	     *    SearchOptions --> similarThresholdPercent
	     *    NormOptions --> labelH

2. ---------------------------------------------------------------------------------------------

	ChemScript 12 provides a migration tool. The script "Upgrader12.py" is installed by
	default in the following folder:

	C:\Program Files\CambridgeSoft\ChemOffice2010\ChemScript 12\Migration from v11 to v12


	This tool can assist you in migrating your script from the ChemScript 11 API to the
	ChemScript 12 API.  Please note that this tool is not expected or intended to work
        perfectly, rather it is intended as an aid to doing a large portion of the renaming work
        that will need to be done when migrating code from ChemScript 11 to ChemScript 12.

	The script creates a new "_12.py" file, renaming any ChemScript function calls
	that were changed between version 11.0 and version 12.0.
	
	The file “Upgrader12.py” searches the current folder for any “.py” Python files and
	creates a new migrated “_12.py” file for every Python file found.

	Then every Python file present in the current folder (except the upgrader and the files
	whose names end with “_12.py”) will be migrated.

	The steps are:

	1)     Put all the scripts (*.py) that are required to be migrated in the same folder
	       as the “Upgrader12.py” is.
	2)     Execute “Upgrader.py”
	3)     Execute every new “<name>_12.py” file migrated (for testing).

	Then there are two ways to do this:

	a)     Copy all the scripts that are required to be migrated to this folder and execute
	       the migration tool.

	b)     Copy the provided script (Upgrader.py) to every folder that contains v11 scripts
	       that are required to be migrated, then run the migration script in each folder.

	The migration tool is a first step that will do most of the work, but there may be
	additional work that needs to be done in order for the migrated script to function
	correctly.

	Additional notes may be included in the migrated scripts in order to warn about special
	cases such as ambiguous names or deprecated classes or methods.  Be sure to look at the
	migrated scripts to find these comments and address them.

	****************************************************************************************
	*                                                                                      *
	*      Please review your script against the API reference file ChemScript12.htm.      *
	*                                                                                      *
	****************************************************************************************
