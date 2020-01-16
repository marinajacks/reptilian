#---------------------------------------------------------------------------------------
# This script assists you in migrating your script from the ChemScript 11 API to
# the ChemScript 12 API.
# The script creates a new "_12.py" file, renaming any ChemScript function calls
# that were changed between version 11.0 and version 12.0.
# Additionally, the script also changes any imports of ChemScript to explicitly
# import ChemScript12 as the generic versionless import for ChemScript is no
# longer supported.
# The correct functioning of the new migrated script cannot be guaranteed.
# The migration of the script is just a starting point.
# Please review your script against the API reference file ChemScript12.htm.
#---------------------------------------------------------------------------------------

import glob
import sys, os, os.path
import re

# Creates lists with all the methods existing in ChemScript11 that can be capitalized directly
_Atom = ['displayName','getCartesian','getElement','getFormalCharge','getRadical',
         'setCartesian','setElement','setFormalCharge','setRadical']

_Bond = ['atom1','atom2','displayName','getBondOrder','getReactionStatus','otherAtom','setBondOrder']

_BondOrder = ['bondChar','bondCode','name']

_CombiChem = ['beginEnum','enumNext','numberOfPermutations','permutations','setCandidate','setCandidates']

_Element = ['atomicNumber','averageMass','commonIsotope','density','discoveredBy','eneg','exactMass',
            'isotopeMassNumber','isotopes','radius','symbol']

_Environment = ['activate','getThrowExceptions','getVerbosity','setC3dItemsFolder','setN2SDataFile',
                'setS2NDataFile','setThrowExceptions','setVerbosity','version']

_IMol = ['loadData','loadFile','readData','readFile','setDataItem','writeData', 'writeFile']

_MolBase =['canonicalCode','clear','clone','containsSubstructure','displayName','formula','geometricCenter',
           'getBound','getDataItem','getDataItems','isEmpty','loadData','loadFile','mimeTypes',
           'moveCenterToOrigin','readData','readFile','resetAtomIDs','rotate','setDataItem','setID',
           'smiles', 'writeData', 'writeFile']

_Mol = ['atomByAtomSearch','atomsWithVacantPiOrbitals','averageMass', 'bondedAtomsOf',
        'bondedBondsOf','canonicalCode','chemicalName','cleanupStructure','clear','clearZCoordinates',
        'clone','containsAtom','containsBond','containsSubstructure','convertTo3DStructure',
        'convertToDelocBondRep','convertToFixedBondRep','countAtoms','createAtom','createBond',
        'createSearchQuery','detectAtomStereoCIP','detectBondStereoCIP',
        'displayName','electronDonatingAtoms','electronWithdrawingAtoms','exactMass','findBond','formula',
        'geometricCenter','getAtoms','getBonds','getBound','getDataItem','getDataItems',
        'hasCharges','hasCoordinates','hasZCoordinates','hydrogenAcceptors',
        'hydrogenDonors','inchi','isEmpty','isPlanarStructure','joinFragments','list','loadData','loadFile',
        'lonePairAtoms','mergeFragments','mimeTypes','mm2Energy','mm2OptimizeGeometry','mostCommonStructure',
        'moveCenterToOrigin','neutralize','normalizeStructure','overlay','partitionCoefficient','readData','readFile',
        'refractivity','removeAtom','removeBond','resetAtomIDs','ringInfo','rotate','scaffoldCleanup','setDataItem',
        'setID','smiles','splitFragments','splitSalt','topology','totalCharge',
        'totalNegativeCharges','totalPositiveCharges','weight','writeData','writeFile']

_Reaction = ['appendStep','atomByAtomMapReaction','canonicalCode','clear','clone','containsSubstructure',
             'createReaction','displayName','formula','getBound','getDataItem',
             'getDataItems','intermediates','isEmpty','layout','loadData','loadFile','mimeTypes',
             'moveCenterToOrigin','perceiveReactionCenters','products','reactants','readData','readFile','resetAtomIDs',
             'rotate','setDataItem','setID','smiles','steps','transform','writeData', 'writeFile']

_Isotope = ['abundancePercent','mass','massNumber','symbol']

_LargestCommonSubstructure = ['atomMapM1','atomMapM2','bondMapM1','bondMapM2','compute']

_PeriodicTable = ['elementCount', 'getElement']

_Ring = ['getAtoms','getBonds','list']

_RingInfo = ['aromaticRings','atomsWithVacantPiOrbitals','basicRings','bridgeAtoms','bridgeBonds','bridgedRings',
             'bridgeheadAtoms','extendedRings','fundamentalRings','fusionAtoms','fusionBonds','hydrogenAcceptorAtoms',
             'hydrogenDonorAtoms','lonePairAtoms','necklaceRings','spiroAtoms']

