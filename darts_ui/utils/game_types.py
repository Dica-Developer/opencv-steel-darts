"""
NOT NEEDED CURRENTLY - WILL KEEP THIS AROUND.
Centralized list of game types and with short identifiers and valid throws.
"""

# Variables with short (maximum 3 char identifiers):
CRICKET = 'CR'
FIVE_OH_ONE = '501'
THREE_OH_ONE = '301'
KILLER = 'KR'

# Current possible game choices
GAME_CHOICES = ((CRICKET, 'Cricket'),
                (FIVE_OH_ONE, '501'),
                (THREE_OH_ONE, '301'),
                (KILLER, 'Killer'))

# # Not needed (yet)
# # Fields on the dart board that can be hit with a throw:
# BOARDER = 'BR'
# BULL = 'BL'
# BULL_DOUBLE = 'DBL'
# TWENTY = '20'
# TWENTY_DOUBLE = 'D20'
# TWENTY_TRIPLE = 'T20'
# NINETEEN = '19'
# NINETEEN_DOUBLE = 'D19'
# NINETEEN_TRIPLE = 'T19'
# EIGHTHEEN = '18'
# EIGHTHEEN_DOUBLE = 'D18'
# EIGHTHEEN_TRIPLE = 'T18'
# SEVENTEEN = '17'
# SEVENTEEN_DOUBLE = 'D17'
# SEVENTEEN_TRIPLE = 'T17'
# SIXTEEN = '16'
# SIXTEEN_DOUBLE = 'D16'
# SIXTEEN_TRIPLE = 'T16'
# FIFTEEN = '15'
# FIFTEEN_DOUBLE = 'D15'
# FIFTEEN_TRIPLE = 'T15'
# FOURTEEN = '14'
# FOURTEEN_DOUBLE = 'D14'
# FOURTEEN_TRIPLE = 'T14'
# THIRTEEN = '13'
# THIRTEEN_DOUBLE = 'D13'
# THIRTEEN_TRIPLE = 'T13'
# TWELVE = '12'
# TWELVE_DOUBLE = 'D12'
# TWELVE_TRIPLE = 'T12'
# ELEVEN = '11'
# ELEVEN_DOUBLE = 'D11'
# ELEVEN_TRIPLE = 'T11'
# TEN = '10'
# TEN_DOUBLE = 'D10'
# TEN_TRIPLE = 'T10'
# NINE = '9'
# NINE_DOUBLE = 'D9'
# NINE_TRIPLE = 'T9'
# EIGHT = '8'
# EIGHT_DOUBLE = 'D8'
# EIGHT_TRIPLE = 'T8'
# SEVEN = '7'
# SEVEN_DOUBLE = 'D7'
# SEVEN_TRIPLE = 'T7'
# SIX = '6'
# SIX_DOUBLE = 'D6'
# SIX_TRIPLE = 'T6'
# FIVE = '5'
# FIVE_DOUBLE = 'D5'
# FIVE_TRIPLE = 'T5'
# FOUR = '4'
# FOUR_DOUBLE = 'D4'
# FOUR_TRIPLE = 'T4'
# THREE = '3'
# THREE_DOUBLE = 'D3'
# THREE_TRIPLE = 'T3'
# TWO = '2'
# TWO_DOUBLE = 'D2'
# TWO_TRIPLE = 'T2'
# ONE = '1'
# ONE_DOUBLE = 'D1'
# ONE_TRIPLE = 'T1'
#
# # Possible throws per game:
# CRICKET_VALID = ((BULL, "Bull's Eye"),
#                  (BULL_DOUBLE, 'Double bull'),
#                  (TWENTY, '20'),
#                  (TWENTY_DOUBLE, 'Double 20'),
#                  (TWENTY_TRIPLE, 'Triple 20'),
#                  (NINETEEN, '19'),
#                  (NINETEEN_DOUBLE, 'Double 19'),
#                  (NINETEEN_TRIPLE, 'Triple 19'),
#                  (EIGHTHEEN, '18'),
#                  (EIGHTHEEN_DOUBLE, 'Double 18'),
#                  (EIGHTHEEN_TRIPLE, 'Triple 18'),
#                  (SEVENTEEN, '17'),
#                  (SEVENTEEN_DOUBLE, 'Double 17'),
#                  (SEVENTEEN_TRIPLE, 'Triple 17'),
#                  (SIXTEEN, '16'),
#                  (SIXTEEN_DOUBLE, 'Double 16'),
#                  (SIXTEEN_TRIPLE, 'Triple 16'),
#                  (FIFTEEN, '15'),
#                  (FIFTEEN_DOUBLE, 'Double 15'),
#                  (FIFTEEN_TRIPLE, 'Triple 15'),
#                  (BOARDER, 'Nothing'))
#
# OH_ONE_VALID = ((BULL, "Bull's Eye"),
#                 (BULL_DOUBLE, 'Double bull'),
#                 (TWENTY, '20'),
#                 (TWENTY_DOUBLE, 'Double 20'),
#                 (TWENTY_TRIPLE, 'Triple 20'),
#                 (NINETEEN, '19'),
#                 (NINETEEN_DOUBLE, 'Double 19'),
#                 (NINETEEN_TRIPLE, 'Triple 19'),
#                 (EIGHTHEEN, '18'),
#                 (EIGHTHEEN_DOUBLE, 'Double 18'),
#                 (EIGHTHEEN_TRIPLE, 'Triple 18'),
#                 (SEVENTEEN, '17'),
#                 (SEVENTEEN_DOUBLE, 'Double 17'),
#                 (SEVENTEEN_TRIPLE, 'Triple 17'),
#                 (SIXTEEN, '16'),
#                 (SIXTEEN_DOUBLE, 'Double 16'),
#                 (SIXTEEN_TRIPLE, 'Triple 16'),
#                 (FIFTEEN, '15'),
#                 (FIFTEEN_DOUBLE, 'Double 15'),
#                 (FIFTEEN_TRIPLE, 'Triple 15'),
#                 (FOURTEEN, '14'),
#                 (FOURTEEN_DOUBLE, 'Double 14'),
#                 (FOURTEEN_TRIPLE, 'Triple 14'),
#                 (THIRTEEN, '13'),
#                 (THIRTEEN_DOUBLE, 'Double 13'),
#                 (THIRTEEN_TRIPLE, 'Triple 13'),
#                 (TWELVE, '12'),
#                 (TWELVE_DOUBLE, 'Double 12'),
#                 (TWELVE_TRIPLE, 'Triple 12'),
#                 (ELEVEN, '11'),
#                 (ELEVEN_DOUBLE, 'Double 11'),
#                 (ELEVEN_TRIPLE, 'Triple 11'),
#                 (TEN, '10'),
#                 (TEN_DOUBLE, 'Double 10'),
#                 (TEN_TRIPLE, 'Triple 10'),
#                 (NINE, '9'),
#                 (NINE_DOUBLE, 'Double 9'),
#                 (NINE_TRIPLE, 'Triple 9'),
#                 (EIGHT, '8'),
#                 (EIGHT_DOUBLE, 'Double 8'),
#                 (EIGHT_TRIPLE, 'Triple 8'),
#                 (SEVEN, '7'),
#                 (SEVEN_DOUBLE, 'Double 7'),
#                 (SEVEN_TRIPLE, 'Triple 7'),
#                 (SIX, '6'),
#                 (SIX_DOUBLE, 'Double 6'),
#                 (SIX_TRIPLE, 'Triple 6'),
#                 (FIVE, '5'),
#                 (FIVE_DOUBLE, 'Double 5'),
#                 (FIVE_TRIPLE, 'Triple 5'),
#                 (FOUR, '4'),
#                 (FOUR_DOUBLE, 'Double 4'),
#                 (FOUR_TRIPLE, 'Triple 4'),
#                 (THREE, '3'),
#                 (THREE_DOUBLE, 'Double 3'),
#                 (THREE_TRIPLE, 'Triple 3'),
#                 (TWO, '2'),
#                 (TWO_DOUBLE, 'Double 2'),
#                 (TWO_TRIPLE, 'Triple 2'),
#                 (ONE, '1'),
#                 (ONE_DOUBLE, 'Double 1'),
#                 (ONE_TRIPLE, 'Triple 1'),
#                 (BOARDER, 'Nothing'))
