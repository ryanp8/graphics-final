
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AA_LINE AMBIENT BASENAME BOX CAMERA CO COMMENT CONSTANTS DISPLAY DOUBLE FOCAL FRAMES GENERATE_RAYFILES ID INT LIGHT LINE MESH MOVE POP PUSH ROTATE SAVE SAVE_COORDS SAVE_KNOBS SCALE SCREEN SET SET_KNOBS SHADING SHADING_TYPE SPHERE STRING TEXTURE TORUS TWEEN VARY WEB XYZinput :\n            | command inputcommand : COMMENTSYMBOL : XYZ\n              | IDTEXT : SYMBOL\n            | STRINGNUMBER : DOUBLEcommand : POP\n                 | PUSHcommand : SCREEN NUMBER NUMBER\n                 | SCREENcommand : SAVE TEXT TEXTcommand : DISPLAYcommand : SPHERE NUMBER NUMBER NUMBER NUMBER\n               | SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER\n               | SPHERE NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : TORUS NUMBER NUMBER NUMBER NUMBER NUMBER\n               | TORUS NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER\n               | TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOLcommand : LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL\n               | LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOLcommand : AA_LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | AA_LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | AA_LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | AA_LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL\n               | AA_LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | AA_LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL\n               | AA_LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER\n               | AA_LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOLcommand : MOVE NUMBER NUMBER NUMBER SYMBOL\n               | MOVE NUMBER NUMBER NUMBERcommand : SCALE NUMBER NUMBER NUMBER SYMBOL\n                 | SCALE NUMBER NUMBER NUMBERcommand : ROTATE XYZ NUMBER SYMBOL\n                 | ROTATE XYZ NUMBERcommand : FRAMES NUMBERcommand : BASENAME TEXTcommand : VARY SYMBOL NUMBER NUMBER NUMBER NUMBERcommand : SET SYMBOL NUMBER\n               | SET_KNOBS NUMBERcommand : AMBIENT NUMBER NUMBER NUMBERcommand : CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER\n               | CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : LIGHT SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : SHADING SHADING_TYPEcommand : CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBERcommand : GENERATE_RAYFILEScommand : MESH CO TEXT\n               | MESH SYMBOL CO TEXT\n               | MESH CO TEXT SYMBOL\n               | MESH SYMBOL CO TEXT SYMBOLcommand : SAVE_KNOBS SYMBOLcommand : SAVE_COORDS SYMBOLcommand : TWEEN NUMBER NUMBER SYMBOL SYMBOLcommand : FOCAL NUMBERcommand : WEBcommand : TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,8,27,33,35,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[-1,0,-1,-3,-9,-10,-12,-14,-60,-69,-2,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'COMMENT':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[3,3,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'POP':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[4,4,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'PUSH':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[5,5,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'SCREEN':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[6,6,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'SAVE':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[7,7,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'DISPLAY':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[8,8,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'SPHERE':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[9,9,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'TORUS':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[10,10,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'BOX':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[11,11,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'LINE':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[12,12,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'AA_LINE':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[13,13,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'MOVE':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[14,14,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'SCALE':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[15,15,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'ROTATE':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[16,16,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'FRAMES':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[17,17,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'BASENAME':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[18,18,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'VARY':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[19,19,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'SET':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[20,20,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'SET_KNOBS':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[21,21,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'AMBIENT':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[22,22,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'CONSTANTS':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[23,23,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'LIGHT':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[24,24,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'SHADING':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[25,25,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'CAMERA':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[26,26,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'GENERATE_RAYFILES':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[27,27,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'MESH':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[28,28,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'SAVE_KNOBS':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[29,29,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'SAVE_COORDS':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[30,30,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'TWEEN':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[31,31,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'FOCAL':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[32,32,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'WEB':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[33,33,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'TEXTURE':([0,2,3,4,5,6,8,27,33,37,39,40,41,42,56,57,60,64,68,69,71,73,74,87,89,94,108,109,110,112,116,117,120,132,133,138,139,141,142,143,155,160,161,162,163,165,169,175,177,178,179,180,181,183,184,185,187,189,191,192,193,194,195,196,197,200,201,204,210,211,],[34,34,-3,-9,-10,-12,-14,-60,-69,-8,-6,-7,-4,-5,-49,-50,-53,-58,-65,-66,-68,-11,-13,-48,-52,-61,-44,-46,-47,-54,-63,-62,-15,-43,-45,-64,-67,-17,-16,-19,-51,-18,-20,-21,-23,-27,-35,-59,-22,-24,-25,-28,-29,-31,-36,-37,-39,-57,-26,-30,-33,-32,-38,-41,-40,-34,-42,-55,-56,-70,]),'DOUBLE':([6,9,10,11,12,13,14,15,17,21,22,26,31,32,36,37,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,58,59,61,62,63,65,70,72,75,76,77,78,79,80,81,82,83,84,85,86,88,90,91,92,93,97,98,99,100,101,102,103,104,105,106,107,111,113,114,115,119,121,122,123,124,125,126,127,128,129,130,131,134,135,136,137,140,144,145,146,147,148,149,150,151,152,153,154,156,157,158,159,164,166,167,168,170,171,172,173,174,176,182,186,188,190,198,199,202,203,204,205,206,207,208,209,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-8,-4,-5,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'STRING':([7,18,38,39,40,41,42,66,95,],[40,40,40,-6,-7,-4,-5,40,40,]),'XYZ':([7,9,10,11,12,13,16,18,19,20,23,24,28,29,30,34,37,38,39,40,41,42,66,87,94,95,96,104,106,108,109,117,118,120,128,131,142,143,162,163,165,169,179,181,183,185,187,193,196,],[41,41,41,41,41,41,55,41,41,41,41,41,41,41,41,41,-8,41,-6,-7,-4,-5,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'ID':([7,9,10,11,12,13,18,19,20,23,24,28,29,30,34,37,38,39,40,41,42,66,87,94,95,96,104,106,108,109,117,118,120,128,131,142,143,162,163,165,169,179,181,183,185,187,193,196,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-8,42,-6,-7,-4,-5,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'SHADING_TYPE':([25,],[64,]),'CO':([28,41,42,67,],[66,-4,-5,95,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'input':([0,2,],[1,35,]),'command':([0,2,],[2,2,]),'NUMBER':([6,9,10,11,12,13,14,15,17,21,22,26,31,32,36,43,44,45,46,47,48,49,50,51,52,53,54,55,58,59,61,62,63,65,70,72,75,76,77,78,79,80,81,82,83,84,85,86,88,90,91,92,93,97,98,99,100,101,102,103,104,105,106,107,111,113,114,115,119,121,122,123,124,125,126,127,128,129,130,131,134,135,136,137,140,144,145,146,147,148,149,150,151,152,153,154,156,157,158,159,164,166,167,168,170,171,172,173,174,176,182,186,188,190,198,199,202,203,204,205,206,207,208,209,],[36,43,45,47,49,51,53,54,56,60,61,65,70,71,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,112,113,114,115,119,120,121,122,123,124,125,126,128,129,131,134,135,136,137,140,142,143,144,145,146,147,148,150,151,152,154,155,156,157,158,159,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,179,181,182,183,185,186,187,188,189,190,193,196,198,199,202,203,204,205,206,207,208,209,210,211,]),'TEXT':([7,18,38,66,95,],[38,57,74,94,117,]),'SYMBOL':([7,9,10,11,12,13,18,19,20,23,24,28,29,30,34,38,66,87,94,95,96,104,106,108,109,117,118,120,128,131,142,143,162,163,165,169,179,181,183,185,187,193,196,],[39,44,46,48,50,52,39,58,59,62,63,67,68,69,72,39,39,110,116,39,118,127,130,132,133,138,139,141,149,153,160,161,177,178,180,184,191,192,194,195,197,200,201,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> input","S'",1,None,None,None),
  ('input -> <empty>','input',0,'p_input','mdl.py',124),
  ('input -> command input','input',2,'p_input','mdl.py',125),
  ('command -> COMMENT','command',1,'p_command_comment','mdl.py',129),
  ('SYMBOL -> XYZ','SYMBOL',1,'p_SYMBOL','mdl.py',133),
  ('SYMBOL -> ID','SYMBOL',1,'p_SYMBOL','mdl.py',134),
  ('TEXT -> SYMBOL','TEXT',1,'p_TEXT','mdl.py',138),
  ('TEXT -> STRING','TEXT',1,'p_TEXT','mdl.py',139),
  ('NUMBER -> DOUBLE','NUMBER',1,'p_NUMBER','mdl.py',143),
  ('command -> POP','command',1,'p_command_stack','mdl.py',147),
  ('command -> PUSH','command',1,'p_command_stack','mdl.py',148),
  ('command -> SCREEN NUMBER NUMBER','command',3,'p_command_screen','mdl.py',152),
  ('command -> SCREEN','command',1,'p_command_screen','mdl.py',153),
  ('command -> SAVE TEXT TEXT','command',3,'p_command_save','mdl.py',160),
  ('command -> DISPLAY','command',1,'p_command_show','mdl.py',164),
  ('command -> SPHERE NUMBER NUMBER NUMBER NUMBER','command',5,'p_command_sphere','mdl.py',168),
  ('command -> SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_sphere','mdl.py',169),
  ('command -> SPHERE NUMBER NUMBER NUMBER NUMBER SYMBOL','command',6,'p_command_sphere','mdl.py',170),
  ('command -> SPHERE SYMBOL NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_sphere','mdl.py',171),
  ('command -> TORUS NUMBER NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_torus','mdl.py',185),
  ('command -> TORUS NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',7,'p_command_torus','mdl.py',186),
  ('command -> TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_torus','mdl.py',187),
  ('command -> TORUS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_torus','mdl.py',188),
  ('command -> BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_box','mdl.py',202),
  ('command -> BOX NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_box','mdl.py',203),
  ('command -> BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_box','mdl.py',204),
  ('command -> BOX SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_box','mdl.py',205),
  ('command -> LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_line','mdl.py',219),
  ('command -> LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_line','mdl.py',220),
  ('command -> LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',8,'p_command_line','mdl.py',221),
  ('command -> LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_line','mdl.py',222),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_line','mdl.py',223),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_line','mdl.py',224),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',9,'p_command_line','mdl.py',225),
  ('command -> LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',10,'p_command_line','mdl.py',226),
  ('command -> AA_LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_aa_line','mdl.py',247),
  ('command -> AA_LINE NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',8,'p_command_aa_line','mdl.py',248),
  ('command -> AA_LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',8,'p_command_aa_line','mdl.py',249),
  ('command -> AA_LINE NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_aa_line','mdl.py',250),
  ('command -> AA_LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_aa_line','mdl.py',251),
  ('command -> AA_LINE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER SYMBOL','command',9,'p_command_aa_line','mdl.py',252),
  ('command -> AA_LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER','command',9,'p_command_aa_line','mdl.py',253),
  ('command -> AA_LINE SYMBOL NUMBER NUMBER NUMBER SYMBOL NUMBER NUMBER NUMBER SYMBOL','command',10,'p_command_aa_line','mdl.py',254),
  ('command -> MOVE NUMBER NUMBER NUMBER SYMBOL','command',5,'p_command_move','mdl.py',275),
  ('command -> MOVE NUMBER NUMBER NUMBER','command',4,'p_command_move','mdl.py',276),
  ('command -> SCALE NUMBER NUMBER NUMBER SYMBOL','command',5,'p_command_scale','mdl.py',284),
  ('command -> SCALE NUMBER NUMBER NUMBER','command',4,'p_command_scale','mdl.py',285),
  ('command -> ROTATE XYZ NUMBER SYMBOL','command',4,'p_command_rotate','mdl.py',293),
  ('command -> ROTATE XYZ NUMBER','command',3,'p_command_rotate','mdl.py',294),
  ('command -> FRAMES NUMBER','command',2,'p_command_frames','mdl.py',302),
  ('command -> BASENAME TEXT','command',2,'p_command_basename','mdl.py',307),
  ('command -> VARY SYMBOL NUMBER NUMBER NUMBER NUMBER','command',6,'p_command_vary','mdl.py',312),
  ('command -> SET SYMBOL NUMBER','command',3,'p_command_knobs','mdl.py',318),
  ('command -> SET_KNOBS NUMBER','command',2,'p_command_knobs','mdl.py',319),
  ('command -> AMBIENT NUMBER NUMBER NUMBER','command',4,'p_command_ambient','mdl.py',330),
  ('command -> CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',11,'p_command_constants','mdl.py',336),
  ('command -> CONSTANTS SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',14,'p_command_constants','mdl.py',337),
  ('command -> LIGHT SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',8,'p_command_light','mdl.py',343),
  ('command -> SHADING SHADING_TYPE','command',2,'p_command_shading','mdl.py',349),
  ('command -> CAMERA NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',7,'p_command_camera','mdl.py',355),
  ('command -> GENERATE_RAYFILES','command',1,'p_command_generate_rayfiles','mdl.py',360),
  ('command -> MESH CO TEXT','command',3,'p_command_mesh','mdl.py',364),
  ('command -> MESH SYMBOL CO TEXT','command',4,'p_command_mesh','mdl.py',365),
  ('command -> MESH CO TEXT SYMBOL','command',4,'p_command_mesh','mdl.py',366),
  ('command -> MESH SYMBOL CO TEXT SYMBOL','command',5,'p_command_mesh','mdl.py',367),
  ('command -> SAVE_KNOBS SYMBOL','command',2,'p_save_knobs','mdl.py',381),
  ('command -> SAVE_COORDS SYMBOL','command',2,'p_save_coords','mdl.py',387),
  ('command -> TWEEN NUMBER NUMBER SYMBOL SYMBOL','command',5,'p_tween','mdl.py',394),
  ('command -> FOCAL NUMBER','command',2,'p_focal','mdl.py',399),
  ('command -> WEB','command',1,'p_web','mdl.py',403),
  ('command -> TEXTURE SYMBOL NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER NUMBER','command',14,'p_texture','mdl.py',407),
]