_RDFileReader = ['close','current','eof','readNext','resetReading']

_RDFileWriter = ['close']

_SDFileReader = ['close','current','eof','readNext','resetReading']

_SDFileWriter = ['close']

_SaltTable = ['ClearFragmentList','PrimeWithCommonOrganicFragments','RegisterFragment','all','clear','listAll',
              'listSalts','listSolvents','loadDefault','registerFragment','registerInchi','registerWithSmiles',
              'registerWithSmilesFile','removeSaltsAndSolvents','salts','solvents','splitSaltAndSolvent',
              'splitSaltsAndSolvents']

_SearchOptions = ['_3D','absHitsRelative','extranFragsOk','extranFragsOkIfRxn','findChargedCarbon','findChargedHet',
                  'findIsotopes','findRadicals','fragsCanOverlap','fullStruct','genericsNotGeneric','ignoreCounterionsInQuery',
                  'implHMatchesSimple','list','looseDelocalization','maxHits','plusSigns',
                  'relativeTetStereo','tautomeric','timeout','useRxnCenters']

_SearchQuery = ['atomByAtomSearch','getAtomByAtomMap','getAtomMapCount']

_NormOptions  = ['anonList','azide','cleaveIntoSalts','collapseZwitterion','createdDelRep_1','createdDelRep_2',
                 'dative','dativeToDouble','dekekulize','delrep','diazo_a','diazo_b','featurelessHydrogens',
                 'isonitrile_fg','list','mergeCharges','mergeMetalSalts','moveChargeFromCarbon',
                 'neutralDiazo_fg','provideMissingCoords','r3NO_b','removeIsotopy','removeLabel',
                 'removeNonGraphStereo','removeRTable','removeRxnCenters','removeTextAtoms','removeValence',
                 'removeWedge','stripEitherDoubleBond','stripEitherSingleBond','thiazole','xMinusToX_fg']

_Topology = ['balabanIndex','clusterCount','cyclomaticNumber','degree','diameter','distance','distanceMatrix',
             'eccentricity','numOfChainBonds','numOfHydrogens','numOfLinkingChainBonds','numOfRingBonds',
             'numOfRotatableBonds','numOfTerminalBonds','numOfValenceElectrons','polarSurfaceArea','radius',
             'shapeAttribute','shapeCoefficient','sumOfDegrees','sumOfValenceDegrees','topologicalIndex',
             'totalConnectivity','totalValenceConnectivity','valence','valenceConnectivityIndex',
             'valenceDegree','wienerIndex']

_Point = ['angle','dihedralAngle','distanceTo','distanceToLine','distanceToPlane','toVector']

_Vector = ['angle','crossProduct','dotProduct','length','normalVector','normalize','toPoint']

version11Methods = [_Atom, _Bond, _BondOrder, _CombiChem, _Element, _Environment, _IMol, _MolBase, _Mol,
                    _Reaction, _Isotope, _LargestCommonSubstructure, _PeriodicTable, _Ring, _RingInfo,
                    _RDFileReader, _RDFileWriter, _SDFileReader, _SDFileWriter, _SaltTable, _SearchOptions,
                    _SearchQuery, _NormOptions, _Topology, _Point, _Vector]

# Creates a dictionary with the special cases
specialCases = {'.fullname':'.FullName', '.ip':'.IP', '.mp':'.MP', '.bp':'.BP', '.cdx':'.CDX', '.id':'.ID', 
                '.translateCoordiantes':'.TranslateCoordinates',
                ' Mol(':' StructureData(', ' Reaction(':' ReactionData(', ' Mol (':' StructureData (',
                ' Reaction (':' ReactionData (', ' Mol.':' StructureData.', ' Reaction.':' ReactionData.',
                ' Rxn(':' ReactionData(', ' Rxn (':' ReactionData (', ' Rxn.':' ReactionData.',
                '.Mol(':'.StructureData(', '.Mol (':'.StructureData (', '.Reaction(':'.ReactionData(',
                '.Rxn(':'.ReactionData(', '.Reaction (':'.ReactionData (', '.Rxn (':'.ReactionData (',
                ' Molecule(':' StructureData(', ' Molecule (':' StructureData (', ' Molecule.':' StructureData.',
                '.Molecule(':'.StructureData(', '.Molecule (':'.StructureData (', '.Mol.':'.StructureData.',
                '.Reaction.':'.ReactionData.', '.Molecule.':'.StructureData.', '.Rxn.':'.ReactionData.'}


# Creates a list with the deprecated Classes and methods
deprecatedClasses = [' Chain',' Color',' DocProp',' Document',' ExcelWriter',' Font',' Group',' MacroMol',' SuperAtom']

