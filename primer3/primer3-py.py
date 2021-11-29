# /usr/bin/env bash
# Author: sYc
# Date: 2020-09-28 12:36:59
# Version: 0.2
# Description: to virerfy primer

# from primer3.thermoanalysis import ThermoAnalysis
from primer3.thermoanalysis import ThermoAnalysis as Thermo

oligo_cala = Thermo()

def VairPrimer(self, primers):
    """
    Description: to virerfy primer
    [ ] I:  for input mod
    [ ] A:  for var mod
    [ ] F:  for file mod
    [ ] 验证primer为元组
    """

    for num in range(0, len(primers)):
        # output
        print('\033[1;34m', num, '\033[0m')
        print('\033[1;31mForward primer\033[0m\t\t\t', end='')
        print('\033[1;32mReverse primer\033[0m')

        # get primer
        for primer in primers:
            for i in range(0, 2):
                result = oligo_cal.calcTm(primer[i])
                i += 1
                print('\033[1;3'+str(i)+'mTm:\033[0m\t', result, '\t', end='')
            print('')

            for i in range(0, 2):
                result = oligo_cal.calcHairpin(primer[i])
                i += 1
                print('\033[1;3'+str(i)+'mHairpin:\033[0m ', end='')
                print('%-s Tm:%-.4f dG:%-.4f' %
                    (result.structure_found, result.tm, result.dg), '\t', end='')
            print('')

            for i in range(0, 2):
                result = oligo_cal.calcHomodimer(primer[i])
                i += 1
                print('\033[1;3'+str(i)+'mHomodimer:\033[0m ', end='')
                print('%-s Tm:%-.4f dG:%-.4f' %
                    (result.structure_found, result.tm, result.dg), '\t', end='')
            print('')

            result = oligo_cal.calcHeterodimer(primer[0], primer[1])
            print('\033[1mHeterodimer:\033[0m', end='')
            print('%-s Tm:%-.4f dG:%-.4f' % (result.structure_found, result.tm, result.dg))

            result = oligo_cal.bindings.calcEndStability(primer[0], primer[1])
            print('\033[1mEndStability:\033[0m', end='')
            print('%-s Tm:%-.4f dG:%-.4f' % (result.structure_found, result.tm, result.dg))

    raise NotImplementedError