deprecatedMethods = ['.createDocProperty','.getDocProperty','.getParent','.setDocProperty','.createSuperAtom','.aminoAcids',
                     '.bases','.getAminoAcid','.getBase','.getSuperAtoms','.units','.ignoreImplicitH','.similar','.similarThresholdPercent',
                     '.labelH']

# Function to Capitalize the method without changing the rest of the letters.
def Capitalize(method):
        return method[0].upper() + method[1:]


# Searches for ".py" files in the current folder
_PyFiles = glob.glob("*.py")

# Gets the current path and the name of the current script
pathName, scriptName = os.path.split(sys.argv[0])

index = 0
# Reads each script existing in the current folder
for index in range(len(_PyFiles)):
    if _PyFiles[index] != scriptName and _PyFiles[index].endswith('_12.py') == False:
        filePath = os.getcwd() +  '\\' + _PyFiles[index]
        # Opens the script
        inputScript = open(filePath, 'r')
        # Reads the file
        script = inputScript.read()
        # Verifies if it is a ChemScript module
        if script.find("ChemScript") > 0:
            note1 = 'print \'#------------------------------------------------------------------------------\'\r\n'
            note1 += 'print \'# NOTE 1: \\\'import\\\' versionless ChemScript is no longer supported from \'\r\n'
            note1 += 'print \'# ChemScript 12. All \\\'import ChemScript\\\', \\\'from ChemScript import *\\\', \'\r\n'
            note1 += 'print \'# \\\'import ChemScript11\\\' or \\\'from ChemScript11 import *\\\'\'\r\n'
            note1 += 'print \'# were replaced with their corresponding \\\'ChemScript12\\\'.\'\r\n'
            note1 += 'print \'# \'\r\n'
            note1 += 'print \'# Mol() and Reaction()/Rxn() were replaced with their corresponding new names:\'\r\n'
            note1 += 'print \'#  StructureData() and ReactionData().\'\r\n'
            note1 += 'print \'#------------------------------------------------------------------------------\'\r\n\r\n'

            note2 = 'print \'#------------------------------------------------------------------------------\'\r\n'
            note2 += 'print \'# NOTE 2: The correct functioning of the new migrated script \'\r\n'
            note2 += 'print \'#         cannot be guaranteed.\'\r\n'
            note2 += 'print \'# The migration of the script is just a starting point.\'\r\n'
            note2 += 'print \'# Please review your script against the API reference file ChemScript12.htm.\'\r\n'
            note2 += 'print \'#------------------------------------------------------------------------------\'\r\n\r\n'
            
            # Replaces any versionless "ChemScript" with "ChemScript12"
            script = script.replace("ChemScript", "ChemScript12")
            script = script.replace("ChemScript11", "ChemScript12")
            script = script.replace("ChemScript1211", "ChemScript12")

            # Verifies the existance of the "close()" method
            note6 = ""
            if script.find('.close()')>=0:
                note6 = 'print \'#------------------------------------------------------------------------------\'\r\n'
                note6 += 'print \'# Warning! All the \\\'close()\\\' methods will be capitalized.\'\r\n'
                note6 += 'print \'# If the \\\'close()\\\' Python method is used then please keep it in lowercase.\'\r\n'
                note6 += 'print \'#\'\r\n'
                note6 += 'print \'# Please review your script against the API reference file ChemScript12.htm.\'\r\n'
                note6 += 'print \'#------------------------------------------------------------------------------\'\r\n\r\n'
                note6 += 'raw_input("Press ENTER to continue...")\r\n\r\n'

            # Verifies the existance of the "mol" property of 'LargestCommonSubstructure'
            note7 = ""
            if script.find('.mol')>=0 and script.find('LargestCommonSubstructure')>=0:
                note7 = 'print \'#------------------------------------------------------------------------------\'\r\n'
                note7 += 'print \'# Warning! your script is probably using the \\\'mol\\\' property\'\r\n'
                note7 += 'print \'# of \\\'LargestCommonSubstructure\\\'. \'\r\n'
                note7 += 'print \'# This property was renamed to \\\'CommonSubstructure\\\' in version 12.\'\r\n'
                note7 += 'print \'# This migration tool will NOT rename this property in order to avoid\'\r\n'
                note7 += 'print \'# potential problems related to \\\'.mol\\\' filenames.\'\r\n'
                note7 += 'print \'# If your script is using this property, please change it manually.\'\r\n'
                note7 += 'print \'#\'\r\n'
                note7 += 'print \'# Please review your script against the API reference file ChemScript12.htm.\'\r\n'
                note7 += 'print \'#------------------------------------------------------------------------------\'\r\n\r\n'
                note7 += 'raw_input("Press ENTER to continue...")\r\n\r\n'

	    
	    # Capitalizes method names
            for classes in version11Methods:
                for method in classes:
                        script = script.replace("." + method, "." + Capitalize(method))
        
            # Replaces the special cases
            for item in specialCases.keys():
                script = script.replace(item, specialCases[item])

	    # Searches for the special case of duplicated names. Decides if 'writeMol' should be replaced
	    SDWriter = False
	    RDWriter = False
	    note5 = ""

	    # by 'WriteStructure' or 'WriteReaction'
            if script.find('.writeMol')>=0:
	        if script.find(' SDFileWriter')>=0:
		    SDWriter = True
		if script.find(' RDFileWriter')>=0:
		    RDWriter = True

	    if RDWriter == True and SDWriter == False:
	        script = script.replace('.writeMol', '.WriteReaction')
            else:
	        script = script.replace('.writeMol', '.WriteStructure')
		# If there is in the script SDFIleWriter and RDFileWriter objects uses SDFileWriter's method 
		# and shows a Warning message.
		if SDWriter == True and RDWriter == True:
                    note5 = 'print \'#------------------------------------------------------------------------------\'\r\n'
                    note5 += 'print \'# Warning! your script uses the method \\\'writeMol\\\' or \\\'writeMols\\\'.\'\r\n'
                    note5 += 'print \'# This method was replaced with \\\'WriteStructure/s\\\' or \\\'WriteReaction/s\\\', \'\r\n'
                    note5 += 'print \'# according to the respective object (SDFileWriter or RDFileWriter).\'\r\n'
	            note5 += 'print \'# Due to the existance of both object types, the method(s) were replaced using \'\r\n'
   	            note5 += 'print \'# only SDFileWriter\\\'s methods.\'\r\n'
                    note5 += 'print \'#\'\r\n'
                    note5 += 'print \'# Please review your script against the API reference file ChemScript12.htm.\'\r\n'
                    note5 += 'print \'#------------------------------------------------------------------------------\'\r\n\r\n'
                    note5 += 'raw_input("Press ENTER to continue...")\r\n\r\n'

	    # Searches for deprecated Classes
            deprecated = False
            for item in deprecatedClasses:
	        if script.find(item)>=0:
		        deprecated = True

            note3 = ""
	    if deprecated == True:
                note3 = 'print \'#------------------------------------------------------------------------------\'\r\n'
                note3 += 'print \'# Warning! your script is probably using deprecated classes.\'\r\n'
                note3 += 'print \'# The deprecated classes are: Chain, Color, DocProp, Document, ExcelWriter,\'\r\n'
                note3 += 'print \'#                             Font, Group, MacroMol and SuperAtom.\'\r\n'
                note3 += 'print \'#\'\r\n'
                note3 += 'print \'# Please review your script against the API reference file ChemScript12.htm.\'\r\n'
                note3 += 'print \'#------------------------------------------------------------------------------\'\r\n\r\n'
                note3 += 'raw_input("Press ENTER to continue...")\r\n\r\n'

	    # Searches for deprecated methods
            deprecated = False
            for item in deprecatedMethods:
	        if script.find(item)>=0:
		        deprecated = True

            note4 = ""
	    if deprecated == True:
                note4 = 'print \'#------------------------------------------------------------------------------\'\r\n'
                note4 += 'print \'# Warning! your script is probably using deprecated methods or properties.\'\r\n'
                note4 += 'print \'# Deprecated methods/props are: createDocProperty, getDocProperty, getParent \'\r\n'
                note4 += 'print \'#                               setDocProperty, createSuperAtom, aminoAcids,\'\r\n'
                note4 += 'print \'#                               bases, getAminoAcid, getBase, getSuperAtoms,\'\r\n'
                note4 += 'print \'#                               units, ignoreImplicitH, similar,\'\r\n'
                note4 += 'print \'#                               similarThresholdPercent and labelH.\'\r\n'
                note4 += 'print \'#\'\r\n'
                note4 += 'print \'# Please review your script against the API reference file ChemScript12.htm.\'\r\n'
                note4 += 'print \'#------------------------------------------------------------------------------\'\r\n\r\n'
                note4 += 'raw_input("Press ENTER to continue...")\r\n\r\n'
   

            # Joins the migrated script with the information notes
            script = note1 + note2 + note3 + note4 + note5 + note6 + note7 + script
    
            # Sets name and path of the new script file
            newScriptName = _PyFiles[index].split('.py')
            targetFilePath = os.getcwd() +  '\\' + newScriptName[0] + '_12.py'
          
            # Saves the converted script with the new name                
            newScript = open(targetFilePath, "w")
            newScript.write(script)

            # Closes new script file
            newScript.close()
           
        # Closes the original script
        inputScript.close()
