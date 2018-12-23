#!/usr/bin/python3
import dimod

################################################################################
## NOT - target: q0_99 ##
################################################################################
if 'q0_99' not in globals():
    q0_99=0

bqm = dimod.BinaryQuadraticModel({'q0_99' : -4, 'outq0_99' : -4}, {('q0_99', 'outq0_99') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_99']==q0_99 and int(energy)==0:
        q0_99_before = sample['q0_99']
        q0_99=sample['outq0_99']
        break

print('#' * 80)
print("NOT operation on q0_99:")
print("    in:  q0_99={0}".format(q0_99_before))
print("    out: q0_99={0}".format(q0_99))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_99 ##
################################################################################
if 'q1_99' not in globals():
    q1_99=0

bqm = dimod.BinaryQuadraticModel({'q1_99' : -4, 'outq1_99' : -4}, {('q1_99', 'outq1_99') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_99']==q1_99 and int(energy)==0:
        q1_99_before = sample['q1_99']
        q1_99=sample['outq1_99']
        break

print('#' * 80)
print("NOT operation on q1_99:")
print("    in:  q1_99={0}".format(q1_99_before))
print("    out: q1_99={0}".format(q1_99))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_98 ##
################################################################################
if 'q0_98' not in globals():
    q0_98=0

bqm = dimod.BinaryQuadraticModel({'q0_98' : -4, 'outq0_98' : -4}, {('q0_98', 'outq0_98') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_98']==q0_98 and int(energy)==0:
        q0_98_before = sample['q0_98']
        q0_98=sample['outq0_98']
        break

print('#' * 80)
print("NOT operation on q0_98:")
print("    in:  q0_98={0}".format(q0_98_before))
print("    out: q0_98={0}".format(q0_98))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_98 ##
################################################################################
if 'q1_98' not in globals():
    q1_98=0

bqm = dimod.BinaryQuadraticModel({'q1_98' : -4, 'outq1_98' : -4}, {('q1_98', 'outq1_98') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_98']==q1_98 and int(energy)==0:
        q1_98_before = sample['q1_98']
        q1_98=sample['outq1_98']
        break

print('#' * 80)
print("NOT operation on q1_98:")
print("    in:  q1_98={0}".format(q1_98_before))
print("    out: q1_98={0}".format(q1_98))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_97 ##
################################################################################
if 'q0_97' not in globals():
    q0_97=0

bqm = dimod.BinaryQuadraticModel({'q0_97' : -4, 'outq0_97' : -4}, {('q0_97', 'outq0_97') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_97']==q0_97 and int(energy)==0:
        q0_97_before = sample['q0_97']
        q0_97=sample['outq0_97']
        break

print('#' * 80)
print("NOT operation on q0_97:")
print("    in:  q0_97={0}".format(q0_97_before))
print("    out: q0_97={0}".format(q0_97))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_97 ##
################################################################################
if 'q1_97' not in globals():
    q1_97=0

bqm = dimod.BinaryQuadraticModel({'q1_97' : -4, 'outq1_97' : -4}, {('q1_97', 'outq1_97') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_97']==q1_97 and int(energy)==0:
        q1_97_before = sample['q1_97']
        q1_97=sample['outq1_97']
        break

print('#' * 80)
print("NOT operation on q1_97:")
print("    in:  q1_97={0}".format(q1_97_before))
print("    out: q1_97={0}".format(q1_97))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_96 ##
################################################################################
if 'q0_96' not in globals():
    q0_96=0

bqm = dimod.BinaryQuadraticModel({'q0_96' : -4, 'outq0_96' : -4}, {('q0_96', 'outq0_96') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_96']==q0_96 and int(energy)==0:
        q0_96_before = sample['q0_96']
        q0_96=sample['outq0_96']
        break

print('#' * 80)
print("NOT operation on q0_96:")
print("    in:  q0_96={0}".format(q0_96_before))
print("    out: q0_96={0}".format(q0_96))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_96 ##
################################################################################
if 'q1_96' not in globals():
    q1_96=0

bqm = dimod.BinaryQuadraticModel({'q1_96' : -4, 'outq1_96' : -4}, {('q1_96', 'outq1_96') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_96']==q1_96 and int(energy)==0:
        q1_96_before = sample['q1_96']
        q1_96=sample['outq1_96']
        break

print('#' * 80)
print("NOT operation on q1_96:")
print("    in:  q1_96={0}".format(q1_96_before))
print("    out: q1_96={0}".format(q1_96))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_95 ##
################################################################################
if 'q0_95' not in globals():
    q0_95=0

bqm = dimod.BinaryQuadraticModel({'q0_95' : -4, 'outq0_95' : -4}, {('q0_95', 'outq0_95') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_95']==q0_95 and int(energy)==0:
        q0_95_before = sample['q0_95']
        q0_95=sample['outq0_95']
        break

print('#' * 80)
print("NOT operation on q0_95:")
print("    in:  q0_95={0}".format(q0_95_before))
print("    out: q0_95={0}".format(q0_95))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_95 ##
################################################################################
if 'q1_95' not in globals():
    q1_95=0

bqm = dimod.BinaryQuadraticModel({'q1_95' : -4, 'outq1_95' : -4}, {('q1_95', 'outq1_95') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_95']==q1_95 and int(energy)==0:
        q1_95_before = sample['q1_95']
        q1_95=sample['outq1_95']
        break

print('#' * 80)
print("NOT operation on q1_95:")
print("    in:  q1_95={0}".format(q1_95_before))
print("    out: q1_95={0}".format(q1_95))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_94 ##
################################################################################
if 'q0_94' not in globals():
    q0_94=0

bqm = dimod.BinaryQuadraticModel({'q0_94' : -4, 'outq0_94' : -4}, {('q0_94', 'outq0_94') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_94']==q0_94 and int(energy)==0:
        q0_94_before = sample['q0_94']
        q0_94=sample['outq0_94']
        break

print('#' * 80)
print("NOT operation on q0_94:")
print("    in:  q0_94={0}".format(q0_94_before))
print("    out: q0_94={0}".format(q0_94))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_94 ##
################################################################################
if 'q1_94' not in globals():
    q1_94=0

bqm = dimod.BinaryQuadraticModel({'q1_94' : -4, 'outq1_94' : -4}, {('q1_94', 'outq1_94') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_94']==q1_94 and int(energy)==0:
        q1_94_before = sample['q1_94']
        q1_94=sample['outq1_94']
        break

print('#' * 80)
print("NOT operation on q1_94:")
print("    in:  q1_94={0}".format(q1_94_before))
print("    out: q1_94={0}".format(q1_94))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_93 ##
################################################################################
if 'q0_93' not in globals():
    q0_93=0

bqm = dimod.BinaryQuadraticModel({'q0_93' : -4, 'outq0_93' : -4}, {('q0_93', 'outq0_93') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_93']==q0_93 and int(energy)==0:
        q0_93_before = sample['q0_93']
        q0_93=sample['outq0_93']
        break

print('#' * 80)
print("NOT operation on q0_93:")
print("    in:  q0_93={0}".format(q0_93_before))
print("    out: q0_93={0}".format(q0_93))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_92 ##
################################################################################
if 'q0_92' not in globals():
    q0_92=0

bqm = dimod.BinaryQuadraticModel({'q0_92' : -4, 'outq0_92' : -4}, {('q0_92', 'outq0_92') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_92']==q0_92 and int(energy)==0:
        q0_92_before = sample['q0_92']
        q0_92=sample['outq0_92']
        break

print('#' * 80)
print("NOT operation on q0_92:")
print("    in:  q0_92={0}".format(q0_92_before))
print("    out: q0_92={0}".format(q0_92))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_92 ##
################################################################################
if 'q1_92' not in globals():
    q1_92=0

bqm = dimod.BinaryQuadraticModel({'q1_92' : -4, 'outq1_92' : -4}, {('q1_92', 'outq1_92') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_92']==q1_92 and int(energy)==0:
        q1_92_before = sample['q1_92']
        q1_92=sample['outq1_92']
        break

print('#' * 80)
print("NOT operation on q1_92:")
print("    in:  q1_92={0}".format(q1_92_before))
print("    out: q1_92={0}".format(q1_92))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_91 ##
################################################################################
if 'q1_91' not in globals():
    q1_91=0

bqm = dimod.BinaryQuadraticModel({'q1_91' : -4, 'outq1_91' : -4}, {('q1_91', 'outq1_91') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_91']==q1_91 and int(energy)==0:
        q1_91_before = sample['q1_91']
        q1_91=sample['outq1_91']
        break

print('#' * 80)
print("NOT operation on q1_91:")
print("    in:  q1_91={0}".format(q1_91_before))
print("    out: q1_91={0}".format(q1_91))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_90 ##
################################################################################
if 'q0_90' not in globals():
    q0_90=0

bqm = dimod.BinaryQuadraticModel({'q0_90' : -4, 'outq0_90' : -4}, {('q0_90', 'outq0_90') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_90']==q0_90 and int(energy)==0:
        q0_90_before = sample['q0_90']
        q0_90=sample['outq0_90']
        break

print('#' * 80)
print("NOT operation on q0_90:")
print("    in:  q0_90={0}".format(q0_90_before))
print("    out: q0_90={0}".format(q0_90))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_90 ##
################################################################################
if 'q1_90' not in globals():
    q1_90=0

bqm = dimod.BinaryQuadraticModel({'q1_90' : -4, 'outq1_90' : -4}, {('q1_90', 'outq1_90') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_90']==q1_90 and int(energy)==0:
        q1_90_before = sample['q1_90']
        q1_90=sample['outq1_90']
        break

print('#' * 80)
print("NOT operation on q1_90:")
print("    in:  q1_90={0}".format(q1_90_before))
print("    out: q1_90={0}".format(q1_90))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_89 ##
################################################################################
if 'q0_89' not in globals():
    q0_89=0

bqm = dimod.BinaryQuadraticModel({'q0_89' : -4, 'outq0_89' : -4}, {('q0_89', 'outq0_89') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_89']==q0_89 and int(energy)==0:
        q0_89_before = sample['q0_89']
        q0_89=sample['outq0_89']
        break

print('#' * 80)
print("NOT operation on q0_89:")
print("    in:  q0_89={0}".format(q0_89_before))
print("    out: q0_89={0}".format(q0_89))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_89 ##
################################################################################
if 'q1_89' not in globals():
    q1_89=0

bqm = dimod.BinaryQuadraticModel({'q1_89' : -4, 'outq1_89' : -4}, {('q1_89', 'outq1_89') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_89']==q1_89 and int(energy)==0:
        q1_89_before = sample['q1_89']
        q1_89=sample['outq1_89']
        break

print('#' * 80)
print("NOT operation on q1_89:")
print("    in:  q1_89={0}".format(q1_89_before))
print("    out: q1_89={0}".format(q1_89))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_88 ##
################################################################################
if 'q0_88' not in globals():
    q0_88=0

bqm = dimod.BinaryQuadraticModel({'q0_88' : -4, 'outq0_88' : -4}, {('q0_88', 'outq0_88') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_88']==q0_88 and int(energy)==0:
        q0_88_before = sample['q0_88']
        q0_88=sample['outq0_88']
        break

print('#' * 80)
print("NOT operation on q0_88:")
print("    in:  q0_88={0}".format(q0_88_before))
print("    out: q0_88={0}".format(q0_88))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_88 ##
################################################################################
if 'q1_88' not in globals():
    q1_88=0

bqm = dimod.BinaryQuadraticModel({'q1_88' : -4, 'outq1_88' : -4}, {('q1_88', 'outq1_88') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_88']==q1_88 and int(energy)==0:
        q1_88_before = sample['q1_88']
        q1_88=sample['outq1_88']
        break

print('#' * 80)
print("NOT operation on q1_88:")
print("    in:  q1_88={0}".format(q1_88_before))
print("    out: q1_88={0}".format(q1_88))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_87 ##
################################################################################
if 'q1_87' not in globals():
    q1_87=0

bqm = dimod.BinaryQuadraticModel({'q1_87' : -4, 'outq1_87' : -4}, {('q1_87', 'outq1_87') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_87']==q1_87 and int(energy)==0:
        q1_87_before = sample['q1_87']
        q1_87=sample['outq1_87']
        break

print('#' * 80)
print("NOT operation on q1_87:")
print("    in:  q1_87={0}".format(q1_87_before))
print("    out: q1_87={0}".format(q1_87))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_86 ##
################################################################################
if 'q0_86' not in globals():
    q0_86=0

bqm = dimod.BinaryQuadraticModel({'q0_86' : -4, 'outq0_86' : -4}, {('q0_86', 'outq0_86') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_86']==q0_86 and int(energy)==0:
        q0_86_before = sample['q0_86']
        q0_86=sample['outq0_86']
        break

print('#' * 80)
print("NOT operation on q0_86:")
print("    in:  q0_86={0}".format(q0_86_before))
print("    out: q0_86={0}".format(q0_86))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_85 ##
################################################################################
if 'q1_85' not in globals():
    q1_85=0

bqm = dimod.BinaryQuadraticModel({'q1_85' : -4, 'outq1_85' : -4}, {('q1_85', 'outq1_85') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_85']==q1_85 and int(energy)==0:
        q1_85_before = sample['q1_85']
        q1_85=sample['outq1_85']
        break

print('#' * 80)
print("NOT operation on q1_85:")
print("    in:  q1_85={0}".format(q1_85_before))
print("    out: q1_85={0}".format(q1_85))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_80 ##
################################################################################
if 'q1_80' not in globals():
    q1_80=0

bqm = dimod.BinaryQuadraticModel({'q1_80' : -4, 'outq1_80' : -4}, {('q1_80', 'outq1_80') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_80']==q1_80 and int(energy)==0:
        q1_80_before = sample['q1_80']
        q1_80=sample['outq1_80']
        break

print('#' * 80)
print("NOT operation on q1_80:")
print("    in:  q1_80={0}".format(q1_80_before))
print("    out: q1_80={0}".format(q1_80))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_79 ##
################################################################################
if 'q0_79' not in globals():
    q0_79=0

bqm = dimod.BinaryQuadraticModel({'q0_79' : -4, 'outq0_79' : -4}, {('q0_79', 'outq0_79') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_79']==q0_79 and int(energy)==0:
        q0_79_before = sample['q0_79']
        q0_79=sample['outq0_79']
        break

print('#' * 80)
print("NOT operation on q0_79:")
print("    in:  q0_79={0}".format(q0_79_before))
print("    out: q0_79={0}".format(q0_79))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_79 ##
################################################################################
if 'q1_79' not in globals():
    q1_79=0

bqm = dimod.BinaryQuadraticModel({'q1_79' : -4, 'outq1_79' : -4}, {('q1_79', 'outq1_79') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_79']==q1_79 and int(energy)==0:
        q1_79_before = sample['q1_79']
        q1_79=sample['outq1_79']
        break

print('#' * 80)
print("NOT operation on q1_79:")
print("    in:  q1_79={0}".format(q1_79_before))
print("    out: q1_79={0}".format(q1_79))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_78 ##
################################################################################
if 'q1_78' not in globals():
    q1_78=0

bqm = dimod.BinaryQuadraticModel({'q1_78' : -4, 'outq1_78' : -4}, {('q1_78', 'outq1_78') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_78']==q1_78 and int(energy)==0:
        q1_78_before = sample['q1_78']
        q1_78=sample['outq1_78']
        break

print('#' * 80)
print("NOT operation on q1_78:")
print("    in:  q1_78={0}".format(q1_78_before))
print("    out: q1_78={0}".format(q1_78))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_77 ##
################################################################################
if 'q0_77' not in globals():
    q0_77=0

bqm = dimod.BinaryQuadraticModel({'q0_77' : -4, 'outq0_77' : -4}, {('q0_77', 'outq0_77') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_77']==q0_77 and int(energy)==0:
        q0_77_before = sample['q0_77']
        q0_77=sample['outq0_77']
        break

print('#' * 80)
print("NOT operation on q0_77:")
print("    in:  q0_77={0}".format(q0_77_before))
print("    out: q0_77={0}".format(q0_77))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_76 ##
################################################################################
if 'q0_76' not in globals():
    q0_76=0

bqm = dimod.BinaryQuadraticModel({'q0_76' : -4, 'outq0_76' : -4}, {('q0_76', 'outq0_76') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_76']==q0_76 and int(energy)==0:
        q0_76_before = sample['q0_76']
        q0_76=sample['outq0_76']
        break

print('#' * 80)
print("NOT operation on q0_76:")
print("    in:  q0_76={0}".format(q0_76_before))
print("    out: q0_76={0}".format(q0_76))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_76 ##
################################################################################
if 'q1_76' not in globals():
    q1_76=0

bqm = dimod.BinaryQuadraticModel({'q1_76' : -4, 'outq1_76' : -4}, {('q1_76', 'outq1_76') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_76']==q1_76 and int(energy)==0:
        q1_76_before = sample['q1_76']
        q1_76=sample['outq1_76']
        break

print('#' * 80)
print("NOT operation on q1_76:")
print("    in:  q1_76={0}".format(q1_76_before))
print("    out: q1_76={0}".format(q1_76))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_75 ##
################################################################################
if 'q0_75' not in globals():
    q0_75=0

bqm = dimod.BinaryQuadraticModel({'q0_75' : -4, 'outq0_75' : -4}, {('q0_75', 'outq0_75') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_75']==q0_75 and int(energy)==0:
        q0_75_before = sample['q0_75']
        q0_75=sample['outq0_75']
        break

print('#' * 80)
print("NOT operation on q0_75:")
print("    in:  q0_75={0}".format(q0_75_before))
print("    out: q0_75={0}".format(q0_75))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_75 ##
################################################################################
if 'q1_75' not in globals():
    q1_75=0

bqm = dimod.BinaryQuadraticModel({'q1_75' : -4, 'outq1_75' : -4}, {('q1_75', 'outq1_75') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_75']==q1_75 and int(energy)==0:
        q1_75_before = sample['q1_75']
        q1_75=sample['outq1_75']
        break

print('#' * 80)
print("NOT operation on q1_75:")
print("    in:  q1_75={0}".format(q1_75_before))
print("    out: q1_75={0}".format(q1_75))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_74 ##
################################################################################
if 'q0_74' not in globals():
    q0_74=0

bqm = dimod.BinaryQuadraticModel({'q0_74' : -4, 'outq0_74' : -4}, {('q0_74', 'outq0_74') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_74']==q0_74 and int(energy)==0:
        q0_74_before = sample['q0_74']
        q0_74=sample['outq0_74']
        break

print('#' * 80)
print("NOT operation on q0_74:")
print("    in:  q0_74={0}".format(q0_74_before))
print("    out: q0_74={0}".format(q0_74))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_73 ##
################################################################################
if 'q1_73' not in globals():
    q1_73=0

bqm = dimod.BinaryQuadraticModel({'q1_73' : -4, 'outq1_73' : -4}, {('q1_73', 'outq1_73') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_73']==q1_73 and int(energy)==0:
        q1_73_before = sample['q1_73']
        q1_73=sample['outq1_73']
        break

print('#' * 80)
print("NOT operation on q1_73:")
print("    in:  q1_73={0}".format(q1_73_before))
print("    out: q1_73={0}".format(q1_73))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_72 ##
################################################################################
if 'q0_72' not in globals():
    q0_72=0

bqm = dimod.BinaryQuadraticModel({'q0_72' : -4, 'outq0_72' : -4}, {('q0_72', 'outq0_72') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_72']==q0_72 and int(energy)==0:
        q0_72_before = sample['q0_72']
        q0_72=sample['outq0_72']
        break

print('#' * 80)
print("NOT operation on q0_72:")
print("    in:  q0_72={0}".format(q0_72_before))
print("    out: q0_72={0}".format(q0_72))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_69 ##
################################################################################
if 'q1_69' not in globals():
    q1_69=0

bqm = dimod.BinaryQuadraticModel({'q1_69' : -4, 'outq1_69' : -4}, {('q1_69', 'outq1_69') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_69']==q1_69 and int(energy)==0:
        q1_69_before = sample['q1_69']
        q1_69=sample['outq1_69']
        break

print('#' * 80)
print("NOT operation on q1_69:")
print("    in:  q1_69={0}".format(q1_69_before))
print("    out: q1_69={0}".format(q1_69))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_68 ##
################################################################################
if 'q0_68' not in globals():
    q0_68=0

bqm = dimod.BinaryQuadraticModel({'q0_68' : -4, 'outq0_68' : -4}, {('q0_68', 'outq0_68') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_68']==q0_68 and int(energy)==0:
        q0_68_before = sample['q0_68']
        q0_68=sample['outq0_68']
        break

print('#' * 80)
print("NOT operation on q0_68:")
print("    in:  q0_68={0}".format(q0_68_before))
print("    out: q0_68={0}".format(q0_68))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_68 ##
################################################################################
if 'q1_68' not in globals():
    q1_68=0

bqm = dimod.BinaryQuadraticModel({'q1_68' : -4, 'outq1_68' : -4}, {('q1_68', 'outq1_68') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_68']==q1_68 and int(energy)==0:
        q1_68_before = sample['q1_68']
        q1_68=sample['outq1_68']
        break

print('#' * 80)
print("NOT operation on q1_68:")
print("    in:  q1_68={0}".format(q1_68_before))
print("    out: q1_68={0}".format(q1_68))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_67 ##
################################################################################
if 'q1_67' not in globals():
    q1_67=0

bqm = dimod.BinaryQuadraticModel({'q1_67' : -4, 'outq1_67' : -4}, {('q1_67', 'outq1_67') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_67']==q1_67 and int(energy)==0:
        q1_67_before = sample['q1_67']
        q1_67=sample['outq1_67']
        break

print('#' * 80)
print("NOT operation on q1_67:")
print("    in:  q1_67={0}".format(q1_67_before))
print("    out: q1_67={0}".format(q1_67))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_65 ##
################################################################################
if 'q1_65' not in globals():
    q1_65=0

bqm = dimod.BinaryQuadraticModel({'q1_65' : -4, 'outq1_65' : -4}, {('q1_65', 'outq1_65') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_65']==q1_65 and int(energy)==0:
        q1_65_before = sample['q1_65']
        q1_65=sample['outq1_65']
        break

print('#' * 80)
print("NOT operation on q1_65:")
print("    in:  q1_65={0}".format(q1_65_before))
print("    out: q1_65={0}".format(q1_65))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_64 ##
################################################################################
if 'q1_64' not in globals():
    q1_64=0

bqm = dimod.BinaryQuadraticModel({'q1_64' : -4, 'outq1_64' : -4}, {('q1_64', 'outq1_64') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_64']==q1_64 and int(energy)==0:
        q1_64_before = sample['q1_64']
        q1_64=sample['outq1_64']
        break

print('#' * 80)
print("NOT operation on q1_64:")
print("    in:  q1_64={0}".format(q1_64_before))
print("    out: q1_64={0}".format(q1_64))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_63 ##
################################################################################
if 'q1_63' not in globals():
    q1_63=0

bqm = dimod.BinaryQuadraticModel({'q1_63' : -4, 'outq1_63' : -4}, {('q1_63', 'outq1_63') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_63']==q1_63 and int(energy)==0:
        q1_63_before = sample['q1_63']
        q1_63=sample['outq1_63']
        break

print('#' * 80)
print("NOT operation on q1_63:")
print("    in:  q1_63={0}".format(q1_63_before))
print("    out: q1_63={0}".format(q1_63))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_57 ##
################################################################################
if 'q1_57' not in globals():
    q1_57=0

bqm = dimod.BinaryQuadraticModel({'q1_57' : -4, 'outq1_57' : -4}, {('q1_57', 'outq1_57') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_57']==q1_57 and int(energy)==0:
        q1_57_before = sample['q1_57']
        q1_57=sample['outq1_57']
        break

print('#' * 80)
print("NOT operation on q1_57:")
print("    in:  q1_57={0}".format(q1_57_before))
print("    out: q1_57={0}".format(q1_57))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_54 ##
################################################################################
if 'q1_54' not in globals():
    q1_54=0

bqm = dimod.BinaryQuadraticModel({'q1_54' : -4, 'outq1_54' : -4}, {('q1_54', 'outq1_54') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_54']==q1_54 and int(energy)==0:
        q1_54_before = sample['q1_54']
        q1_54=sample['outq1_54']
        break

print('#' * 80)
print("NOT operation on q1_54:")
print("    in:  q1_54={0}".format(q1_54_before))
print("    out: q1_54={0}".format(q1_54))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_51 ##
################################################################################
if 'q1_51' not in globals():
    q1_51=0

bqm = dimod.BinaryQuadraticModel({'q1_51' : -4, 'outq1_51' : -4}, {('q1_51', 'outq1_51') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_51']==q1_51 and int(energy)==0:
        q1_51_before = sample['q1_51']
        q1_51=sample['outq1_51']
        break

print('#' * 80)
print("NOT operation on q1_51:")
print("    in:  q1_51={0}".format(q1_51_before))
print("    out: q1_51={0}".format(q1_51))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_50 ##
################################################################################
if 'q1_50' not in globals():
    q1_50=0

bqm = dimod.BinaryQuadraticModel({'q1_50' : -4, 'outq1_50' : -4}, {('q1_50', 'outq1_50') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_50']==q1_50 and int(energy)==0:
        q1_50_before = sample['q1_50']
        q1_50=sample['outq1_50']
        break

print('#' * 80)
print("NOT operation on q1_50:")
print("    in:  q1_50={0}".format(q1_50_before))
print("    out: q1_50={0}".format(q1_50))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_49 ##
################################################################################
if 'q1_49' not in globals():
    q1_49=0

bqm = dimod.BinaryQuadraticModel({'q1_49' : -4, 'outq1_49' : -4}, {('q1_49', 'outq1_49') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_49']==q1_49 and int(energy)==0:
        q1_49_before = sample['q1_49']
        q1_49=sample['outq1_49']
        break

print('#' * 80)
print("NOT operation on q1_49:")
print("    in:  q1_49={0}".format(q1_49_before))
print("    out: q1_49={0}".format(q1_49))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_48 ##
################################################################################
if 'q1_48' not in globals():
    q1_48=0

bqm = dimod.BinaryQuadraticModel({'q1_48' : -4, 'outq1_48' : -4}, {('q1_48', 'outq1_48') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_48']==q1_48 and int(energy)==0:
        q1_48_before = sample['q1_48']
        q1_48=sample['outq1_48']
        break

print('#' * 80)
print("NOT operation on q1_48:")
print("    in:  q1_48={0}".format(q1_48_before))
print("    out: q1_48={0}".format(q1_48))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_47 ##
################################################################################
if 'q1_47' not in globals():
    q1_47=0

bqm = dimod.BinaryQuadraticModel({'q1_47' : -4, 'outq1_47' : -4}, {('q1_47', 'outq1_47') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_47']==q1_47 and int(energy)==0:
        q1_47_before = sample['q1_47']
        q1_47=sample['outq1_47']
        break

print('#' * 80)
print("NOT operation on q1_47:")
print("    in:  q1_47={0}".format(q1_47_before))
print("    out: q1_47={0}".format(q1_47))
print('#' * 80)
print()
################################################################################
## NOT - target: q3_0 ##
################################################################################
if 'q3_0' not in globals():
    q3_0=0

bqm = dimod.BinaryQuadraticModel({'q3_0' : -4, 'outq3_0' : -4}, {('q3_0', 'outq3_0') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q3_0']==q3_0 and int(energy)==0:
        q3_0_before = sample['q3_0']
        q3_0=sample['outq3_0']
        break

print('#' * 80)
print("NOT operation on q3_0:")
print("    in:  q3_0={0}".format(q3_0_before))
print("    out: q3_0={0}".format(q3_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q3_0 target: q4_0 ##
################################################################################
if 'q3_0' not in globals():
    q3_0=0
if 'q4_0' not in globals():
    q4_0=0

bqm = dimod.BinaryQuadraticModel({'q3_0' : 1, 'q4_0' : 1, 'outq4_0' : 1, 'anc' : 4}, {('q3_0', 'q4_0') : 2, ('q3_0', 'outq4_0') : -2, ('q4_0', 'outq4_0') : -2, ('q3_0', 'anc') : -4, ('q4_0', 'anc') : -4, ('outq4_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q3_0']==q3_0 and sample['q4_0']==q4_0 and int(energy)==0:
        q3_0=sample['q3_0']
        q4_0=sample['outq4_0']
        tgt_before = sample['q4_0']
        break

print('#' * 80)
print("CNOT operation on q3_0 (control) and q4_0 (target):")
print("    in:  q3_0={0}, q4_0={1}".format(q3_0,tgt_before))
print("    out: q3_0={0}, q4_0={1}".format(q3_0,q4_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_99 control2: q3_0 target: q4_0 ##
################################################################################
if 'q0_99' not in globals():
    q0_99=0
if 'q3_0' not in globals():
    q3_0=0
if 'q4_0' not in globals():
    q4_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq4_0' : 1, 'q4_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq4_0') : 4, ('anc1','q4_0') : -4, ('anc2', 'q0_99') : -2, ('anc2', 'q3_0') : -2, ('anc2', 'outq4_0') : -2, ('anc2', 'q4_0') : 2, ('q0_99', 'q3_0') : 1, ('outq4_0', 'q4_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_99']==q0_99 and sample['q3_0']==q3_0 and sample['q4_0']==q4_0 and int(energy)==0:
        q0_99=sample['q0_99']
        q3_0=sample['q3_0']
        q4_0=sample['outq4_0']
        tgt_before = sample['q4_0']
        break

print('#' * 80)
print("CCNOT operation on q0_99 (control1), q3_0 (control2) and q4_0 (target):")
print("    in:  q0_99={0}, q3_0={1}, q4_0={2}".format(q0_99,q3_0,tgt_before))
print("    out: q0_99={0}, q3_0={1}, q4_0={2}".format(q0_99,q3_0,q4_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_99 control2: q3_0 target: q4_0 ##
################################################################################
if 'q1_99' not in globals():
    q1_99=0
if 'q3_0' not in globals():
    q3_0=0
if 'q4_0' not in globals():
    q4_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq4_0' : 1, 'q4_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq4_0') : 4, ('anc1','q4_0') : -4, ('anc2', 'q1_99') : -2, ('anc2', 'q3_0') : -2, ('anc2', 'outq4_0') : -2, ('anc2', 'q4_0') : 2, ('q1_99', 'q3_0') : 1, ('outq4_0', 'q4_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_99']==q1_99 and sample['q3_0']==q3_0 and sample['q4_0']==q4_0 and int(energy)==0:
        q1_99=sample['q1_99']
        q3_0=sample['q3_0']
        q4_0=sample['outq4_0']
        tgt_before = sample['q4_0']
        break

print('#' * 80)
print("CCNOT operation on q1_99 (control1), q3_0 (control2) and q4_0 (target):")
print("    in:  q1_99={0}, q3_0={1}, q4_0={2}".format(q1_99,q3_0,tgt_before))
print("    out: q1_99={0}, q3_0={1}, q4_0={2}".format(q1_99,q3_0,q4_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q4_0 target: q5_0 ##
################################################################################
if 'q4_0' not in globals():
    q4_0=0
if 'q5_0' not in globals():
    q5_0=0

bqm = dimod.BinaryQuadraticModel({'q4_0' : 1, 'q5_0' : 1, 'outq5_0' : 1, 'anc' : 4}, {('q4_0', 'q5_0') : 2, ('q4_0', 'outq5_0') : -2, ('q5_0', 'outq5_0') : -2, ('q4_0', 'anc') : -4, ('q5_0', 'anc') : -4, ('outq5_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q4_0']==q4_0 and sample['q5_0']==q5_0 and int(energy)==0:
        q4_0=sample['q4_0']
        q5_0=sample['outq5_0']
        tgt_before = sample['q5_0']
        break

print('#' * 80)
print("CNOT operation on q4_0 (control) and q5_0 (target):")
print("    in:  q4_0={0}, q5_0={1}".format(q4_0,tgt_before))
print("    out: q4_0={0}, q5_0={1}".format(q4_0,q5_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_98 control2: q4_0 target: q5_0 ##
################################################################################
if 'q0_98' not in globals():
    q0_98=0
if 'q4_0' not in globals():
    q4_0=0
if 'q5_0' not in globals():
    q5_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq5_0' : 1, 'q5_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq5_0') : 4, ('anc1','q5_0') : -4, ('anc2', 'q0_98') : -2, ('anc2', 'q4_0') : -2, ('anc2', 'outq5_0') : -2, ('anc2', 'q5_0') : 2, ('q0_98', 'q4_0') : 1, ('outq5_0', 'q5_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_98']==q0_98 and sample['q4_0']==q4_0 and sample['q5_0']==q5_0 and int(energy)==0:
        q0_98=sample['q0_98']
        q4_0=sample['q4_0']
        q5_0=sample['outq5_0']
        tgt_before = sample['q5_0']
        break

print('#' * 80)
print("CCNOT operation on q0_98 (control1), q4_0 (control2) and q5_0 (target):")
print("    in:  q0_98={0}, q4_0={1}, q5_0={2}".format(q0_98,q4_0,tgt_before))
print("    out: q0_98={0}, q4_0={1}, q5_0={2}".format(q0_98,q4_0,q5_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_98 control2: q4_0 target: q5_0 ##
################################################################################
if 'q1_98' not in globals():
    q1_98=0
if 'q4_0' not in globals():
    q4_0=0
if 'q5_0' not in globals():
    q5_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq5_0' : 1, 'q5_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq5_0') : 4, ('anc1','q5_0') : -4, ('anc2', 'q1_98') : -2, ('anc2', 'q4_0') : -2, ('anc2', 'outq5_0') : -2, ('anc2', 'q5_0') : 2, ('q1_98', 'q4_0') : 1, ('outq5_0', 'q5_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_98']==q1_98 and sample['q4_0']==q4_0 and sample['q5_0']==q5_0 and int(energy)==0:
        q1_98=sample['q1_98']
        q4_0=sample['q4_0']
        q5_0=sample['outq5_0']
        tgt_before = sample['q5_0']
        break

print('#' * 80)
print("CCNOT operation on q1_98 (control1), q4_0 (control2) and q5_0 (target):")
print("    in:  q1_98={0}, q4_0={1}, q5_0={2}".format(q1_98,q4_0,tgt_before))
print("    out: q1_98={0}, q4_0={1}, q5_0={2}".format(q1_98,q4_0,q5_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q5_0 target: q6_0 ##
################################################################################
if 'q5_0' not in globals():
    q5_0=0
if 'q6_0' not in globals():
    q6_0=0

bqm = dimod.BinaryQuadraticModel({'q5_0' : 1, 'q6_0' : 1, 'outq6_0' : 1, 'anc' : 4}, {('q5_0', 'q6_0') : 2, ('q5_0', 'outq6_0') : -2, ('q6_0', 'outq6_0') : -2, ('q5_0', 'anc') : -4, ('q6_0', 'anc') : -4, ('outq6_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q5_0']==q5_0 and sample['q6_0']==q6_0 and int(energy)==0:
        q5_0=sample['q5_0']
        q6_0=sample['outq6_0']
        tgt_before = sample['q6_0']
        break

print('#' * 80)
print("CNOT operation on q5_0 (control) and q6_0 (target):")
print("    in:  q5_0={0}, q6_0={1}".format(q5_0,tgt_before))
print("    out: q5_0={0}, q6_0={1}".format(q5_0,q6_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_97 control2: q5_0 target: q6_0 ##
################################################################################
if 'q0_97' not in globals():
    q0_97=0
if 'q5_0' not in globals():
    q5_0=0
if 'q6_0' not in globals():
    q6_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq6_0' : 1, 'q6_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq6_0') : 4, ('anc1','q6_0') : -4, ('anc2', 'q0_97') : -2, ('anc2', 'q5_0') : -2, ('anc2', 'outq6_0') : -2, ('anc2', 'q6_0') : 2, ('q0_97', 'q5_0') : 1, ('outq6_0', 'q6_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_97']==q0_97 and sample['q5_0']==q5_0 and sample['q6_0']==q6_0 and int(energy)==0:
        q0_97=sample['q0_97']
        q5_0=sample['q5_0']
        q6_0=sample['outq6_0']
        tgt_before = sample['q6_0']
        break

print('#' * 80)
print("CCNOT operation on q0_97 (control1), q5_0 (control2) and q6_0 (target):")
print("    in:  q0_97={0}, q5_0={1}, q6_0={2}".format(q0_97,q5_0,tgt_before))
print("    out: q0_97={0}, q5_0={1}, q6_0={2}".format(q0_97,q5_0,q6_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_97 control2: q5_0 target: q6_0 ##
################################################################################
if 'q1_97' not in globals():
    q1_97=0
if 'q5_0' not in globals():
    q5_0=0
if 'q6_0' not in globals():
    q6_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq6_0' : 1, 'q6_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq6_0') : 4, ('anc1','q6_0') : -4, ('anc2', 'q1_97') : -2, ('anc2', 'q5_0') : -2, ('anc2', 'outq6_0') : -2, ('anc2', 'q6_0') : 2, ('q1_97', 'q5_0') : 1, ('outq6_0', 'q6_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_97']==q1_97 and sample['q5_0']==q5_0 and sample['q6_0']==q6_0 and int(energy)==0:
        q1_97=sample['q1_97']
        q5_0=sample['q5_0']
        q6_0=sample['outq6_0']
        tgt_before = sample['q6_0']
        break

print('#' * 80)
print("CCNOT operation on q1_97 (control1), q5_0 (control2) and q6_0 (target):")
print("    in:  q1_97={0}, q5_0={1}, q6_0={2}".format(q1_97,q5_0,tgt_before))
print("    out: q1_97={0}, q5_0={1}, q6_0={2}".format(q1_97,q5_0,q6_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q6_0 target: q7_0 ##
################################################################################
if 'q6_0' not in globals():
    q6_0=0
if 'q7_0' not in globals():
    q7_0=0

bqm = dimod.BinaryQuadraticModel({'q6_0' : 1, 'q7_0' : 1, 'outq7_0' : 1, 'anc' : 4}, {('q6_0', 'q7_0') : 2, ('q6_0', 'outq7_0') : -2, ('q7_0', 'outq7_0') : -2, ('q6_0', 'anc') : -4, ('q7_0', 'anc') : -4, ('outq7_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q6_0']==q6_0 and sample['q7_0']==q7_0 and int(energy)==0:
        q6_0=sample['q6_0']
        q7_0=sample['outq7_0']
        tgt_before = sample['q7_0']
        break

print('#' * 80)
print("CNOT operation on q6_0 (control) and q7_0 (target):")
print("    in:  q6_0={0}, q7_0={1}".format(q6_0,tgt_before))
print("    out: q6_0={0}, q7_0={1}".format(q6_0,q7_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_96 control2: q6_0 target: q7_0 ##
################################################################################
if 'q0_96' not in globals():
    q0_96=0
if 'q6_0' not in globals():
    q6_0=0
if 'q7_0' not in globals():
    q7_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq7_0' : 1, 'q7_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq7_0') : 4, ('anc1','q7_0') : -4, ('anc2', 'q0_96') : -2, ('anc2', 'q6_0') : -2, ('anc2', 'outq7_0') : -2, ('anc2', 'q7_0') : 2, ('q0_96', 'q6_0') : 1, ('outq7_0', 'q7_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_96']==q0_96 and sample['q6_0']==q6_0 and sample['q7_0']==q7_0 and int(energy)==0:
        q0_96=sample['q0_96']
        q6_0=sample['q6_0']
        q7_0=sample['outq7_0']
        tgt_before = sample['q7_0']
        break

print('#' * 80)
print("CCNOT operation on q0_96 (control1), q6_0 (control2) and q7_0 (target):")
print("    in:  q0_96={0}, q6_0={1}, q7_0={2}".format(q0_96,q6_0,tgt_before))
print("    out: q0_96={0}, q6_0={1}, q7_0={2}".format(q0_96,q6_0,q7_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_96 control2: q6_0 target: q7_0 ##
################################################################################
if 'q1_96' not in globals():
    q1_96=0
if 'q6_0' not in globals():
    q6_0=0
if 'q7_0' not in globals():
    q7_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq7_0' : 1, 'q7_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq7_0') : 4, ('anc1','q7_0') : -4, ('anc2', 'q1_96') : -2, ('anc2', 'q6_0') : -2, ('anc2', 'outq7_0') : -2, ('anc2', 'q7_0') : 2, ('q1_96', 'q6_0') : 1, ('outq7_0', 'q7_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_96']==q1_96 and sample['q6_0']==q6_0 and sample['q7_0']==q7_0 and int(energy)==0:
        q1_96=sample['q1_96']
        q6_0=sample['q6_0']
        q7_0=sample['outq7_0']
        tgt_before = sample['q7_0']
        break

print('#' * 80)
print("CCNOT operation on q1_96 (control1), q6_0 (control2) and q7_0 (target):")
print("    in:  q1_96={0}, q6_0={1}, q7_0={2}".format(q1_96,q6_0,tgt_before))
print("    out: q1_96={0}, q6_0={1}, q7_0={2}".format(q1_96,q6_0,q7_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q7_0 target: q8_0 ##
################################################################################
if 'q7_0' not in globals():
    q7_0=0
if 'q8_0' not in globals():
    q8_0=0

bqm = dimod.BinaryQuadraticModel({'q7_0' : 1, 'q8_0' : 1, 'outq8_0' : 1, 'anc' : 4}, {('q7_0', 'q8_0') : 2, ('q7_0', 'outq8_0') : -2, ('q8_0', 'outq8_0') : -2, ('q7_0', 'anc') : -4, ('q8_0', 'anc') : -4, ('outq8_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q7_0']==q7_0 and sample['q8_0']==q8_0 and int(energy)==0:
        q7_0=sample['q7_0']
        q8_0=sample['outq8_0']
        tgt_before = sample['q8_0']
        break

print('#' * 80)
print("CNOT operation on q7_0 (control) and q8_0 (target):")
print("    in:  q7_0={0}, q8_0={1}".format(q7_0,tgt_before))
print("    out: q7_0={0}, q8_0={1}".format(q7_0,q8_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_95 control2: q7_0 target: q8_0 ##
################################################################################
if 'q0_95' not in globals():
    q0_95=0
if 'q7_0' not in globals():
    q7_0=0
if 'q8_0' not in globals():
    q8_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq8_0' : 1, 'q8_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq8_0') : 4, ('anc1','q8_0') : -4, ('anc2', 'q0_95') : -2, ('anc2', 'q7_0') : -2, ('anc2', 'outq8_0') : -2, ('anc2', 'q8_0') : 2, ('q0_95', 'q7_0') : 1, ('outq8_0', 'q8_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_95']==q0_95 and sample['q7_0']==q7_0 and sample['q8_0']==q8_0 and int(energy)==0:
        q0_95=sample['q0_95']
        q7_0=sample['q7_0']
        q8_0=sample['outq8_0']
        tgt_before = sample['q8_0']
        break

print('#' * 80)
print("CCNOT operation on q0_95 (control1), q7_0 (control2) and q8_0 (target):")
print("    in:  q0_95={0}, q7_0={1}, q8_0={2}".format(q0_95,q7_0,tgt_before))
print("    out: q0_95={0}, q7_0={1}, q8_0={2}".format(q0_95,q7_0,q8_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_95 control2: q7_0 target: q8_0 ##
################################################################################
if 'q1_95' not in globals():
    q1_95=0
if 'q7_0' not in globals():
    q7_0=0
if 'q8_0' not in globals():
    q8_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq8_0' : 1, 'q8_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq8_0') : 4, ('anc1','q8_0') : -4, ('anc2', 'q1_95') : -2, ('anc2', 'q7_0') : -2, ('anc2', 'outq8_0') : -2, ('anc2', 'q8_0') : 2, ('q1_95', 'q7_0') : 1, ('outq8_0', 'q8_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_95']==q1_95 and sample['q7_0']==q7_0 and sample['q8_0']==q8_0 and int(energy)==0:
        q1_95=sample['q1_95']
        q7_0=sample['q7_0']
        q8_0=sample['outq8_0']
        tgt_before = sample['q8_0']
        break

print('#' * 80)
print("CCNOT operation on q1_95 (control1), q7_0 (control2) and q8_0 (target):")
print("    in:  q1_95={0}, q7_0={1}, q8_0={2}".format(q1_95,q7_0,tgt_before))
print("    out: q1_95={0}, q7_0={1}, q8_0={2}".format(q1_95,q7_0,q8_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q8_0 target: q9_0 ##
################################################################################
if 'q8_0' not in globals():
    q8_0=0
if 'q9_0' not in globals():
    q9_0=0

bqm = dimod.BinaryQuadraticModel({'q8_0' : 1, 'q9_0' : 1, 'outq9_0' : 1, 'anc' : 4}, {('q8_0', 'q9_0') : 2, ('q8_0', 'outq9_0') : -2, ('q9_0', 'outq9_0') : -2, ('q8_0', 'anc') : -4, ('q9_0', 'anc') : -4, ('outq9_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q8_0']==q8_0 and sample['q9_0']==q9_0 and int(energy)==0:
        q8_0=sample['q8_0']
        q9_0=sample['outq9_0']
        tgt_before = sample['q9_0']
        break

print('#' * 80)
print("CNOT operation on q8_0 (control) and q9_0 (target):")
print("    in:  q8_0={0}, q9_0={1}".format(q8_0,tgt_before))
print("    out: q8_0={0}, q9_0={1}".format(q8_0,q9_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_94 control2: q8_0 target: q9_0 ##
################################################################################
if 'q0_94' not in globals():
    q0_94=0
if 'q8_0' not in globals():
    q8_0=0
if 'q9_0' not in globals():
    q9_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq9_0' : 1, 'q9_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq9_0') : 4, ('anc1','q9_0') : -4, ('anc2', 'q0_94') : -2, ('anc2', 'q8_0') : -2, ('anc2', 'outq9_0') : -2, ('anc2', 'q9_0') : 2, ('q0_94', 'q8_0') : 1, ('outq9_0', 'q9_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_94']==q0_94 and sample['q8_0']==q8_0 and sample['q9_0']==q9_0 and int(energy)==0:
        q0_94=sample['q0_94']
        q8_0=sample['q8_0']
        q9_0=sample['outq9_0']
        tgt_before = sample['q9_0']
        break

print('#' * 80)
print("CCNOT operation on q0_94 (control1), q8_0 (control2) and q9_0 (target):")
print("    in:  q0_94={0}, q8_0={1}, q9_0={2}".format(q0_94,q8_0,tgt_before))
print("    out: q0_94={0}, q8_0={1}, q9_0={2}".format(q0_94,q8_0,q9_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_94 control2: q8_0 target: q9_0 ##
################################################################################
if 'q1_94' not in globals():
    q1_94=0
if 'q8_0' not in globals():
    q8_0=0
if 'q9_0' not in globals():
    q9_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq9_0' : 1, 'q9_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq9_0') : 4, ('anc1','q9_0') : -4, ('anc2', 'q1_94') : -2, ('anc2', 'q8_0') : -2, ('anc2', 'outq9_0') : -2, ('anc2', 'q9_0') : 2, ('q1_94', 'q8_0') : 1, ('outq9_0', 'q9_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_94']==q1_94 and sample['q8_0']==q8_0 and sample['q9_0']==q9_0 and int(energy)==0:
        q1_94=sample['q1_94']
        q8_0=sample['q8_0']
        q9_0=sample['outq9_0']
        tgt_before = sample['q9_0']
        break

print('#' * 80)
print("CCNOT operation on q1_94 (control1), q8_0 (control2) and q9_0 (target):")
print("    in:  q1_94={0}, q8_0={1}, q9_0={2}".format(q1_94,q8_0,tgt_before))
print("    out: q1_94={0}, q8_0={1}, q9_0={2}".format(q1_94,q8_0,q9_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q9_0 target: q10_0 ##
################################################################################
if 'q9_0' not in globals():
    q9_0=0
if 'q10_0' not in globals():
    q10_0=0

bqm = dimod.BinaryQuadraticModel({'q9_0' : 1, 'q10_0' : 1, 'outq10_0' : 1, 'anc' : 4}, {('q9_0', 'q10_0') : 2, ('q9_0', 'outq10_0') : -2, ('q10_0', 'outq10_0') : -2, ('q9_0', 'anc') : -4, ('q10_0', 'anc') : -4, ('outq10_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q9_0']==q9_0 and sample['q10_0']==q10_0 and int(energy)==0:
        q9_0=sample['q9_0']
        q10_0=sample['outq10_0']
        tgt_before = sample['q10_0']
        break

print('#' * 80)
print("CNOT operation on q9_0 (control) and q10_0 (target):")
print("    in:  q9_0={0}, q10_0={1}".format(q9_0,tgt_before))
print("    out: q9_0={0}, q10_0={1}".format(q9_0,q10_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_93 control2: q9_0 target: q10_0 ##
################################################################################
if 'q0_93' not in globals():
    q0_93=0
if 'q9_0' not in globals():
    q9_0=0
if 'q10_0' not in globals():
    q10_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq10_0' : 1, 'q10_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq10_0') : 4, ('anc1','q10_0') : -4, ('anc2', 'q0_93') : -2, ('anc2', 'q9_0') : -2, ('anc2', 'outq10_0') : -2, ('anc2', 'q10_0') : 2, ('q0_93', 'q9_0') : 1, ('outq10_0', 'q10_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_93']==q0_93 and sample['q9_0']==q9_0 and sample['q10_0']==q10_0 and int(energy)==0:
        q0_93=sample['q0_93']
        q9_0=sample['q9_0']
        q10_0=sample['outq10_0']
        tgt_before = sample['q10_0']
        break

print('#' * 80)
print("CCNOT operation on q0_93 (control1), q9_0 (control2) and q10_0 (target):")
print("    in:  q0_93={0}, q9_0={1}, q10_0={2}".format(q0_93,q9_0,tgt_before))
print("    out: q0_93={0}, q9_0={1}, q10_0={2}".format(q0_93,q9_0,q10_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_93 control2: q9_0 target: q10_0 ##
################################################################################
if 'q1_93' not in globals():
    q1_93=0
if 'q9_0' not in globals():
    q9_0=0
if 'q10_0' not in globals():
    q10_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq10_0' : 1, 'q10_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq10_0') : 4, ('anc1','q10_0') : -4, ('anc2', 'q1_93') : -2, ('anc2', 'q9_0') : -2, ('anc2', 'outq10_0') : -2, ('anc2', 'q10_0') : 2, ('q1_93', 'q9_0') : 1, ('outq10_0', 'q10_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_93']==q1_93 and sample['q9_0']==q9_0 and sample['q10_0']==q10_0 and int(energy)==0:
        q1_93=sample['q1_93']
        q9_0=sample['q9_0']
        q10_0=sample['outq10_0']
        tgt_before = sample['q10_0']
        break

print('#' * 80)
print("CCNOT operation on q1_93 (control1), q9_0 (control2) and q10_0 (target):")
print("    in:  q1_93={0}, q9_0={1}, q10_0={2}".format(q1_93,q9_0,tgt_before))
print("    out: q1_93={0}, q9_0={1}, q10_0={2}".format(q1_93,q9_0,q10_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q10_0 target: q11_0 ##
################################################################################
if 'q10_0' not in globals():
    q10_0=0
if 'q11_0' not in globals():
    q11_0=0

bqm = dimod.BinaryQuadraticModel({'q10_0' : 1, 'q11_0' : 1, 'outq11_0' : 1, 'anc' : 4}, {('q10_0', 'q11_0') : 2, ('q10_0', 'outq11_0') : -2, ('q11_0', 'outq11_0') : -2, ('q10_0', 'anc') : -4, ('q11_0', 'anc') : -4, ('outq11_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q10_0']==q10_0 and sample['q11_0']==q11_0 and int(energy)==0:
        q10_0=sample['q10_0']
        q11_0=sample['outq11_0']
        tgt_before = sample['q11_0']
        break

print('#' * 80)
print("CNOT operation on q10_0 (control) and q11_0 (target):")
print("    in:  q10_0={0}, q11_0={1}".format(q10_0,tgt_before))
print("    out: q10_0={0}, q11_0={1}".format(q10_0,q11_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_92 control2: q10_0 target: q11_0 ##
################################################################################
if 'q0_92' not in globals():
    q0_92=0
if 'q10_0' not in globals():
    q10_0=0
if 'q11_0' not in globals():
    q11_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq11_0' : 1, 'q11_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq11_0') : 4, ('anc1','q11_0') : -4, ('anc2', 'q0_92') : -2, ('anc2', 'q10_0') : -2, ('anc2', 'outq11_0') : -2, ('anc2', 'q11_0') : 2, ('q0_92', 'q10_0') : 1, ('outq11_0', 'q11_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_92']==q0_92 and sample['q10_0']==q10_0 and sample['q11_0']==q11_0 and int(energy)==0:
        q0_92=sample['q0_92']
        q10_0=sample['q10_0']
        q11_0=sample['outq11_0']
        tgt_before = sample['q11_0']
        break

print('#' * 80)
print("CCNOT operation on q0_92 (control1), q10_0 (control2) and q11_0 (target):")
print("    in:  q0_92={0}, q10_0={1}, q11_0={2}".format(q0_92,q10_0,tgt_before))
print("    out: q0_92={0}, q10_0={1}, q11_0={2}".format(q0_92,q10_0,q11_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_92 control2: q10_0 target: q11_0 ##
################################################################################
if 'q1_92' not in globals():
    q1_92=0
if 'q10_0' not in globals():
    q10_0=0
if 'q11_0' not in globals():
    q11_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq11_0' : 1, 'q11_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq11_0') : 4, ('anc1','q11_0') : -4, ('anc2', 'q1_92') : -2, ('anc2', 'q10_0') : -2, ('anc2', 'outq11_0') : -2, ('anc2', 'q11_0') : 2, ('q1_92', 'q10_0') : 1, ('outq11_0', 'q11_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_92']==q1_92 and sample['q10_0']==q10_0 and sample['q11_0']==q11_0 and int(energy)==0:
        q1_92=sample['q1_92']
        q10_0=sample['q10_0']
        q11_0=sample['outq11_0']
        tgt_before = sample['q11_0']
        break

print('#' * 80)
print("CCNOT operation on q1_92 (control1), q10_0 (control2) and q11_0 (target):")
print("    in:  q1_92={0}, q10_0={1}, q11_0={2}".format(q1_92,q10_0,tgt_before))
print("    out: q1_92={0}, q10_0={1}, q11_0={2}".format(q1_92,q10_0,q11_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q11_0 target: q12_0 ##
################################################################################
if 'q11_0' not in globals():
    q11_0=0
if 'q12_0' not in globals():
    q12_0=0

bqm = dimod.BinaryQuadraticModel({'q11_0' : 1, 'q12_0' : 1, 'outq12_0' : 1, 'anc' : 4}, {('q11_0', 'q12_0') : 2, ('q11_0', 'outq12_0') : -2, ('q12_0', 'outq12_0') : -2, ('q11_0', 'anc') : -4, ('q12_0', 'anc') : -4, ('outq12_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q11_0']==q11_0 and sample['q12_0']==q12_0 and int(energy)==0:
        q11_0=sample['q11_0']
        q12_0=sample['outq12_0']
        tgt_before = sample['q12_0']
        break

print('#' * 80)
print("CNOT operation on q11_0 (control) and q12_0 (target):")
print("    in:  q11_0={0}, q12_0={1}".format(q11_0,tgt_before))
print("    out: q11_0={0}, q12_0={1}".format(q11_0,q12_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_91 control2: q11_0 target: q12_0 ##
################################################################################
if 'q0_91' not in globals():
    q0_91=0
if 'q11_0' not in globals():
    q11_0=0
if 'q12_0' not in globals():
    q12_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq12_0' : 1, 'q12_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq12_0') : 4, ('anc1','q12_0') : -4, ('anc2', 'q0_91') : -2, ('anc2', 'q11_0') : -2, ('anc2', 'outq12_0') : -2, ('anc2', 'q12_0') : 2, ('q0_91', 'q11_0') : 1, ('outq12_0', 'q12_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_91']==q0_91 and sample['q11_0']==q11_0 and sample['q12_0']==q12_0 and int(energy)==0:
        q0_91=sample['q0_91']
        q11_0=sample['q11_0']
        q12_0=sample['outq12_0']
        tgt_before = sample['q12_0']
        break

print('#' * 80)
print("CCNOT operation on q0_91 (control1), q11_0 (control2) and q12_0 (target):")
print("    in:  q0_91={0}, q11_0={1}, q12_0={2}".format(q0_91,q11_0,tgt_before))
print("    out: q0_91={0}, q11_0={1}, q12_0={2}".format(q0_91,q11_0,q12_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_91 control2: q11_0 target: q12_0 ##
################################################################################
if 'q1_91' not in globals():
    q1_91=0
if 'q11_0' not in globals():
    q11_0=0
if 'q12_0' not in globals():
    q12_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq12_0' : 1, 'q12_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq12_0') : 4, ('anc1','q12_0') : -4, ('anc2', 'q1_91') : -2, ('anc2', 'q11_0') : -2, ('anc2', 'outq12_0') : -2, ('anc2', 'q12_0') : 2, ('q1_91', 'q11_0') : 1, ('outq12_0', 'q12_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_91']==q1_91 and sample['q11_0']==q11_0 and sample['q12_0']==q12_0 and int(energy)==0:
        q1_91=sample['q1_91']
        q11_0=sample['q11_0']
        q12_0=sample['outq12_0']
        tgt_before = sample['q12_0']
        break

print('#' * 80)
print("CCNOT operation on q1_91 (control1), q11_0 (control2) and q12_0 (target):")
print("    in:  q1_91={0}, q11_0={1}, q12_0={2}".format(q1_91,q11_0,tgt_before))
print("    out: q1_91={0}, q11_0={1}, q12_0={2}".format(q1_91,q11_0,q12_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q12_0 target: q13_0 ##
################################################################################
if 'q12_0' not in globals():
    q12_0=0
if 'q13_0' not in globals():
    q13_0=0

bqm = dimod.BinaryQuadraticModel({'q12_0' : 1, 'q13_0' : 1, 'outq13_0' : 1, 'anc' : 4}, {('q12_0', 'q13_0') : 2, ('q12_0', 'outq13_0') : -2, ('q13_0', 'outq13_0') : -2, ('q12_0', 'anc') : -4, ('q13_0', 'anc') : -4, ('outq13_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q12_0']==q12_0 and sample['q13_0']==q13_0 and int(energy)==0:
        q12_0=sample['q12_0']
        q13_0=sample['outq13_0']
        tgt_before = sample['q13_0']
        break

print('#' * 80)
print("CNOT operation on q12_0 (control) and q13_0 (target):")
print("    in:  q12_0={0}, q13_0={1}".format(q12_0,tgt_before))
print("    out: q12_0={0}, q13_0={1}".format(q12_0,q13_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_90 control2: q12_0 target: q13_0 ##
################################################################################
if 'q0_90' not in globals():
    q0_90=0
if 'q12_0' not in globals():
    q12_0=0
if 'q13_0' not in globals():
    q13_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq13_0' : 1, 'q13_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq13_0') : 4, ('anc1','q13_0') : -4, ('anc2', 'q0_90') : -2, ('anc2', 'q12_0') : -2, ('anc2', 'outq13_0') : -2, ('anc2', 'q13_0') : 2, ('q0_90', 'q12_0') : 1, ('outq13_0', 'q13_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_90']==q0_90 and sample['q12_0']==q12_0 and sample['q13_0']==q13_0 and int(energy)==0:
        q0_90=sample['q0_90']
        q12_0=sample['q12_0']
        q13_0=sample['outq13_0']
        tgt_before = sample['q13_0']
        break

print('#' * 80)
print("CCNOT operation on q0_90 (control1), q12_0 (control2) and q13_0 (target):")
print("    in:  q0_90={0}, q12_0={1}, q13_0={2}".format(q0_90,q12_0,tgt_before))
print("    out: q0_90={0}, q12_0={1}, q13_0={2}".format(q0_90,q12_0,q13_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_90 control2: q12_0 target: q13_0 ##
################################################################################
if 'q1_90' not in globals():
    q1_90=0
if 'q12_0' not in globals():
    q12_0=0
if 'q13_0' not in globals():
    q13_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq13_0' : 1, 'q13_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq13_0') : 4, ('anc1','q13_0') : -4, ('anc2', 'q1_90') : -2, ('anc2', 'q12_0') : -2, ('anc2', 'outq13_0') : -2, ('anc2', 'q13_0') : 2, ('q1_90', 'q12_0') : 1, ('outq13_0', 'q13_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_90']==q1_90 and sample['q12_0']==q12_0 and sample['q13_0']==q13_0 and int(energy)==0:
        q1_90=sample['q1_90']
        q12_0=sample['q12_0']
        q13_0=sample['outq13_0']
        tgt_before = sample['q13_0']
        break

print('#' * 80)
print("CCNOT operation on q1_90 (control1), q12_0 (control2) and q13_0 (target):")
print("    in:  q1_90={0}, q12_0={1}, q13_0={2}".format(q1_90,q12_0,tgt_before))
print("    out: q1_90={0}, q12_0={1}, q13_0={2}".format(q1_90,q12_0,q13_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q13_0 target: q14_0 ##
################################################################################
if 'q13_0' not in globals():
    q13_0=0
if 'q14_0' not in globals():
    q14_0=0

bqm = dimod.BinaryQuadraticModel({'q13_0' : 1, 'q14_0' : 1, 'outq14_0' : 1, 'anc' : 4}, {('q13_0', 'q14_0') : 2, ('q13_0', 'outq14_0') : -2, ('q14_0', 'outq14_0') : -2, ('q13_0', 'anc') : -4, ('q14_0', 'anc') : -4, ('outq14_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q13_0']==q13_0 and sample['q14_0']==q14_0 and int(energy)==0:
        q13_0=sample['q13_0']
        q14_0=sample['outq14_0']
        tgt_before = sample['q14_0']
        break

print('#' * 80)
print("CNOT operation on q13_0 (control) and q14_0 (target):")
print("    in:  q13_0={0}, q14_0={1}".format(q13_0,tgt_before))
print("    out: q13_0={0}, q14_0={1}".format(q13_0,q14_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_89 control2: q13_0 target: q14_0 ##
################################################################################
if 'q0_89' not in globals():
    q0_89=0
if 'q13_0' not in globals():
    q13_0=0
if 'q14_0' not in globals():
    q14_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq14_0' : 1, 'q14_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq14_0') : 4, ('anc1','q14_0') : -4, ('anc2', 'q0_89') : -2, ('anc2', 'q13_0') : -2, ('anc2', 'outq14_0') : -2, ('anc2', 'q14_0') : 2, ('q0_89', 'q13_0') : 1, ('outq14_0', 'q14_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_89']==q0_89 and sample['q13_0']==q13_0 and sample['q14_0']==q14_0 and int(energy)==0:
        q0_89=sample['q0_89']
        q13_0=sample['q13_0']
        q14_0=sample['outq14_0']
        tgt_before = sample['q14_0']
        break

print('#' * 80)
print("CCNOT operation on q0_89 (control1), q13_0 (control2) and q14_0 (target):")
print("    in:  q0_89={0}, q13_0={1}, q14_0={2}".format(q0_89,q13_0,tgt_before))
print("    out: q0_89={0}, q13_0={1}, q14_0={2}".format(q0_89,q13_0,q14_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_89 control2: q13_0 target: q14_0 ##
################################################################################
if 'q1_89' not in globals():
    q1_89=0
if 'q13_0' not in globals():
    q13_0=0
if 'q14_0' not in globals():
    q14_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq14_0' : 1, 'q14_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq14_0') : 4, ('anc1','q14_0') : -4, ('anc2', 'q1_89') : -2, ('anc2', 'q13_0') : -2, ('anc2', 'outq14_0') : -2, ('anc2', 'q14_0') : 2, ('q1_89', 'q13_0') : 1, ('outq14_0', 'q14_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_89']==q1_89 and sample['q13_0']==q13_0 and sample['q14_0']==q14_0 and int(energy)==0:
        q1_89=sample['q1_89']
        q13_0=sample['q13_0']
        q14_0=sample['outq14_0']
        tgt_before = sample['q14_0']
        break

print('#' * 80)
print("CCNOT operation on q1_89 (control1), q13_0 (control2) and q14_0 (target):")
print("    in:  q1_89={0}, q13_0={1}, q14_0={2}".format(q1_89,q13_0,tgt_before))
print("    out: q1_89={0}, q13_0={1}, q14_0={2}".format(q1_89,q13_0,q14_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q14_0 target: q15_0 ##
################################################################################
if 'q14_0' not in globals():
    q14_0=0
if 'q15_0' not in globals():
    q15_0=0

bqm = dimod.BinaryQuadraticModel({'q14_0' : 1, 'q15_0' : 1, 'outq15_0' : 1, 'anc' : 4}, {('q14_0', 'q15_0') : 2, ('q14_0', 'outq15_0') : -2, ('q15_0', 'outq15_0') : -2, ('q14_0', 'anc') : -4, ('q15_0', 'anc') : -4, ('outq15_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q14_0']==q14_0 and sample['q15_0']==q15_0 and int(energy)==0:
        q14_0=sample['q14_0']
        q15_0=sample['outq15_0']
        tgt_before = sample['q15_0']
        break

print('#' * 80)
print("CNOT operation on q14_0 (control) and q15_0 (target):")
print("    in:  q14_0={0}, q15_0={1}".format(q14_0,tgt_before))
print("    out: q14_0={0}, q15_0={1}".format(q14_0,q15_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_88 control2: q14_0 target: q15_0 ##
################################################################################
if 'q0_88' not in globals():
    q0_88=0
if 'q14_0' not in globals():
    q14_0=0
if 'q15_0' not in globals():
    q15_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq15_0' : 1, 'q15_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq15_0') : 4, ('anc1','q15_0') : -4, ('anc2', 'q0_88') : -2, ('anc2', 'q14_0') : -2, ('anc2', 'outq15_0') : -2, ('anc2', 'q15_0') : 2, ('q0_88', 'q14_0') : 1, ('outq15_0', 'q15_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_88']==q0_88 and sample['q14_0']==q14_0 and sample['q15_0']==q15_0 and int(energy)==0:
        q0_88=sample['q0_88']
        q14_0=sample['q14_0']
        q15_0=sample['outq15_0']
        tgt_before = sample['q15_0']
        break

print('#' * 80)
print("CCNOT operation on q0_88 (control1), q14_0 (control2) and q15_0 (target):")
print("    in:  q0_88={0}, q14_0={1}, q15_0={2}".format(q0_88,q14_0,tgt_before))
print("    out: q0_88={0}, q14_0={1}, q15_0={2}".format(q0_88,q14_0,q15_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_88 control2: q14_0 target: q15_0 ##
################################################################################
if 'q1_88' not in globals():
    q1_88=0
if 'q14_0' not in globals():
    q14_0=0
if 'q15_0' not in globals():
    q15_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq15_0' : 1, 'q15_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq15_0') : 4, ('anc1','q15_0') : -4, ('anc2', 'q1_88') : -2, ('anc2', 'q14_0') : -2, ('anc2', 'outq15_0') : -2, ('anc2', 'q15_0') : 2, ('q1_88', 'q14_0') : 1, ('outq15_0', 'q15_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_88']==q1_88 and sample['q14_0']==q14_0 and sample['q15_0']==q15_0 and int(energy)==0:
        q1_88=sample['q1_88']
        q14_0=sample['q14_0']
        q15_0=sample['outq15_0']
        tgt_before = sample['q15_0']
        break

print('#' * 80)
print("CCNOT operation on q1_88 (control1), q14_0 (control2) and q15_0 (target):")
print("    in:  q1_88={0}, q14_0={1}, q15_0={2}".format(q1_88,q14_0,tgt_before))
print("    out: q1_88={0}, q14_0={1}, q15_0={2}".format(q1_88,q14_0,q15_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q15_0 target: q16_0 ##
################################################################################
if 'q15_0' not in globals():
    q15_0=0
if 'q16_0' not in globals():
    q16_0=0

bqm = dimod.BinaryQuadraticModel({'q15_0' : 1, 'q16_0' : 1, 'outq16_0' : 1, 'anc' : 4}, {('q15_0', 'q16_0') : 2, ('q15_0', 'outq16_0') : -2, ('q16_0', 'outq16_0') : -2, ('q15_0', 'anc') : -4, ('q16_0', 'anc') : -4, ('outq16_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q15_0']==q15_0 and sample['q16_0']==q16_0 and int(energy)==0:
        q15_0=sample['q15_0']
        q16_0=sample['outq16_0']
        tgt_before = sample['q16_0']
        break

print('#' * 80)
print("CNOT operation on q15_0 (control) and q16_0 (target):")
print("    in:  q15_0={0}, q16_0={1}".format(q15_0,tgt_before))
print("    out: q15_0={0}, q16_0={1}".format(q15_0,q16_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_87 control2: q15_0 target: q16_0 ##
################################################################################
if 'q0_87' not in globals():
    q0_87=0
if 'q15_0' not in globals():
    q15_0=0
if 'q16_0' not in globals():
    q16_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq16_0' : 1, 'q16_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq16_0') : 4, ('anc1','q16_0') : -4, ('anc2', 'q0_87') : -2, ('anc2', 'q15_0') : -2, ('anc2', 'outq16_0') : -2, ('anc2', 'q16_0') : 2, ('q0_87', 'q15_0') : 1, ('outq16_0', 'q16_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_87']==q0_87 and sample['q15_0']==q15_0 and sample['q16_0']==q16_0 and int(energy)==0:
        q0_87=sample['q0_87']
        q15_0=sample['q15_0']
        q16_0=sample['outq16_0']
        tgt_before = sample['q16_0']
        break

print('#' * 80)
print("CCNOT operation on q0_87 (control1), q15_0 (control2) and q16_0 (target):")
print("    in:  q0_87={0}, q15_0={1}, q16_0={2}".format(q0_87,q15_0,tgt_before))
print("    out: q0_87={0}, q15_0={1}, q16_0={2}".format(q0_87,q15_0,q16_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_87 control2: q15_0 target: q16_0 ##
################################################################################
if 'q1_87' not in globals():
    q1_87=0
if 'q15_0' not in globals():
    q15_0=0
if 'q16_0' not in globals():
    q16_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq16_0' : 1, 'q16_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq16_0') : 4, ('anc1','q16_0') : -4, ('anc2', 'q1_87') : -2, ('anc2', 'q15_0') : -2, ('anc2', 'outq16_0') : -2, ('anc2', 'q16_0') : 2, ('q1_87', 'q15_0') : 1, ('outq16_0', 'q16_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_87']==q1_87 and sample['q15_0']==q15_0 and sample['q16_0']==q16_0 and int(energy)==0:
        q1_87=sample['q1_87']
        q15_0=sample['q15_0']
        q16_0=sample['outq16_0']
        tgt_before = sample['q16_0']
        break

print('#' * 80)
print("CCNOT operation on q1_87 (control1), q15_0 (control2) and q16_0 (target):")
print("    in:  q1_87={0}, q15_0={1}, q16_0={2}".format(q1_87,q15_0,tgt_before))
print("    out: q1_87={0}, q15_0={1}, q16_0={2}".format(q1_87,q15_0,q16_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q16_0 target: q17_0 ##
################################################################################
if 'q16_0' not in globals():
    q16_0=0
if 'q17_0' not in globals():
    q17_0=0

bqm = dimod.BinaryQuadraticModel({'q16_0' : 1, 'q17_0' : 1, 'outq17_0' : 1, 'anc' : 4}, {('q16_0', 'q17_0') : 2, ('q16_0', 'outq17_0') : -2, ('q17_0', 'outq17_0') : -2, ('q16_0', 'anc') : -4, ('q17_0', 'anc') : -4, ('outq17_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q16_0']==q16_0 and sample['q17_0']==q17_0 and int(energy)==0:
        q16_0=sample['q16_0']
        q17_0=sample['outq17_0']
        tgt_before = sample['q17_0']
        break

print('#' * 80)
print("CNOT operation on q16_0 (control) and q17_0 (target):")
print("    in:  q16_0={0}, q17_0={1}".format(q16_0,tgt_before))
print("    out: q16_0={0}, q17_0={1}".format(q16_0,q17_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_86 control2: q16_0 target: q17_0 ##
################################################################################
if 'q0_86' not in globals():
    q0_86=0
if 'q16_0' not in globals():
    q16_0=0
if 'q17_0' not in globals():
    q17_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq17_0' : 1, 'q17_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq17_0') : 4, ('anc1','q17_0') : -4, ('anc2', 'q0_86') : -2, ('anc2', 'q16_0') : -2, ('anc2', 'outq17_0') : -2, ('anc2', 'q17_0') : 2, ('q0_86', 'q16_0') : 1, ('outq17_0', 'q17_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_86']==q0_86 and sample['q16_0']==q16_0 and sample['q17_0']==q17_0 and int(energy)==0:
        q0_86=sample['q0_86']
        q16_0=sample['q16_0']
        q17_0=sample['outq17_0']
        tgt_before = sample['q17_0']
        break

print('#' * 80)
print("CCNOT operation on q0_86 (control1), q16_0 (control2) and q17_0 (target):")
print("    in:  q0_86={0}, q16_0={1}, q17_0={2}".format(q0_86,q16_0,tgt_before))
print("    out: q0_86={0}, q16_0={1}, q17_0={2}".format(q0_86,q16_0,q17_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_86 control2: q16_0 target: q17_0 ##
################################################################################
if 'q1_86' not in globals():
    q1_86=0
if 'q16_0' not in globals():
    q16_0=0
if 'q17_0' not in globals():
    q17_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq17_0' : 1, 'q17_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq17_0') : 4, ('anc1','q17_0') : -4, ('anc2', 'q1_86') : -2, ('anc2', 'q16_0') : -2, ('anc2', 'outq17_0') : -2, ('anc2', 'q17_0') : 2, ('q1_86', 'q16_0') : 1, ('outq17_0', 'q17_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_86']==q1_86 and sample['q16_0']==q16_0 and sample['q17_0']==q17_0 and int(energy)==0:
        q1_86=sample['q1_86']
        q16_0=sample['q16_0']
        q17_0=sample['outq17_0']
        tgt_before = sample['q17_0']
        break

print('#' * 80)
print("CCNOT operation on q1_86 (control1), q16_0 (control2) and q17_0 (target):")
print("    in:  q1_86={0}, q16_0={1}, q17_0={2}".format(q1_86,q16_0,tgt_before))
print("    out: q1_86={0}, q16_0={1}, q17_0={2}".format(q1_86,q16_0,q17_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q17_0 target: q18_0 ##
################################################################################
if 'q17_0' not in globals():
    q17_0=0
if 'q18_0' not in globals():
    q18_0=0

bqm = dimod.BinaryQuadraticModel({'q17_0' : 1, 'q18_0' : 1, 'outq18_0' : 1, 'anc' : 4}, {('q17_0', 'q18_0') : 2, ('q17_0', 'outq18_0') : -2, ('q18_0', 'outq18_0') : -2, ('q17_0', 'anc') : -4, ('q18_0', 'anc') : -4, ('outq18_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q17_0']==q17_0 and sample['q18_0']==q18_0 and int(energy)==0:
        q17_0=sample['q17_0']
        q18_0=sample['outq18_0']
        tgt_before = sample['q18_0']
        break

print('#' * 80)
print("CNOT operation on q17_0 (control) and q18_0 (target):")
print("    in:  q17_0={0}, q18_0={1}".format(q17_0,tgt_before))
print("    out: q17_0={0}, q18_0={1}".format(q17_0,q18_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_85 control2: q17_0 target: q18_0 ##
################################################################################
if 'q0_85' not in globals():
    q0_85=0
if 'q17_0' not in globals():
    q17_0=0
if 'q18_0' not in globals():
    q18_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq18_0' : 1, 'q18_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq18_0') : 4, ('anc1','q18_0') : -4, ('anc2', 'q0_85') : -2, ('anc2', 'q17_0') : -2, ('anc2', 'outq18_0') : -2, ('anc2', 'q18_0') : 2, ('q0_85', 'q17_0') : 1, ('outq18_0', 'q18_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_85']==q0_85 and sample['q17_0']==q17_0 and sample['q18_0']==q18_0 and int(energy)==0:
        q0_85=sample['q0_85']
        q17_0=sample['q17_0']
        q18_0=sample['outq18_0']
        tgt_before = sample['q18_0']
        break

print('#' * 80)
print("CCNOT operation on q0_85 (control1), q17_0 (control2) and q18_0 (target):")
print("    in:  q0_85={0}, q17_0={1}, q18_0={2}".format(q0_85,q17_0,tgt_before))
print("    out: q0_85={0}, q17_0={1}, q18_0={2}".format(q0_85,q17_0,q18_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_85 control2: q17_0 target: q18_0 ##
################################################################################
if 'q1_85' not in globals():
    q1_85=0
if 'q17_0' not in globals():
    q17_0=0
if 'q18_0' not in globals():
    q18_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq18_0' : 1, 'q18_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq18_0') : 4, ('anc1','q18_0') : -4, ('anc2', 'q1_85') : -2, ('anc2', 'q17_0') : -2, ('anc2', 'outq18_0') : -2, ('anc2', 'q18_0') : 2, ('q1_85', 'q17_0') : 1, ('outq18_0', 'q18_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_85']==q1_85 and sample['q17_0']==q17_0 and sample['q18_0']==q18_0 and int(energy)==0:
        q1_85=sample['q1_85']
        q17_0=sample['q17_0']
        q18_0=sample['outq18_0']
        tgt_before = sample['q18_0']
        break

print('#' * 80)
print("CCNOT operation on q1_85 (control1), q17_0 (control2) and q18_0 (target):")
print("    in:  q1_85={0}, q17_0={1}, q18_0={2}".format(q1_85,q17_0,tgt_before))
print("    out: q1_85={0}, q17_0={1}, q18_0={2}".format(q1_85,q17_0,q18_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q18_0 target: q19_0 ##
################################################################################
if 'q18_0' not in globals():
    q18_0=0
if 'q19_0' not in globals():
    q19_0=0

bqm = dimod.BinaryQuadraticModel({'q18_0' : 1, 'q19_0' : 1, 'outq19_0' : 1, 'anc' : 4}, {('q18_0', 'q19_0') : 2, ('q18_0', 'outq19_0') : -2, ('q19_0', 'outq19_0') : -2, ('q18_0', 'anc') : -4, ('q19_0', 'anc') : -4, ('outq19_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q18_0']==q18_0 and sample['q19_0']==q19_0 and int(energy)==0:
        q18_0=sample['q18_0']
        q19_0=sample['outq19_0']
        tgt_before = sample['q19_0']
        break

print('#' * 80)
print("CNOT operation on q18_0 (control) and q19_0 (target):")
print("    in:  q18_0={0}, q19_0={1}".format(q18_0,tgt_before))
print("    out: q18_0={0}, q19_0={1}".format(q18_0,q19_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_84 control2: q18_0 target: q19_0 ##
################################################################################
if 'q0_84' not in globals():
    q0_84=0
if 'q18_0' not in globals():
    q18_0=0
if 'q19_0' not in globals():
    q19_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq19_0' : 1, 'q19_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq19_0') : 4, ('anc1','q19_0') : -4, ('anc2', 'q0_84') : -2, ('anc2', 'q18_0') : -2, ('anc2', 'outq19_0') : -2, ('anc2', 'q19_0') : 2, ('q0_84', 'q18_0') : 1, ('outq19_0', 'q19_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_84']==q0_84 and sample['q18_0']==q18_0 and sample['q19_0']==q19_0 and int(energy)==0:
        q0_84=sample['q0_84']
        q18_0=sample['q18_0']
        q19_0=sample['outq19_0']
        tgt_before = sample['q19_0']
        break

print('#' * 80)
print("CCNOT operation on q0_84 (control1), q18_0 (control2) and q19_0 (target):")
print("    in:  q0_84={0}, q18_0={1}, q19_0={2}".format(q0_84,q18_0,tgt_before))
print("    out: q0_84={0}, q18_0={1}, q19_0={2}".format(q0_84,q18_0,q19_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_84 control2: q18_0 target: q19_0 ##
################################################################################
if 'q1_84' not in globals():
    q1_84=0
if 'q18_0' not in globals():
    q18_0=0
if 'q19_0' not in globals():
    q19_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq19_0' : 1, 'q19_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq19_0') : 4, ('anc1','q19_0') : -4, ('anc2', 'q1_84') : -2, ('anc2', 'q18_0') : -2, ('anc2', 'outq19_0') : -2, ('anc2', 'q19_0') : 2, ('q1_84', 'q18_0') : 1, ('outq19_0', 'q19_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_84']==q1_84 and sample['q18_0']==q18_0 and sample['q19_0']==q19_0 and int(energy)==0:
        q1_84=sample['q1_84']
        q18_0=sample['q18_0']
        q19_0=sample['outq19_0']
        tgt_before = sample['q19_0']
        break

print('#' * 80)
print("CCNOT operation on q1_84 (control1), q18_0 (control2) and q19_0 (target):")
print("    in:  q1_84={0}, q18_0={1}, q19_0={2}".format(q1_84,q18_0,tgt_before))
print("    out: q1_84={0}, q18_0={1}, q19_0={2}".format(q1_84,q18_0,q19_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q19_0 target: q20_0 ##
################################################################################
if 'q19_0' not in globals():
    q19_0=0
if 'q20_0' not in globals():
    q20_0=0

bqm = dimod.BinaryQuadraticModel({'q19_0' : 1, 'q20_0' : 1, 'outq20_0' : 1, 'anc' : 4}, {('q19_0', 'q20_0') : 2, ('q19_0', 'outq20_0') : -2, ('q20_0', 'outq20_0') : -2, ('q19_0', 'anc') : -4, ('q20_0', 'anc') : -4, ('outq20_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q19_0']==q19_0 and sample['q20_0']==q20_0 and int(energy)==0:
        q19_0=sample['q19_0']
        q20_0=sample['outq20_0']
        tgt_before = sample['q20_0']
        break

print('#' * 80)
print("CNOT operation on q19_0 (control) and q20_0 (target):")
print("    in:  q19_0={0}, q20_0={1}".format(q19_0,tgt_before))
print("    out: q19_0={0}, q20_0={1}".format(q19_0,q20_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_83 control2: q19_0 target: q20_0 ##
################################################################################
if 'q0_83' not in globals():
    q0_83=0
if 'q19_0' not in globals():
    q19_0=0
if 'q20_0' not in globals():
    q20_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq20_0' : 1, 'q20_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq20_0') : 4, ('anc1','q20_0') : -4, ('anc2', 'q0_83') : -2, ('anc2', 'q19_0') : -2, ('anc2', 'outq20_0') : -2, ('anc2', 'q20_0') : 2, ('q0_83', 'q19_0') : 1, ('outq20_0', 'q20_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_83']==q0_83 and sample['q19_0']==q19_0 and sample['q20_0']==q20_0 and int(energy)==0:
        q0_83=sample['q0_83']
        q19_0=sample['q19_0']
        q20_0=sample['outq20_0']
        tgt_before = sample['q20_0']
        break

print('#' * 80)
print("CCNOT operation on q0_83 (control1), q19_0 (control2) and q20_0 (target):")
print("    in:  q0_83={0}, q19_0={1}, q20_0={2}".format(q0_83,q19_0,tgt_before))
print("    out: q0_83={0}, q19_0={1}, q20_0={2}".format(q0_83,q19_0,q20_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_83 control2: q19_0 target: q20_0 ##
################################################################################
if 'q1_83' not in globals():
    q1_83=0
if 'q19_0' not in globals():
    q19_0=0
if 'q20_0' not in globals():
    q20_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq20_0' : 1, 'q20_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq20_0') : 4, ('anc1','q20_0') : -4, ('anc2', 'q1_83') : -2, ('anc2', 'q19_0') : -2, ('anc2', 'outq20_0') : -2, ('anc2', 'q20_0') : 2, ('q1_83', 'q19_0') : 1, ('outq20_0', 'q20_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_83']==q1_83 and sample['q19_0']==q19_0 and sample['q20_0']==q20_0 and int(energy)==0:
        q1_83=sample['q1_83']
        q19_0=sample['q19_0']
        q20_0=sample['outq20_0']
        tgt_before = sample['q20_0']
        break

print('#' * 80)
print("CCNOT operation on q1_83 (control1), q19_0 (control2) and q20_0 (target):")
print("    in:  q1_83={0}, q19_0={1}, q20_0={2}".format(q1_83,q19_0,tgt_before))
print("    out: q1_83={0}, q19_0={1}, q20_0={2}".format(q1_83,q19_0,q20_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q20_0 target: q21_0 ##
################################################################################
if 'q20_0' not in globals():
    q20_0=0
if 'q21_0' not in globals():
    q21_0=0

bqm = dimod.BinaryQuadraticModel({'q20_0' : 1, 'q21_0' : 1, 'outq21_0' : 1, 'anc' : 4}, {('q20_0', 'q21_0') : 2, ('q20_0', 'outq21_0') : -2, ('q21_0', 'outq21_0') : -2, ('q20_0', 'anc') : -4, ('q21_0', 'anc') : -4, ('outq21_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q20_0']==q20_0 and sample['q21_0']==q21_0 and int(energy)==0:
        q20_0=sample['q20_0']
        q21_0=sample['outq21_0']
        tgt_before = sample['q21_0']
        break

print('#' * 80)
print("CNOT operation on q20_0 (control) and q21_0 (target):")
print("    in:  q20_0={0}, q21_0={1}".format(q20_0,tgt_before))
print("    out: q20_0={0}, q21_0={1}".format(q20_0,q21_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_82 control2: q20_0 target: q21_0 ##
################################################################################
if 'q0_82' not in globals():
    q0_82=0
if 'q20_0' not in globals():
    q20_0=0
if 'q21_0' not in globals():
    q21_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq21_0' : 1, 'q21_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq21_0') : 4, ('anc1','q21_0') : -4, ('anc2', 'q0_82') : -2, ('anc2', 'q20_0') : -2, ('anc2', 'outq21_0') : -2, ('anc2', 'q21_0') : 2, ('q0_82', 'q20_0') : 1, ('outq21_0', 'q21_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_82']==q0_82 and sample['q20_0']==q20_0 and sample['q21_0']==q21_0 and int(energy)==0:
        q0_82=sample['q0_82']
        q20_0=sample['q20_0']
        q21_0=sample['outq21_0']
        tgt_before = sample['q21_0']
        break

print('#' * 80)
print("CCNOT operation on q0_82 (control1), q20_0 (control2) and q21_0 (target):")
print("    in:  q0_82={0}, q20_0={1}, q21_0={2}".format(q0_82,q20_0,tgt_before))
print("    out: q0_82={0}, q20_0={1}, q21_0={2}".format(q0_82,q20_0,q21_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_82 control2: q20_0 target: q21_0 ##
################################################################################
if 'q1_82' not in globals():
    q1_82=0
if 'q20_0' not in globals():
    q20_0=0
if 'q21_0' not in globals():
    q21_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq21_0' : 1, 'q21_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq21_0') : 4, ('anc1','q21_0') : -4, ('anc2', 'q1_82') : -2, ('anc2', 'q20_0') : -2, ('anc2', 'outq21_0') : -2, ('anc2', 'q21_0') : 2, ('q1_82', 'q20_0') : 1, ('outq21_0', 'q21_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_82']==q1_82 and sample['q20_0']==q20_0 and sample['q21_0']==q21_0 and int(energy)==0:
        q1_82=sample['q1_82']
        q20_0=sample['q20_0']
        q21_0=sample['outq21_0']
        tgt_before = sample['q21_0']
        break

print('#' * 80)
print("CCNOT operation on q1_82 (control1), q20_0 (control2) and q21_0 (target):")
print("    in:  q1_82={0}, q20_0={1}, q21_0={2}".format(q1_82,q20_0,tgt_before))
print("    out: q1_82={0}, q20_0={1}, q21_0={2}".format(q1_82,q20_0,q21_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q21_0 target: q22_0 ##
################################################################################
if 'q21_0' not in globals():
    q21_0=0
if 'q22_0' not in globals():
    q22_0=0

bqm = dimod.BinaryQuadraticModel({'q21_0' : 1, 'q22_0' : 1, 'outq22_0' : 1, 'anc' : 4}, {('q21_0', 'q22_0') : 2, ('q21_0', 'outq22_0') : -2, ('q22_0', 'outq22_0') : -2, ('q21_0', 'anc') : -4, ('q22_0', 'anc') : -4, ('outq22_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q21_0']==q21_0 and sample['q22_0']==q22_0 and int(energy)==0:
        q21_0=sample['q21_0']
        q22_0=sample['outq22_0']
        tgt_before = sample['q22_0']
        break

print('#' * 80)
print("CNOT operation on q21_0 (control) and q22_0 (target):")
print("    in:  q21_0={0}, q22_0={1}".format(q21_0,tgt_before))
print("    out: q21_0={0}, q22_0={1}".format(q21_0,q22_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_81 control2: q21_0 target: q22_0 ##
################################################################################
if 'q0_81' not in globals():
    q0_81=0
if 'q21_0' not in globals():
    q21_0=0
if 'q22_0' not in globals():
    q22_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq22_0' : 1, 'q22_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq22_0') : 4, ('anc1','q22_0') : -4, ('anc2', 'q0_81') : -2, ('anc2', 'q21_0') : -2, ('anc2', 'outq22_0') : -2, ('anc2', 'q22_0') : 2, ('q0_81', 'q21_0') : 1, ('outq22_0', 'q22_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_81']==q0_81 and sample['q21_0']==q21_0 and sample['q22_0']==q22_0 and int(energy)==0:
        q0_81=sample['q0_81']
        q21_0=sample['q21_0']
        q22_0=sample['outq22_0']
        tgt_before = sample['q22_0']
        break

print('#' * 80)
print("CCNOT operation on q0_81 (control1), q21_0 (control2) and q22_0 (target):")
print("    in:  q0_81={0}, q21_0={1}, q22_0={2}".format(q0_81,q21_0,tgt_before))
print("    out: q0_81={0}, q21_0={1}, q22_0={2}".format(q0_81,q21_0,q22_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_81 control2: q21_0 target: q22_0 ##
################################################################################
if 'q1_81' not in globals():
    q1_81=0
if 'q21_0' not in globals():
    q21_0=0
if 'q22_0' not in globals():
    q22_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq22_0' : 1, 'q22_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq22_0') : 4, ('anc1','q22_0') : -4, ('anc2', 'q1_81') : -2, ('anc2', 'q21_0') : -2, ('anc2', 'outq22_0') : -2, ('anc2', 'q22_0') : 2, ('q1_81', 'q21_0') : 1, ('outq22_0', 'q22_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_81']==q1_81 and sample['q21_0']==q21_0 and sample['q22_0']==q22_0 and int(energy)==0:
        q1_81=sample['q1_81']
        q21_0=sample['q21_0']
        q22_0=sample['outq22_0']
        tgt_before = sample['q22_0']
        break

print('#' * 80)
print("CCNOT operation on q1_81 (control1), q21_0 (control2) and q22_0 (target):")
print("    in:  q1_81={0}, q21_0={1}, q22_0={2}".format(q1_81,q21_0,tgt_before))
print("    out: q1_81={0}, q21_0={1}, q22_0={2}".format(q1_81,q21_0,q22_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q22_0 target: q23_0 ##
################################################################################
if 'q22_0' not in globals():
    q22_0=0
if 'q23_0' not in globals():
    q23_0=0

bqm = dimod.BinaryQuadraticModel({'q22_0' : 1, 'q23_0' : 1, 'outq23_0' : 1, 'anc' : 4}, {('q22_0', 'q23_0') : 2, ('q22_0', 'outq23_0') : -2, ('q23_0', 'outq23_0') : -2, ('q22_0', 'anc') : -4, ('q23_0', 'anc') : -4, ('outq23_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q22_0']==q22_0 and sample['q23_0']==q23_0 and int(energy)==0:
        q22_0=sample['q22_0']
        q23_0=sample['outq23_0']
        tgt_before = sample['q23_0']
        break

print('#' * 80)
print("CNOT operation on q22_0 (control) and q23_0 (target):")
print("    in:  q22_0={0}, q23_0={1}".format(q22_0,tgt_before))
print("    out: q22_0={0}, q23_0={1}".format(q22_0,q23_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_80 control2: q22_0 target: q23_0 ##
################################################################################
if 'q0_80' not in globals():
    q0_80=0
if 'q22_0' not in globals():
    q22_0=0
if 'q23_0' not in globals():
    q23_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq23_0' : 1, 'q23_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq23_0') : 4, ('anc1','q23_0') : -4, ('anc2', 'q0_80') : -2, ('anc2', 'q22_0') : -2, ('anc2', 'outq23_0') : -2, ('anc2', 'q23_0') : 2, ('q0_80', 'q22_0') : 1, ('outq23_0', 'q23_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_80']==q0_80 and sample['q22_0']==q22_0 and sample['q23_0']==q23_0 and int(energy)==0:
        q0_80=sample['q0_80']
        q22_0=sample['q22_0']
        q23_0=sample['outq23_0']
        tgt_before = sample['q23_0']
        break

print('#' * 80)
print("CCNOT operation on q0_80 (control1), q22_0 (control2) and q23_0 (target):")
print("    in:  q0_80={0}, q22_0={1}, q23_0={2}".format(q0_80,q22_0,tgt_before))
print("    out: q0_80={0}, q22_0={1}, q23_0={2}".format(q0_80,q22_0,q23_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_80 control2: q22_0 target: q23_0 ##
################################################################################
if 'q1_80' not in globals():
    q1_80=0
if 'q22_0' not in globals():
    q22_0=0
if 'q23_0' not in globals():
    q23_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq23_0' : 1, 'q23_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq23_0') : 4, ('anc1','q23_0') : -4, ('anc2', 'q1_80') : -2, ('anc2', 'q22_0') : -2, ('anc2', 'outq23_0') : -2, ('anc2', 'q23_0') : 2, ('q1_80', 'q22_0') : 1, ('outq23_0', 'q23_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_80']==q1_80 and sample['q22_0']==q22_0 and sample['q23_0']==q23_0 and int(energy)==0:
        q1_80=sample['q1_80']
        q22_0=sample['q22_0']
        q23_0=sample['outq23_0']
        tgt_before = sample['q23_0']
        break

print('#' * 80)
print("CCNOT operation on q1_80 (control1), q22_0 (control2) and q23_0 (target):")
print("    in:  q1_80={0}, q22_0={1}, q23_0={2}".format(q1_80,q22_0,tgt_before))
print("    out: q1_80={0}, q22_0={1}, q23_0={2}".format(q1_80,q22_0,q23_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q23_0 target: q24_0 ##
################################################################################
if 'q23_0' not in globals():
    q23_0=0
if 'q24_0' not in globals():
    q24_0=0

bqm = dimod.BinaryQuadraticModel({'q23_0' : 1, 'q24_0' : 1, 'outq24_0' : 1, 'anc' : 4}, {('q23_0', 'q24_0') : 2, ('q23_0', 'outq24_0') : -2, ('q24_0', 'outq24_0') : -2, ('q23_0', 'anc') : -4, ('q24_0', 'anc') : -4, ('outq24_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q23_0']==q23_0 and sample['q24_0']==q24_0 and int(energy)==0:
        q23_0=sample['q23_0']
        q24_0=sample['outq24_0']
        tgt_before = sample['q24_0']
        break

print('#' * 80)
print("CNOT operation on q23_0 (control) and q24_0 (target):")
print("    in:  q23_0={0}, q24_0={1}".format(q23_0,tgt_before))
print("    out: q23_0={0}, q24_0={1}".format(q23_0,q24_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_79 control2: q23_0 target: q24_0 ##
################################################################################
if 'q0_79' not in globals():
    q0_79=0
if 'q23_0' not in globals():
    q23_0=0
if 'q24_0' not in globals():
    q24_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq24_0' : 1, 'q24_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq24_0') : 4, ('anc1','q24_0') : -4, ('anc2', 'q0_79') : -2, ('anc2', 'q23_0') : -2, ('anc2', 'outq24_0') : -2, ('anc2', 'q24_0') : 2, ('q0_79', 'q23_0') : 1, ('outq24_0', 'q24_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_79']==q0_79 and sample['q23_0']==q23_0 and sample['q24_0']==q24_0 and int(energy)==0:
        q0_79=sample['q0_79']
        q23_0=sample['q23_0']
        q24_0=sample['outq24_0']
        tgt_before = sample['q24_0']
        break

print('#' * 80)
print("CCNOT operation on q0_79 (control1), q23_0 (control2) and q24_0 (target):")
print("    in:  q0_79={0}, q23_0={1}, q24_0={2}".format(q0_79,q23_0,tgt_before))
print("    out: q0_79={0}, q23_0={1}, q24_0={2}".format(q0_79,q23_0,q24_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_79 control2: q23_0 target: q24_0 ##
################################################################################
if 'q1_79' not in globals():
    q1_79=0
if 'q23_0' not in globals():
    q23_0=0
if 'q24_0' not in globals():
    q24_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq24_0' : 1, 'q24_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq24_0') : 4, ('anc1','q24_0') : -4, ('anc2', 'q1_79') : -2, ('anc2', 'q23_0') : -2, ('anc2', 'outq24_0') : -2, ('anc2', 'q24_0') : 2, ('q1_79', 'q23_0') : 1, ('outq24_0', 'q24_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_79']==q1_79 and sample['q23_0']==q23_0 and sample['q24_0']==q24_0 and int(energy)==0:
        q1_79=sample['q1_79']
        q23_0=sample['q23_0']
        q24_0=sample['outq24_0']
        tgt_before = sample['q24_0']
        break

print('#' * 80)
print("CCNOT operation on q1_79 (control1), q23_0 (control2) and q24_0 (target):")
print("    in:  q1_79={0}, q23_0={1}, q24_0={2}".format(q1_79,q23_0,tgt_before))
print("    out: q1_79={0}, q23_0={1}, q24_0={2}".format(q1_79,q23_0,q24_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q24_0 target: q25_0 ##
################################################################################
if 'q24_0' not in globals():
    q24_0=0
if 'q25_0' not in globals():
    q25_0=0

bqm = dimod.BinaryQuadraticModel({'q24_0' : 1, 'q25_0' : 1, 'outq25_0' : 1, 'anc' : 4}, {('q24_0', 'q25_0') : 2, ('q24_0', 'outq25_0') : -2, ('q25_0', 'outq25_0') : -2, ('q24_0', 'anc') : -4, ('q25_0', 'anc') : -4, ('outq25_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q24_0']==q24_0 and sample['q25_0']==q25_0 and int(energy)==0:
        q24_0=sample['q24_0']
        q25_0=sample['outq25_0']
        tgt_before = sample['q25_0']
        break

print('#' * 80)
print("CNOT operation on q24_0 (control) and q25_0 (target):")
print("    in:  q24_0={0}, q25_0={1}".format(q24_0,tgt_before))
print("    out: q24_0={0}, q25_0={1}".format(q24_0,q25_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_78 control2: q24_0 target: q25_0 ##
################################################################################
if 'q0_78' not in globals():
    q0_78=0
if 'q24_0' not in globals():
    q24_0=0
if 'q25_0' not in globals():
    q25_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq25_0' : 1, 'q25_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq25_0') : 4, ('anc1','q25_0') : -4, ('anc2', 'q0_78') : -2, ('anc2', 'q24_0') : -2, ('anc2', 'outq25_0') : -2, ('anc2', 'q25_0') : 2, ('q0_78', 'q24_0') : 1, ('outq25_0', 'q25_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_78']==q0_78 and sample['q24_0']==q24_0 and sample['q25_0']==q25_0 and int(energy)==0:
        q0_78=sample['q0_78']
        q24_0=sample['q24_0']
        q25_0=sample['outq25_0']
        tgt_before = sample['q25_0']
        break

print('#' * 80)
print("CCNOT operation on q0_78 (control1), q24_0 (control2) and q25_0 (target):")
print("    in:  q0_78={0}, q24_0={1}, q25_0={2}".format(q0_78,q24_0,tgt_before))
print("    out: q0_78={0}, q24_0={1}, q25_0={2}".format(q0_78,q24_0,q25_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_78 control2: q24_0 target: q25_0 ##
################################################################################
if 'q1_78' not in globals():
    q1_78=0
if 'q24_0' not in globals():
    q24_0=0
if 'q25_0' not in globals():
    q25_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq25_0' : 1, 'q25_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq25_0') : 4, ('anc1','q25_0') : -4, ('anc2', 'q1_78') : -2, ('anc2', 'q24_0') : -2, ('anc2', 'outq25_0') : -2, ('anc2', 'q25_0') : 2, ('q1_78', 'q24_0') : 1, ('outq25_0', 'q25_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_78']==q1_78 and sample['q24_0']==q24_0 and sample['q25_0']==q25_0 and int(energy)==0:
        q1_78=sample['q1_78']
        q24_0=sample['q24_0']
        q25_0=sample['outq25_0']
        tgt_before = sample['q25_0']
        break

print('#' * 80)
print("CCNOT operation on q1_78 (control1), q24_0 (control2) and q25_0 (target):")
print("    in:  q1_78={0}, q24_0={1}, q25_0={2}".format(q1_78,q24_0,tgt_before))
print("    out: q1_78={0}, q24_0={1}, q25_0={2}".format(q1_78,q24_0,q25_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q25_0 target: q26_0 ##
################################################################################
if 'q25_0' not in globals():
    q25_0=0
if 'q26_0' not in globals():
    q26_0=0

bqm = dimod.BinaryQuadraticModel({'q25_0' : 1, 'q26_0' : 1, 'outq26_0' : 1, 'anc' : 4}, {('q25_0', 'q26_0') : 2, ('q25_0', 'outq26_0') : -2, ('q26_0', 'outq26_0') : -2, ('q25_0', 'anc') : -4, ('q26_0', 'anc') : -4, ('outq26_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q25_0']==q25_0 and sample['q26_0']==q26_0 and int(energy)==0:
        q25_0=sample['q25_0']
        q26_0=sample['outq26_0']
        tgt_before = sample['q26_0']
        break

print('#' * 80)
print("CNOT operation on q25_0 (control) and q26_0 (target):")
print("    in:  q25_0={0}, q26_0={1}".format(q25_0,tgt_before))
print("    out: q25_0={0}, q26_0={1}".format(q25_0,q26_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_77 control2: q25_0 target: q26_0 ##
################################################################################
if 'q0_77' not in globals():
    q0_77=0
if 'q25_0' not in globals():
    q25_0=0
if 'q26_0' not in globals():
    q26_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq26_0' : 1, 'q26_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq26_0') : 4, ('anc1','q26_0') : -4, ('anc2', 'q0_77') : -2, ('anc2', 'q25_0') : -2, ('anc2', 'outq26_0') : -2, ('anc2', 'q26_0') : 2, ('q0_77', 'q25_0') : 1, ('outq26_0', 'q26_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_77']==q0_77 and sample['q25_0']==q25_0 and sample['q26_0']==q26_0 and int(energy)==0:
        q0_77=sample['q0_77']
        q25_0=sample['q25_0']
        q26_0=sample['outq26_0']
        tgt_before = sample['q26_0']
        break

print('#' * 80)
print("CCNOT operation on q0_77 (control1), q25_0 (control2) and q26_0 (target):")
print("    in:  q0_77={0}, q25_0={1}, q26_0={2}".format(q0_77,q25_0,tgt_before))
print("    out: q0_77={0}, q25_0={1}, q26_0={2}".format(q0_77,q25_0,q26_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_77 control2: q25_0 target: q26_0 ##
################################################################################
if 'q1_77' not in globals():
    q1_77=0
if 'q25_0' not in globals():
    q25_0=0
if 'q26_0' not in globals():
    q26_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq26_0' : 1, 'q26_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq26_0') : 4, ('anc1','q26_0') : -4, ('anc2', 'q1_77') : -2, ('anc2', 'q25_0') : -2, ('anc2', 'outq26_0') : -2, ('anc2', 'q26_0') : 2, ('q1_77', 'q25_0') : 1, ('outq26_0', 'q26_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_77']==q1_77 and sample['q25_0']==q25_0 and sample['q26_0']==q26_0 and int(energy)==0:
        q1_77=sample['q1_77']
        q25_0=sample['q25_0']
        q26_0=sample['outq26_0']
        tgt_before = sample['q26_0']
        break

print('#' * 80)
print("CCNOT operation on q1_77 (control1), q25_0 (control2) and q26_0 (target):")
print("    in:  q1_77={0}, q25_0={1}, q26_0={2}".format(q1_77,q25_0,tgt_before))
print("    out: q1_77={0}, q25_0={1}, q26_0={2}".format(q1_77,q25_0,q26_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q26_0 target: q27_0 ##
################################################################################
if 'q26_0' not in globals():
    q26_0=0
if 'q27_0' not in globals():
    q27_0=0

bqm = dimod.BinaryQuadraticModel({'q26_0' : 1, 'q27_0' : 1, 'outq27_0' : 1, 'anc' : 4}, {('q26_0', 'q27_0') : 2, ('q26_0', 'outq27_0') : -2, ('q27_0', 'outq27_0') : -2, ('q26_0', 'anc') : -4, ('q27_0', 'anc') : -4, ('outq27_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q26_0']==q26_0 and sample['q27_0']==q27_0 and int(energy)==0:
        q26_0=sample['q26_0']
        q27_0=sample['outq27_0']
        tgt_before = sample['q27_0']
        break

print('#' * 80)
print("CNOT operation on q26_0 (control) and q27_0 (target):")
print("    in:  q26_0={0}, q27_0={1}".format(q26_0,tgt_before))
print("    out: q26_0={0}, q27_0={1}".format(q26_0,q27_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_76 control2: q26_0 target: q27_0 ##
################################################################################
if 'q0_76' not in globals():
    q0_76=0
if 'q26_0' not in globals():
    q26_0=0
if 'q27_0' not in globals():
    q27_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq27_0' : 1, 'q27_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq27_0') : 4, ('anc1','q27_0') : -4, ('anc2', 'q0_76') : -2, ('anc2', 'q26_0') : -2, ('anc2', 'outq27_0') : -2, ('anc2', 'q27_0') : 2, ('q0_76', 'q26_0') : 1, ('outq27_0', 'q27_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_76']==q0_76 and sample['q26_0']==q26_0 and sample['q27_0']==q27_0 and int(energy)==0:
        q0_76=sample['q0_76']
        q26_0=sample['q26_0']
        q27_0=sample['outq27_0']
        tgt_before = sample['q27_0']
        break

print('#' * 80)
print("CCNOT operation on q0_76 (control1), q26_0 (control2) and q27_0 (target):")
print("    in:  q0_76={0}, q26_0={1}, q27_0={2}".format(q0_76,q26_0,tgt_before))
print("    out: q0_76={0}, q26_0={1}, q27_0={2}".format(q0_76,q26_0,q27_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_76 control2: q26_0 target: q27_0 ##
################################################################################
if 'q1_76' not in globals():
    q1_76=0
if 'q26_0' not in globals():
    q26_0=0
if 'q27_0' not in globals():
    q27_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq27_0' : 1, 'q27_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq27_0') : 4, ('anc1','q27_0') : -4, ('anc2', 'q1_76') : -2, ('anc2', 'q26_0') : -2, ('anc2', 'outq27_0') : -2, ('anc2', 'q27_0') : 2, ('q1_76', 'q26_0') : 1, ('outq27_0', 'q27_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_76']==q1_76 and sample['q26_0']==q26_0 and sample['q27_0']==q27_0 and int(energy)==0:
        q1_76=sample['q1_76']
        q26_0=sample['q26_0']
        q27_0=sample['outq27_0']
        tgt_before = sample['q27_0']
        break

print('#' * 80)
print("CCNOT operation on q1_76 (control1), q26_0 (control2) and q27_0 (target):")
print("    in:  q1_76={0}, q26_0={1}, q27_0={2}".format(q1_76,q26_0,tgt_before))
print("    out: q1_76={0}, q26_0={1}, q27_0={2}".format(q1_76,q26_0,q27_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q27_0 target: q28_0 ##
################################################################################
if 'q27_0' not in globals():
    q27_0=0
if 'q28_0' not in globals():
    q28_0=0

bqm = dimod.BinaryQuadraticModel({'q27_0' : 1, 'q28_0' : 1, 'outq28_0' : 1, 'anc' : 4}, {('q27_0', 'q28_0') : 2, ('q27_0', 'outq28_0') : -2, ('q28_0', 'outq28_0') : -2, ('q27_0', 'anc') : -4, ('q28_0', 'anc') : -4, ('outq28_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q27_0']==q27_0 and sample['q28_0']==q28_0 and int(energy)==0:
        q27_0=sample['q27_0']
        q28_0=sample['outq28_0']
        tgt_before = sample['q28_0']
        break

print('#' * 80)
print("CNOT operation on q27_0 (control) and q28_0 (target):")
print("    in:  q27_0={0}, q28_0={1}".format(q27_0,tgt_before))
print("    out: q27_0={0}, q28_0={1}".format(q27_0,q28_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_75 control2: q27_0 target: q28_0 ##
################################################################################
if 'q0_75' not in globals():
    q0_75=0
if 'q27_0' not in globals():
    q27_0=0
if 'q28_0' not in globals():
    q28_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq28_0' : 1, 'q28_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq28_0') : 4, ('anc1','q28_0') : -4, ('anc2', 'q0_75') : -2, ('anc2', 'q27_0') : -2, ('anc2', 'outq28_0') : -2, ('anc2', 'q28_0') : 2, ('q0_75', 'q27_0') : 1, ('outq28_0', 'q28_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_75']==q0_75 and sample['q27_0']==q27_0 and sample['q28_0']==q28_0 and int(energy)==0:
        q0_75=sample['q0_75']
        q27_0=sample['q27_0']
        q28_0=sample['outq28_0']
        tgt_before = sample['q28_0']
        break

print('#' * 80)
print("CCNOT operation on q0_75 (control1), q27_0 (control2) and q28_0 (target):")
print("    in:  q0_75={0}, q27_0={1}, q28_0={2}".format(q0_75,q27_0,tgt_before))
print("    out: q0_75={0}, q27_0={1}, q28_0={2}".format(q0_75,q27_0,q28_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_75 control2: q27_0 target: q28_0 ##
################################################################################
if 'q1_75' not in globals():
    q1_75=0
if 'q27_0' not in globals():
    q27_0=0
if 'q28_0' not in globals():
    q28_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq28_0' : 1, 'q28_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq28_0') : 4, ('anc1','q28_0') : -4, ('anc2', 'q1_75') : -2, ('anc2', 'q27_0') : -2, ('anc2', 'outq28_0') : -2, ('anc2', 'q28_0') : 2, ('q1_75', 'q27_0') : 1, ('outq28_0', 'q28_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_75']==q1_75 and sample['q27_0']==q27_0 and sample['q28_0']==q28_0 and int(energy)==0:
        q1_75=sample['q1_75']
        q27_0=sample['q27_0']
        q28_0=sample['outq28_0']
        tgt_before = sample['q28_0']
        break

print('#' * 80)
print("CCNOT operation on q1_75 (control1), q27_0 (control2) and q28_0 (target):")
print("    in:  q1_75={0}, q27_0={1}, q28_0={2}".format(q1_75,q27_0,tgt_before))
print("    out: q1_75={0}, q27_0={1}, q28_0={2}".format(q1_75,q27_0,q28_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q28_0 target: q29_0 ##
################################################################################
if 'q28_0' not in globals():
    q28_0=0
if 'q29_0' not in globals():
    q29_0=0

bqm = dimod.BinaryQuadraticModel({'q28_0' : 1, 'q29_0' : 1, 'outq29_0' : 1, 'anc' : 4}, {('q28_0', 'q29_0') : 2, ('q28_0', 'outq29_0') : -2, ('q29_0', 'outq29_0') : -2, ('q28_0', 'anc') : -4, ('q29_0', 'anc') : -4, ('outq29_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q28_0']==q28_0 and sample['q29_0']==q29_0 and int(energy)==0:
        q28_0=sample['q28_0']
        q29_0=sample['outq29_0']
        tgt_before = sample['q29_0']
        break

print('#' * 80)
print("CNOT operation on q28_0 (control) and q29_0 (target):")
print("    in:  q28_0={0}, q29_0={1}".format(q28_0,tgt_before))
print("    out: q28_0={0}, q29_0={1}".format(q28_0,q29_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_74 control2: q28_0 target: q29_0 ##
################################################################################
if 'q0_74' not in globals():
    q0_74=0
if 'q28_0' not in globals():
    q28_0=0
if 'q29_0' not in globals():
    q29_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq29_0' : 1, 'q29_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq29_0') : 4, ('anc1','q29_0') : -4, ('anc2', 'q0_74') : -2, ('anc2', 'q28_0') : -2, ('anc2', 'outq29_0') : -2, ('anc2', 'q29_0') : 2, ('q0_74', 'q28_0') : 1, ('outq29_0', 'q29_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_74']==q0_74 and sample['q28_0']==q28_0 and sample['q29_0']==q29_0 and int(energy)==0:
        q0_74=sample['q0_74']
        q28_0=sample['q28_0']
        q29_0=sample['outq29_0']
        tgt_before = sample['q29_0']
        break

print('#' * 80)
print("CCNOT operation on q0_74 (control1), q28_0 (control2) and q29_0 (target):")
print("    in:  q0_74={0}, q28_0={1}, q29_0={2}".format(q0_74,q28_0,tgt_before))
print("    out: q0_74={0}, q28_0={1}, q29_0={2}".format(q0_74,q28_0,q29_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_74 control2: q28_0 target: q29_0 ##
################################################################################
if 'q1_74' not in globals():
    q1_74=0
if 'q28_0' not in globals():
    q28_0=0
if 'q29_0' not in globals():
    q29_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq29_0' : 1, 'q29_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq29_0') : 4, ('anc1','q29_0') : -4, ('anc2', 'q1_74') : -2, ('anc2', 'q28_0') : -2, ('anc2', 'outq29_0') : -2, ('anc2', 'q29_0') : 2, ('q1_74', 'q28_0') : 1, ('outq29_0', 'q29_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_74']==q1_74 and sample['q28_0']==q28_0 and sample['q29_0']==q29_0 and int(energy)==0:
        q1_74=sample['q1_74']
        q28_0=sample['q28_0']
        q29_0=sample['outq29_0']
        tgt_before = sample['q29_0']
        break

print('#' * 80)
print("CCNOT operation on q1_74 (control1), q28_0 (control2) and q29_0 (target):")
print("    in:  q1_74={0}, q28_0={1}, q29_0={2}".format(q1_74,q28_0,tgt_before))
print("    out: q1_74={0}, q28_0={1}, q29_0={2}".format(q1_74,q28_0,q29_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q29_0 target: q30_0 ##
################################################################################
if 'q29_0' not in globals():
    q29_0=0
if 'q30_0' not in globals():
    q30_0=0

bqm = dimod.BinaryQuadraticModel({'q29_0' : 1, 'q30_0' : 1, 'outq30_0' : 1, 'anc' : 4}, {('q29_0', 'q30_0') : 2, ('q29_0', 'outq30_0') : -2, ('q30_0', 'outq30_0') : -2, ('q29_0', 'anc') : -4, ('q30_0', 'anc') : -4, ('outq30_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q29_0']==q29_0 and sample['q30_0']==q30_0 and int(energy)==0:
        q29_0=sample['q29_0']
        q30_0=sample['outq30_0']
        tgt_before = sample['q30_0']
        break

print('#' * 80)
print("CNOT operation on q29_0 (control) and q30_0 (target):")
print("    in:  q29_0={0}, q30_0={1}".format(q29_0,tgt_before))
print("    out: q29_0={0}, q30_0={1}".format(q29_0,q30_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_73 control2: q29_0 target: q30_0 ##
################################################################################
if 'q0_73' not in globals():
    q0_73=0
if 'q29_0' not in globals():
    q29_0=0
if 'q30_0' not in globals():
    q30_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq30_0' : 1, 'q30_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq30_0') : 4, ('anc1','q30_0') : -4, ('anc2', 'q0_73') : -2, ('anc2', 'q29_0') : -2, ('anc2', 'outq30_0') : -2, ('anc2', 'q30_0') : 2, ('q0_73', 'q29_0') : 1, ('outq30_0', 'q30_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_73']==q0_73 and sample['q29_0']==q29_0 and sample['q30_0']==q30_0 and int(energy)==0:
        q0_73=sample['q0_73']
        q29_0=sample['q29_0']
        q30_0=sample['outq30_0']
        tgt_before = sample['q30_0']
        break

print('#' * 80)
print("CCNOT operation on q0_73 (control1), q29_0 (control2) and q30_0 (target):")
print("    in:  q0_73={0}, q29_0={1}, q30_0={2}".format(q0_73,q29_0,tgt_before))
print("    out: q0_73={0}, q29_0={1}, q30_0={2}".format(q0_73,q29_0,q30_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_73 control2: q29_0 target: q30_0 ##
################################################################################
if 'q1_73' not in globals():
    q1_73=0
if 'q29_0' not in globals():
    q29_0=0
if 'q30_0' not in globals():
    q30_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq30_0' : 1, 'q30_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq30_0') : 4, ('anc1','q30_0') : -4, ('anc2', 'q1_73') : -2, ('anc2', 'q29_0') : -2, ('anc2', 'outq30_0') : -2, ('anc2', 'q30_0') : 2, ('q1_73', 'q29_0') : 1, ('outq30_0', 'q30_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_73']==q1_73 and sample['q29_0']==q29_0 and sample['q30_0']==q30_0 and int(energy)==0:
        q1_73=sample['q1_73']
        q29_0=sample['q29_0']
        q30_0=sample['outq30_0']
        tgt_before = sample['q30_0']
        break

print('#' * 80)
print("CCNOT operation on q1_73 (control1), q29_0 (control2) and q30_0 (target):")
print("    in:  q1_73={0}, q29_0={1}, q30_0={2}".format(q1_73,q29_0,tgt_before))
print("    out: q1_73={0}, q29_0={1}, q30_0={2}".format(q1_73,q29_0,q30_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q30_0 target: q31_0 ##
################################################################################
if 'q30_0' not in globals():
    q30_0=0
if 'q31_0' not in globals():
    q31_0=0

bqm = dimod.BinaryQuadraticModel({'q30_0' : 1, 'q31_0' : 1, 'outq31_0' : 1, 'anc' : 4}, {('q30_0', 'q31_0') : 2, ('q30_0', 'outq31_0') : -2, ('q31_0', 'outq31_0') : -2, ('q30_0', 'anc') : -4, ('q31_0', 'anc') : -4, ('outq31_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q30_0']==q30_0 and sample['q31_0']==q31_0 and int(energy)==0:
        q30_0=sample['q30_0']
        q31_0=sample['outq31_0']
        tgt_before = sample['q31_0']
        break

print('#' * 80)
print("CNOT operation on q30_0 (control) and q31_0 (target):")
print("    in:  q30_0={0}, q31_0={1}".format(q30_0,tgt_before))
print("    out: q30_0={0}, q31_0={1}".format(q30_0,q31_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_72 control2: q30_0 target: q31_0 ##
################################################################################
if 'q0_72' not in globals():
    q0_72=0
if 'q30_0' not in globals():
    q30_0=0
if 'q31_0' not in globals():
    q31_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq31_0' : 1, 'q31_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq31_0') : 4, ('anc1','q31_0') : -4, ('anc2', 'q0_72') : -2, ('anc2', 'q30_0') : -2, ('anc2', 'outq31_0') : -2, ('anc2', 'q31_0') : 2, ('q0_72', 'q30_0') : 1, ('outq31_0', 'q31_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_72']==q0_72 and sample['q30_0']==q30_0 and sample['q31_0']==q31_0 and int(energy)==0:
        q0_72=sample['q0_72']
        q30_0=sample['q30_0']
        q31_0=sample['outq31_0']
        tgt_before = sample['q31_0']
        break

print('#' * 80)
print("CCNOT operation on q0_72 (control1), q30_0 (control2) and q31_0 (target):")
print("    in:  q0_72={0}, q30_0={1}, q31_0={2}".format(q0_72,q30_0,tgt_before))
print("    out: q0_72={0}, q30_0={1}, q31_0={2}".format(q0_72,q30_0,q31_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_72 control2: q30_0 target: q31_0 ##
################################################################################
if 'q1_72' not in globals():
    q1_72=0
if 'q30_0' not in globals():
    q30_0=0
if 'q31_0' not in globals():
    q31_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq31_0' : 1, 'q31_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq31_0') : 4, ('anc1','q31_0') : -4, ('anc2', 'q1_72') : -2, ('anc2', 'q30_0') : -2, ('anc2', 'outq31_0') : -2, ('anc2', 'q31_0') : 2, ('q1_72', 'q30_0') : 1, ('outq31_0', 'q31_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_72']==q1_72 and sample['q30_0']==q30_0 and sample['q31_0']==q31_0 and int(energy)==0:
        q1_72=sample['q1_72']
        q30_0=sample['q30_0']
        q31_0=sample['outq31_0']
        tgt_before = sample['q31_0']
        break

print('#' * 80)
print("CCNOT operation on q1_72 (control1), q30_0 (control2) and q31_0 (target):")
print("    in:  q1_72={0}, q30_0={1}, q31_0={2}".format(q1_72,q30_0,tgt_before))
print("    out: q1_72={0}, q30_0={1}, q31_0={2}".format(q1_72,q30_0,q31_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q31_0 target: q32_0 ##
################################################################################
if 'q31_0' not in globals():
    q31_0=0
if 'q32_0' not in globals():
    q32_0=0

bqm = dimod.BinaryQuadraticModel({'q31_0' : 1, 'q32_0' : 1, 'outq32_0' : 1, 'anc' : 4}, {('q31_0', 'q32_0') : 2, ('q31_0', 'outq32_0') : -2, ('q32_0', 'outq32_0') : -2, ('q31_0', 'anc') : -4, ('q32_0', 'anc') : -4, ('outq32_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q31_0']==q31_0 and sample['q32_0']==q32_0 and int(energy)==0:
        q31_0=sample['q31_0']
        q32_0=sample['outq32_0']
        tgt_before = sample['q32_0']
        break

print('#' * 80)
print("CNOT operation on q31_0 (control) and q32_0 (target):")
print("    in:  q31_0={0}, q32_0={1}".format(q31_0,tgt_before))
print("    out: q31_0={0}, q32_0={1}".format(q31_0,q32_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_71 control2: q31_0 target: q32_0 ##
################################################################################
if 'q0_71' not in globals():
    q0_71=0
if 'q31_0' not in globals():
    q31_0=0
if 'q32_0' not in globals():
    q32_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq32_0' : 1, 'q32_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq32_0') : 4, ('anc1','q32_0') : -4, ('anc2', 'q0_71') : -2, ('anc2', 'q31_0') : -2, ('anc2', 'outq32_0') : -2, ('anc2', 'q32_0') : 2, ('q0_71', 'q31_0') : 1, ('outq32_0', 'q32_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_71']==q0_71 and sample['q31_0']==q31_0 and sample['q32_0']==q32_0 and int(energy)==0:
        q0_71=sample['q0_71']
        q31_0=sample['q31_0']
        q32_0=sample['outq32_0']
        tgt_before = sample['q32_0']
        break

print('#' * 80)
print("CCNOT operation on q0_71 (control1), q31_0 (control2) and q32_0 (target):")
print("    in:  q0_71={0}, q31_0={1}, q32_0={2}".format(q0_71,q31_0,tgt_before))
print("    out: q0_71={0}, q31_0={1}, q32_0={2}".format(q0_71,q31_0,q32_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_71 control2: q31_0 target: q32_0 ##
################################################################################
if 'q1_71' not in globals():
    q1_71=0
if 'q31_0' not in globals():
    q31_0=0
if 'q32_0' not in globals():
    q32_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq32_0' : 1, 'q32_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq32_0') : 4, ('anc1','q32_0') : -4, ('anc2', 'q1_71') : -2, ('anc2', 'q31_0') : -2, ('anc2', 'outq32_0') : -2, ('anc2', 'q32_0') : 2, ('q1_71', 'q31_0') : 1, ('outq32_0', 'q32_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_71']==q1_71 and sample['q31_0']==q31_0 and sample['q32_0']==q32_0 and int(energy)==0:
        q1_71=sample['q1_71']
        q31_0=sample['q31_0']
        q32_0=sample['outq32_0']
        tgt_before = sample['q32_0']
        break

print('#' * 80)
print("CCNOT operation on q1_71 (control1), q31_0 (control2) and q32_0 (target):")
print("    in:  q1_71={0}, q31_0={1}, q32_0={2}".format(q1_71,q31_0,tgt_before))
print("    out: q1_71={0}, q31_0={1}, q32_0={2}".format(q1_71,q31_0,q32_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q32_0 target: q33_0 ##
################################################################################
if 'q32_0' not in globals():
    q32_0=0
if 'q33_0' not in globals():
    q33_0=0

bqm = dimod.BinaryQuadraticModel({'q32_0' : 1, 'q33_0' : 1, 'outq33_0' : 1, 'anc' : 4}, {('q32_0', 'q33_0') : 2, ('q32_0', 'outq33_0') : -2, ('q33_0', 'outq33_0') : -2, ('q32_0', 'anc') : -4, ('q33_0', 'anc') : -4, ('outq33_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q32_0']==q32_0 and sample['q33_0']==q33_0 and int(energy)==0:
        q32_0=sample['q32_0']
        q33_0=sample['outq33_0']
        tgt_before = sample['q33_0']
        break

print('#' * 80)
print("CNOT operation on q32_0 (control) and q33_0 (target):")
print("    in:  q32_0={0}, q33_0={1}".format(q32_0,tgt_before))
print("    out: q32_0={0}, q33_0={1}".format(q32_0,q33_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_70 control2: q32_0 target: q33_0 ##
################################################################################
if 'q0_70' not in globals():
    q0_70=0
if 'q32_0' not in globals():
    q32_0=0
if 'q33_0' not in globals():
    q33_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq33_0' : 1, 'q33_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq33_0') : 4, ('anc1','q33_0') : -4, ('anc2', 'q0_70') : -2, ('anc2', 'q32_0') : -2, ('anc2', 'outq33_0') : -2, ('anc2', 'q33_0') : 2, ('q0_70', 'q32_0') : 1, ('outq33_0', 'q33_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_70']==q0_70 and sample['q32_0']==q32_0 and sample['q33_0']==q33_0 and int(energy)==0:
        q0_70=sample['q0_70']
        q32_0=sample['q32_0']
        q33_0=sample['outq33_0']
        tgt_before = sample['q33_0']
        break

print('#' * 80)
print("CCNOT operation on q0_70 (control1), q32_0 (control2) and q33_0 (target):")
print("    in:  q0_70={0}, q32_0={1}, q33_0={2}".format(q0_70,q32_0,tgt_before))
print("    out: q0_70={0}, q32_0={1}, q33_0={2}".format(q0_70,q32_0,q33_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_70 control2: q32_0 target: q33_0 ##
################################################################################
if 'q1_70' not in globals():
    q1_70=0
if 'q32_0' not in globals():
    q32_0=0
if 'q33_0' not in globals():
    q33_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq33_0' : 1, 'q33_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq33_0') : 4, ('anc1','q33_0') : -4, ('anc2', 'q1_70') : -2, ('anc2', 'q32_0') : -2, ('anc2', 'outq33_0') : -2, ('anc2', 'q33_0') : 2, ('q1_70', 'q32_0') : 1, ('outq33_0', 'q33_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_70']==q1_70 and sample['q32_0']==q32_0 and sample['q33_0']==q33_0 and int(energy)==0:
        q1_70=sample['q1_70']
        q32_0=sample['q32_0']
        q33_0=sample['outq33_0']
        tgt_before = sample['q33_0']
        break

print('#' * 80)
print("CCNOT operation on q1_70 (control1), q32_0 (control2) and q33_0 (target):")
print("    in:  q1_70={0}, q32_0={1}, q33_0={2}".format(q1_70,q32_0,tgt_before))
print("    out: q1_70={0}, q32_0={1}, q33_0={2}".format(q1_70,q32_0,q33_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q33_0 target: q34_0 ##
################################################################################
if 'q33_0' not in globals():
    q33_0=0
if 'q34_0' not in globals():
    q34_0=0

bqm = dimod.BinaryQuadraticModel({'q33_0' : 1, 'q34_0' : 1, 'outq34_0' : 1, 'anc' : 4}, {('q33_0', 'q34_0') : 2, ('q33_0', 'outq34_0') : -2, ('q34_0', 'outq34_0') : -2, ('q33_0', 'anc') : -4, ('q34_0', 'anc') : -4, ('outq34_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q33_0']==q33_0 and sample['q34_0']==q34_0 and int(energy)==0:
        q33_0=sample['q33_0']
        q34_0=sample['outq34_0']
        tgt_before = sample['q34_0']
        break

print('#' * 80)
print("CNOT operation on q33_0 (control) and q34_0 (target):")
print("    in:  q33_0={0}, q34_0={1}".format(q33_0,tgt_before))
print("    out: q33_0={0}, q34_0={1}".format(q33_0,q34_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_69 control2: q33_0 target: q34_0 ##
################################################################################
if 'q0_69' not in globals():
    q0_69=0
if 'q33_0' not in globals():
    q33_0=0
if 'q34_0' not in globals():
    q34_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq34_0' : 1, 'q34_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq34_0') : 4, ('anc1','q34_0') : -4, ('anc2', 'q0_69') : -2, ('anc2', 'q33_0') : -2, ('anc2', 'outq34_0') : -2, ('anc2', 'q34_0') : 2, ('q0_69', 'q33_0') : 1, ('outq34_0', 'q34_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_69']==q0_69 and sample['q33_0']==q33_0 and sample['q34_0']==q34_0 and int(energy)==0:
        q0_69=sample['q0_69']
        q33_0=sample['q33_0']
        q34_0=sample['outq34_0']
        tgt_before = sample['q34_0']
        break

print('#' * 80)
print("CCNOT operation on q0_69 (control1), q33_0 (control2) and q34_0 (target):")
print("    in:  q0_69={0}, q33_0={1}, q34_0={2}".format(q0_69,q33_0,tgt_before))
print("    out: q0_69={0}, q33_0={1}, q34_0={2}".format(q0_69,q33_0,q34_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_69 control2: q33_0 target: q34_0 ##
################################################################################
if 'q1_69' not in globals():
    q1_69=0
if 'q33_0' not in globals():
    q33_0=0
if 'q34_0' not in globals():
    q34_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq34_0' : 1, 'q34_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq34_0') : 4, ('anc1','q34_0') : -4, ('anc2', 'q1_69') : -2, ('anc2', 'q33_0') : -2, ('anc2', 'outq34_0') : -2, ('anc2', 'q34_0') : 2, ('q1_69', 'q33_0') : 1, ('outq34_0', 'q34_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_69']==q1_69 and sample['q33_0']==q33_0 and sample['q34_0']==q34_0 and int(energy)==0:
        q1_69=sample['q1_69']
        q33_0=sample['q33_0']
        q34_0=sample['outq34_0']
        tgt_before = sample['q34_0']
        break

print('#' * 80)
print("CCNOT operation on q1_69 (control1), q33_0 (control2) and q34_0 (target):")
print("    in:  q1_69={0}, q33_0={1}, q34_0={2}".format(q1_69,q33_0,tgt_before))
print("    out: q1_69={0}, q33_0={1}, q34_0={2}".format(q1_69,q33_0,q34_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q34_0 target: q35_0 ##
################################################################################
if 'q34_0' not in globals():
    q34_0=0
if 'q35_0' not in globals():
    q35_0=0

bqm = dimod.BinaryQuadraticModel({'q34_0' : 1, 'q35_0' : 1, 'outq35_0' : 1, 'anc' : 4}, {('q34_0', 'q35_0') : 2, ('q34_0', 'outq35_0') : -2, ('q35_0', 'outq35_0') : -2, ('q34_0', 'anc') : -4, ('q35_0', 'anc') : -4, ('outq35_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q34_0']==q34_0 and sample['q35_0']==q35_0 and int(energy)==0:
        q34_0=sample['q34_0']
        q35_0=sample['outq35_0']
        tgt_before = sample['q35_0']
        break

print('#' * 80)
print("CNOT operation on q34_0 (control) and q35_0 (target):")
print("    in:  q34_0={0}, q35_0={1}".format(q34_0,tgt_before))
print("    out: q34_0={0}, q35_0={1}".format(q34_0,q35_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_68 control2: q34_0 target: q35_0 ##
################################################################################
if 'q0_68' not in globals():
    q0_68=0
if 'q34_0' not in globals():
    q34_0=0
if 'q35_0' not in globals():
    q35_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq35_0' : 1, 'q35_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq35_0') : 4, ('anc1','q35_0') : -4, ('anc2', 'q0_68') : -2, ('anc2', 'q34_0') : -2, ('anc2', 'outq35_0') : -2, ('anc2', 'q35_0') : 2, ('q0_68', 'q34_0') : 1, ('outq35_0', 'q35_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_68']==q0_68 and sample['q34_0']==q34_0 and sample['q35_0']==q35_0 and int(energy)==0:
        q0_68=sample['q0_68']
        q34_0=sample['q34_0']
        q35_0=sample['outq35_0']
        tgt_before = sample['q35_0']
        break

print('#' * 80)
print("CCNOT operation on q0_68 (control1), q34_0 (control2) and q35_0 (target):")
print("    in:  q0_68={0}, q34_0={1}, q35_0={2}".format(q0_68,q34_0,tgt_before))
print("    out: q0_68={0}, q34_0={1}, q35_0={2}".format(q0_68,q34_0,q35_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_68 control2: q34_0 target: q35_0 ##
################################################################################
if 'q1_68' not in globals():
    q1_68=0
if 'q34_0' not in globals():
    q34_0=0
if 'q35_0' not in globals():
    q35_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq35_0' : 1, 'q35_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq35_0') : 4, ('anc1','q35_0') : -4, ('anc2', 'q1_68') : -2, ('anc2', 'q34_0') : -2, ('anc2', 'outq35_0') : -2, ('anc2', 'q35_0') : 2, ('q1_68', 'q34_0') : 1, ('outq35_0', 'q35_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_68']==q1_68 and sample['q34_0']==q34_0 and sample['q35_0']==q35_0 and int(energy)==0:
        q1_68=sample['q1_68']
        q34_0=sample['q34_0']
        q35_0=sample['outq35_0']
        tgt_before = sample['q35_0']
        break

print('#' * 80)
print("CCNOT operation on q1_68 (control1), q34_0 (control2) and q35_0 (target):")
print("    in:  q1_68={0}, q34_0={1}, q35_0={2}".format(q1_68,q34_0,tgt_before))
print("    out: q1_68={0}, q34_0={1}, q35_0={2}".format(q1_68,q34_0,q35_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q35_0 target: q36_0 ##
################################################################################
if 'q35_0' not in globals():
    q35_0=0
if 'q36_0' not in globals():
    q36_0=0

bqm = dimod.BinaryQuadraticModel({'q35_0' : 1, 'q36_0' : 1, 'outq36_0' : 1, 'anc' : 4}, {('q35_0', 'q36_0') : 2, ('q35_0', 'outq36_0') : -2, ('q36_0', 'outq36_0') : -2, ('q35_0', 'anc') : -4, ('q36_0', 'anc') : -4, ('outq36_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q35_0']==q35_0 and sample['q36_0']==q36_0 and int(energy)==0:
        q35_0=sample['q35_0']
        q36_0=sample['outq36_0']
        tgt_before = sample['q36_0']
        break

print('#' * 80)
print("CNOT operation on q35_0 (control) and q36_0 (target):")
print("    in:  q35_0={0}, q36_0={1}".format(q35_0,tgt_before))
print("    out: q35_0={0}, q36_0={1}".format(q35_0,q36_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_67 control2: q35_0 target: q36_0 ##
################################################################################
if 'q0_67' not in globals():
    q0_67=0
if 'q35_0' not in globals():
    q35_0=0
if 'q36_0' not in globals():
    q36_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq36_0' : 1, 'q36_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq36_0') : 4, ('anc1','q36_0') : -4, ('anc2', 'q0_67') : -2, ('anc2', 'q35_0') : -2, ('anc2', 'outq36_0') : -2, ('anc2', 'q36_0') : 2, ('q0_67', 'q35_0') : 1, ('outq36_0', 'q36_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_67']==q0_67 and sample['q35_0']==q35_0 and sample['q36_0']==q36_0 and int(energy)==0:
        q0_67=sample['q0_67']
        q35_0=sample['q35_0']
        q36_0=sample['outq36_0']
        tgt_before = sample['q36_0']
        break

print('#' * 80)
print("CCNOT operation on q0_67 (control1), q35_0 (control2) and q36_0 (target):")
print("    in:  q0_67={0}, q35_0={1}, q36_0={2}".format(q0_67,q35_0,tgt_before))
print("    out: q0_67={0}, q35_0={1}, q36_0={2}".format(q0_67,q35_0,q36_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_67 control2: q35_0 target: q36_0 ##
################################################################################
if 'q1_67' not in globals():
    q1_67=0
if 'q35_0' not in globals():
    q35_0=0
if 'q36_0' not in globals():
    q36_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq36_0' : 1, 'q36_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq36_0') : 4, ('anc1','q36_0') : -4, ('anc2', 'q1_67') : -2, ('anc2', 'q35_0') : -2, ('anc2', 'outq36_0') : -2, ('anc2', 'q36_0') : 2, ('q1_67', 'q35_0') : 1, ('outq36_0', 'q36_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_67']==q1_67 and sample['q35_0']==q35_0 and sample['q36_0']==q36_0 and int(energy)==0:
        q1_67=sample['q1_67']
        q35_0=sample['q35_0']
        q36_0=sample['outq36_0']
        tgt_before = sample['q36_0']
        break

print('#' * 80)
print("CCNOT operation on q1_67 (control1), q35_0 (control2) and q36_0 (target):")
print("    in:  q1_67={0}, q35_0={1}, q36_0={2}".format(q1_67,q35_0,tgt_before))
print("    out: q1_67={0}, q35_0={1}, q36_0={2}".format(q1_67,q35_0,q36_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q36_0 target: q37_0 ##
################################################################################
if 'q36_0' not in globals():
    q36_0=0
if 'q37_0' not in globals():
    q37_0=0

bqm = dimod.BinaryQuadraticModel({'q36_0' : 1, 'q37_0' : 1, 'outq37_0' : 1, 'anc' : 4}, {('q36_0', 'q37_0') : 2, ('q36_0', 'outq37_0') : -2, ('q37_0', 'outq37_0') : -2, ('q36_0', 'anc') : -4, ('q37_0', 'anc') : -4, ('outq37_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q36_0']==q36_0 and sample['q37_0']==q37_0 and int(energy)==0:
        q36_0=sample['q36_0']
        q37_0=sample['outq37_0']
        tgt_before = sample['q37_0']
        break

print('#' * 80)
print("CNOT operation on q36_0 (control) and q37_0 (target):")
print("    in:  q36_0={0}, q37_0={1}".format(q36_0,tgt_before))
print("    out: q36_0={0}, q37_0={1}".format(q36_0,q37_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_66 control2: q36_0 target: q37_0 ##
################################################################################
if 'q0_66' not in globals():
    q0_66=0
if 'q36_0' not in globals():
    q36_0=0
if 'q37_0' not in globals():
    q37_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq37_0' : 1, 'q37_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq37_0') : 4, ('anc1','q37_0') : -4, ('anc2', 'q0_66') : -2, ('anc2', 'q36_0') : -2, ('anc2', 'outq37_0') : -2, ('anc2', 'q37_0') : 2, ('q0_66', 'q36_0') : 1, ('outq37_0', 'q37_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_66']==q0_66 and sample['q36_0']==q36_0 and sample['q37_0']==q37_0 and int(energy)==0:
        q0_66=sample['q0_66']
        q36_0=sample['q36_0']
        q37_0=sample['outq37_0']
        tgt_before = sample['q37_0']
        break

print('#' * 80)
print("CCNOT operation on q0_66 (control1), q36_0 (control2) and q37_0 (target):")
print("    in:  q0_66={0}, q36_0={1}, q37_0={2}".format(q0_66,q36_0,tgt_before))
print("    out: q0_66={0}, q36_0={1}, q37_0={2}".format(q0_66,q36_0,q37_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_66 control2: q36_0 target: q37_0 ##
################################################################################
if 'q1_66' not in globals():
    q1_66=0
if 'q36_0' not in globals():
    q36_0=0
if 'q37_0' not in globals():
    q37_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq37_0' : 1, 'q37_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq37_0') : 4, ('anc1','q37_0') : -4, ('anc2', 'q1_66') : -2, ('anc2', 'q36_0') : -2, ('anc2', 'outq37_0') : -2, ('anc2', 'q37_0') : 2, ('q1_66', 'q36_0') : 1, ('outq37_0', 'q37_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_66']==q1_66 and sample['q36_0']==q36_0 and sample['q37_0']==q37_0 and int(energy)==0:
        q1_66=sample['q1_66']
        q36_0=sample['q36_0']
        q37_0=sample['outq37_0']
        tgt_before = sample['q37_0']
        break

print('#' * 80)
print("CCNOT operation on q1_66 (control1), q36_0 (control2) and q37_0 (target):")
print("    in:  q1_66={0}, q36_0={1}, q37_0={2}".format(q1_66,q36_0,tgt_before))
print("    out: q1_66={0}, q36_0={1}, q37_0={2}".format(q1_66,q36_0,q37_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q37_0 target: q38_0 ##
################################################################################
if 'q37_0' not in globals():
    q37_0=0
if 'q38_0' not in globals():
    q38_0=0

bqm = dimod.BinaryQuadraticModel({'q37_0' : 1, 'q38_0' : 1, 'outq38_0' : 1, 'anc' : 4}, {('q37_0', 'q38_0') : 2, ('q37_0', 'outq38_0') : -2, ('q38_0', 'outq38_0') : -2, ('q37_0', 'anc') : -4, ('q38_0', 'anc') : -4, ('outq38_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q37_0']==q37_0 and sample['q38_0']==q38_0 and int(energy)==0:
        q37_0=sample['q37_0']
        q38_0=sample['outq38_0']
        tgt_before = sample['q38_0']
        break

print('#' * 80)
print("CNOT operation on q37_0 (control) and q38_0 (target):")
print("    in:  q37_0={0}, q38_0={1}".format(q37_0,tgt_before))
print("    out: q37_0={0}, q38_0={1}".format(q37_0,q38_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_65 control2: q37_0 target: q38_0 ##
################################################################################
if 'q0_65' not in globals():
    q0_65=0
if 'q37_0' not in globals():
    q37_0=0
if 'q38_0' not in globals():
    q38_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq38_0' : 1, 'q38_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq38_0') : 4, ('anc1','q38_0') : -4, ('anc2', 'q0_65') : -2, ('anc2', 'q37_0') : -2, ('anc2', 'outq38_0') : -2, ('anc2', 'q38_0') : 2, ('q0_65', 'q37_0') : 1, ('outq38_0', 'q38_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_65']==q0_65 and sample['q37_0']==q37_0 and sample['q38_0']==q38_0 and int(energy)==0:
        q0_65=sample['q0_65']
        q37_0=sample['q37_0']
        q38_0=sample['outq38_0']
        tgt_before = sample['q38_0']
        break

print('#' * 80)
print("CCNOT operation on q0_65 (control1), q37_0 (control2) and q38_0 (target):")
print("    in:  q0_65={0}, q37_0={1}, q38_0={2}".format(q0_65,q37_0,tgt_before))
print("    out: q0_65={0}, q37_0={1}, q38_0={2}".format(q0_65,q37_0,q38_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_65 control2: q37_0 target: q38_0 ##
################################################################################
if 'q1_65' not in globals():
    q1_65=0
if 'q37_0' not in globals():
    q37_0=0
if 'q38_0' not in globals():
    q38_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq38_0' : 1, 'q38_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq38_0') : 4, ('anc1','q38_0') : -4, ('anc2', 'q1_65') : -2, ('anc2', 'q37_0') : -2, ('anc2', 'outq38_0') : -2, ('anc2', 'q38_0') : 2, ('q1_65', 'q37_0') : 1, ('outq38_0', 'q38_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_65']==q1_65 and sample['q37_0']==q37_0 and sample['q38_0']==q38_0 and int(energy)==0:
        q1_65=sample['q1_65']
        q37_0=sample['q37_0']
        q38_0=sample['outq38_0']
        tgt_before = sample['q38_0']
        break

print('#' * 80)
print("CCNOT operation on q1_65 (control1), q37_0 (control2) and q38_0 (target):")
print("    in:  q1_65={0}, q37_0={1}, q38_0={2}".format(q1_65,q37_0,tgt_before))
print("    out: q1_65={0}, q37_0={1}, q38_0={2}".format(q1_65,q37_0,q38_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q38_0 target: q39_0 ##
################################################################################
if 'q38_0' not in globals():
    q38_0=0
if 'q39_0' not in globals():
    q39_0=0

bqm = dimod.BinaryQuadraticModel({'q38_0' : 1, 'q39_0' : 1, 'outq39_0' : 1, 'anc' : 4}, {('q38_0', 'q39_0') : 2, ('q38_0', 'outq39_0') : -2, ('q39_0', 'outq39_0') : -2, ('q38_0', 'anc') : -4, ('q39_0', 'anc') : -4, ('outq39_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q38_0']==q38_0 and sample['q39_0']==q39_0 and int(energy)==0:
        q38_0=sample['q38_0']
        q39_0=sample['outq39_0']
        tgt_before = sample['q39_0']
        break

print('#' * 80)
print("CNOT operation on q38_0 (control) and q39_0 (target):")
print("    in:  q38_0={0}, q39_0={1}".format(q38_0,tgt_before))
print("    out: q38_0={0}, q39_0={1}".format(q38_0,q39_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_64 control2: q38_0 target: q39_0 ##
################################################################################
if 'q0_64' not in globals():
    q0_64=0
if 'q38_0' not in globals():
    q38_0=0
if 'q39_0' not in globals():
    q39_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq39_0' : 1, 'q39_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq39_0') : 4, ('anc1','q39_0') : -4, ('anc2', 'q0_64') : -2, ('anc2', 'q38_0') : -2, ('anc2', 'outq39_0') : -2, ('anc2', 'q39_0') : 2, ('q0_64', 'q38_0') : 1, ('outq39_0', 'q39_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_64']==q0_64 and sample['q38_0']==q38_0 and sample['q39_0']==q39_0 and int(energy)==0:
        q0_64=sample['q0_64']
        q38_0=sample['q38_0']
        q39_0=sample['outq39_0']
        tgt_before = sample['q39_0']
        break

print('#' * 80)
print("CCNOT operation on q0_64 (control1), q38_0 (control2) and q39_0 (target):")
print("    in:  q0_64={0}, q38_0={1}, q39_0={2}".format(q0_64,q38_0,tgt_before))
print("    out: q0_64={0}, q38_0={1}, q39_0={2}".format(q0_64,q38_0,q39_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_64 control2: q38_0 target: q39_0 ##
################################################################################
if 'q1_64' not in globals():
    q1_64=0
if 'q38_0' not in globals():
    q38_0=0
if 'q39_0' not in globals():
    q39_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq39_0' : 1, 'q39_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq39_0') : 4, ('anc1','q39_0') : -4, ('anc2', 'q1_64') : -2, ('anc2', 'q38_0') : -2, ('anc2', 'outq39_0') : -2, ('anc2', 'q39_0') : 2, ('q1_64', 'q38_0') : 1, ('outq39_0', 'q39_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_64']==q1_64 and sample['q38_0']==q38_0 and sample['q39_0']==q39_0 and int(energy)==0:
        q1_64=sample['q1_64']
        q38_0=sample['q38_0']
        q39_0=sample['outq39_0']
        tgt_before = sample['q39_0']
        break

print('#' * 80)
print("CCNOT operation on q1_64 (control1), q38_0 (control2) and q39_0 (target):")
print("    in:  q1_64={0}, q38_0={1}, q39_0={2}".format(q1_64,q38_0,tgt_before))
print("    out: q1_64={0}, q38_0={1}, q39_0={2}".format(q1_64,q38_0,q39_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q39_0 target: q40_0 ##
################################################################################
if 'q39_0' not in globals():
    q39_0=0
if 'q40_0' not in globals():
    q40_0=0

bqm = dimod.BinaryQuadraticModel({'q39_0' : 1, 'q40_0' : 1, 'outq40_0' : 1, 'anc' : 4}, {('q39_0', 'q40_0') : 2, ('q39_0', 'outq40_0') : -2, ('q40_0', 'outq40_0') : -2, ('q39_0', 'anc') : -4, ('q40_0', 'anc') : -4, ('outq40_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q39_0']==q39_0 and sample['q40_0']==q40_0 and int(energy)==0:
        q39_0=sample['q39_0']
        q40_0=sample['outq40_0']
        tgt_before = sample['q40_0']
        break

print('#' * 80)
print("CNOT operation on q39_0 (control) and q40_0 (target):")
print("    in:  q39_0={0}, q40_0={1}".format(q39_0,tgt_before))
print("    out: q39_0={0}, q40_0={1}".format(q39_0,q40_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_63 control2: q39_0 target: q40_0 ##
################################################################################
if 'q0_63' not in globals():
    q0_63=0
if 'q39_0' not in globals():
    q39_0=0
if 'q40_0' not in globals():
    q40_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq40_0' : 1, 'q40_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq40_0') : 4, ('anc1','q40_0') : -4, ('anc2', 'q0_63') : -2, ('anc2', 'q39_0') : -2, ('anc2', 'outq40_0') : -2, ('anc2', 'q40_0') : 2, ('q0_63', 'q39_0') : 1, ('outq40_0', 'q40_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_63']==q0_63 and sample['q39_0']==q39_0 and sample['q40_0']==q40_0 and int(energy)==0:
        q0_63=sample['q0_63']
        q39_0=sample['q39_0']
        q40_0=sample['outq40_0']
        tgt_before = sample['q40_0']
        break

print('#' * 80)
print("CCNOT operation on q0_63 (control1), q39_0 (control2) and q40_0 (target):")
print("    in:  q0_63={0}, q39_0={1}, q40_0={2}".format(q0_63,q39_0,tgt_before))
print("    out: q0_63={0}, q39_0={1}, q40_0={2}".format(q0_63,q39_0,q40_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_63 control2: q39_0 target: q40_0 ##
################################################################################
if 'q1_63' not in globals():
    q1_63=0
if 'q39_0' not in globals():
    q39_0=0
if 'q40_0' not in globals():
    q40_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq40_0' : 1, 'q40_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq40_0') : 4, ('anc1','q40_0') : -4, ('anc2', 'q1_63') : -2, ('anc2', 'q39_0') : -2, ('anc2', 'outq40_0') : -2, ('anc2', 'q40_0') : 2, ('q1_63', 'q39_0') : 1, ('outq40_0', 'q40_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_63']==q1_63 and sample['q39_0']==q39_0 and sample['q40_0']==q40_0 and int(energy)==0:
        q1_63=sample['q1_63']
        q39_0=sample['q39_0']
        q40_0=sample['outq40_0']
        tgt_before = sample['q40_0']
        break

print('#' * 80)
print("CCNOT operation on q1_63 (control1), q39_0 (control2) and q40_0 (target):")
print("    in:  q1_63={0}, q39_0={1}, q40_0={2}".format(q1_63,q39_0,tgt_before))
print("    out: q1_63={0}, q39_0={1}, q40_0={2}".format(q1_63,q39_0,q40_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q40_0 target: q41_0 ##
################################################################################
if 'q40_0' not in globals():
    q40_0=0
if 'q41_0' not in globals():
    q41_0=0

bqm = dimod.BinaryQuadraticModel({'q40_0' : 1, 'q41_0' : 1, 'outq41_0' : 1, 'anc' : 4}, {('q40_0', 'q41_0') : 2, ('q40_0', 'outq41_0') : -2, ('q41_0', 'outq41_0') : -2, ('q40_0', 'anc') : -4, ('q41_0', 'anc') : -4, ('outq41_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q40_0']==q40_0 and sample['q41_0']==q41_0 and int(energy)==0:
        q40_0=sample['q40_0']
        q41_0=sample['outq41_0']
        tgt_before = sample['q41_0']
        break

print('#' * 80)
print("CNOT operation on q40_0 (control) and q41_0 (target):")
print("    in:  q40_0={0}, q41_0={1}".format(q40_0,tgt_before))
print("    out: q40_0={0}, q41_0={1}".format(q40_0,q41_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_62 control2: q40_0 target: q41_0 ##
################################################################################
if 'q0_62' not in globals():
    q0_62=0
if 'q40_0' not in globals():
    q40_0=0
if 'q41_0' not in globals():
    q41_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq41_0' : 1, 'q41_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq41_0') : 4, ('anc1','q41_0') : -4, ('anc2', 'q0_62') : -2, ('anc2', 'q40_0') : -2, ('anc2', 'outq41_0') : -2, ('anc2', 'q41_0') : 2, ('q0_62', 'q40_0') : 1, ('outq41_0', 'q41_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_62']==q0_62 and sample['q40_0']==q40_0 and sample['q41_0']==q41_0 and int(energy)==0:
        q0_62=sample['q0_62']
        q40_0=sample['q40_0']
        q41_0=sample['outq41_0']
        tgt_before = sample['q41_0']
        break

print('#' * 80)
print("CCNOT operation on q0_62 (control1), q40_0 (control2) and q41_0 (target):")
print("    in:  q0_62={0}, q40_0={1}, q41_0={2}".format(q0_62,q40_0,tgt_before))
print("    out: q0_62={0}, q40_0={1}, q41_0={2}".format(q0_62,q40_0,q41_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_62 control2: q40_0 target: q41_0 ##
################################################################################
if 'q1_62' not in globals():
    q1_62=0
if 'q40_0' not in globals():
    q40_0=0
if 'q41_0' not in globals():
    q41_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq41_0' : 1, 'q41_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq41_0') : 4, ('anc1','q41_0') : -4, ('anc2', 'q1_62') : -2, ('anc2', 'q40_0') : -2, ('anc2', 'outq41_0') : -2, ('anc2', 'q41_0') : 2, ('q1_62', 'q40_0') : 1, ('outq41_0', 'q41_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_62']==q1_62 and sample['q40_0']==q40_0 and sample['q41_0']==q41_0 and int(energy)==0:
        q1_62=sample['q1_62']
        q40_0=sample['q40_0']
        q41_0=sample['outq41_0']
        tgt_before = sample['q41_0']
        break

print('#' * 80)
print("CCNOT operation on q1_62 (control1), q40_0 (control2) and q41_0 (target):")
print("    in:  q1_62={0}, q40_0={1}, q41_0={2}".format(q1_62,q40_0,tgt_before))
print("    out: q1_62={0}, q40_0={1}, q41_0={2}".format(q1_62,q40_0,q41_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q41_0 target: q42_0 ##
################################################################################
if 'q41_0' not in globals():
    q41_0=0
if 'q42_0' not in globals():
    q42_0=0

bqm = dimod.BinaryQuadraticModel({'q41_0' : 1, 'q42_0' : 1, 'outq42_0' : 1, 'anc' : 4}, {('q41_0', 'q42_0') : 2, ('q41_0', 'outq42_0') : -2, ('q42_0', 'outq42_0') : -2, ('q41_0', 'anc') : -4, ('q42_0', 'anc') : -4, ('outq42_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q41_0']==q41_0 and sample['q42_0']==q42_0 and int(energy)==0:
        q41_0=sample['q41_0']
        q42_0=sample['outq42_0']
        tgt_before = sample['q42_0']
        break

print('#' * 80)
print("CNOT operation on q41_0 (control) and q42_0 (target):")
print("    in:  q41_0={0}, q42_0={1}".format(q41_0,tgt_before))
print("    out: q41_0={0}, q42_0={1}".format(q41_0,q42_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_61 control2: q41_0 target: q42_0 ##
################################################################################
if 'q0_61' not in globals():
    q0_61=0
if 'q41_0' not in globals():
    q41_0=0
if 'q42_0' not in globals():
    q42_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq42_0' : 1, 'q42_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq42_0') : 4, ('anc1','q42_0') : -4, ('anc2', 'q0_61') : -2, ('anc2', 'q41_0') : -2, ('anc2', 'outq42_0') : -2, ('anc2', 'q42_0') : 2, ('q0_61', 'q41_0') : 1, ('outq42_0', 'q42_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_61']==q0_61 and sample['q41_0']==q41_0 and sample['q42_0']==q42_0 and int(energy)==0:
        q0_61=sample['q0_61']
        q41_0=sample['q41_0']
        q42_0=sample['outq42_0']
        tgt_before = sample['q42_0']
        break

print('#' * 80)
print("CCNOT operation on q0_61 (control1), q41_0 (control2) and q42_0 (target):")
print("    in:  q0_61={0}, q41_0={1}, q42_0={2}".format(q0_61,q41_0,tgt_before))
print("    out: q0_61={0}, q41_0={1}, q42_0={2}".format(q0_61,q41_0,q42_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_61 control2: q41_0 target: q42_0 ##
################################################################################
if 'q1_61' not in globals():
    q1_61=0
if 'q41_0' not in globals():
    q41_0=0
if 'q42_0' not in globals():
    q42_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq42_0' : 1, 'q42_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq42_0') : 4, ('anc1','q42_0') : -4, ('anc2', 'q1_61') : -2, ('anc2', 'q41_0') : -2, ('anc2', 'outq42_0') : -2, ('anc2', 'q42_0') : 2, ('q1_61', 'q41_0') : 1, ('outq42_0', 'q42_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_61']==q1_61 and sample['q41_0']==q41_0 and sample['q42_0']==q42_0 and int(energy)==0:
        q1_61=sample['q1_61']
        q41_0=sample['q41_0']
        q42_0=sample['outq42_0']
        tgt_before = sample['q42_0']
        break

print('#' * 80)
print("CCNOT operation on q1_61 (control1), q41_0 (control2) and q42_0 (target):")
print("    in:  q1_61={0}, q41_0={1}, q42_0={2}".format(q1_61,q41_0,tgt_before))
print("    out: q1_61={0}, q41_0={1}, q42_0={2}".format(q1_61,q41_0,q42_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q42_0 target: q43_0 ##
################################################################################
if 'q42_0' not in globals():
    q42_0=0
if 'q43_0' not in globals():
    q43_0=0

bqm = dimod.BinaryQuadraticModel({'q42_0' : 1, 'q43_0' : 1, 'outq43_0' : 1, 'anc' : 4}, {('q42_0', 'q43_0') : 2, ('q42_0', 'outq43_0') : -2, ('q43_0', 'outq43_0') : -2, ('q42_0', 'anc') : -4, ('q43_0', 'anc') : -4, ('outq43_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q42_0']==q42_0 and sample['q43_0']==q43_0 and int(energy)==0:
        q42_0=sample['q42_0']
        q43_0=sample['outq43_0']
        tgt_before = sample['q43_0']
        break

print('#' * 80)
print("CNOT operation on q42_0 (control) and q43_0 (target):")
print("    in:  q42_0={0}, q43_0={1}".format(q42_0,tgt_before))
print("    out: q42_0={0}, q43_0={1}".format(q42_0,q43_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_60 control2: q42_0 target: q43_0 ##
################################################################################
if 'q0_60' not in globals():
    q0_60=0
if 'q42_0' not in globals():
    q42_0=0
if 'q43_0' not in globals():
    q43_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq43_0' : 1, 'q43_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq43_0') : 4, ('anc1','q43_0') : -4, ('anc2', 'q0_60') : -2, ('anc2', 'q42_0') : -2, ('anc2', 'outq43_0') : -2, ('anc2', 'q43_0') : 2, ('q0_60', 'q42_0') : 1, ('outq43_0', 'q43_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_60']==q0_60 and sample['q42_0']==q42_0 and sample['q43_0']==q43_0 and int(energy)==0:
        q0_60=sample['q0_60']
        q42_0=sample['q42_0']
        q43_0=sample['outq43_0']
        tgt_before = sample['q43_0']
        break

print('#' * 80)
print("CCNOT operation on q0_60 (control1), q42_0 (control2) and q43_0 (target):")
print("    in:  q0_60={0}, q42_0={1}, q43_0={2}".format(q0_60,q42_0,tgt_before))
print("    out: q0_60={0}, q42_0={1}, q43_0={2}".format(q0_60,q42_0,q43_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_60 control2: q42_0 target: q43_0 ##
################################################################################
if 'q1_60' not in globals():
    q1_60=0
if 'q42_0' not in globals():
    q42_0=0
if 'q43_0' not in globals():
    q43_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq43_0' : 1, 'q43_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq43_0') : 4, ('anc1','q43_0') : -4, ('anc2', 'q1_60') : -2, ('anc2', 'q42_0') : -2, ('anc2', 'outq43_0') : -2, ('anc2', 'q43_0') : 2, ('q1_60', 'q42_0') : 1, ('outq43_0', 'q43_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_60']==q1_60 and sample['q42_0']==q42_0 and sample['q43_0']==q43_0 and int(energy)==0:
        q1_60=sample['q1_60']
        q42_0=sample['q42_0']
        q43_0=sample['outq43_0']
        tgt_before = sample['q43_0']
        break

print('#' * 80)
print("CCNOT operation on q1_60 (control1), q42_0 (control2) and q43_0 (target):")
print("    in:  q1_60={0}, q42_0={1}, q43_0={2}".format(q1_60,q42_0,tgt_before))
print("    out: q1_60={0}, q42_0={1}, q43_0={2}".format(q1_60,q42_0,q43_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q43_0 target: q44_0 ##
################################################################################
if 'q43_0' not in globals():
    q43_0=0
if 'q44_0' not in globals():
    q44_0=0

bqm = dimod.BinaryQuadraticModel({'q43_0' : 1, 'q44_0' : 1, 'outq44_0' : 1, 'anc' : 4}, {('q43_0', 'q44_0') : 2, ('q43_0', 'outq44_0') : -2, ('q44_0', 'outq44_0') : -2, ('q43_0', 'anc') : -4, ('q44_0', 'anc') : -4, ('outq44_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q43_0']==q43_0 and sample['q44_0']==q44_0 and int(energy)==0:
        q43_0=sample['q43_0']
        q44_0=sample['outq44_0']
        tgt_before = sample['q44_0']
        break

print('#' * 80)
print("CNOT operation on q43_0 (control) and q44_0 (target):")
print("    in:  q43_0={0}, q44_0={1}".format(q43_0,tgt_before))
print("    out: q43_0={0}, q44_0={1}".format(q43_0,q44_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_59 control2: q43_0 target: q44_0 ##
################################################################################
if 'q0_59' not in globals():
    q0_59=0
if 'q43_0' not in globals():
    q43_0=0
if 'q44_0' not in globals():
    q44_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq44_0' : 1, 'q44_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq44_0') : 4, ('anc1','q44_0') : -4, ('anc2', 'q0_59') : -2, ('anc2', 'q43_0') : -2, ('anc2', 'outq44_0') : -2, ('anc2', 'q44_0') : 2, ('q0_59', 'q43_0') : 1, ('outq44_0', 'q44_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_59']==q0_59 and sample['q43_0']==q43_0 and sample['q44_0']==q44_0 and int(energy)==0:
        q0_59=sample['q0_59']
        q43_0=sample['q43_0']
        q44_0=sample['outq44_0']
        tgt_before = sample['q44_0']
        break

print('#' * 80)
print("CCNOT operation on q0_59 (control1), q43_0 (control2) and q44_0 (target):")
print("    in:  q0_59={0}, q43_0={1}, q44_0={2}".format(q0_59,q43_0,tgt_before))
print("    out: q0_59={0}, q43_0={1}, q44_0={2}".format(q0_59,q43_0,q44_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_59 control2: q43_0 target: q44_0 ##
################################################################################
if 'q1_59' not in globals():
    q1_59=0
if 'q43_0' not in globals():
    q43_0=0
if 'q44_0' not in globals():
    q44_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq44_0' : 1, 'q44_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq44_0') : 4, ('anc1','q44_0') : -4, ('anc2', 'q1_59') : -2, ('anc2', 'q43_0') : -2, ('anc2', 'outq44_0') : -2, ('anc2', 'q44_0') : 2, ('q1_59', 'q43_0') : 1, ('outq44_0', 'q44_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_59']==q1_59 and sample['q43_0']==q43_0 and sample['q44_0']==q44_0 and int(energy)==0:
        q1_59=sample['q1_59']
        q43_0=sample['q43_0']
        q44_0=sample['outq44_0']
        tgt_before = sample['q44_0']
        break

print('#' * 80)
print("CCNOT operation on q1_59 (control1), q43_0 (control2) and q44_0 (target):")
print("    in:  q1_59={0}, q43_0={1}, q44_0={2}".format(q1_59,q43_0,tgt_before))
print("    out: q1_59={0}, q43_0={1}, q44_0={2}".format(q1_59,q43_0,q44_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q44_0 target: q45_0 ##
################################################################################
if 'q44_0' not in globals():
    q44_0=0
if 'q45_0' not in globals():
    q45_0=0

bqm = dimod.BinaryQuadraticModel({'q44_0' : 1, 'q45_0' : 1, 'outq45_0' : 1, 'anc' : 4}, {('q44_0', 'q45_0') : 2, ('q44_0', 'outq45_0') : -2, ('q45_0', 'outq45_0') : -2, ('q44_0', 'anc') : -4, ('q45_0', 'anc') : -4, ('outq45_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q44_0']==q44_0 and sample['q45_0']==q45_0 and int(energy)==0:
        q44_0=sample['q44_0']
        q45_0=sample['outq45_0']
        tgt_before = sample['q45_0']
        break

print('#' * 80)
print("CNOT operation on q44_0 (control) and q45_0 (target):")
print("    in:  q44_0={0}, q45_0={1}".format(q44_0,tgt_before))
print("    out: q44_0={0}, q45_0={1}".format(q44_0,q45_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_58 control2: q44_0 target: q45_0 ##
################################################################################
if 'q0_58' not in globals():
    q0_58=0
if 'q44_0' not in globals():
    q44_0=0
if 'q45_0' not in globals():
    q45_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq45_0' : 1, 'q45_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq45_0') : 4, ('anc1','q45_0') : -4, ('anc2', 'q0_58') : -2, ('anc2', 'q44_0') : -2, ('anc2', 'outq45_0') : -2, ('anc2', 'q45_0') : 2, ('q0_58', 'q44_0') : 1, ('outq45_0', 'q45_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_58']==q0_58 and sample['q44_0']==q44_0 and sample['q45_0']==q45_0 and int(energy)==0:
        q0_58=sample['q0_58']
        q44_0=sample['q44_0']
        q45_0=sample['outq45_0']
        tgt_before = sample['q45_0']
        break

print('#' * 80)
print("CCNOT operation on q0_58 (control1), q44_0 (control2) and q45_0 (target):")
print("    in:  q0_58={0}, q44_0={1}, q45_0={2}".format(q0_58,q44_0,tgt_before))
print("    out: q0_58={0}, q44_0={1}, q45_0={2}".format(q0_58,q44_0,q45_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_58 control2: q44_0 target: q45_0 ##
################################################################################
if 'q1_58' not in globals():
    q1_58=0
if 'q44_0' not in globals():
    q44_0=0
if 'q45_0' not in globals():
    q45_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq45_0' : 1, 'q45_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq45_0') : 4, ('anc1','q45_0') : -4, ('anc2', 'q1_58') : -2, ('anc2', 'q44_0') : -2, ('anc2', 'outq45_0') : -2, ('anc2', 'q45_0') : 2, ('q1_58', 'q44_0') : 1, ('outq45_0', 'q45_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_58']==q1_58 and sample['q44_0']==q44_0 and sample['q45_0']==q45_0 and int(energy)==0:
        q1_58=sample['q1_58']
        q44_0=sample['q44_0']
        q45_0=sample['outq45_0']
        tgt_before = sample['q45_0']
        break

print('#' * 80)
print("CCNOT operation on q1_58 (control1), q44_0 (control2) and q45_0 (target):")
print("    in:  q1_58={0}, q44_0={1}, q45_0={2}".format(q1_58,q44_0,tgt_before))
print("    out: q1_58={0}, q44_0={1}, q45_0={2}".format(q1_58,q44_0,q45_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q45_0 target: q46_0 ##
################################################################################
if 'q45_0' not in globals():
    q45_0=0
if 'q46_0' not in globals():
    q46_0=0

bqm = dimod.BinaryQuadraticModel({'q45_0' : 1, 'q46_0' : 1, 'outq46_0' : 1, 'anc' : 4}, {('q45_0', 'q46_0') : 2, ('q45_0', 'outq46_0') : -2, ('q46_0', 'outq46_0') : -2, ('q45_0', 'anc') : -4, ('q46_0', 'anc') : -4, ('outq46_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q45_0']==q45_0 and sample['q46_0']==q46_0 and int(energy)==0:
        q45_0=sample['q45_0']
        q46_0=sample['outq46_0']
        tgt_before = sample['q46_0']
        break

print('#' * 80)
print("CNOT operation on q45_0 (control) and q46_0 (target):")
print("    in:  q45_0={0}, q46_0={1}".format(q45_0,tgt_before))
print("    out: q45_0={0}, q46_0={1}".format(q45_0,q46_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_57 control2: q45_0 target: q46_0 ##
################################################################################
if 'q0_57' not in globals():
    q0_57=0
if 'q45_0' not in globals():
    q45_0=0
if 'q46_0' not in globals():
    q46_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq46_0' : 1, 'q46_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq46_0') : 4, ('anc1','q46_0') : -4, ('anc2', 'q0_57') : -2, ('anc2', 'q45_0') : -2, ('anc2', 'outq46_0') : -2, ('anc2', 'q46_0') : 2, ('q0_57', 'q45_0') : 1, ('outq46_0', 'q46_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_57']==q0_57 and sample['q45_0']==q45_0 and sample['q46_0']==q46_0 and int(energy)==0:
        q0_57=sample['q0_57']
        q45_0=sample['q45_0']
        q46_0=sample['outq46_0']
        tgt_before = sample['q46_0']
        break

print('#' * 80)
print("CCNOT operation on q0_57 (control1), q45_0 (control2) and q46_0 (target):")
print("    in:  q0_57={0}, q45_0={1}, q46_0={2}".format(q0_57,q45_0,tgt_before))
print("    out: q0_57={0}, q45_0={1}, q46_0={2}".format(q0_57,q45_0,q46_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_57 control2: q45_0 target: q46_0 ##
################################################################################
if 'q1_57' not in globals():
    q1_57=0
if 'q45_0' not in globals():
    q45_0=0
if 'q46_0' not in globals():
    q46_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq46_0' : 1, 'q46_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq46_0') : 4, ('anc1','q46_0') : -4, ('anc2', 'q1_57') : -2, ('anc2', 'q45_0') : -2, ('anc2', 'outq46_0') : -2, ('anc2', 'q46_0') : 2, ('q1_57', 'q45_0') : 1, ('outq46_0', 'q46_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_57']==q1_57 and sample['q45_0']==q45_0 and sample['q46_0']==q46_0 and int(energy)==0:
        q1_57=sample['q1_57']
        q45_0=sample['q45_0']
        q46_0=sample['outq46_0']
        tgt_before = sample['q46_0']
        break

print('#' * 80)
print("CCNOT operation on q1_57 (control1), q45_0 (control2) and q46_0 (target):")
print("    in:  q1_57={0}, q45_0={1}, q46_0={2}".format(q1_57,q45_0,tgt_before))
print("    out: q1_57={0}, q45_0={1}, q46_0={2}".format(q1_57,q45_0,q46_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q46_0 target: q47_0 ##
################################################################################
if 'q46_0' not in globals():
    q46_0=0
if 'q47_0' not in globals():
    q47_0=0

bqm = dimod.BinaryQuadraticModel({'q46_0' : 1, 'q47_0' : 1, 'outq47_0' : 1, 'anc' : 4}, {('q46_0', 'q47_0') : 2, ('q46_0', 'outq47_0') : -2, ('q47_0', 'outq47_0') : -2, ('q46_0', 'anc') : -4, ('q47_0', 'anc') : -4, ('outq47_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q46_0']==q46_0 and sample['q47_0']==q47_0 and int(energy)==0:
        q46_0=sample['q46_0']
        q47_0=sample['outq47_0']
        tgt_before = sample['q47_0']
        break

print('#' * 80)
print("CNOT operation on q46_0 (control) and q47_0 (target):")
print("    in:  q46_0={0}, q47_0={1}".format(q46_0,tgt_before))
print("    out: q46_0={0}, q47_0={1}".format(q46_0,q47_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_56 control2: q46_0 target: q47_0 ##
################################################################################
if 'q0_56' not in globals():
    q0_56=0
if 'q46_0' not in globals():
    q46_0=0
if 'q47_0' not in globals():
    q47_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq47_0' : 1, 'q47_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq47_0') : 4, ('anc1','q47_0') : -4, ('anc2', 'q0_56') : -2, ('anc2', 'q46_0') : -2, ('anc2', 'outq47_0') : -2, ('anc2', 'q47_0') : 2, ('q0_56', 'q46_0') : 1, ('outq47_0', 'q47_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_56']==q0_56 and sample['q46_0']==q46_0 and sample['q47_0']==q47_0 and int(energy)==0:
        q0_56=sample['q0_56']
        q46_0=sample['q46_0']
        q47_0=sample['outq47_0']
        tgt_before = sample['q47_0']
        break

print('#' * 80)
print("CCNOT operation on q0_56 (control1), q46_0 (control2) and q47_0 (target):")
print("    in:  q0_56={0}, q46_0={1}, q47_0={2}".format(q0_56,q46_0,tgt_before))
print("    out: q0_56={0}, q46_0={1}, q47_0={2}".format(q0_56,q46_0,q47_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_56 control2: q46_0 target: q47_0 ##
################################################################################
if 'q1_56' not in globals():
    q1_56=0
if 'q46_0' not in globals():
    q46_0=0
if 'q47_0' not in globals():
    q47_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq47_0' : 1, 'q47_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq47_0') : 4, ('anc1','q47_0') : -4, ('anc2', 'q1_56') : -2, ('anc2', 'q46_0') : -2, ('anc2', 'outq47_0') : -2, ('anc2', 'q47_0') : 2, ('q1_56', 'q46_0') : 1, ('outq47_0', 'q47_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_56']==q1_56 and sample['q46_0']==q46_0 and sample['q47_0']==q47_0 and int(energy)==0:
        q1_56=sample['q1_56']
        q46_0=sample['q46_0']
        q47_0=sample['outq47_0']
        tgt_before = sample['q47_0']
        break

print('#' * 80)
print("CCNOT operation on q1_56 (control1), q46_0 (control2) and q47_0 (target):")
print("    in:  q1_56={0}, q46_0={1}, q47_0={2}".format(q1_56,q46_0,tgt_before))
print("    out: q1_56={0}, q46_0={1}, q47_0={2}".format(q1_56,q46_0,q47_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q47_0 target: q48_0 ##
################################################################################
if 'q47_0' not in globals():
    q47_0=0
if 'q48_0' not in globals():
    q48_0=0

bqm = dimod.BinaryQuadraticModel({'q47_0' : 1, 'q48_0' : 1, 'outq48_0' : 1, 'anc' : 4}, {('q47_0', 'q48_0') : 2, ('q47_0', 'outq48_0') : -2, ('q48_0', 'outq48_0') : -2, ('q47_0', 'anc') : -4, ('q48_0', 'anc') : -4, ('outq48_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q47_0']==q47_0 and sample['q48_0']==q48_0 and int(energy)==0:
        q47_0=sample['q47_0']
        q48_0=sample['outq48_0']
        tgt_before = sample['q48_0']
        break

print('#' * 80)
print("CNOT operation on q47_0 (control) and q48_0 (target):")
print("    in:  q47_0={0}, q48_0={1}".format(q47_0,tgt_before))
print("    out: q47_0={0}, q48_0={1}".format(q47_0,q48_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_55 control2: q47_0 target: q48_0 ##
################################################################################
if 'q0_55' not in globals():
    q0_55=0
if 'q47_0' not in globals():
    q47_0=0
if 'q48_0' not in globals():
    q48_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq48_0' : 1, 'q48_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq48_0') : 4, ('anc1','q48_0') : -4, ('anc2', 'q0_55') : -2, ('anc2', 'q47_0') : -2, ('anc2', 'outq48_0') : -2, ('anc2', 'q48_0') : 2, ('q0_55', 'q47_0') : 1, ('outq48_0', 'q48_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_55']==q0_55 and sample['q47_0']==q47_0 and sample['q48_0']==q48_0 and int(energy)==0:
        q0_55=sample['q0_55']
        q47_0=sample['q47_0']
        q48_0=sample['outq48_0']
        tgt_before = sample['q48_0']
        break

print('#' * 80)
print("CCNOT operation on q0_55 (control1), q47_0 (control2) and q48_0 (target):")
print("    in:  q0_55={0}, q47_0={1}, q48_0={2}".format(q0_55,q47_0,tgt_before))
print("    out: q0_55={0}, q47_0={1}, q48_0={2}".format(q0_55,q47_0,q48_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_55 control2: q47_0 target: q48_0 ##
################################################################################
if 'q1_55' not in globals():
    q1_55=0
if 'q47_0' not in globals():
    q47_0=0
if 'q48_0' not in globals():
    q48_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq48_0' : 1, 'q48_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq48_0') : 4, ('anc1','q48_0') : -4, ('anc2', 'q1_55') : -2, ('anc2', 'q47_0') : -2, ('anc2', 'outq48_0') : -2, ('anc2', 'q48_0') : 2, ('q1_55', 'q47_0') : 1, ('outq48_0', 'q48_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_55']==q1_55 and sample['q47_0']==q47_0 and sample['q48_0']==q48_0 and int(energy)==0:
        q1_55=sample['q1_55']
        q47_0=sample['q47_0']
        q48_0=sample['outq48_0']
        tgt_before = sample['q48_0']
        break

print('#' * 80)
print("CCNOT operation on q1_55 (control1), q47_0 (control2) and q48_0 (target):")
print("    in:  q1_55={0}, q47_0={1}, q48_0={2}".format(q1_55,q47_0,tgt_before))
print("    out: q1_55={0}, q47_0={1}, q48_0={2}".format(q1_55,q47_0,q48_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q48_0 target: q49_0 ##
################################################################################
if 'q48_0' not in globals():
    q48_0=0
if 'q49_0' not in globals():
    q49_0=0

bqm = dimod.BinaryQuadraticModel({'q48_0' : 1, 'q49_0' : 1, 'outq49_0' : 1, 'anc' : 4}, {('q48_0', 'q49_0') : 2, ('q48_0', 'outq49_0') : -2, ('q49_0', 'outq49_0') : -2, ('q48_0', 'anc') : -4, ('q49_0', 'anc') : -4, ('outq49_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q48_0']==q48_0 and sample['q49_0']==q49_0 and int(energy)==0:
        q48_0=sample['q48_0']
        q49_0=sample['outq49_0']
        tgt_before = sample['q49_0']
        break

print('#' * 80)
print("CNOT operation on q48_0 (control) and q49_0 (target):")
print("    in:  q48_0={0}, q49_0={1}".format(q48_0,tgt_before))
print("    out: q48_0={0}, q49_0={1}".format(q48_0,q49_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_54 control2: q48_0 target: q49_0 ##
################################################################################
if 'q0_54' not in globals():
    q0_54=0
if 'q48_0' not in globals():
    q48_0=0
if 'q49_0' not in globals():
    q49_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq49_0' : 1, 'q49_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq49_0') : 4, ('anc1','q49_0') : -4, ('anc2', 'q0_54') : -2, ('anc2', 'q48_0') : -2, ('anc2', 'outq49_0') : -2, ('anc2', 'q49_0') : 2, ('q0_54', 'q48_0') : 1, ('outq49_0', 'q49_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_54']==q0_54 and sample['q48_0']==q48_0 and sample['q49_0']==q49_0 and int(energy)==0:
        q0_54=sample['q0_54']
        q48_0=sample['q48_0']
        q49_0=sample['outq49_0']
        tgt_before = sample['q49_0']
        break

print('#' * 80)
print("CCNOT operation on q0_54 (control1), q48_0 (control2) and q49_0 (target):")
print("    in:  q0_54={0}, q48_0={1}, q49_0={2}".format(q0_54,q48_0,tgt_before))
print("    out: q0_54={0}, q48_0={1}, q49_0={2}".format(q0_54,q48_0,q49_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_54 control2: q48_0 target: q49_0 ##
################################################################################
if 'q1_54' not in globals():
    q1_54=0
if 'q48_0' not in globals():
    q48_0=0
if 'q49_0' not in globals():
    q49_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq49_0' : 1, 'q49_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq49_0') : 4, ('anc1','q49_0') : -4, ('anc2', 'q1_54') : -2, ('anc2', 'q48_0') : -2, ('anc2', 'outq49_0') : -2, ('anc2', 'q49_0') : 2, ('q1_54', 'q48_0') : 1, ('outq49_0', 'q49_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_54']==q1_54 and sample['q48_0']==q48_0 and sample['q49_0']==q49_0 and int(energy)==0:
        q1_54=sample['q1_54']
        q48_0=sample['q48_0']
        q49_0=sample['outq49_0']
        tgt_before = sample['q49_0']
        break

print('#' * 80)
print("CCNOT operation on q1_54 (control1), q48_0 (control2) and q49_0 (target):")
print("    in:  q1_54={0}, q48_0={1}, q49_0={2}".format(q1_54,q48_0,tgt_before))
print("    out: q1_54={0}, q48_0={1}, q49_0={2}".format(q1_54,q48_0,q49_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q49_0 target: q50_0 ##
################################################################################
if 'q49_0' not in globals():
    q49_0=0
if 'q50_0' not in globals():
    q50_0=0

bqm = dimod.BinaryQuadraticModel({'q49_0' : 1, 'q50_0' : 1, 'outq50_0' : 1, 'anc' : 4}, {('q49_0', 'q50_0') : 2, ('q49_0', 'outq50_0') : -2, ('q50_0', 'outq50_0') : -2, ('q49_0', 'anc') : -4, ('q50_0', 'anc') : -4, ('outq50_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q49_0']==q49_0 and sample['q50_0']==q50_0 and int(energy)==0:
        q49_0=sample['q49_0']
        q50_0=sample['outq50_0']
        tgt_before = sample['q50_0']
        break

print('#' * 80)
print("CNOT operation on q49_0 (control) and q50_0 (target):")
print("    in:  q49_0={0}, q50_0={1}".format(q49_0,tgt_before))
print("    out: q49_0={0}, q50_0={1}".format(q49_0,q50_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_53 control2: q49_0 target: q50_0 ##
################################################################################
if 'q0_53' not in globals():
    q0_53=0
if 'q49_0' not in globals():
    q49_0=0
if 'q50_0' not in globals():
    q50_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq50_0' : 1, 'q50_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq50_0') : 4, ('anc1','q50_0') : -4, ('anc2', 'q0_53') : -2, ('anc2', 'q49_0') : -2, ('anc2', 'outq50_0') : -2, ('anc2', 'q50_0') : 2, ('q0_53', 'q49_0') : 1, ('outq50_0', 'q50_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_53']==q0_53 and sample['q49_0']==q49_0 and sample['q50_0']==q50_0 and int(energy)==0:
        q0_53=sample['q0_53']
        q49_0=sample['q49_0']
        q50_0=sample['outq50_0']
        tgt_before = sample['q50_0']
        break

print('#' * 80)
print("CCNOT operation on q0_53 (control1), q49_0 (control2) and q50_0 (target):")
print("    in:  q0_53={0}, q49_0={1}, q50_0={2}".format(q0_53,q49_0,tgt_before))
print("    out: q0_53={0}, q49_0={1}, q50_0={2}".format(q0_53,q49_0,q50_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_53 control2: q49_0 target: q50_0 ##
################################################################################
if 'q1_53' not in globals():
    q1_53=0
if 'q49_0' not in globals():
    q49_0=0
if 'q50_0' not in globals():
    q50_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq50_0' : 1, 'q50_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq50_0') : 4, ('anc1','q50_0') : -4, ('anc2', 'q1_53') : -2, ('anc2', 'q49_0') : -2, ('anc2', 'outq50_0') : -2, ('anc2', 'q50_0') : 2, ('q1_53', 'q49_0') : 1, ('outq50_0', 'q50_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_53']==q1_53 and sample['q49_0']==q49_0 and sample['q50_0']==q50_0 and int(energy)==0:
        q1_53=sample['q1_53']
        q49_0=sample['q49_0']
        q50_0=sample['outq50_0']
        tgt_before = sample['q50_0']
        break

print('#' * 80)
print("CCNOT operation on q1_53 (control1), q49_0 (control2) and q50_0 (target):")
print("    in:  q1_53={0}, q49_0={1}, q50_0={2}".format(q1_53,q49_0,tgt_before))
print("    out: q1_53={0}, q49_0={1}, q50_0={2}".format(q1_53,q49_0,q50_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q50_0 target: q51_0 ##
################################################################################
if 'q50_0' not in globals():
    q50_0=0
if 'q51_0' not in globals():
    q51_0=0

bqm = dimod.BinaryQuadraticModel({'q50_0' : 1, 'q51_0' : 1, 'outq51_0' : 1, 'anc' : 4}, {('q50_0', 'q51_0') : 2, ('q50_0', 'outq51_0') : -2, ('q51_0', 'outq51_0') : -2, ('q50_0', 'anc') : -4, ('q51_0', 'anc') : -4, ('outq51_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q50_0']==q50_0 and sample['q51_0']==q51_0 and int(energy)==0:
        q50_0=sample['q50_0']
        q51_0=sample['outq51_0']
        tgt_before = sample['q51_0']
        break

print('#' * 80)
print("CNOT operation on q50_0 (control) and q51_0 (target):")
print("    in:  q50_0={0}, q51_0={1}".format(q50_0,tgt_before))
print("    out: q50_0={0}, q51_0={1}".format(q50_0,q51_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_52 control2: q50_0 target: q51_0 ##
################################################################################
if 'q0_52' not in globals():
    q0_52=0
if 'q50_0' not in globals():
    q50_0=0
if 'q51_0' not in globals():
    q51_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq51_0' : 1, 'q51_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq51_0') : 4, ('anc1','q51_0') : -4, ('anc2', 'q0_52') : -2, ('anc2', 'q50_0') : -2, ('anc2', 'outq51_0') : -2, ('anc2', 'q51_0') : 2, ('q0_52', 'q50_0') : 1, ('outq51_0', 'q51_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_52']==q0_52 and sample['q50_0']==q50_0 and sample['q51_0']==q51_0 and int(energy)==0:
        q0_52=sample['q0_52']
        q50_0=sample['q50_0']
        q51_0=sample['outq51_0']
        tgt_before = sample['q51_0']
        break

print('#' * 80)
print("CCNOT operation on q0_52 (control1), q50_0 (control2) and q51_0 (target):")
print("    in:  q0_52={0}, q50_0={1}, q51_0={2}".format(q0_52,q50_0,tgt_before))
print("    out: q0_52={0}, q50_0={1}, q51_0={2}".format(q0_52,q50_0,q51_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_52 control2: q50_0 target: q51_0 ##
################################################################################
if 'q1_52' not in globals():
    q1_52=0
if 'q50_0' not in globals():
    q50_0=0
if 'q51_0' not in globals():
    q51_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq51_0' : 1, 'q51_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq51_0') : 4, ('anc1','q51_0') : -4, ('anc2', 'q1_52') : -2, ('anc2', 'q50_0') : -2, ('anc2', 'outq51_0') : -2, ('anc2', 'q51_0') : 2, ('q1_52', 'q50_0') : 1, ('outq51_0', 'q51_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_52']==q1_52 and sample['q50_0']==q50_0 and sample['q51_0']==q51_0 and int(energy)==0:
        q1_52=sample['q1_52']
        q50_0=sample['q50_0']
        q51_0=sample['outq51_0']
        tgt_before = sample['q51_0']
        break

print('#' * 80)
print("CCNOT operation on q1_52 (control1), q50_0 (control2) and q51_0 (target):")
print("    in:  q1_52={0}, q50_0={1}, q51_0={2}".format(q1_52,q50_0,tgt_before))
print("    out: q1_52={0}, q50_0={1}, q51_0={2}".format(q1_52,q50_0,q51_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q51_0 target: q52_0 ##
################################################################################
if 'q51_0' not in globals():
    q51_0=0
if 'q52_0' not in globals():
    q52_0=0

bqm = dimod.BinaryQuadraticModel({'q51_0' : 1, 'q52_0' : 1, 'outq52_0' : 1, 'anc' : 4}, {('q51_0', 'q52_0') : 2, ('q51_0', 'outq52_0') : -2, ('q52_0', 'outq52_0') : -2, ('q51_0', 'anc') : -4, ('q52_0', 'anc') : -4, ('outq52_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q51_0']==q51_0 and sample['q52_0']==q52_0 and int(energy)==0:
        q51_0=sample['q51_0']
        q52_0=sample['outq52_0']
        tgt_before = sample['q52_0']
        break

print('#' * 80)
print("CNOT operation on q51_0 (control) and q52_0 (target):")
print("    in:  q51_0={0}, q52_0={1}".format(q51_0,tgt_before))
print("    out: q51_0={0}, q52_0={1}".format(q51_0,q52_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_51 control2: q51_0 target: q52_0 ##
################################################################################
if 'q0_51' not in globals():
    q0_51=0
if 'q51_0' not in globals():
    q51_0=0
if 'q52_0' not in globals():
    q52_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq52_0' : 1, 'q52_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq52_0') : 4, ('anc1','q52_0') : -4, ('anc2', 'q0_51') : -2, ('anc2', 'q51_0') : -2, ('anc2', 'outq52_0') : -2, ('anc2', 'q52_0') : 2, ('q0_51', 'q51_0') : 1, ('outq52_0', 'q52_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_51']==q0_51 and sample['q51_0']==q51_0 and sample['q52_0']==q52_0 and int(energy)==0:
        q0_51=sample['q0_51']
        q51_0=sample['q51_0']
        q52_0=sample['outq52_0']
        tgt_before = sample['q52_0']
        break

print('#' * 80)
print("CCNOT operation on q0_51 (control1), q51_0 (control2) and q52_0 (target):")
print("    in:  q0_51={0}, q51_0={1}, q52_0={2}".format(q0_51,q51_0,tgt_before))
print("    out: q0_51={0}, q51_0={1}, q52_0={2}".format(q0_51,q51_0,q52_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_51 control2: q51_0 target: q52_0 ##
################################################################################
if 'q1_51' not in globals():
    q1_51=0
if 'q51_0' not in globals():
    q51_0=0
if 'q52_0' not in globals():
    q52_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq52_0' : 1, 'q52_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq52_0') : 4, ('anc1','q52_0') : -4, ('anc2', 'q1_51') : -2, ('anc2', 'q51_0') : -2, ('anc2', 'outq52_0') : -2, ('anc2', 'q52_0') : 2, ('q1_51', 'q51_0') : 1, ('outq52_0', 'q52_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_51']==q1_51 and sample['q51_0']==q51_0 and sample['q52_0']==q52_0 and int(energy)==0:
        q1_51=sample['q1_51']
        q51_0=sample['q51_0']
        q52_0=sample['outq52_0']
        tgt_before = sample['q52_0']
        break

print('#' * 80)
print("CCNOT operation on q1_51 (control1), q51_0 (control2) and q52_0 (target):")
print("    in:  q1_51={0}, q51_0={1}, q52_0={2}".format(q1_51,q51_0,tgt_before))
print("    out: q1_51={0}, q51_0={1}, q52_0={2}".format(q1_51,q51_0,q52_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q52_0 target: q53_0 ##
################################################################################
if 'q52_0' not in globals():
    q52_0=0
if 'q53_0' not in globals():
    q53_0=0

bqm = dimod.BinaryQuadraticModel({'q52_0' : 1, 'q53_0' : 1, 'outq53_0' : 1, 'anc' : 4}, {('q52_0', 'q53_0') : 2, ('q52_0', 'outq53_0') : -2, ('q53_0', 'outq53_0') : -2, ('q52_0', 'anc') : -4, ('q53_0', 'anc') : -4, ('outq53_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q52_0']==q52_0 and sample['q53_0']==q53_0 and int(energy)==0:
        q52_0=sample['q52_0']
        q53_0=sample['outq53_0']
        tgt_before = sample['q53_0']
        break

print('#' * 80)
print("CNOT operation on q52_0 (control) and q53_0 (target):")
print("    in:  q52_0={0}, q53_0={1}".format(q52_0,tgt_before))
print("    out: q52_0={0}, q53_0={1}".format(q52_0,q53_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_50 control2: q52_0 target: q53_0 ##
################################################################################
if 'q0_50' not in globals():
    q0_50=0
if 'q52_0' not in globals():
    q52_0=0
if 'q53_0' not in globals():
    q53_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq53_0' : 1, 'q53_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq53_0') : 4, ('anc1','q53_0') : -4, ('anc2', 'q0_50') : -2, ('anc2', 'q52_0') : -2, ('anc2', 'outq53_0') : -2, ('anc2', 'q53_0') : 2, ('q0_50', 'q52_0') : 1, ('outq53_0', 'q53_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_50']==q0_50 and sample['q52_0']==q52_0 and sample['q53_0']==q53_0 and int(energy)==0:
        q0_50=sample['q0_50']
        q52_0=sample['q52_0']
        q53_0=sample['outq53_0']
        tgt_before = sample['q53_0']
        break

print('#' * 80)
print("CCNOT operation on q0_50 (control1), q52_0 (control2) and q53_0 (target):")
print("    in:  q0_50={0}, q52_0={1}, q53_0={2}".format(q0_50,q52_0,tgt_before))
print("    out: q0_50={0}, q52_0={1}, q53_0={2}".format(q0_50,q52_0,q53_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_50 control2: q52_0 target: q53_0 ##
################################################################################
if 'q1_50' not in globals():
    q1_50=0
if 'q52_0' not in globals():
    q52_0=0
if 'q53_0' not in globals():
    q53_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq53_0' : 1, 'q53_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq53_0') : 4, ('anc1','q53_0') : -4, ('anc2', 'q1_50') : -2, ('anc2', 'q52_0') : -2, ('anc2', 'outq53_0') : -2, ('anc2', 'q53_0') : 2, ('q1_50', 'q52_0') : 1, ('outq53_0', 'q53_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_50']==q1_50 and sample['q52_0']==q52_0 and sample['q53_0']==q53_0 and int(energy)==0:
        q1_50=sample['q1_50']
        q52_0=sample['q52_0']
        q53_0=sample['outq53_0']
        tgt_before = sample['q53_0']
        break

print('#' * 80)
print("CCNOT operation on q1_50 (control1), q52_0 (control2) and q53_0 (target):")
print("    in:  q1_50={0}, q52_0={1}, q53_0={2}".format(q1_50,q52_0,tgt_before))
print("    out: q1_50={0}, q52_0={1}, q53_0={2}".format(q1_50,q52_0,q53_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q53_0 target: q54_0 ##
################################################################################
if 'q53_0' not in globals():
    q53_0=0
if 'q54_0' not in globals():
    q54_0=0

bqm = dimod.BinaryQuadraticModel({'q53_0' : 1, 'q54_0' : 1, 'outq54_0' : 1, 'anc' : 4}, {('q53_0', 'q54_0') : 2, ('q53_0', 'outq54_0') : -2, ('q54_0', 'outq54_0') : -2, ('q53_0', 'anc') : -4, ('q54_0', 'anc') : -4, ('outq54_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q53_0']==q53_0 and sample['q54_0']==q54_0 and int(energy)==0:
        q53_0=sample['q53_0']
        q54_0=sample['outq54_0']
        tgt_before = sample['q54_0']
        break

print('#' * 80)
print("CNOT operation on q53_0 (control) and q54_0 (target):")
print("    in:  q53_0={0}, q54_0={1}".format(q53_0,tgt_before))
print("    out: q53_0={0}, q54_0={1}".format(q53_0,q54_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_49 control2: q53_0 target: q54_0 ##
################################################################################
if 'q0_49' not in globals():
    q0_49=0
if 'q53_0' not in globals():
    q53_0=0
if 'q54_0' not in globals():
    q54_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq54_0' : 1, 'q54_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq54_0') : 4, ('anc1','q54_0') : -4, ('anc2', 'q0_49') : -2, ('anc2', 'q53_0') : -2, ('anc2', 'outq54_0') : -2, ('anc2', 'q54_0') : 2, ('q0_49', 'q53_0') : 1, ('outq54_0', 'q54_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_49']==q0_49 and sample['q53_0']==q53_0 and sample['q54_0']==q54_0 and int(energy)==0:
        q0_49=sample['q0_49']
        q53_0=sample['q53_0']
        q54_0=sample['outq54_0']
        tgt_before = sample['q54_0']
        break

print('#' * 80)
print("CCNOT operation on q0_49 (control1), q53_0 (control2) and q54_0 (target):")
print("    in:  q0_49={0}, q53_0={1}, q54_0={2}".format(q0_49,q53_0,tgt_before))
print("    out: q0_49={0}, q53_0={1}, q54_0={2}".format(q0_49,q53_0,q54_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_49 control2: q53_0 target: q54_0 ##
################################################################################
if 'q1_49' not in globals():
    q1_49=0
if 'q53_0' not in globals():
    q53_0=0
if 'q54_0' not in globals():
    q54_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq54_0' : 1, 'q54_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq54_0') : 4, ('anc1','q54_0') : -4, ('anc2', 'q1_49') : -2, ('anc2', 'q53_0') : -2, ('anc2', 'outq54_0') : -2, ('anc2', 'q54_0') : 2, ('q1_49', 'q53_0') : 1, ('outq54_0', 'q54_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_49']==q1_49 and sample['q53_0']==q53_0 and sample['q54_0']==q54_0 and int(energy)==0:
        q1_49=sample['q1_49']
        q53_0=sample['q53_0']
        q54_0=sample['outq54_0']
        tgt_before = sample['q54_0']
        break

print('#' * 80)
print("CCNOT operation on q1_49 (control1), q53_0 (control2) and q54_0 (target):")
print("    in:  q1_49={0}, q53_0={1}, q54_0={2}".format(q1_49,q53_0,tgt_before))
print("    out: q1_49={0}, q53_0={1}, q54_0={2}".format(q1_49,q53_0,q54_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q54_0 target: q55_0 ##
################################################################################
if 'q54_0' not in globals():
    q54_0=0
if 'q55_0' not in globals():
    q55_0=0

bqm = dimod.BinaryQuadraticModel({'q54_0' : 1, 'q55_0' : 1, 'outq55_0' : 1, 'anc' : 4}, {('q54_0', 'q55_0') : 2, ('q54_0', 'outq55_0') : -2, ('q55_0', 'outq55_0') : -2, ('q54_0', 'anc') : -4, ('q55_0', 'anc') : -4, ('outq55_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q54_0']==q54_0 and sample['q55_0']==q55_0 and int(energy)==0:
        q54_0=sample['q54_0']
        q55_0=sample['outq55_0']
        tgt_before = sample['q55_0']
        break

print('#' * 80)
print("CNOT operation on q54_0 (control) and q55_0 (target):")
print("    in:  q54_0={0}, q55_0={1}".format(q54_0,tgt_before))
print("    out: q54_0={0}, q55_0={1}".format(q54_0,q55_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_48 control2: q54_0 target: q55_0 ##
################################################################################
if 'q0_48' not in globals():
    q0_48=0
if 'q54_0' not in globals():
    q54_0=0
if 'q55_0' not in globals():
    q55_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq55_0' : 1, 'q55_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq55_0') : 4, ('anc1','q55_0') : -4, ('anc2', 'q0_48') : -2, ('anc2', 'q54_0') : -2, ('anc2', 'outq55_0') : -2, ('anc2', 'q55_0') : 2, ('q0_48', 'q54_0') : 1, ('outq55_0', 'q55_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_48']==q0_48 and sample['q54_0']==q54_0 and sample['q55_0']==q55_0 and int(energy)==0:
        q0_48=sample['q0_48']
        q54_0=sample['q54_0']
        q55_0=sample['outq55_0']
        tgt_before = sample['q55_0']
        break

print('#' * 80)
print("CCNOT operation on q0_48 (control1), q54_0 (control2) and q55_0 (target):")
print("    in:  q0_48={0}, q54_0={1}, q55_0={2}".format(q0_48,q54_0,tgt_before))
print("    out: q0_48={0}, q54_0={1}, q55_0={2}".format(q0_48,q54_0,q55_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_48 control2: q54_0 target: q55_0 ##
################################################################################
if 'q1_48' not in globals():
    q1_48=0
if 'q54_0' not in globals():
    q54_0=0
if 'q55_0' not in globals():
    q55_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq55_0' : 1, 'q55_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq55_0') : 4, ('anc1','q55_0') : -4, ('anc2', 'q1_48') : -2, ('anc2', 'q54_0') : -2, ('anc2', 'outq55_0') : -2, ('anc2', 'q55_0') : 2, ('q1_48', 'q54_0') : 1, ('outq55_0', 'q55_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_48']==q1_48 and sample['q54_0']==q54_0 and sample['q55_0']==q55_0 and int(energy)==0:
        q1_48=sample['q1_48']
        q54_0=sample['q54_0']
        q55_0=sample['outq55_0']
        tgt_before = sample['q55_0']
        break

print('#' * 80)
print("CCNOT operation on q1_48 (control1), q54_0 (control2) and q55_0 (target):")
print("    in:  q1_48={0}, q54_0={1}, q55_0={2}".format(q1_48,q54_0,tgt_before))
print("    out: q1_48={0}, q54_0={1}, q55_0={2}".format(q1_48,q54_0,q55_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q55_0 target: q56_0 ##
################################################################################
if 'q55_0' not in globals():
    q55_0=0
if 'q56_0' not in globals():
    q56_0=0

bqm = dimod.BinaryQuadraticModel({'q55_0' : 1, 'q56_0' : 1, 'outq56_0' : 1, 'anc' : 4}, {('q55_0', 'q56_0') : 2, ('q55_0', 'outq56_0') : -2, ('q56_0', 'outq56_0') : -2, ('q55_0', 'anc') : -4, ('q56_0', 'anc') : -4, ('outq56_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q55_0']==q55_0 and sample['q56_0']==q56_0 and int(energy)==0:
        q55_0=sample['q55_0']
        q56_0=sample['outq56_0']
        tgt_before = sample['q56_0']
        break

print('#' * 80)
print("CNOT operation on q55_0 (control) and q56_0 (target):")
print("    in:  q55_0={0}, q56_0={1}".format(q55_0,tgt_before))
print("    out: q55_0={0}, q56_0={1}".format(q55_0,q56_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_47 control2: q55_0 target: q56_0 ##
################################################################################
if 'q0_47' not in globals():
    q0_47=0
if 'q55_0' not in globals():
    q55_0=0
if 'q56_0' not in globals():
    q56_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq56_0' : 1, 'q56_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq56_0') : 4, ('anc1','q56_0') : -4, ('anc2', 'q0_47') : -2, ('anc2', 'q55_0') : -2, ('anc2', 'outq56_0') : -2, ('anc2', 'q56_0') : 2, ('q0_47', 'q55_0') : 1, ('outq56_0', 'q56_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_47']==q0_47 and sample['q55_0']==q55_0 and sample['q56_0']==q56_0 and int(energy)==0:
        q0_47=sample['q0_47']
        q55_0=sample['q55_0']
        q56_0=sample['outq56_0']
        tgt_before = sample['q56_0']
        break

print('#' * 80)
print("CCNOT operation on q0_47 (control1), q55_0 (control2) and q56_0 (target):")
print("    in:  q0_47={0}, q55_0={1}, q56_0={2}".format(q0_47,q55_0,tgt_before))
print("    out: q0_47={0}, q55_0={1}, q56_0={2}".format(q0_47,q55_0,q56_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_47 control2: q55_0 target: q56_0 ##
################################################################################
if 'q1_47' not in globals():
    q1_47=0
if 'q55_0' not in globals():
    q55_0=0
if 'q56_0' not in globals():
    q56_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq56_0' : 1, 'q56_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq56_0') : 4, ('anc1','q56_0') : -4, ('anc2', 'q1_47') : -2, ('anc2', 'q55_0') : -2, ('anc2', 'outq56_0') : -2, ('anc2', 'q56_0') : 2, ('q1_47', 'q55_0') : 1, ('outq56_0', 'q56_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_47']==q1_47 and sample['q55_0']==q55_0 and sample['q56_0']==q56_0 and int(energy)==0:
        q1_47=sample['q1_47']
        q55_0=sample['q55_0']
        q56_0=sample['outq56_0']
        tgt_before = sample['q56_0']
        break

print('#' * 80)
print("CCNOT operation on q1_47 (control1), q55_0 (control2) and q56_0 (target):")
print("    in:  q1_47={0}, q55_0={1}, q56_0={2}".format(q1_47,q55_0,tgt_before))
print("    out: q1_47={0}, q55_0={1}, q56_0={2}".format(q1_47,q55_0,q56_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q56_0 target: q57_0 ##
################################################################################
if 'q56_0' not in globals():
    q56_0=0
if 'q57_0' not in globals():
    q57_0=0

bqm = dimod.BinaryQuadraticModel({'q56_0' : 1, 'q57_0' : 1, 'outq57_0' : 1, 'anc' : 4}, {('q56_0', 'q57_0') : 2, ('q56_0', 'outq57_0') : -2, ('q57_0', 'outq57_0') : -2, ('q56_0', 'anc') : -4, ('q57_0', 'anc') : -4, ('outq57_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q56_0']==q56_0 and sample['q57_0']==q57_0 and int(energy)==0:
        q56_0=sample['q56_0']
        q57_0=sample['outq57_0']
        tgt_before = sample['q57_0']
        break

print('#' * 80)
print("CNOT operation on q56_0 (control) and q57_0 (target):")
print("    in:  q56_0={0}, q57_0={1}".format(q56_0,tgt_before))
print("    out: q56_0={0}, q57_0={1}".format(q56_0,q57_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_46 control2: q56_0 target: q57_0 ##
################################################################################
if 'q0_46' not in globals():
    q0_46=0
if 'q56_0' not in globals():
    q56_0=0
if 'q57_0' not in globals():
    q57_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq57_0' : 1, 'q57_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq57_0') : 4, ('anc1','q57_0') : -4, ('anc2', 'q0_46') : -2, ('anc2', 'q56_0') : -2, ('anc2', 'outq57_0') : -2, ('anc2', 'q57_0') : 2, ('q0_46', 'q56_0') : 1, ('outq57_0', 'q57_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_46']==q0_46 and sample['q56_0']==q56_0 and sample['q57_0']==q57_0 and int(energy)==0:
        q0_46=sample['q0_46']
        q56_0=sample['q56_0']
        q57_0=sample['outq57_0']
        tgt_before = sample['q57_0']
        break

print('#' * 80)
print("CCNOT operation on q0_46 (control1), q56_0 (control2) and q57_0 (target):")
print("    in:  q0_46={0}, q56_0={1}, q57_0={2}".format(q0_46,q56_0,tgt_before))
print("    out: q0_46={0}, q56_0={1}, q57_0={2}".format(q0_46,q56_0,q57_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_46 control2: q56_0 target: q57_0 ##
################################################################################
if 'q1_46' not in globals():
    q1_46=0
if 'q56_0' not in globals():
    q56_0=0
if 'q57_0' not in globals():
    q57_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq57_0' : 1, 'q57_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq57_0') : 4, ('anc1','q57_0') : -4, ('anc2', 'q1_46') : -2, ('anc2', 'q56_0') : -2, ('anc2', 'outq57_0') : -2, ('anc2', 'q57_0') : 2, ('q1_46', 'q56_0') : 1, ('outq57_0', 'q57_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_46']==q1_46 and sample['q56_0']==q56_0 and sample['q57_0']==q57_0 and int(energy)==0:
        q1_46=sample['q1_46']
        q56_0=sample['q56_0']
        q57_0=sample['outq57_0']
        tgt_before = sample['q57_0']
        break

print('#' * 80)
print("CCNOT operation on q1_46 (control1), q56_0 (control2) and q57_0 (target):")
print("    in:  q1_46={0}, q56_0={1}, q57_0={2}".format(q1_46,q56_0,tgt_before))
print("    out: q1_46={0}, q56_0={1}, q57_0={2}".format(q1_46,q56_0,q57_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q57_0 target: q58_0 ##
################################################################################
if 'q57_0' not in globals():
    q57_0=0
if 'q58_0' not in globals():
    q58_0=0

bqm = dimod.BinaryQuadraticModel({'q57_0' : 1, 'q58_0' : 1, 'outq58_0' : 1, 'anc' : 4}, {('q57_0', 'q58_0') : 2, ('q57_0', 'outq58_0') : -2, ('q58_0', 'outq58_0') : -2, ('q57_0', 'anc') : -4, ('q58_0', 'anc') : -4, ('outq58_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q57_0']==q57_0 and sample['q58_0']==q58_0 and int(energy)==0:
        q57_0=sample['q57_0']
        q58_0=sample['outq58_0']
        tgt_before = sample['q58_0']
        break

print('#' * 80)
print("CNOT operation on q57_0 (control) and q58_0 (target):")
print("    in:  q57_0={0}, q58_0={1}".format(q57_0,tgt_before))
print("    out: q57_0={0}, q58_0={1}".format(q57_0,q58_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_45 control2: q57_0 target: q58_0 ##
################################################################################
if 'q0_45' not in globals():
    q0_45=0
if 'q57_0' not in globals():
    q57_0=0
if 'q58_0' not in globals():
    q58_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq58_0' : 1, 'q58_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq58_0') : 4, ('anc1','q58_0') : -4, ('anc2', 'q0_45') : -2, ('anc2', 'q57_0') : -2, ('anc2', 'outq58_0') : -2, ('anc2', 'q58_0') : 2, ('q0_45', 'q57_0') : 1, ('outq58_0', 'q58_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_45']==q0_45 and sample['q57_0']==q57_0 and sample['q58_0']==q58_0 and int(energy)==0:
        q0_45=sample['q0_45']
        q57_0=sample['q57_0']
        q58_0=sample['outq58_0']
        tgt_before = sample['q58_0']
        break

print('#' * 80)
print("CCNOT operation on q0_45 (control1), q57_0 (control2) and q58_0 (target):")
print("    in:  q0_45={0}, q57_0={1}, q58_0={2}".format(q0_45,q57_0,tgt_before))
print("    out: q0_45={0}, q57_0={1}, q58_0={2}".format(q0_45,q57_0,q58_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_45 control2: q57_0 target: q58_0 ##
################################################################################
if 'q1_45' not in globals():
    q1_45=0
if 'q57_0' not in globals():
    q57_0=0
if 'q58_0' not in globals():
    q58_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq58_0' : 1, 'q58_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq58_0') : 4, ('anc1','q58_0') : -4, ('anc2', 'q1_45') : -2, ('anc2', 'q57_0') : -2, ('anc2', 'outq58_0') : -2, ('anc2', 'q58_0') : 2, ('q1_45', 'q57_0') : 1, ('outq58_0', 'q58_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_45']==q1_45 and sample['q57_0']==q57_0 and sample['q58_0']==q58_0 and int(energy)==0:
        q1_45=sample['q1_45']
        q57_0=sample['q57_0']
        q58_0=sample['outq58_0']
        tgt_before = sample['q58_0']
        break

print('#' * 80)
print("CCNOT operation on q1_45 (control1), q57_0 (control2) and q58_0 (target):")
print("    in:  q1_45={0}, q57_0={1}, q58_0={2}".format(q1_45,q57_0,tgt_before))
print("    out: q1_45={0}, q57_0={1}, q58_0={2}".format(q1_45,q57_0,q58_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q58_0 target: q59_0 ##
################################################################################
if 'q58_0' not in globals():
    q58_0=0
if 'q59_0' not in globals():
    q59_0=0

bqm = dimod.BinaryQuadraticModel({'q58_0' : 1, 'q59_0' : 1, 'outq59_0' : 1, 'anc' : 4}, {('q58_0', 'q59_0') : 2, ('q58_0', 'outq59_0') : -2, ('q59_0', 'outq59_0') : -2, ('q58_0', 'anc') : -4, ('q59_0', 'anc') : -4, ('outq59_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q58_0']==q58_0 and sample['q59_0']==q59_0 and int(energy)==0:
        q58_0=sample['q58_0']
        q59_0=sample['outq59_0']
        tgt_before = sample['q59_0']
        break

print('#' * 80)
print("CNOT operation on q58_0 (control) and q59_0 (target):")
print("    in:  q58_0={0}, q59_0={1}".format(q58_0,tgt_before))
print("    out: q58_0={0}, q59_0={1}".format(q58_0,q59_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_44 control2: q58_0 target: q59_0 ##
################################################################################
if 'q0_44' not in globals():
    q0_44=0
if 'q58_0' not in globals():
    q58_0=0
if 'q59_0' not in globals():
    q59_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq59_0' : 1, 'q59_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq59_0') : 4, ('anc1','q59_0') : -4, ('anc2', 'q0_44') : -2, ('anc2', 'q58_0') : -2, ('anc2', 'outq59_0') : -2, ('anc2', 'q59_0') : 2, ('q0_44', 'q58_0') : 1, ('outq59_0', 'q59_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_44']==q0_44 and sample['q58_0']==q58_0 and sample['q59_0']==q59_0 and int(energy)==0:
        q0_44=sample['q0_44']
        q58_0=sample['q58_0']
        q59_0=sample['outq59_0']
        tgt_before = sample['q59_0']
        break

print('#' * 80)
print("CCNOT operation on q0_44 (control1), q58_0 (control2) and q59_0 (target):")
print("    in:  q0_44={0}, q58_0={1}, q59_0={2}".format(q0_44,q58_0,tgt_before))
print("    out: q0_44={0}, q58_0={1}, q59_0={2}".format(q0_44,q58_0,q59_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_44 control2: q58_0 target: q59_0 ##
################################################################################
if 'q1_44' not in globals():
    q1_44=0
if 'q58_0' not in globals():
    q58_0=0
if 'q59_0' not in globals():
    q59_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq59_0' : 1, 'q59_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq59_0') : 4, ('anc1','q59_0') : -4, ('anc2', 'q1_44') : -2, ('anc2', 'q58_0') : -2, ('anc2', 'outq59_0') : -2, ('anc2', 'q59_0') : 2, ('q1_44', 'q58_0') : 1, ('outq59_0', 'q59_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_44']==q1_44 and sample['q58_0']==q58_0 and sample['q59_0']==q59_0 and int(energy)==0:
        q1_44=sample['q1_44']
        q58_0=sample['q58_0']
        q59_0=sample['outq59_0']
        tgt_before = sample['q59_0']
        break

print('#' * 80)
print("CCNOT operation on q1_44 (control1), q58_0 (control2) and q59_0 (target):")
print("    in:  q1_44={0}, q58_0={1}, q59_0={2}".format(q1_44,q58_0,tgt_before))
print("    out: q1_44={0}, q58_0={1}, q59_0={2}".format(q1_44,q58_0,q59_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q59_0 target: q60_0 ##
################################################################################
if 'q59_0' not in globals():
    q59_0=0
if 'q60_0' not in globals():
    q60_0=0

bqm = dimod.BinaryQuadraticModel({'q59_0' : 1, 'q60_0' : 1, 'outq60_0' : 1, 'anc' : 4}, {('q59_0', 'q60_0') : 2, ('q59_0', 'outq60_0') : -2, ('q60_0', 'outq60_0') : -2, ('q59_0', 'anc') : -4, ('q60_0', 'anc') : -4, ('outq60_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q59_0']==q59_0 and sample['q60_0']==q60_0 and int(energy)==0:
        q59_0=sample['q59_0']
        q60_0=sample['outq60_0']
        tgt_before = sample['q60_0']
        break

print('#' * 80)
print("CNOT operation on q59_0 (control) and q60_0 (target):")
print("    in:  q59_0={0}, q60_0={1}".format(q59_0,tgt_before))
print("    out: q59_0={0}, q60_0={1}".format(q59_0,q60_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_43 control2: q59_0 target: q60_0 ##
################################################################################
if 'q0_43' not in globals():
    q0_43=0
if 'q59_0' not in globals():
    q59_0=0
if 'q60_0' not in globals():
    q60_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq60_0' : 1, 'q60_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq60_0') : 4, ('anc1','q60_0') : -4, ('anc2', 'q0_43') : -2, ('anc2', 'q59_0') : -2, ('anc2', 'outq60_0') : -2, ('anc2', 'q60_0') : 2, ('q0_43', 'q59_0') : 1, ('outq60_0', 'q60_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_43']==q0_43 and sample['q59_0']==q59_0 and sample['q60_0']==q60_0 and int(energy)==0:
        q0_43=sample['q0_43']
        q59_0=sample['q59_0']
        q60_0=sample['outq60_0']
        tgt_before = sample['q60_0']
        break

print('#' * 80)
print("CCNOT operation on q0_43 (control1), q59_0 (control2) and q60_0 (target):")
print("    in:  q0_43={0}, q59_0={1}, q60_0={2}".format(q0_43,q59_0,tgt_before))
print("    out: q0_43={0}, q59_0={1}, q60_0={2}".format(q0_43,q59_0,q60_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_43 control2: q59_0 target: q60_0 ##
################################################################################
if 'q1_43' not in globals():
    q1_43=0
if 'q59_0' not in globals():
    q59_0=0
if 'q60_0' not in globals():
    q60_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq60_0' : 1, 'q60_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq60_0') : 4, ('anc1','q60_0') : -4, ('anc2', 'q1_43') : -2, ('anc2', 'q59_0') : -2, ('anc2', 'outq60_0') : -2, ('anc2', 'q60_0') : 2, ('q1_43', 'q59_0') : 1, ('outq60_0', 'q60_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_43']==q1_43 and sample['q59_0']==q59_0 and sample['q60_0']==q60_0 and int(energy)==0:
        q1_43=sample['q1_43']
        q59_0=sample['q59_0']
        q60_0=sample['outq60_0']
        tgt_before = sample['q60_0']
        break

print('#' * 80)
print("CCNOT operation on q1_43 (control1), q59_0 (control2) and q60_0 (target):")
print("    in:  q1_43={0}, q59_0={1}, q60_0={2}".format(q1_43,q59_0,tgt_before))
print("    out: q1_43={0}, q59_0={1}, q60_0={2}".format(q1_43,q59_0,q60_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q60_0 target: q61_0 ##
################################################################################
if 'q60_0' not in globals():
    q60_0=0
if 'q61_0' not in globals():
    q61_0=0

bqm = dimod.BinaryQuadraticModel({'q60_0' : 1, 'q61_0' : 1, 'outq61_0' : 1, 'anc' : 4}, {('q60_0', 'q61_0') : 2, ('q60_0', 'outq61_0') : -2, ('q61_0', 'outq61_0') : -2, ('q60_0', 'anc') : -4, ('q61_0', 'anc') : -4, ('outq61_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q60_0']==q60_0 and sample['q61_0']==q61_0 and int(energy)==0:
        q60_0=sample['q60_0']
        q61_0=sample['outq61_0']
        tgt_before = sample['q61_0']
        break

print('#' * 80)
print("CNOT operation on q60_0 (control) and q61_0 (target):")
print("    in:  q60_0={0}, q61_0={1}".format(q60_0,tgt_before))
print("    out: q60_0={0}, q61_0={1}".format(q60_0,q61_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_42 control2: q60_0 target: q61_0 ##
################################################################################
if 'q0_42' not in globals():
    q0_42=0
if 'q60_0' not in globals():
    q60_0=0
if 'q61_0' not in globals():
    q61_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq61_0' : 1, 'q61_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq61_0') : 4, ('anc1','q61_0') : -4, ('anc2', 'q0_42') : -2, ('anc2', 'q60_0') : -2, ('anc2', 'outq61_0') : -2, ('anc2', 'q61_0') : 2, ('q0_42', 'q60_0') : 1, ('outq61_0', 'q61_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_42']==q0_42 and sample['q60_0']==q60_0 and sample['q61_0']==q61_0 and int(energy)==0:
        q0_42=sample['q0_42']
        q60_0=sample['q60_0']
        q61_0=sample['outq61_0']
        tgt_before = sample['q61_0']
        break

print('#' * 80)
print("CCNOT operation on q0_42 (control1), q60_0 (control2) and q61_0 (target):")
print("    in:  q0_42={0}, q60_0={1}, q61_0={2}".format(q0_42,q60_0,tgt_before))
print("    out: q0_42={0}, q60_0={1}, q61_0={2}".format(q0_42,q60_0,q61_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_42 control2: q60_0 target: q61_0 ##
################################################################################
if 'q1_42' not in globals():
    q1_42=0
if 'q60_0' not in globals():
    q60_0=0
if 'q61_0' not in globals():
    q61_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq61_0' : 1, 'q61_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq61_0') : 4, ('anc1','q61_0') : -4, ('anc2', 'q1_42') : -2, ('anc2', 'q60_0') : -2, ('anc2', 'outq61_0') : -2, ('anc2', 'q61_0') : 2, ('q1_42', 'q60_0') : 1, ('outq61_0', 'q61_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_42']==q1_42 and sample['q60_0']==q60_0 and sample['q61_0']==q61_0 and int(energy)==0:
        q1_42=sample['q1_42']
        q60_0=sample['q60_0']
        q61_0=sample['outq61_0']
        tgt_before = sample['q61_0']
        break

print('#' * 80)
print("CCNOT operation on q1_42 (control1), q60_0 (control2) and q61_0 (target):")
print("    in:  q1_42={0}, q60_0={1}, q61_0={2}".format(q1_42,q60_0,tgt_before))
print("    out: q1_42={0}, q60_0={1}, q61_0={2}".format(q1_42,q60_0,q61_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q61_0 target: q62_0 ##
################################################################################
if 'q61_0' not in globals():
    q61_0=0
if 'q62_0' not in globals():
    q62_0=0

bqm = dimod.BinaryQuadraticModel({'q61_0' : 1, 'q62_0' : 1, 'outq62_0' : 1, 'anc' : 4}, {('q61_0', 'q62_0') : 2, ('q61_0', 'outq62_0') : -2, ('q62_0', 'outq62_0') : -2, ('q61_0', 'anc') : -4, ('q62_0', 'anc') : -4, ('outq62_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q61_0']==q61_0 and sample['q62_0']==q62_0 and int(energy)==0:
        q61_0=sample['q61_0']
        q62_0=sample['outq62_0']
        tgt_before = sample['q62_0']
        break

print('#' * 80)
print("CNOT operation on q61_0 (control) and q62_0 (target):")
print("    in:  q61_0={0}, q62_0={1}".format(q61_0,tgt_before))
print("    out: q61_0={0}, q62_0={1}".format(q61_0,q62_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_41 control2: q61_0 target: q62_0 ##
################################################################################
if 'q0_41' not in globals():
    q0_41=0
if 'q61_0' not in globals():
    q61_0=0
if 'q62_0' not in globals():
    q62_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq62_0' : 1, 'q62_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq62_0') : 4, ('anc1','q62_0') : -4, ('anc2', 'q0_41') : -2, ('anc2', 'q61_0') : -2, ('anc2', 'outq62_0') : -2, ('anc2', 'q62_0') : 2, ('q0_41', 'q61_0') : 1, ('outq62_0', 'q62_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_41']==q0_41 and sample['q61_0']==q61_0 and sample['q62_0']==q62_0 and int(energy)==0:
        q0_41=sample['q0_41']
        q61_0=sample['q61_0']
        q62_0=sample['outq62_0']
        tgt_before = sample['q62_0']
        break

print('#' * 80)
print("CCNOT operation on q0_41 (control1), q61_0 (control2) and q62_0 (target):")
print("    in:  q0_41={0}, q61_0={1}, q62_0={2}".format(q0_41,q61_0,tgt_before))
print("    out: q0_41={0}, q61_0={1}, q62_0={2}".format(q0_41,q61_0,q62_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_41 control2: q61_0 target: q62_0 ##
################################################################################
if 'q1_41' not in globals():
    q1_41=0
if 'q61_0' not in globals():
    q61_0=0
if 'q62_0' not in globals():
    q62_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq62_0' : 1, 'q62_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq62_0') : 4, ('anc1','q62_0') : -4, ('anc2', 'q1_41') : -2, ('anc2', 'q61_0') : -2, ('anc2', 'outq62_0') : -2, ('anc2', 'q62_0') : 2, ('q1_41', 'q61_0') : 1, ('outq62_0', 'q62_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_41']==q1_41 and sample['q61_0']==q61_0 and sample['q62_0']==q62_0 and int(energy)==0:
        q1_41=sample['q1_41']
        q61_0=sample['q61_0']
        q62_0=sample['outq62_0']
        tgt_before = sample['q62_0']
        break

print('#' * 80)
print("CCNOT operation on q1_41 (control1), q61_0 (control2) and q62_0 (target):")
print("    in:  q1_41={0}, q61_0={1}, q62_0={2}".format(q1_41,q61_0,tgt_before))
print("    out: q1_41={0}, q61_0={1}, q62_0={2}".format(q1_41,q61_0,q62_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q62_0 target: q63_0 ##
################################################################################
if 'q62_0' not in globals():
    q62_0=0
if 'q63_0' not in globals():
    q63_0=0

bqm = dimod.BinaryQuadraticModel({'q62_0' : 1, 'q63_0' : 1, 'outq63_0' : 1, 'anc' : 4}, {('q62_0', 'q63_0') : 2, ('q62_0', 'outq63_0') : -2, ('q63_0', 'outq63_0') : -2, ('q62_0', 'anc') : -4, ('q63_0', 'anc') : -4, ('outq63_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q62_0']==q62_0 and sample['q63_0']==q63_0 and int(energy)==0:
        q62_0=sample['q62_0']
        q63_0=sample['outq63_0']
        tgt_before = sample['q63_0']
        break

print('#' * 80)
print("CNOT operation on q62_0 (control) and q63_0 (target):")
print("    in:  q62_0={0}, q63_0={1}".format(q62_0,tgt_before))
print("    out: q62_0={0}, q63_0={1}".format(q62_0,q63_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_40 control2: q62_0 target: q63_0 ##
################################################################################
if 'q0_40' not in globals():
    q0_40=0
if 'q62_0' not in globals():
    q62_0=0
if 'q63_0' not in globals():
    q63_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq63_0' : 1, 'q63_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq63_0') : 4, ('anc1','q63_0') : -4, ('anc2', 'q0_40') : -2, ('anc2', 'q62_0') : -2, ('anc2', 'outq63_0') : -2, ('anc2', 'q63_0') : 2, ('q0_40', 'q62_0') : 1, ('outq63_0', 'q63_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_40']==q0_40 and sample['q62_0']==q62_0 and sample['q63_0']==q63_0 and int(energy)==0:
        q0_40=sample['q0_40']
        q62_0=sample['q62_0']
        q63_0=sample['outq63_0']
        tgt_before = sample['q63_0']
        break

print('#' * 80)
print("CCNOT operation on q0_40 (control1), q62_0 (control2) and q63_0 (target):")
print("    in:  q0_40={0}, q62_0={1}, q63_0={2}".format(q0_40,q62_0,tgt_before))
print("    out: q0_40={0}, q62_0={1}, q63_0={2}".format(q0_40,q62_0,q63_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_40 control2: q62_0 target: q63_0 ##
################################################################################
if 'q1_40' not in globals():
    q1_40=0
if 'q62_0' not in globals():
    q62_0=0
if 'q63_0' not in globals():
    q63_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq63_0' : 1, 'q63_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq63_0') : 4, ('anc1','q63_0') : -4, ('anc2', 'q1_40') : -2, ('anc2', 'q62_0') : -2, ('anc2', 'outq63_0') : -2, ('anc2', 'q63_0') : 2, ('q1_40', 'q62_0') : 1, ('outq63_0', 'q63_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_40']==q1_40 and sample['q62_0']==q62_0 and sample['q63_0']==q63_0 and int(energy)==0:
        q1_40=sample['q1_40']
        q62_0=sample['q62_0']
        q63_0=sample['outq63_0']
        tgt_before = sample['q63_0']
        break

print('#' * 80)
print("CCNOT operation on q1_40 (control1), q62_0 (control2) and q63_0 (target):")
print("    in:  q1_40={0}, q62_0={1}, q63_0={2}".format(q1_40,q62_0,tgt_before))
print("    out: q1_40={0}, q62_0={1}, q63_0={2}".format(q1_40,q62_0,q63_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q63_0 target: q64_0 ##
################################################################################
if 'q63_0' not in globals():
    q63_0=0
if 'q64_0' not in globals():
    q64_0=0

bqm = dimod.BinaryQuadraticModel({'q63_0' : 1, 'q64_0' : 1, 'outq64_0' : 1, 'anc' : 4}, {('q63_0', 'q64_0') : 2, ('q63_0', 'outq64_0') : -2, ('q64_0', 'outq64_0') : -2, ('q63_0', 'anc') : -4, ('q64_0', 'anc') : -4, ('outq64_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q63_0']==q63_0 and sample['q64_0']==q64_0 and int(energy)==0:
        q63_0=sample['q63_0']
        q64_0=sample['outq64_0']
        tgt_before = sample['q64_0']
        break

print('#' * 80)
print("CNOT operation on q63_0 (control) and q64_0 (target):")
print("    in:  q63_0={0}, q64_0={1}".format(q63_0,tgt_before))
print("    out: q63_0={0}, q64_0={1}".format(q63_0,q64_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_39 control2: q63_0 target: q64_0 ##
################################################################################
if 'q0_39' not in globals():
    q0_39=0
if 'q63_0' not in globals():
    q63_0=0
if 'q64_0' not in globals():
    q64_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq64_0' : 1, 'q64_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq64_0') : 4, ('anc1','q64_0') : -4, ('anc2', 'q0_39') : -2, ('anc2', 'q63_0') : -2, ('anc2', 'outq64_0') : -2, ('anc2', 'q64_0') : 2, ('q0_39', 'q63_0') : 1, ('outq64_0', 'q64_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_39']==q0_39 and sample['q63_0']==q63_0 and sample['q64_0']==q64_0 and int(energy)==0:
        q0_39=sample['q0_39']
        q63_0=sample['q63_0']
        q64_0=sample['outq64_0']
        tgt_before = sample['q64_0']
        break

print('#' * 80)
print("CCNOT operation on q0_39 (control1), q63_0 (control2) and q64_0 (target):")
print("    in:  q0_39={0}, q63_0={1}, q64_0={2}".format(q0_39,q63_0,tgt_before))
print("    out: q0_39={0}, q63_0={1}, q64_0={2}".format(q0_39,q63_0,q64_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_39 control2: q63_0 target: q64_0 ##
################################################################################
if 'q1_39' not in globals():
    q1_39=0
if 'q63_0' not in globals():
    q63_0=0
if 'q64_0' not in globals():
    q64_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq64_0' : 1, 'q64_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq64_0') : 4, ('anc1','q64_0') : -4, ('anc2', 'q1_39') : -2, ('anc2', 'q63_0') : -2, ('anc2', 'outq64_0') : -2, ('anc2', 'q64_0') : 2, ('q1_39', 'q63_0') : 1, ('outq64_0', 'q64_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_39']==q1_39 and sample['q63_0']==q63_0 and sample['q64_0']==q64_0 and int(energy)==0:
        q1_39=sample['q1_39']
        q63_0=sample['q63_0']
        q64_0=sample['outq64_0']
        tgt_before = sample['q64_0']
        break

print('#' * 80)
print("CCNOT operation on q1_39 (control1), q63_0 (control2) and q64_0 (target):")
print("    in:  q1_39={0}, q63_0={1}, q64_0={2}".format(q1_39,q63_0,tgt_before))
print("    out: q1_39={0}, q63_0={1}, q64_0={2}".format(q1_39,q63_0,q64_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q64_0 target: q65_0 ##
################################################################################
if 'q64_0' not in globals():
    q64_0=0
if 'q65_0' not in globals():
    q65_0=0

bqm = dimod.BinaryQuadraticModel({'q64_0' : 1, 'q65_0' : 1, 'outq65_0' : 1, 'anc' : 4}, {('q64_0', 'q65_0') : 2, ('q64_0', 'outq65_0') : -2, ('q65_0', 'outq65_0') : -2, ('q64_0', 'anc') : -4, ('q65_0', 'anc') : -4, ('outq65_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q64_0']==q64_0 and sample['q65_0']==q65_0 and int(energy)==0:
        q64_0=sample['q64_0']
        q65_0=sample['outq65_0']
        tgt_before = sample['q65_0']
        break

print('#' * 80)
print("CNOT operation on q64_0 (control) and q65_0 (target):")
print("    in:  q64_0={0}, q65_0={1}".format(q64_0,tgt_before))
print("    out: q64_0={0}, q65_0={1}".format(q64_0,q65_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_38 control2: q64_0 target: q65_0 ##
################################################################################
if 'q0_38' not in globals():
    q0_38=0
if 'q64_0' not in globals():
    q64_0=0
if 'q65_0' not in globals():
    q65_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq65_0' : 1, 'q65_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq65_0') : 4, ('anc1','q65_0') : -4, ('anc2', 'q0_38') : -2, ('anc2', 'q64_0') : -2, ('anc2', 'outq65_0') : -2, ('anc2', 'q65_0') : 2, ('q0_38', 'q64_0') : 1, ('outq65_0', 'q65_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_38']==q0_38 and sample['q64_0']==q64_0 and sample['q65_0']==q65_0 and int(energy)==0:
        q0_38=sample['q0_38']
        q64_0=sample['q64_0']
        q65_0=sample['outq65_0']
        tgt_before = sample['q65_0']
        break

print('#' * 80)
print("CCNOT operation on q0_38 (control1), q64_0 (control2) and q65_0 (target):")
print("    in:  q0_38={0}, q64_0={1}, q65_0={2}".format(q0_38,q64_0,tgt_before))
print("    out: q0_38={0}, q64_0={1}, q65_0={2}".format(q0_38,q64_0,q65_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_38 control2: q64_0 target: q65_0 ##
################################################################################
if 'q1_38' not in globals():
    q1_38=0
if 'q64_0' not in globals():
    q64_0=0
if 'q65_0' not in globals():
    q65_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq65_0' : 1, 'q65_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq65_0') : 4, ('anc1','q65_0') : -4, ('anc2', 'q1_38') : -2, ('anc2', 'q64_0') : -2, ('anc2', 'outq65_0') : -2, ('anc2', 'q65_0') : 2, ('q1_38', 'q64_0') : 1, ('outq65_0', 'q65_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_38']==q1_38 and sample['q64_0']==q64_0 and sample['q65_0']==q65_0 and int(energy)==0:
        q1_38=sample['q1_38']
        q64_0=sample['q64_0']
        q65_0=sample['outq65_0']
        tgt_before = sample['q65_0']
        break

print('#' * 80)
print("CCNOT operation on q1_38 (control1), q64_0 (control2) and q65_0 (target):")
print("    in:  q1_38={0}, q64_0={1}, q65_0={2}".format(q1_38,q64_0,tgt_before))
print("    out: q1_38={0}, q64_0={1}, q65_0={2}".format(q1_38,q64_0,q65_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q65_0 target: q66_0 ##
################################################################################
if 'q65_0' not in globals():
    q65_0=0
if 'q66_0' not in globals():
    q66_0=0

bqm = dimod.BinaryQuadraticModel({'q65_0' : 1, 'q66_0' : 1, 'outq66_0' : 1, 'anc' : 4}, {('q65_0', 'q66_0') : 2, ('q65_0', 'outq66_0') : -2, ('q66_0', 'outq66_0') : -2, ('q65_0', 'anc') : -4, ('q66_0', 'anc') : -4, ('outq66_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q65_0']==q65_0 and sample['q66_0']==q66_0 and int(energy)==0:
        q65_0=sample['q65_0']
        q66_0=sample['outq66_0']
        tgt_before = sample['q66_0']
        break

print('#' * 80)
print("CNOT operation on q65_0 (control) and q66_0 (target):")
print("    in:  q65_0={0}, q66_0={1}".format(q65_0,tgt_before))
print("    out: q65_0={0}, q66_0={1}".format(q65_0,q66_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_37 control2: q65_0 target: q66_0 ##
################################################################################
if 'q0_37' not in globals():
    q0_37=0
if 'q65_0' not in globals():
    q65_0=0
if 'q66_0' not in globals():
    q66_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq66_0' : 1, 'q66_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq66_0') : 4, ('anc1','q66_0') : -4, ('anc2', 'q0_37') : -2, ('anc2', 'q65_0') : -2, ('anc2', 'outq66_0') : -2, ('anc2', 'q66_0') : 2, ('q0_37', 'q65_0') : 1, ('outq66_0', 'q66_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_37']==q0_37 and sample['q65_0']==q65_0 and sample['q66_0']==q66_0 and int(energy)==0:
        q0_37=sample['q0_37']
        q65_0=sample['q65_0']
        q66_0=sample['outq66_0']
        tgt_before = sample['q66_0']
        break

print('#' * 80)
print("CCNOT operation on q0_37 (control1), q65_0 (control2) and q66_0 (target):")
print("    in:  q0_37={0}, q65_0={1}, q66_0={2}".format(q0_37,q65_0,tgt_before))
print("    out: q0_37={0}, q65_0={1}, q66_0={2}".format(q0_37,q65_0,q66_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_37 control2: q65_0 target: q66_0 ##
################################################################################
if 'q1_37' not in globals():
    q1_37=0
if 'q65_0' not in globals():
    q65_0=0
if 'q66_0' not in globals():
    q66_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq66_0' : 1, 'q66_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq66_0') : 4, ('anc1','q66_0') : -4, ('anc2', 'q1_37') : -2, ('anc2', 'q65_0') : -2, ('anc2', 'outq66_0') : -2, ('anc2', 'q66_0') : 2, ('q1_37', 'q65_0') : 1, ('outq66_0', 'q66_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_37']==q1_37 and sample['q65_0']==q65_0 and sample['q66_0']==q66_0 and int(energy)==0:
        q1_37=sample['q1_37']
        q65_0=sample['q65_0']
        q66_0=sample['outq66_0']
        tgt_before = sample['q66_0']
        break

print('#' * 80)
print("CCNOT operation on q1_37 (control1), q65_0 (control2) and q66_0 (target):")
print("    in:  q1_37={0}, q65_0={1}, q66_0={2}".format(q1_37,q65_0,tgt_before))
print("    out: q1_37={0}, q65_0={1}, q66_0={2}".format(q1_37,q65_0,q66_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q66_0 target: q67_0 ##
################################################################################
if 'q66_0' not in globals():
    q66_0=0
if 'q67_0' not in globals():
    q67_0=0

bqm = dimod.BinaryQuadraticModel({'q66_0' : 1, 'q67_0' : 1, 'outq67_0' : 1, 'anc' : 4}, {('q66_0', 'q67_0') : 2, ('q66_0', 'outq67_0') : -2, ('q67_0', 'outq67_0') : -2, ('q66_0', 'anc') : -4, ('q67_0', 'anc') : -4, ('outq67_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q66_0']==q66_0 and sample['q67_0']==q67_0 and int(energy)==0:
        q66_0=sample['q66_0']
        q67_0=sample['outq67_0']
        tgt_before = sample['q67_0']
        break

print('#' * 80)
print("CNOT operation on q66_0 (control) and q67_0 (target):")
print("    in:  q66_0={0}, q67_0={1}".format(q66_0,tgt_before))
print("    out: q66_0={0}, q67_0={1}".format(q66_0,q67_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_36 control2: q66_0 target: q67_0 ##
################################################################################
if 'q0_36' not in globals():
    q0_36=0
if 'q66_0' not in globals():
    q66_0=0
if 'q67_0' not in globals():
    q67_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq67_0' : 1, 'q67_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq67_0') : 4, ('anc1','q67_0') : -4, ('anc2', 'q0_36') : -2, ('anc2', 'q66_0') : -2, ('anc2', 'outq67_0') : -2, ('anc2', 'q67_0') : 2, ('q0_36', 'q66_0') : 1, ('outq67_0', 'q67_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_36']==q0_36 and sample['q66_0']==q66_0 and sample['q67_0']==q67_0 and int(energy)==0:
        q0_36=sample['q0_36']
        q66_0=sample['q66_0']
        q67_0=sample['outq67_0']
        tgt_before = sample['q67_0']
        break

print('#' * 80)
print("CCNOT operation on q0_36 (control1), q66_0 (control2) and q67_0 (target):")
print("    in:  q0_36={0}, q66_0={1}, q67_0={2}".format(q0_36,q66_0,tgt_before))
print("    out: q0_36={0}, q66_0={1}, q67_0={2}".format(q0_36,q66_0,q67_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_36 control2: q66_0 target: q67_0 ##
################################################################################
if 'q1_36' not in globals():
    q1_36=0
if 'q66_0' not in globals():
    q66_0=0
if 'q67_0' not in globals():
    q67_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq67_0' : 1, 'q67_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq67_0') : 4, ('anc1','q67_0') : -4, ('anc2', 'q1_36') : -2, ('anc2', 'q66_0') : -2, ('anc2', 'outq67_0') : -2, ('anc2', 'q67_0') : 2, ('q1_36', 'q66_0') : 1, ('outq67_0', 'q67_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_36']==q1_36 and sample['q66_0']==q66_0 and sample['q67_0']==q67_0 and int(energy)==0:
        q1_36=sample['q1_36']
        q66_0=sample['q66_0']
        q67_0=sample['outq67_0']
        tgt_before = sample['q67_0']
        break

print('#' * 80)
print("CCNOT operation on q1_36 (control1), q66_0 (control2) and q67_0 (target):")
print("    in:  q1_36={0}, q66_0={1}, q67_0={2}".format(q1_36,q66_0,tgt_before))
print("    out: q1_36={0}, q66_0={1}, q67_0={2}".format(q1_36,q66_0,q67_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q67_0 target: q68_0 ##
################################################################################
if 'q67_0' not in globals():
    q67_0=0
if 'q68_0' not in globals():
    q68_0=0

bqm = dimod.BinaryQuadraticModel({'q67_0' : 1, 'q68_0' : 1, 'outq68_0' : 1, 'anc' : 4}, {('q67_0', 'q68_0') : 2, ('q67_0', 'outq68_0') : -2, ('q68_0', 'outq68_0') : -2, ('q67_0', 'anc') : -4, ('q68_0', 'anc') : -4, ('outq68_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q67_0']==q67_0 and sample['q68_0']==q68_0 and int(energy)==0:
        q67_0=sample['q67_0']
        q68_0=sample['outq68_0']
        tgt_before = sample['q68_0']
        break

print('#' * 80)
print("CNOT operation on q67_0 (control) and q68_0 (target):")
print("    in:  q67_0={0}, q68_0={1}".format(q67_0,tgt_before))
print("    out: q67_0={0}, q68_0={1}".format(q67_0,q68_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_35 control2: q67_0 target: q68_0 ##
################################################################################
if 'q0_35' not in globals():
    q0_35=0
if 'q67_0' not in globals():
    q67_0=0
if 'q68_0' not in globals():
    q68_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq68_0' : 1, 'q68_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq68_0') : 4, ('anc1','q68_0') : -4, ('anc2', 'q0_35') : -2, ('anc2', 'q67_0') : -2, ('anc2', 'outq68_0') : -2, ('anc2', 'q68_0') : 2, ('q0_35', 'q67_0') : 1, ('outq68_0', 'q68_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_35']==q0_35 and sample['q67_0']==q67_0 and sample['q68_0']==q68_0 and int(energy)==0:
        q0_35=sample['q0_35']
        q67_0=sample['q67_0']
        q68_0=sample['outq68_0']
        tgt_before = sample['q68_0']
        break

print('#' * 80)
print("CCNOT operation on q0_35 (control1), q67_0 (control2) and q68_0 (target):")
print("    in:  q0_35={0}, q67_0={1}, q68_0={2}".format(q0_35,q67_0,tgt_before))
print("    out: q0_35={0}, q67_0={1}, q68_0={2}".format(q0_35,q67_0,q68_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_35 control2: q67_0 target: q68_0 ##
################################################################################
if 'q1_35' not in globals():
    q1_35=0
if 'q67_0' not in globals():
    q67_0=0
if 'q68_0' not in globals():
    q68_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq68_0' : 1, 'q68_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq68_0') : 4, ('anc1','q68_0') : -4, ('anc2', 'q1_35') : -2, ('anc2', 'q67_0') : -2, ('anc2', 'outq68_0') : -2, ('anc2', 'q68_0') : 2, ('q1_35', 'q67_0') : 1, ('outq68_0', 'q68_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_35']==q1_35 and sample['q67_0']==q67_0 and sample['q68_0']==q68_0 and int(energy)==0:
        q1_35=sample['q1_35']
        q67_0=sample['q67_0']
        q68_0=sample['outq68_0']
        tgt_before = sample['q68_0']
        break

print('#' * 80)
print("CCNOT operation on q1_35 (control1), q67_0 (control2) and q68_0 (target):")
print("    in:  q1_35={0}, q67_0={1}, q68_0={2}".format(q1_35,q67_0,tgt_before))
print("    out: q1_35={0}, q67_0={1}, q68_0={2}".format(q1_35,q67_0,q68_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q68_0 target: q69_0 ##
################################################################################
if 'q68_0' not in globals():
    q68_0=0
if 'q69_0' not in globals():
    q69_0=0

bqm = dimod.BinaryQuadraticModel({'q68_0' : 1, 'q69_0' : 1, 'outq69_0' : 1, 'anc' : 4}, {('q68_0', 'q69_0') : 2, ('q68_0', 'outq69_0') : -2, ('q69_0', 'outq69_0') : -2, ('q68_0', 'anc') : -4, ('q69_0', 'anc') : -4, ('outq69_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q68_0']==q68_0 and sample['q69_0']==q69_0 and int(energy)==0:
        q68_0=sample['q68_0']
        q69_0=sample['outq69_0']
        tgt_before = sample['q69_0']
        break

print('#' * 80)
print("CNOT operation on q68_0 (control) and q69_0 (target):")
print("    in:  q68_0={0}, q69_0={1}".format(q68_0,tgt_before))
print("    out: q68_0={0}, q69_0={1}".format(q68_0,q69_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_34 control2: q68_0 target: q69_0 ##
################################################################################
if 'q0_34' not in globals():
    q0_34=0
if 'q68_0' not in globals():
    q68_0=0
if 'q69_0' not in globals():
    q69_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq69_0' : 1, 'q69_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq69_0') : 4, ('anc1','q69_0') : -4, ('anc2', 'q0_34') : -2, ('anc2', 'q68_0') : -2, ('anc2', 'outq69_0') : -2, ('anc2', 'q69_0') : 2, ('q0_34', 'q68_0') : 1, ('outq69_0', 'q69_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_34']==q0_34 and sample['q68_0']==q68_0 and sample['q69_0']==q69_0 and int(energy)==0:
        q0_34=sample['q0_34']
        q68_0=sample['q68_0']
        q69_0=sample['outq69_0']
        tgt_before = sample['q69_0']
        break

print('#' * 80)
print("CCNOT operation on q0_34 (control1), q68_0 (control2) and q69_0 (target):")
print("    in:  q0_34={0}, q68_0={1}, q69_0={2}".format(q0_34,q68_0,tgt_before))
print("    out: q0_34={0}, q68_0={1}, q69_0={2}".format(q0_34,q68_0,q69_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_34 control2: q68_0 target: q69_0 ##
################################################################################
if 'q1_34' not in globals():
    q1_34=0
if 'q68_0' not in globals():
    q68_0=0
if 'q69_0' not in globals():
    q69_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq69_0' : 1, 'q69_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq69_0') : 4, ('anc1','q69_0') : -4, ('anc2', 'q1_34') : -2, ('anc2', 'q68_0') : -2, ('anc2', 'outq69_0') : -2, ('anc2', 'q69_0') : 2, ('q1_34', 'q68_0') : 1, ('outq69_0', 'q69_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_34']==q1_34 and sample['q68_0']==q68_0 and sample['q69_0']==q69_0 and int(energy)==0:
        q1_34=sample['q1_34']
        q68_0=sample['q68_0']
        q69_0=sample['outq69_0']
        tgt_before = sample['q69_0']
        break

print('#' * 80)
print("CCNOT operation on q1_34 (control1), q68_0 (control2) and q69_0 (target):")
print("    in:  q1_34={0}, q68_0={1}, q69_0={2}".format(q1_34,q68_0,tgt_before))
print("    out: q1_34={0}, q68_0={1}, q69_0={2}".format(q1_34,q68_0,q69_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q69_0 target: q70_0 ##
################################################################################
if 'q69_0' not in globals():
    q69_0=0
if 'q70_0' not in globals():
    q70_0=0

bqm = dimod.BinaryQuadraticModel({'q69_0' : 1, 'q70_0' : 1, 'outq70_0' : 1, 'anc' : 4}, {('q69_0', 'q70_0') : 2, ('q69_0', 'outq70_0') : -2, ('q70_0', 'outq70_0') : -2, ('q69_0', 'anc') : -4, ('q70_0', 'anc') : -4, ('outq70_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q69_0']==q69_0 and sample['q70_0']==q70_0 and int(energy)==0:
        q69_0=sample['q69_0']
        q70_0=sample['outq70_0']
        tgt_before = sample['q70_0']
        break

print('#' * 80)
print("CNOT operation on q69_0 (control) and q70_0 (target):")
print("    in:  q69_0={0}, q70_0={1}".format(q69_0,tgt_before))
print("    out: q69_0={0}, q70_0={1}".format(q69_0,q70_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_33 control2: q69_0 target: q70_0 ##
################################################################################
if 'q0_33' not in globals():
    q0_33=0
if 'q69_0' not in globals():
    q69_0=0
if 'q70_0' not in globals():
    q70_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq70_0' : 1, 'q70_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq70_0') : 4, ('anc1','q70_0') : -4, ('anc2', 'q0_33') : -2, ('anc2', 'q69_0') : -2, ('anc2', 'outq70_0') : -2, ('anc2', 'q70_0') : 2, ('q0_33', 'q69_0') : 1, ('outq70_0', 'q70_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_33']==q0_33 and sample['q69_0']==q69_0 and sample['q70_0']==q70_0 and int(energy)==0:
        q0_33=sample['q0_33']
        q69_0=sample['q69_0']
        q70_0=sample['outq70_0']
        tgt_before = sample['q70_0']
        break

print('#' * 80)
print("CCNOT operation on q0_33 (control1), q69_0 (control2) and q70_0 (target):")
print("    in:  q0_33={0}, q69_0={1}, q70_0={2}".format(q0_33,q69_0,tgt_before))
print("    out: q0_33={0}, q69_0={1}, q70_0={2}".format(q0_33,q69_0,q70_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_33 control2: q69_0 target: q70_0 ##
################################################################################
if 'q1_33' not in globals():
    q1_33=0
if 'q69_0' not in globals():
    q69_0=0
if 'q70_0' not in globals():
    q70_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq70_0' : 1, 'q70_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq70_0') : 4, ('anc1','q70_0') : -4, ('anc2', 'q1_33') : -2, ('anc2', 'q69_0') : -2, ('anc2', 'outq70_0') : -2, ('anc2', 'q70_0') : 2, ('q1_33', 'q69_0') : 1, ('outq70_0', 'q70_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_33']==q1_33 and sample['q69_0']==q69_0 and sample['q70_0']==q70_0 and int(energy)==0:
        q1_33=sample['q1_33']
        q69_0=sample['q69_0']
        q70_0=sample['outq70_0']
        tgt_before = sample['q70_0']
        break

print('#' * 80)
print("CCNOT operation on q1_33 (control1), q69_0 (control2) and q70_0 (target):")
print("    in:  q1_33={0}, q69_0={1}, q70_0={2}".format(q1_33,q69_0,tgt_before))
print("    out: q1_33={0}, q69_0={1}, q70_0={2}".format(q1_33,q69_0,q70_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q70_0 target: q71_0 ##
################################################################################
if 'q70_0' not in globals():
    q70_0=0
if 'q71_0' not in globals():
    q71_0=0

bqm = dimod.BinaryQuadraticModel({'q70_0' : 1, 'q71_0' : 1, 'outq71_0' : 1, 'anc' : 4}, {('q70_0', 'q71_0') : 2, ('q70_0', 'outq71_0') : -2, ('q71_0', 'outq71_0') : -2, ('q70_0', 'anc') : -4, ('q71_0', 'anc') : -4, ('outq71_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q70_0']==q70_0 and sample['q71_0']==q71_0 and int(energy)==0:
        q70_0=sample['q70_0']
        q71_0=sample['outq71_0']
        tgt_before = sample['q71_0']
        break

print('#' * 80)
print("CNOT operation on q70_0 (control) and q71_0 (target):")
print("    in:  q70_0={0}, q71_0={1}".format(q70_0,tgt_before))
print("    out: q70_0={0}, q71_0={1}".format(q70_0,q71_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_32 control2: q70_0 target: q71_0 ##
################################################################################
if 'q0_32' not in globals():
    q0_32=0
if 'q70_0' not in globals():
    q70_0=0
if 'q71_0' not in globals():
    q71_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq71_0' : 1, 'q71_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq71_0') : 4, ('anc1','q71_0') : -4, ('anc2', 'q0_32') : -2, ('anc2', 'q70_0') : -2, ('anc2', 'outq71_0') : -2, ('anc2', 'q71_0') : 2, ('q0_32', 'q70_0') : 1, ('outq71_0', 'q71_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_32']==q0_32 and sample['q70_0']==q70_0 and sample['q71_0']==q71_0 and int(energy)==0:
        q0_32=sample['q0_32']
        q70_0=sample['q70_0']
        q71_0=sample['outq71_0']
        tgt_before = sample['q71_0']
        break

print('#' * 80)
print("CCNOT operation on q0_32 (control1), q70_0 (control2) and q71_0 (target):")
print("    in:  q0_32={0}, q70_0={1}, q71_0={2}".format(q0_32,q70_0,tgt_before))
print("    out: q0_32={0}, q70_0={1}, q71_0={2}".format(q0_32,q70_0,q71_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_32 control2: q70_0 target: q71_0 ##
################################################################################
if 'q1_32' not in globals():
    q1_32=0
if 'q70_0' not in globals():
    q70_0=0
if 'q71_0' not in globals():
    q71_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq71_0' : 1, 'q71_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq71_0') : 4, ('anc1','q71_0') : -4, ('anc2', 'q1_32') : -2, ('anc2', 'q70_0') : -2, ('anc2', 'outq71_0') : -2, ('anc2', 'q71_0') : 2, ('q1_32', 'q70_0') : 1, ('outq71_0', 'q71_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_32']==q1_32 and sample['q70_0']==q70_0 and sample['q71_0']==q71_0 and int(energy)==0:
        q1_32=sample['q1_32']
        q70_0=sample['q70_0']
        q71_0=sample['outq71_0']
        tgt_before = sample['q71_0']
        break

print('#' * 80)
print("CCNOT operation on q1_32 (control1), q70_0 (control2) and q71_0 (target):")
print("    in:  q1_32={0}, q70_0={1}, q71_0={2}".format(q1_32,q70_0,tgt_before))
print("    out: q1_32={0}, q70_0={1}, q71_0={2}".format(q1_32,q70_0,q71_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q71_0 target: q72_0 ##
################################################################################
if 'q71_0' not in globals():
    q71_0=0
if 'q72_0' not in globals():
    q72_0=0

bqm = dimod.BinaryQuadraticModel({'q71_0' : 1, 'q72_0' : 1, 'outq72_0' : 1, 'anc' : 4}, {('q71_0', 'q72_0') : 2, ('q71_0', 'outq72_0') : -2, ('q72_0', 'outq72_0') : -2, ('q71_0', 'anc') : -4, ('q72_0', 'anc') : -4, ('outq72_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q71_0']==q71_0 and sample['q72_0']==q72_0 and int(energy)==0:
        q71_0=sample['q71_0']
        q72_0=sample['outq72_0']
        tgt_before = sample['q72_0']
        break

print('#' * 80)
print("CNOT operation on q71_0 (control) and q72_0 (target):")
print("    in:  q71_0={0}, q72_0={1}".format(q71_0,tgt_before))
print("    out: q71_0={0}, q72_0={1}".format(q71_0,q72_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_31 control2: q71_0 target: q72_0 ##
################################################################################
if 'q0_31' not in globals():
    q0_31=0
if 'q71_0' not in globals():
    q71_0=0
if 'q72_0' not in globals():
    q72_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq72_0' : 1, 'q72_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq72_0') : 4, ('anc1','q72_0') : -4, ('anc2', 'q0_31') : -2, ('anc2', 'q71_0') : -2, ('anc2', 'outq72_0') : -2, ('anc2', 'q72_0') : 2, ('q0_31', 'q71_0') : 1, ('outq72_0', 'q72_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_31']==q0_31 and sample['q71_0']==q71_0 and sample['q72_0']==q72_0 and int(energy)==0:
        q0_31=sample['q0_31']
        q71_0=sample['q71_0']
        q72_0=sample['outq72_0']
        tgt_before = sample['q72_0']
        break

print('#' * 80)
print("CCNOT operation on q0_31 (control1), q71_0 (control2) and q72_0 (target):")
print("    in:  q0_31={0}, q71_0={1}, q72_0={2}".format(q0_31,q71_0,tgt_before))
print("    out: q0_31={0}, q71_0={1}, q72_0={2}".format(q0_31,q71_0,q72_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_31 control2: q71_0 target: q72_0 ##
################################################################################
if 'q1_31' not in globals():
    q1_31=0
if 'q71_0' not in globals():
    q71_0=0
if 'q72_0' not in globals():
    q72_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq72_0' : 1, 'q72_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq72_0') : 4, ('anc1','q72_0') : -4, ('anc2', 'q1_31') : -2, ('anc2', 'q71_0') : -2, ('anc2', 'outq72_0') : -2, ('anc2', 'q72_0') : 2, ('q1_31', 'q71_0') : 1, ('outq72_0', 'q72_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_31']==q1_31 and sample['q71_0']==q71_0 and sample['q72_0']==q72_0 and int(energy)==0:
        q1_31=sample['q1_31']
        q71_0=sample['q71_0']
        q72_0=sample['outq72_0']
        tgt_before = sample['q72_0']
        break

print('#' * 80)
print("CCNOT operation on q1_31 (control1), q71_0 (control2) and q72_0 (target):")
print("    in:  q1_31={0}, q71_0={1}, q72_0={2}".format(q1_31,q71_0,tgt_before))
print("    out: q1_31={0}, q71_0={1}, q72_0={2}".format(q1_31,q71_0,q72_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q72_0 target: q73_0 ##
################################################################################
if 'q72_0' not in globals():
    q72_0=0
if 'q73_0' not in globals():
    q73_0=0

bqm = dimod.BinaryQuadraticModel({'q72_0' : 1, 'q73_0' : 1, 'outq73_0' : 1, 'anc' : 4}, {('q72_0', 'q73_0') : 2, ('q72_0', 'outq73_0') : -2, ('q73_0', 'outq73_0') : -2, ('q72_0', 'anc') : -4, ('q73_0', 'anc') : -4, ('outq73_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q72_0']==q72_0 and sample['q73_0']==q73_0 and int(energy)==0:
        q72_0=sample['q72_0']
        q73_0=sample['outq73_0']
        tgt_before = sample['q73_0']
        break

print('#' * 80)
print("CNOT operation on q72_0 (control) and q73_0 (target):")
print("    in:  q72_0={0}, q73_0={1}".format(q72_0,tgt_before))
print("    out: q72_0={0}, q73_0={1}".format(q72_0,q73_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_30 control2: q72_0 target: q73_0 ##
################################################################################
if 'q0_30' not in globals():
    q0_30=0
if 'q72_0' not in globals():
    q72_0=0
if 'q73_0' not in globals():
    q73_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq73_0' : 1, 'q73_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq73_0') : 4, ('anc1','q73_0') : -4, ('anc2', 'q0_30') : -2, ('anc2', 'q72_0') : -2, ('anc2', 'outq73_0') : -2, ('anc2', 'q73_0') : 2, ('q0_30', 'q72_0') : 1, ('outq73_0', 'q73_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_30']==q0_30 and sample['q72_0']==q72_0 and sample['q73_0']==q73_0 and int(energy)==0:
        q0_30=sample['q0_30']
        q72_0=sample['q72_0']
        q73_0=sample['outq73_0']
        tgt_before = sample['q73_0']
        break

print('#' * 80)
print("CCNOT operation on q0_30 (control1), q72_0 (control2) and q73_0 (target):")
print("    in:  q0_30={0}, q72_0={1}, q73_0={2}".format(q0_30,q72_0,tgt_before))
print("    out: q0_30={0}, q72_0={1}, q73_0={2}".format(q0_30,q72_0,q73_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_30 control2: q72_0 target: q73_0 ##
################################################################################
if 'q1_30' not in globals():
    q1_30=0
if 'q72_0' not in globals():
    q72_0=0
if 'q73_0' not in globals():
    q73_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq73_0' : 1, 'q73_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq73_0') : 4, ('anc1','q73_0') : -4, ('anc2', 'q1_30') : -2, ('anc2', 'q72_0') : -2, ('anc2', 'outq73_0') : -2, ('anc2', 'q73_0') : 2, ('q1_30', 'q72_0') : 1, ('outq73_0', 'q73_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_30']==q1_30 and sample['q72_0']==q72_0 and sample['q73_0']==q73_0 and int(energy)==0:
        q1_30=sample['q1_30']
        q72_0=sample['q72_0']
        q73_0=sample['outq73_0']
        tgt_before = sample['q73_0']
        break

print('#' * 80)
print("CCNOT operation on q1_30 (control1), q72_0 (control2) and q73_0 (target):")
print("    in:  q1_30={0}, q72_0={1}, q73_0={2}".format(q1_30,q72_0,tgt_before))
print("    out: q1_30={0}, q72_0={1}, q73_0={2}".format(q1_30,q72_0,q73_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q73_0 target: q74_0 ##
################################################################################
if 'q73_0' not in globals():
    q73_0=0
if 'q74_0' not in globals():
    q74_0=0

bqm = dimod.BinaryQuadraticModel({'q73_0' : 1, 'q74_0' : 1, 'outq74_0' : 1, 'anc' : 4}, {('q73_0', 'q74_0') : 2, ('q73_0', 'outq74_0') : -2, ('q74_0', 'outq74_0') : -2, ('q73_0', 'anc') : -4, ('q74_0', 'anc') : -4, ('outq74_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q73_0']==q73_0 and sample['q74_0']==q74_0 and int(energy)==0:
        q73_0=sample['q73_0']
        q74_0=sample['outq74_0']
        tgt_before = sample['q74_0']
        break

print('#' * 80)
print("CNOT operation on q73_0 (control) and q74_0 (target):")
print("    in:  q73_0={0}, q74_0={1}".format(q73_0,tgt_before))
print("    out: q73_0={0}, q74_0={1}".format(q73_0,q74_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_29 control2: q73_0 target: q74_0 ##
################################################################################
if 'q0_29' not in globals():
    q0_29=0
if 'q73_0' not in globals():
    q73_0=0
if 'q74_0' not in globals():
    q74_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq74_0' : 1, 'q74_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq74_0') : 4, ('anc1','q74_0') : -4, ('anc2', 'q0_29') : -2, ('anc2', 'q73_0') : -2, ('anc2', 'outq74_0') : -2, ('anc2', 'q74_0') : 2, ('q0_29', 'q73_0') : 1, ('outq74_0', 'q74_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_29']==q0_29 and sample['q73_0']==q73_0 and sample['q74_0']==q74_0 and int(energy)==0:
        q0_29=sample['q0_29']
        q73_0=sample['q73_0']
        q74_0=sample['outq74_0']
        tgt_before = sample['q74_0']
        break

print('#' * 80)
print("CCNOT operation on q0_29 (control1), q73_0 (control2) and q74_0 (target):")
print("    in:  q0_29={0}, q73_0={1}, q74_0={2}".format(q0_29,q73_0,tgt_before))
print("    out: q0_29={0}, q73_0={1}, q74_0={2}".format(q0_29,q73_0,q74_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_29 control2: q73_0 target: q74_0 ##
################################################################################
if 'q1_29' not in globals():
    q1_29=0
if 'q73_0' not in globals():
    q73_0=0
if 'q74_0' not in globals():
    q74_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq74_0' : 1, 'q74_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq74_0') : 4, ('anc1','q74_0') : -4, ('anc2', 'q1_29') : -2, ('anc2', 'q73_0') : -2, ('anc2', 'outq74_0') : -2, ('anc2', 'q74_0') : 2, ('q1_29', 'q73_0') : 1, ('outq74_0', 'q74_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_29']==q1_29 and sample['q73_0']==q73_0 and sample['q74_0']==q74_0 and int(energy)==0:
        q1_29=sample['q1_29']
        q73_0=sample['q73_0']
        q74_0=sample['outq74_0']
        tgt_before = sample['q74_0']
        break

print('#' * 80)
print("CCNOT operation on q1_29 (control1), q73_0 (control2) and q74_0 (target):")
print("    in:  q1_29={0}, q73_0={1}, q74_0={2}".format(q1_29,q73_0,tgt_before))
print("    out: q1_29={0}, q73_0={1}, q74_0={2}".format(q1_29,q73_0,q74_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q74_0 target: q75_0 ##
################################################################################
if 'q74_0' not in globals():
    q74_0=0
if 'q75_0' not in globals():
    q75_0=0

bqm = dimod.BinaryQuadraticModel({'q74_0' : 1, 'q75_0' : 1, 'outq75_0' : 1, 'anc' : 4}, {('q74_0', 'q75_0') : 2, ('q74_0', 'outq75_0') : -2, ('q75_0', 'outq75_0') : -2, ('q74_0', 'anc') : -4, ('q75_0', 'anc') : -4, ('outq75_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q74_0']==q74_0 and sample['q75_0']==q75_0 and int(energy)==0:
        q74_0=sample['q74_0']
        q75_0=sample['outq75_0']
        tgt_before = sample['q75_0']
        break

print('#' * 80)
print("CNOT operation on q74_0 (control) and q75_0 (target):")
print("    in:  q74_0={0}, q75_0={1}".format(q74_0,tgt_before))
print("    out: q74_0={0}, q75_0={1}".format(q74_0,q75_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_28 control2: q74_0 target: q75_0 ##
################################################################################
if 'q0_28' not in globals():
    q0_28=0
if 'q74_0' not in globals():
    q74_0=0
if 'q75_0' not in globals():
    q75_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq75_0' : 1, 'q75_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq75_0') : 4, ('anc1','q75_0') : -4, ('anc2', 'q0_28') : -2, ('anc2', 'q74_0') : -2, ('anc2', 'outq75_0') : -2, ('anc2', 'q75_0') : 2, ('q0_28', 'q74_0') : 1, ('outq75_0', 'q75_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_28']==q0_28 and sample['q74_0']==q74_0 and sample['q75_0']==q75_0 and int(energy)==0:
        q0_28=sample['q0_28']
        q74_0=sample['q74_0']
        q75_0=sample['outq75_0']
        tgt_before = sample['q75_0']
        break

print('#' * 80)
print("CCNOT operation on q0_28 (control1), q74_0 (control2) and q75_0 (target):")
print("    in:  q0_28={0}, q74_0={1}, q75_0={2}".format(q0_28,q74_0,tgt_before))
print("    out: q0_28={0}, q74_0={1}, q75_0={2}".format(q0_28,q74_0,q75_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_28 control2: q74_0 target: q75_0 ##
################################################################################
if 'q1_28' not in globals():
    q1_28=0
if 'q74_0' not in globals():
    q74_0=0
if 'q75_0' not in globals():
    q75_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq75_0' : 1, 'q75_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq75_0') : 4, ('anc1','q75_0') : -4, ('anc2', 'q1_28') : -2, ('anc2', 'q74_0') : -2, ('anc2', 'outq75_0') : -2, ('anc2', 'q75_0') : 2, ('q1_28', 'q74_0') : 1, ('outq75_0', 'q75_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_28']==q1_28 and sample['q74_0']==q74_0 and sample['q75_0']==q75_0 and int(energy)==0:
        q1_28=sample['q1_28']
        q74_0=sample['q74_0']
        q75_0=sample['outq75_0']
        tgt_before = sample['q75_0']
        break

print('#' * 80)
print("CCNOT operation on q1_28 (control1), q74_0 (control2) and q75_0 (target):")
print("    in:  q1_28={0}, q74_0={1}, q75_0={2}".format(q1_28,q74_0,tgt_before))
print("    out: q1_28={0}, q74_0={1}, q75_0={2}".format(q1_28,q74_0,q75_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q75_0 target: q76_0 ##
################################################################################
if 'q75_0' not in globals():
    q75_0=0
if 'q76_0' not in globals():
    q76_0=0

bqm = dimod.BinaryQuadraticModel({'q75_0' : 1, 'q76_0' : 1, 'outq76_0' : 1, 'anc' : 4}, {('q75_0', 'q76_0') : 2, ('q75_0', 'outq76_0') : -2, ('q76_0', 'outq76_0') : -2, ('q75_0', 'anc') : -4, ('q76_0', 'anc') : -4, ('outq76_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q75_0']==q75_0 and sample['q76_0']==q76_0 and int(energy)==0:
        q75_0=sample['q75_0']
        q76_0=sample['outq76_0']
        tgt_before = sample['q76_0']
        break

print('#' * 80)
print("CNOT operation on q75_0 (control) and q76_0 (target):")
print("    in:  q75_0={0}, q76_0={1}".format(q75_0,tgt_before))
print("    out: q75_0={0}, q76_0={1}".format(q75_0,q76_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_27 control2: q75_0 target: q76_0 ##
################################################################################
if 'q0_27' not in globals():
    q0_27=0
if 'q75_0' not in globals():
    q75_0=0
if 'q76_0' not in globals():
    q76_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq76_0' : 1, 'q76_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq76_0') : 4, ('anc1','q76_0') : -4, ('anc2', 'q0_27') : -2, ('anc2', 'q75_0') : -2, ('anc2', 'outq76_0') : -2, ('anc2', 'q76_0') : 2, ('q0_27', 'q75_0') : 1, ('outq76_0', 'q76_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_27']==q0_27 and sample['q75_0']==q75_0 and sample['q76_0']==q76_0 and int(energy)==0:
        q0_27=sample['q0_27']
        q75_0=sample['q75_0']
        q76_0=sample['outq76_0']
        tgt_before = sample['q76_0']
        break

print('#' * 80)
print("CCNOT operation on q0_27 (control1), q75_0 (control2) and q76_0 (target):")
print("    in:  q0_27={0}, q75_0={1}, q76_0={2}".format(q0_27,q75_0,tgt_before))
print("    out: q0_27={0}, q75_0={1}, q76_0={2}".format(q0_27,q75_0,q76_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_27 control2: q75_0 target: q76_0 ##
################################################################################
if 'q1_27' not in globals():
    q1_27=0
if 'q75_0' not in globals():
    q75_0=0
if 'q76_0' not in globals():
    q76_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq76_0' : 1, 'q76_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq76_0') : 4, ('anc1','q76_0') : -4, ('anc2', 'q1_27') : -2, ('anc2', 'q75_0') : -2, ('anc2', 'outq76_0') : -2, ('anc2', 'q76_0') : 2, ('q1_27', 'q75_0') : 1, ('outq76_0', 'q76_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_27']==q1_27 and sample['q75_0']==q75_0 and sample['q76_0']==q76_0 and int(energy)==0:
        q1_27=sample['q1_27']
        q75_0=sample['q75_0']
        q76_0=sample['outq76_0']
        tgt_before = sample['q76_0']
        break

print('#' * 80)
print("CCNOT operation on q1_27 (control1), q75_0 (control2) and q76_0 (target):")
print("    in:  q1_27={0}, q75_0={1}, q76_0={2}".format(q1_27,q75_0,tgt_before))
print("    out: q1_27={0}, q75_0={1}, q76_0={2}".format(q1_27,q75_0,q76_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q76_0 target: q77_0 ##
################################################################################
if 'q76_0' not in globals():
    q76_0=0
if 'q77_0' not in globals():
    q77_0=0

bqm = dimod.BinaryQuadraticModel({'q76_0' : 1, 'q77_0' : 1, 'outq77_0' : 1, 'anc' : 4}, {('q76_0', 'q77_0') : 2, ('q76_0', 'outq77_0') : -2, ('q77_0', 'outq77_0') : -2, ('q76_0', 'anc') : -4, ('q77_0', 'anc') : -4, ('outq77_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q76_0']==q76_0 and sample['q77_0']==q77_0 and int(energy)==0:
        q76_0=sample['q76_0']
        q77_0=sample['outq77_0']
        tgt_before = sample['q77_0']
        break

print('#' * 80)
print("CNOT operation on q76_0 (control) and q77_0 (target):")
print("    in:  q76_0={0}, q77_0={1}".format(q76_0,tgt_before))
print("    out: q76_0={0}, q77_0={1}".format(q76_0,q77_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_26 control2: q76_0 target: q77_0 ##
################################################################################
if 'q0_26' not in globals():
    q0_26=0
if 'q76_0' not in globals():
    q76_0=0
if 'q77_0' not in globals():
    q77_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq77_0' : 1, 'q77_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq77_0') : 4, ('anc1','q77_0') : -4, ('anc2', 'q0_26') : -2, ('anc2', 'q76_0') : -2, ('anc2', 'outq77_0') : -2, ('anc2', 'q77_0') : 2, ('q0_26', 'q76_0') : 1, ('outq77_0', 'q77_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_26']==q0_26 and sample['q76_0']==q76_0 and sample['q77_0']==q77_0 and int(energy)==0:
        q0_26=sample['q0_26']
        q76_0=sample['q76_0']
        q77_0=sample['outq77_0']
        tgt_before = sample['q77_0']
        break

print('#' * 80)
print("CCNOT operation on q0_26 (control1), q76_0 (control2) and q77_0 (target):")
print("    in:  q0_26={0}, q76_0={1}, q77_0={2}".format(q0_26,q76_0,tgt_before))
print("    out: q0_26={0}, q76_0={1}, q77_0={2}".format(q0_26,q76_0,q77_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_26 control2: q76_0 target: q77_0 ##
################################################################################
if 'q1_26' not in globals():
    q1_26=0
if 'q76_0' not in globals():
    q76_0=0
if 'q77_0' not in globals():
    q77_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq77_0' : 1, 'q77_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq77_0') : 4, ('anc1','q77_0') : -4, ('anc2', 'q1_26') : -2, ('anc2', 'q76_0') : -2, ('anc2', 'outq77_0') : -2, ('anc2', 'q77_0') : 2, ('q1_26', 'q76_0') : 1, ('outq77_0', 'q77_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_26']==q1_26 and sample['q76_0']==q76_0 and sample['q77_0']==q77_0 and int(energy)==0:
        q1_26=sample['q1_26']
        q76_0=sample['q76_0']
        q77_0=sample['outq77_0']
        tgt_before = sample['q77_0']
        break

print('#' * 80)
print("CCNOT operation on q1_26 (control1), q76_0 (control2) and q77_0 (target):")
print("    in:  q1_26={0}, q76_0={1}, q77_0={2}".format(q1_26,q76_0,tgt_before))
print("    out: q1_26={0}, q76_0={1}, q77_0={2}".format(q1_26,q76_0,q77_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q77_0 target: q78_0 ##
################################################################################
if 'q77_0' not in globals():
    q77_0=0
if 'q78_0' not in globals():
    q78_0=0

bqm = dimod.BinaryQuadraticModel({'q77_0' : 1, 'q78_0' : 1, 'outq78_0' : 1, 'anc' : 4}, {('q77_0', 'q78_0') : 2, ('q77_0', 'outq78_0') : -2, ('q78_0', 'outq78_0') : -2, ('q77_0', 'anc') : -4, ('q78_0', 'anc') : -4, ('outq78_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q77_0']==q77_0 and sample['q78_0']==q78_0 and int(energy)==0:
        q77_0=sample['q77_0']
        q78_0=sample['outq78_0']
        tgt_before = sample['q78_0']
        break

print('#' * 80)
print("CNOT operation on q77_0 (control) and q78_0 (target):")
print("    in:  q77_0={0}, q78_0={1}".format(q77_0,tgt_before))
print("    out: q77_0={0}, q78_0={1}".format(q77_0,q78_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_25 control2: q77_0 target: q78_0 ##
################################################################################
if 'q0_25' not in globals():
    q0_25=0
if 'q77_0' not in globals():
    q77_0=0
if 'q78_0' not in globals():
    q78_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq78_0' : 1, 'q78_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq78_0') : 4, ('anc1','q78_0') : -4, ('anc2', 'q0_25') : -2, ('anc2', 'q77_0') : -2, ('anc2', 'outq78_0') : -2, ('anc2', 'q78_0') : 2, ('q0_25', 'q77_0') : 1, ('outq78_0', 'q78_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_25']==q0_25 and sample['q77_0']==q77_0 and sample['q78_0']==q78_0 and int(energy)==0:
        q0_25=sample['q0_25']
        q77_0=sample['q77_0']
        q78_0=sample['outq78_0']
        tgt_before = sample['q78_0']
        break

print('#' * 80)
print("CCNOT operation on q0_25 (control1), q77_0 (control2) and q78_0 (target):")
print("    in:  q0_25={0}, q77_0={1}, q78_0={2}".format(q0_25,q77_0,tgt_before))
print("    out: q0_25={0}, q77_0={1}, q78_0={2}".format(q0_25,q77_0,q78_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_25 control2: q77_0 target: q78_0 ##
################################################################################
if 'q1_25' not in globals():
    q1_25=0
if 'q77_0' not in globals():
    q77_0=0
if 'q78_0' not in globals():
    q78_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq78_0' : 1, 'q78_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq78_0') : 4, ('anc1','q78_0') : -4, ('anc2', 'q1_25') : -2, ('anc2', 'q77_0') : -2, ('anc2', 'outq78_0') : -2, ('anc2', 'q78_0') : 2, ('q1_25', 'q77_0') : 1, ('outq78_0', 'q78_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_25']==q1_25 and sample['q77_0']==q77_0 and sample['q78_0']==q78_0 and int(energy)==0:
        q1_25=sample['q1_25']
        q77_0=sample['q77_0']
        q78_0=sample['outq78_0']
        tgt_before = sample['q78_0']
        break

print('#' * 80)
print("CCNOT operation on q1_25 (control1), q77_0 (control2) and q78_0 (target):")
print("    in:  q1_25={0}, q77_0={1}, q78_0={2}".format(q1_25,q77_0,tgt_before))
print("    out: q1_25={0}, q77_0={1}, q78_0={2}".format(q1_25,q77_0,q78_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q78_0 target: q79_0 ##
################################################################################
if 'q78_0' not in globals():
    q78_0=0
if 'q79_0' not in globals():
    q79_0=0

bqm = dimod.BinaryQuadraticModel({'q78_0' : 1, 'q79_0' : 1, 'outq79_0' : 1, 'anc' : 4}, {('q78_0', 'q79_0') : 2, ('q78_0', 'outq79_0') : -2, ('q79_0', 'outq79_0') : -2, ('q78_0', 'anc') : -4, ('q79_0', 'anc') : -4, ('outq79_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q78_0']==q78_0 and sample['q79_0']==q79_0 and int(energy)==0:
        q78_0=sample['q78_0']
        q79_0=sample['outq79_0']
        tgt_before = sample['q79_0']
        break

print('#' * 80)
print("CNOT operation on q78_0 (control) and q79_0 (target):")
print("    in:  q78_0={0}, q79_0={1}".format(q78_0,tgt_before))
print("    out: q78_0={0}, q79_0={1}".format(q78_0,q79_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_24 control2: q78_0 target: q79_0 ##
################################################################################
if 'q0_24' not in globals():
    q0_24=0
if 'q78_0' not in globals():
    q78_0=0
if 'q79_0' not in globals():
    q79_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq79_0' : 1, 'q79_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq79_0') : 4, ('anc1','q79_0') : -4, ('anc2', 'q0_24') : -2, ('anc2', 'q78_0') : -2, ('anc2', 'outq79_0') : -2, ('anc2', 'q79_0') : 2, ('q0_24', 'q78_0') : 1, ('outq79_0', 'q79_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_24']==q0_24 and sample['q78_0']==q78_0 and sample['q79_0']==q79_0 and int(energy)==0:
        q0_24=sample['q0_24']
        q78_0=sample['q78_0']
        q79_0=sample['outq79_0']
        tgt_before = sample['q79_0']
        break

print('#' * 80)
print("CCNOT operation on q0_24 (control1), q78_0 (control2) and q79_0 (target):")
print("    in:  q0_24={0}, q78_0={1}, q79_0={2}".format(q0_24,q78_0,tgt_before))
print("    out: q0_24={0}, q78_0={1}, q79_0={2}".format(q0_24,q78_0,q79_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_24 control2: q78_0 target: q79_0 ##
################################################################################
if 'q1_24' not in globals():
    q1_24=0
if 'q78_0' not in globals():
    q78_0=0
if 'q79_0' not in globals():
    q79_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq79_0' : 1, 'q79_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq79_0') : 4, ('anc1','q79_0') : -4, ('anc2', 'q1_24') : -2, ('anc2', 'q78_0') : -2, ('anc2', 'outq79_0') : -2, ('anc2', 'q79_0') : 2, ('q1_24', 'q78_0') : 1, ('outq79_0', 'q79_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_24']==q1_24 and sample['q78_0']==q78_0 and sample['q79_0']==q79_0 and int(energy)==0:
        q1_24=sample['q1_24']
        q78_0=sample['q78_0']
        q79_0=sample['outq79_0']
        tgt_before = sample['q79_0']
        break

print('#' * 80)
print("CCNOT operation on q1_24 (control1), q78_0 (control2) and q79_0 (target):")
print("    in:  q1_24={0}, q78_0={1}, q79_0={2}".format(q1_24,q78_0,tgt_before))
print("    out: q1_24={0}, q78_0={1}, q79_0={2}".format(q1_24,q78_0,q79_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q79_0 target: q80_0 ##
################################################################################
if 'q79_0' not in globals():
    q79_0=0
if 'q80_0' not in globals():
    q80_0=0

bqm = dimod.BinaryQuadraticModel({'q79_0' : 1, 'q80_0' : 1, 'outq80_0' : 1, 'anc' : 4}, {('q79_0', 'q80_0') : 2, ('q79_0', 'outq80_0') : -2, ('q80_0', 'outq80_0') : -2, ('q79_0', 'anc') : -4, ('q80_0', 'anc') : -4, ('outq80_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q79_0']==q79_0 and sample['q80_0']==q80_0 and int(energy)==0:
        q79_0=sample['q79_0']
        q80_0=sample['outq80_0']
        tgt_before = sample['q80_0']
        break

print('#' * 80)
print("CNOT operation on q79_0 (control) and q80_0 (target):")
print("    in:  q79_0={0}, q80_0={1}".format(q79_0,tgt_before))
print("    out: q79_0={0}, q80_0={1}".format(q79_0,q80_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_23 control2: q79_0 target: q80_0 ##
################################################################################
if 'q0_23' not in globals():
    q0_23=0
if 'q79_0' not in globals():
    q79_0=0
if 'q80_0' not in globals():
    q80_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq80_0' : 1, 'q80_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq80_0') : 4, ('anc1','q80_0') : -4, ('anc2', 'q0_23') : -2, ('anc2', 'q79_0') : -2, ('anc2', 'outq80_0') : -2, ('anc2', 'q80_0') : 2, ('q0_23', 'q79_0') : 1, ('outq80_0', 'q80_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_23']==q0_23 and sample['q79_0']==q79_0 and sample['q80_0']==q80_0 and int(energy)==0:
        q0_23=sample['q0_23']
        q79_0=sample['q79_0']
        q80_0=sample['outq80_0']
        tgt_before = sample['q80_0']
        break

print('#' * 80)
print("CCNOT operation on q0_23 (control1), q79_0 (control2) and q80_0 (target):")
print("    in:  q0_23={0}, q79_0={1}, q80_0={2}".format(q0_23,q79_0,tgt_before))
print("    out: q0_23={0}, q79_0={1}, q80_0={2}".format(q0_23,q79_0,q80_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_23 control2: q79_0 target: q80_0 ##
################################################################################
if 'q1_23' not in globals():
    q1_23=0
if 'q79_0' not in globals():
    q79_0=0
if 'q80_0' not in globals():
    q80_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq80_0' : 1, 'q80_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq80_0') : 4, ('anc1','q80_0') : -4, ('anc2', 'q1_23') : -2, ('anc2', 'q79_0') : -2, ('anc2', 'outq80_0') : -2, ('anc2', 'q80_0') : 2, ('q1_23', 'q79_0') : 1, ('outq80_0', 'q80_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_23']==q1_23 and sample['q79_0']==q79_0 and sample['q80_0']==q80_0 and int(energy)==0:
        q1_23=sample['q1_23']
        q79_0=sample['q79_0']
        q80_0=sample['outq80_0']
        tgt_before = sample['q80_0']
        break

print('#' * 80)
print("CCNOT operation on q1_23 (control1), q79_0 (control2) and q80_0 (target):")
print("    in:  q1_23={0}, q79_0={1}, q80_0={2}".format(q1_23,q79_0,tgt_before))
print("    out: q1_23={0}, q79_0={1}, q80_0={2}".format(q1_23,q79_0,q80_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q80_0 target: q81_0 ##
################################################################################
if 'q80_0' not in globals():
    q80_0=0
if 'q81_0' not in globals():
    q81_0=0

bqm = dimod.BinaryQuadraticModel({'q80_0' : 1, 'q81_0' : 1, 'outq81_0' : 1, 'anc' : 4}, {('q80_0', 'q81_0') : 2, ('q80_0', 'outq81_0') : -2, ('q81_0', 'outq81_0') : -2, ('q80_0', 'anc') : -4, ('q81_0', 'anc') : -4, ('outq81_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q80_0']==q80_0 and sample['q81_0']==q81_0 and int(energy)==0:
        q80_0=sample['q80_0']
        q81_0=sample['outq81_0']
        tgt_before = sample['q81_0']
        break

print('#' * 80)
print("CNOT operation on q80_0 (control) and q81_0 (target):")
print("    in:  q80_0={0}, q81_0={1}".format(q80_0,tgt_before))
print("    out: q80_0={0}, q81_0={1}".format(q80_0,q81_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_22 control2: q80_0 target: q81_0 ##
################################################################################
if 'q0_22' not in globals():
    q0_22=0
if 'q80_0' not in globals():
    q80_0=0
if 'q81_0' not in globals():
    q81_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq81_0' : 1, 'q81_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq81_0') : 4, ('anc1','q81_0') : -4, ('anc2', 'q0_22') : -2, ('anc2', 'q80_0') : -2, ('anc2', 'outq81_0') : -2, ('anc2', 'q81_0') : 2, ('q0_22', 'q80_0') : 1, ('outq81_0', 'q81_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_22']==q0_22 and sample['q80_0']==q80_0 and sample['q81_0']==q81_0 and int(energy)==0:
        q0_22=sample['q0_22']
        q80_0=sample['q80_0']
        q81_0=sample['outq81_0']
        tgt_before = sample['q81_0']
        break

print('#' * 80)
print("CCNOT operation on q0_22 (control1), q80_0 (control2) and q81_0 (target):")
print("    in:  q0_22={0}, q80_0={1}, q81_0={2}".format(q0_22,q80_0,tgt_before))
print("    out: q0_22={0}, q80_0={1}, q81_0={2}".format(q0_22,q80_0,q81_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_22 control2: q80_0 target: q81_0 ##
################################################################################
if 'q1_22' not in globals():
    q1_22=0
if 'q80_0' not in globals():
    q80_0=0
if 'q81_0' not in globals():
    q81_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq81_0' : 1, 'q81_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq81_0') : 4, ('anc1','q81_0') : -4, ('anc2', 'q1_22') : -2, ('anc2', 'q80_0') : -2, ('anc2', 'outq81_0') : -2, ('anc2', 'q81_0') : 2, ('q1_22', 'q80_0') : 1, ('outq81_0', 'q81_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_22']==q1_22 and sample['q80_0']==q80_0 and sample['q81_0']==q81_0 and int(energy)==0:
        q1_22=sample['q1_22']
        q80_0=sample['q80_0']
        q81_0=sample['outq81_0']
        tgt_before = sample['q81_0']
        break

print('#' * 80)
print("CCNOT operation on q1_22 (control1), q80_0 (control2) and q81_0 (target):")
print("    in:  q1_22={0}, q80_0={1}, q81_0={2}".format(q1_22,q80_0,tgt_before))
print("    out: q1_22={0}, q80_0={1}, q81_0={2}".format(q1_22,q80_0,q81_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q81_0 target: q82_0 ##
################################################################################
if 'q81_0' not in globals():
    q81_0=0
if 'q82_0' not in globals():
    q82_0=0

bqm = dimod.BinaryQuadraticModel({'q81_0' : 1, 'q82_0' : 1, 'outq82_0' : 1, 'anc' : 4}, {('q81_0', 'q82_0') : 2, ('q81_0', 'outq82_0') : -2, ('q82_0', 'outq82_0') : -2, ('q81_0', 'anc') : -4, ('q82_0', 'anc') : -4, ('outq82_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q81_0']==q81_0 and sample['q82_0']==q82_0 and int(energy)==0:
        q81_0=sample['q81_0']
        q82_0=sample['outq82_0']
        tgt_before = sample['q82_0']
        break

print('#' * 80)
print("CNOT operation on q81_0 (control) and q82_0 (target):")
print("    in:  q81_0={0}, q82_0={1}".format(q81_0,tgt_before))
print("    out: q81_0={0}, q82_0={1}".format(q81_0,q82_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_21 control2: q81_0 target: q82_0 ##
################################################################################
if 'q0_21' not in globals():
    q0_21=0
if 'q81_0' not in globals():
    q81_0=0
if 'q82_0' not in globals():
    q82_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq82_0' : 1, 'q82_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq82_0') : 4, ('anc1','q82_0') : -4, ('anc2', 'q0_21') : -2, ('anc2', 'q81_0') : -2, ('anc2', 'outq82_0') : -2, ('anc2', 'q82_0') : 2, ('q0_21', 'q81_0') : 1, ('outq82_0', 'q82_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_21']==q0_21 and sample['q81_0']==q81_0 and sample['q82_0']==q82_0 and int(energy)==0:
        q0_21=sample['q0_21']
        q81_0=sample['q81_0']
        q82_0=sample['outq82_0']
        tgt_before = sample['q82_0']
        break

print('#' * 80)
print("CCNOT operation on q0_21 (control1), q81_0 (control2) and q82_0 (target):")
print("    in:  q0_21={0}, q81_0={1}, q82_0={2}".format(q0_21,q81_0,tgt_before))
print("    out: q0_21={0}, q81_0={1}, q82_0={2}".format(q0_21,q81_0,q82_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_21 control2: q81_0 target: q82_0 ##
################################################################################
if 'q1_21' not in globals():
    q1_21=0
if 'q81_0' not in globals():
    q81_0=0
if 'q82_0' not in globals():
    q82_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq82_0' : 1, 'q82_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq82_0') : 4, ('anc1','q82_0') : -4, ('anc2', 'q1_21') : -2, ('anc2', 'q81_0') : -2, ('anc2', 'outq82_0') : -2, ('anc2', 'q82_0') : 2, ('q1_21', 'q81_0') : 1, ('outq82_0', 'q82_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_21']==q1_21 and sample['q81_0']==q81_0 and sample['q82_0']==q82_0 and int(energy)==0:
        q1_21=sample['q1_21']
        q81_0=sample['q81_0']
        q82_0=sample['outq82_0']
        tgt_before = sample['q82_0']
        break

print('#' * 80)
print("CCNOT operation on q1_21 (control1), q81_0 (control2) and q82_0 (target):")
print("    in:  q1_21={0}, q81_0={1}, q82_0={2}".format(q1_21,q81_0,tgt_before))
print("    out: q1_21={0}, q81_0={1}, q82_0={2}".format(q1_21,q81_0,q82_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q82_0 target: q83_0 ##
################################################################################
if 'q82_0' not in globals():
    q82_0=0
if 'q83_0' not in globals():
    q83_0=0

bqm = dimod.BinaryQuadraticModel({'q82_0' : 1, 'q83_0' : 1, 'outq83_0' : 1, 'anc' : 4}, {('q82_0', 'q83_0') : 2, ('q82_0', 'outq83_0') : -2, ('q83_0', 'outq83_0') : -2, ('q82_0', 'anc') : -4, ('q83_0', 'anc') : -4, ('outq83_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q82_0']==q82_0 and sample['q83_0']==q83_0 and int(energy)==0:
        q82_0=sample['q82_0']
        q83_0=sample['outq83_0']
        tgt_before = sample['q83_0']
        break

print('#' * 80)
print("CNOT operation on q82_0 (control) and q83_0 (target):")
print("    in:  q82_0={0}, q83_0={1}".format(q82_0,tgt_before))
print("    out: q82_0={0}, q83_0={1}".format(q82_0,q83_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_20 control2: q82_0 target: q83_0 ##
################################################################################
if 'q0_20' not in globals():
    q0_20=0
if 'q82_0' not in globals():
    q82_0=0
if 'q83_0' not in globals():
    q83_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq83_0' : 1, 'q83_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq83_0') : 4, ('anc1','q83_0') : -4, ('anc2', 'q0_20') : -2, ('anc2', 'q82_0') : -2, ('anc2', 'outq83_0') : -2, ('anc2', 'q83_0') : 2, ('q0_20', 'q82_0') : 1, ('outq83_0', 'q83_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_20']==q0_20 and sample['q82_0']==q82_0 and sample['q83_0']==q83_0 and int(energy)==0:
        q0_20=sample['q0_20']
        q82_0=sample['q82_0']
        q83_0=sample['outq83_0']
        tgt_before = sample['q83_0']
        break

print('#' * 80)
print("CCNOT operation on q0_20 (control1), q82_0 (control2) and q83_0 (target):")
print("    in:  q0_20={0}, q82_0={1}, q83_0={2}".format(q0_20,q82_0,tgt_before))
print("    out: q0_20={0}, q82_0={1}, q83_0={2}".format(q0_20,q82_0,q83_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_20 control2: q82_0 target: q83_0 ##
################################################################################
if 'q1_20' not in globals():
    q1_20=0
if 'q82_0' not in globals():
    q82_0=0
if 'q83_0' not in globals():
    q83_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq83_0' : 1, 'q83_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq83_0') : 4, ('anc1','q83_0') : -4, ('anc2', 'q1_20') : -2, ('anc2', 'q82_0') : -2, ('anc2', 'outq83_0') : -2, ('anc2', 'q83_0') : 2, ('q1_20', 'q82_0') : 1, ('outq83_0', 'q83_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_20']==q1_20 and sample['q82_0']==q82_0 and sample['q83_0']==q83_0 and int(energy)==0:
        q1_20=sample['q1_20']
        q82_0=sample['q82_0']
        q83_0=sample['outq83_0']
        tgt_before = sample['q83_0']
        break

print('#' * 80)
print("CCNOT operation on q1_20 (control1), q82_0 (control2) and q83_0 (target):")
print("    in:  q1_20={0}, q82_0={1}, q83_0={2}".format(q1_20,q82_0,tgt_before))
print("    out: q1_20={0}, q82_0={1}, q83_0={2}".format(q1_20,q82_0,q83_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q83_0 target: q84_0 ##
################################################################################
if 'q83_0' not in globals():
    q83_0=0
if 'q84_0' not in globals():
    q84_0=0

bqm = dimod.BinaryQuadraticModel({'q83_0' : 1, 'q84_0' : 1, 'outq84_0' : 1, 'anc' : 4}, {('q83_0', 'q84_0') : 2, ('q83_0', 'outq84_0') : -2, ('q84_0', 'outq84_0') : -2, ('q83_0', 'anc') : -4, ('q84_0', 'anc') : -4, ('outq84_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q83_0']==q83_0 and sample['q84_0']==q84_0 and int(energy)==0:
        q83_0=sample['q83_0']
        q84_0=sample['outq84_0']
        tgt_before = sample['q84_0']
        break

print('#' * 80)
print("CNOT operation on q83_0 (control) and q84_0 (target):")
print("    in:  q83_0={0}, q84_0={1}".format(q83_0,tgt_before))
print("    out: q83_0={0}, q84_0={1}".format(q83_0,q84_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_19 control2: q83_0 target: q84_0 ##
################################################################################
if 'q0_19' not in globals():
    q0_19=0
if 'q83_0' not in globals():
    q83_0=0
if 'q84_0' not in globals():
    q84_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq84_0' : 1, 'q84_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq84_0') : 4, ('anc1','q84_0') : -4, ('anc2', 'q0_19') : -2, ('anc2', 'q83_0') : -2, ('anc2', 'outq84_0') : -2, ('anc2', 'q84_0') : 2, ('q0_19', 'q83_0') : 1, ('outq84_0', 'q84_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_19']==q0_19 and sample['q83_0']==q83_0 and sample['q84_0']==q84_0 and int(energy)==0:
        q0_19=sample['q0_19']
        q83_0=sample['q83_0']
        q84_0=sample['outq84_0']
        tgt_before = sample['q84_0']
        break

print('#' * 80)
print("CCNOT operation on q0_19 (control1), q83_0 (control2) and q84_0 (target):")
print("    in:  q0_19={0}, q83_0={1}, q84_0={2}".format(q0_19,q83_0,tgt_before))
print("    out: q0_19={0}, q83_0={1}, q84_0={2}".format(q0_19,q83_0,q84_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_19 control2: q83_0 target: q84_0 ##
################################################################################
if 'q1_19' not in globals():
    q1_19=0
if 'q83_0' not in globals():
    q83_0=0
if 'q84_0' not in globals():
    q84_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq84_0' : 1, 'q84_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq84_0') : 4, ('anc1','q84_0') : -4, ('anc2', 'q1_19') : -2, ('anc2', 'q83_0') : -2, ('anc2', 'outq84_0') : -2, ('anc2', 'q84_0') : 2, ('q1_19', 'q83_0') : 1, ('outq84_0', 'q84_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_19']==q1_19 and sample['q83_0']==q83_0 and sample['q84_0']==q84_0 and int(energy)==0:
        q1_19=sample['q1_19']
        q83_0=sample['q83_0']
        q84_0=sample['outq84_0']
        tgt_before = sample['q84_0']
        break

print('#' * 80)
print("CCNOT operation on q1_19 (control1), q83_0 (control2) and q84_0 (target):")
print("    in:  q1_19={0}, q83_0={1}, q84_0={2}".format(q1_19,q83_0,tgt_before))
print("    out: q1_19={0}, q83_0={1}, q84_0={2}".format(q1_19,q83_0,q84_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q84_0 target: q85_0 ##
################################################################################
if 'q84_0' not in globals():
    q84_0=0
if 'q85_0' not in globals():
    q85_0=0

bqm = dimod.BinaryQuadraticModel({'q84_0' : 1, 'q85_0' : 1, 'outq85_0' : 1, 'anc' : 4}, {('q84_0', 'q85_0') : 2, ('q84_0', 'outq85_0') : -2, ('q85_0', 'outq85_0') : -2, ('q84_0', 'anc') : -4, ('q85_0', 'anc') : -4, ('outq85_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q84_0']==q84_0 and sample['q85_0']==q85_0 and int(energy)==0:
        q84_0=sample['q84_0']
        q85_0=sample['outq85_0']
        tgt_before = sample['q85_0']
        break

print('#' * 80)
print("CNOT operation on q84_0 (control) and q85_0 (target):")
print("    in:  q84_0={0}, q85_0={1}".format(q84_0,tgt_before))
print("    out: q84_0={0}, q85_0={1}".format(q84_0,q85_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_18 control2: q84_0 target: q85_0 ##
################################################################################
if 'q0_18' not in globals():
    q0_18=0
if 'q84_0' not in globals():
    q84_0=0
if 'q85_0' not in globals():
    q85_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq85_0' : 1, 'q85_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq85_0') : 4, ('anc1','q85_0') : -4, ('anc2', 'q0_18') : -2, ('anc2', 'q84_0') : -2, ('anc2', 'outq85_0') : -2, ('anc2', 'q85_0') : 2, ('q0_18', 'q84_0') : 1, ('outq85_0', 'q85_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_18']==q0_18 and sample['q84_0']==q84_0 and sample['q85_0']==q85_0 and int(energy)==0:
        q0_18=sample['q0_18']
        q84_0=sample['q84_0']
        q85_0=sample['outq85_0']
        tgt_before = sample['q85_0']
        break

print('#' * 80)
print("CCNOT operation on q0_18 (control1), q84_0 (control2) and q85_0 (target):")
print("    in:  q0_18={0}, q84_0={1}, q85_0={2}".format(q0_18,q84_0,tgt_before))
print("    out: q0_18={0}, q84_0={1}, q85_0={2}".format(q0_18,q84_0,q85_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_18 control2: q84_0 target: q85_0 ##
################################################################################
if 'q1_18' not in globals():
    q1_18=0
if 'q84_0' not in globals():
    q84_0=0
if 'q85_0' not in globals():
    q85_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq85_0' : 1, 'q85_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq85_0') : 4, ('anc1','q85_0') : -4, ('anc2', 'q1_18') : -2, ('anc2', 'q84_0') : -2, ('anc2', 'outq85_0') : -2, ('anc2', 'q85_0') : 2, ('q1_18', 'q84_0') : 1, ('outq85_0', 'q85_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_18']==q1_18 and sample['q84_0']==q84_0 and sample['q85_0']==q85_0 and int(energy)==0:
        q1_18=sample['q1_18']
        q84_0=sample['q84_0']
        q85_0=sample['outq85_0']
        tgt_before = sample['q85_0']
        break

print('#' * 80)
print("CCNOT operation on q1_18 (control1), q84_0 (control2) and q85_0 (target):")
print("    in:  q1_18={0}, q84_0={1}, q85_0={2}".format(q1_18,q84_0,tgt_before))
print("    out: q1_18={0}, q84_0={1}, q85_0={2}".format(q1_18,q84_0,q85_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q85_0 target: q86_0 ##
################################################################################
if 'q85_0' not in globals():
    q85_0=0
if 'q86_0' not in globals():
    q86_0=0

bqm = dimod.BinaryQuadraticModel({'q85_0' : 1, 'q86_0' : 1, 'outq86_0' : 1, 'anc' : 4}, {('q85_0', 'q86_0') : 2, ('q85_0', 'outq86_0') : -2, ('q86_0', 'outq86_0') : -2, ('q85_0', 'anc') : -4, ('q86_0', 'anc') : -4, ('outq86_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q85_0']==q85_0 and sample['q86_0']==q86_0 and int(energy)==0:
        q85_0=sample['q85_0']
        q86_0=sample['outq86_0']
        tgt_before = sample['q86_0']
        break

print('#' * 80)
print("CNOT operation on q85_0 (control) and q86_0 (target):")
print("    in:  q85_0={0}, q86_0={1}".format(q85_0,tgt_before))
print("    out: q85_0={0}, q86_0={1}".format(q85_0,q86_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_17 control2: q85_0 target: q86_0 ##
################################################################################
if 'q0_17' not in globals():
    q0_17=0
if 'q85_0' not in globals():
    q85_0=0
if 'q86_0' not in globals():
    q86_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq86_0' : 1, 'q86_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq86_0') : 4, ('anc1','q86_0') : -4, ('anc2', 'q0_17') : -2, ('anc2', 'q85_0') : -2, ('anc2', 'outq86_0') : -2, ('anc2', 'q86_0') : 2, ('q0_17', 'q85_0') : 1, ('outq86_0', 'q86_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_17']==q0_17 and sample['q85_0']==q85_0 and sample['q86_0']==q86_0 and int(energy)==0:
        q0_17=sample['q0_17']
        q85_0=sample['q85_0']
        q86_0=sample['outq86_0']
        tgt_before = sample['q86_0']
        break

print('#' * 80)
print("CCNOT operation on q0_17 (control1), q85_0 (control2) and q86_0 (target):")
print("    in:  q0_17={0}, q85_0={1}, q86_0={2}".format(q0_17,q85_0,tgt_before))
print("    out: q0_17={0}, q85_0={1}, q86_0={2}".format(q0_17,q85_0,q86_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_17 control2: q85_0 target: q86_0 ##
################################################################################
if 'q1_17' not in globals():
    q1_17=0
if 'q85_0' not in globals():
    q85_0=0
if 'q86_0' not in globals():
    q86_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq86_0' : 1, 'q86_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq86_0') : 4, ('anc1','q86_0') : -4, ('anc2', 'q1_17') : -2, ('anc2', 'q85_0') : -2, ('anc2', 'outq86_0') : -2, ('anc2', 'q86_0') : 2, ('q1_17', 'q85_0') : 1, ('outq86_0', 'q86_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_17']==q1_17 and sample['q85_0']==q85_0 and sample['q86_0']==q86_0 and int(energy)==0:
        q1_17=sample['q1_17']
        q85_0=sample['q85_0']
        q86_0=sample['outq86_0']
        tgt_before = sample['q86_0']
        break

print('#' * 80)
print("CCNOT operation on q1_17 (control1), q85_0 (control2) and q86_0 (target):")
print("    in:  q1_17={0}, q85_0={1}, q86_0={2}".format(q1_17,q85_0,tgt_before))
print("    out: q1_17={0}, q85_0={1}, q86_0={2}".format(q1_17,q85_0,q86_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q86_0 target: q87_0 ##
################################################################################
if 'q86_0' not in globals():
    q86_0=0
if 'q87_0' not in globals():
    q87_0=0

bqm = dimod.BinaryQuadraticModel({'q86_0' : 1, 'q87_0' : 1, 'outq87_0' : 1, 'anc' : 4}, {('q86_0', 'q87_0') : 2, ('q86_0', 'outq87_0') : -2, ('q87_0', 'outq87_0') : -2, ('q86_0', 'anc') : -4, ('q87_0', 'anc') : -4, ('outq87_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q86_0']==q86_0 and sample['q87_0']==q87_0 and int(energy)==0:
        q86_0=sample['q86_0']
        q87_0=sample['outq87_0']
        tgt_before = sample['q87_0']
        break

print('#' * 80)
print("CNOT operation on q86_0 (control) and q87_0 (target):")
print("    in:  q86_0={0}, q87_0={1}".format(q86_0,tgt_before))
print("    out: q86_0={0}, q87_0={1}".format(q86_0,q87_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_16 control2: q86_0 target: q87_0 ##
################################################################################
if 'q0_16' not in globals():
    q0_16=0
if 'q86_0' not in globals():
    q86_0=0
if 'q87_0' not in globals():
    q87_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq87_0' : 1, 'q87_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq87_0') : 4, ('anc1','q87_0') : -4, ('anc2', 'q0_16') : -2, ('anc2', 'q86_0') : -2, ('anc2', 'outq87_0') : -2, ('anc2', 'q87_0') : 2, ('q0_16', 'q86_0') : 1, ('outq87_0', 'q87_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_16']==q0_16 and sample['q86_0']==q86_0 and sample['q87_0']==q87_0 and int(energy)==0:
        q0_16=sample['q0_16']
        q86_0=sample['q86_0']
        q87_0=sample['outq87_0']
        tgt_before = sample['q87_0']
        break

print('#' * 80)
print("CCNOT operation on q0_16 (control1), q86_0 (control2) and q87_0 (target):")
print("    in:  q0_16={0}, q86_0={1}, q87_0={2}".format(q0_16,q86_0,tgt_before))
print("    out: q0_16={0}, q86_0={1}, q87_0={2}".format(q0_16,q86_0,q87_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_16 control2: q86_0 target: q87_0 ##
################################################################################
if 'q1_16' not in globals():
    q1_16=0
if 'q86_0' not in globals():
    q86_0=0
if 'q87_0' not in globals():
    q87_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq87_0' : 1, 'q87_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq87_0') : 4, ('anc1','q87_0') : -4, ('anc2', 'q1_16') : -2, ('anc2', 'q86_0') : -2, ('anc2', 'outq87_0') : -2, ('anc2', 'q87_0') : 2, ('q1_16', 'q86_0') : 1, ('outq87_0', 'q87_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_16']==q1_16 and sample['q86_0']==q86_0 and sample['q87_0']==q87_0 and int(energy)==0:
        q1_16=sample['q1_16']
        q86_0=sample['q86_0']
        q87_0=sample['outq87_0']
        tgt_before = sample['q87_0']
        break

print('#' * 80)
print("CCNOT operation on q1_16 (control1), q86_0 (control2) and q87_0 (target):")
print("    in:  q1_16={0}, q86_0={1}, q87_0={2}".format(q1_16,q86_0,tgt_before))
print("    out: q1_16={0}, q86_0={1}, q87_0={2}".format(q1_16,q86_0,q87_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q87_0 target: q88_0 ##
################################################################################
if 'q87_0' not in globals():
    q87_0=0
if 'q88_0' not in globals():
    q88_0=0

bqm = dimod.BinaryQuadraticModel({'q87_0' : 1, 'q88_0' : 1, 'outq88_0' : 1, 'anc' : 4}, {('q87_0', 'q88_0') : 2, ('q87_0', 'outq88_0') : -2, ('q88_0', 'outq88_0') : -2, ('q87_0', 'anc') : -4, ('q88_0', 'anc') : -4, ('outq88_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q87_0']==q87_0 and sample['q88_0']==q88_0 and int(energy)==0:
        q87_0=sample['q87_0']
        q88_0=sample['outq88_0']
        tgt_before = sample['q88_0']
        break

print('#' * 80)
print("CNOT operation on q87_0 (control) and q88_0 (target):")
print("    in:  q87_0={0}, q88_0={1}".format(q87_0,tgt_before))
print("    out: q87_0={0}, q88_0={1}".format(q87_0,q88_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_15 control2: q87_0 target: q88_0 ##
################################################################################
if 'q0_15' not in globals():
    q0_15=0
if 'q87_0' not in globals():
    q87_0=0
if 'q88_0' not in globals():
    q88_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq88_0' : 1, 'q88_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq88_0') : 4, ('anc1','q88_0') : -4, ('anc2', 'q0_15') : -2, ('anc2', 'q87_0') : -2, ('anc2', 'outq88_0') : -2, ('anc2', 'q88_0') : 2, ('q0_15', 'q87_0') : 1, ('outq88_0', 'q88_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_15']==q0_15 and sample['q87_0']==q87_0 and sample['q88_0']==q88_0 and int(energy)==0:
        q0_15=sample['q0_15']
        q87_0=sample['q87_0']
        q88_0=sample['outq88_0']
        tgt_before = sample['q88_0']
        break

print('#' * 80)
print("CCNOT operation on q0_15 (control1), q87_0 (control2) and q88_0 (target):")
print("    in:  q0_15={0}, q87_0={1}, q88_0={2}".format(q0_15,q87_0,tgt_before))
print("    out: q0_15={0}, q87_0={1}, q88_0={2}".format(q0_15,q87_0,q88_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_15 control2: q87_0 target: q88_0 ##
################################################################################
if 'q1_15' not in globals():
    q1_15=0
if 'q87_0' not in globals():
    q87_0=0
if 'q88_0' not in globals():
    q88_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq88_0' : 1, 'q88_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq88_0') : 4, ('anc1','q88_0') : -4, ('anc2', 'q1_15') : -2, ('anc2', 'q87_0') : -2, ('anc2', 'outq88_0') : -2, ('anc2', 'q88_0') : 2, ('q1_15', 'q87_0') : 1, ('outq88_0', 'q88_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_15']==q1_15 and sample['q87_0']==q87_0 and sample['q88_0']==q88_0 and int(energy)==0:
        q1_15=sample['q1_15']
        q87_0=sample['q87_0']
        q88_0=sample['outq88_0']
        tgt_before = sample['q88_0']
        break

print('#' * 80)
print("CCNOT operation on q1_15 (control1), q87_0 (control2) and q88_0 (target):")
print("    in:  q1_15={0}, q87_0={1}, q88_0={2}".format(q1_15,q87_0,tgt_before))
print("    out: q1_15={0}, q87_0={1}, q88_0={2}".format(q1_15,q87_0,q88_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q88_0 target: q89_0 ##
################################################################################
if 'q88_0' not in globals():
    q88_0=0
if 'q89_0' not in globals():
    q89_0=0

bqm = dimod.BinaryQuadraticModel({'q88_0' : 1, 'q89_0' : 1, 'outq89_0' : 1, 'anc' : 4}, {('q88_0', 'q89_0') : 2, ('q88_0', 'outq89_0') : -2, ('q89_0', 'outq89_0') : -2, ('q88_0', 'anc') : -4, ('q89_0', 'anc') : -4, ('outq89_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q88_0']==q88_0 and sample['q89_0']==q89_0 and int(energy)==0:
        q88_0=sample['q88_0']
        q89_0=sample['outq89_0']
        tgt_before = sample['q89_0']
        break

print('#' * 80)
print("CNOT operation on q88_0 (control) and q89_0 (target):")
print("    in:  q88_0={0}, q89_0={1}".format(q88_0,tgt_before))
print("    out: q88_0={0}, q89_0={1}".format(q88_0,q89_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_14 control2: q88_0 target: q89_0 ##
################################################################################
if 'q0_14' not in globals():
    q0_14=0
if 'q88_0' not in globals():
    q88_0=0
if 'q89_0' not in globals():
    q89_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq89_0' : 1, 'q89_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq89_0') : 4, ('anc1','q89_0') : -4, ('anc2', 'q0_14') : -2, ('anc2', 'q88_0') : -2, ('anc2', 'outq89_0') : -2, ('anc2', 'q89_0') : 2, ('q0_14', 'q88_0') : 1, ('outq89_0', 'q89_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_14']==q0_14 and sample['q88_0']==q88_0 and sample['q89_0']==q89_0 and int(energy)==0:
        q0_14=sample['q0_14']
        q88_0=sample['q88_0']
        q89_0=sample['outq89_0']
        tgt_before = sample['q89_0']
        break

print('#' * 80)
print("CCNOT operation on q0_14 (control1), q88_0 (control2) and q89_0 (target):")
print("    in:  q0_14={0}, q88_0={1}, q89_0={2}".format(q0_14,q88_0,tgt_before))
print("    out: q0_14={0}, q88_0={1}, q89_0={2}".format(q0_14,q88_0,q89_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_14 control2: q88_0 target: q89_0 ##
################################################################################
if 'q1_14' not in globals():
    q1_14=0
if 'q88_0' not in globals():
    q88_0=0
if 'q89_0' not in globals():
    q89_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq89_0' : 1, 'q89_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq89_0') : 4, ('anc1','q89_0') : -4, ('anc2', 'q1_14') : -2, ('anc2', 'q88_0') : -2, ('anc2', 'outq89_0') : -2, ('anc2', 'q89_0') : 2, ('q1_14', 'q88_0') : 1, ('outq89_0', 'q89_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_14']==q1_14 and sample['q88_0']==q88_0 and sample['q89_0']==q89_0 and int(energy)==0:
        q1_14=sample['q1_14']
        q88_0=sample['q88_0']
        q89_0=sample['outq89_0']
        tgt_before = sample['q89_0']
        break

print('#' * 80)
print("CCNOT operation on q1_14 (control1), q88_0 (control2) and q89_0 (target):")
print("    in:  q1_14={0}, q88_0={1}, q89_0={2}".format(q1_14,q88_0,tgt_before))
print("    out: q1_14={0}, q88_0={1}, q89_0={2}".format(q1_14,q88_0,q89_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q89_0 target: q90_0 ##
################################################################################
if 'q89_0' not in globals():
    q89_0=0
if 'q90_0' not in globals():
    q90_0=0

bqm = dimod.BinaryQuadraticModel({'q89_0' : 1, 'q90_0' : 1, 'outq90_0' : 1, 'anc' : 4}, {('q89_0', 'q90_0') : 2, ('q89_0', 'outq90_0') : -2, ('q90_0', 'outq90_0') : -2, ('q89_0', 'anc') : -4, ('q90_0', 'anc') : -4, ('outq90_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q89_0']==q89_0 and sample['q90_0']==q90_0 and int(energy)==0:
        q89_0=sample['q89_0']
        q90_0=sample['outq90_0']
        tgt_before = sample['q90_0']
        break

print('#' * 80)
print("CNOT operation on q89_0 (control) and q90_0 (target):")
print("    in:  q89_0={0}, q90_0={1}".format(q89_0,tgt_before))
print("    out: q89_0={0}, q90_0={1}".format(q89_0,q90_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_13 control2: q89_0 target: q90_0 ##
################################################################################
if 'q0_13' not in globals():
    q0_13=0
if 'q89_0' not in globals():
    q89_0=0
if 'q90_0' not in globals():
    q90_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq90_0' : 1, 'q90_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq90_0') : 4, ('anc1','q90_0') : -4, ('anc2', 'q0_13') : -2, ('anc2', 'q89_0') : -2, ('anc2', 'outq90_0') : -2, ('anc2', 'q90_0') : 2, ('q0_13', 'q89_0') : 1, ('outq90_0', 'q90_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_13']==q0_13 and sample['q89_0']==q89_0 and sample['q90_0']==q90_0 and int(energy)==0:
        q0_13=sample['q0_13']
        q89_0=sample['q89_0']
        q90_0=sample['outq90_0']
        tgt_before = sample['q90_0']
        break

print('#' * 80)
print("CCNOT operation on q0_13 (control1), q89_0 (control2) and q90_0 (target):")
print("    in:  q0_13={0}, q89_0={1}, q90_0={2}".format(q0_13,q89_0,tgt_before))
print("    out: q0_13={0}, q89_0={1}, q90_0={2}".format(q0_13,q89_0,q90_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_13 control2: q89_0 target: q90_0 ##
################################################################################
if 'q1_13' not in globals():
    q1_13=0
if 'q89_0' not in globals():
    q89_0=0
if 'q90_0' not in globals():
    q90_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq90_0' : 1, 'q90_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq90_0') : 4, ('anc1','q90_0') : -4, ('anc2', 'q1_13') : -2, ('anc2', 'q89_0') : -2, ('anc2', 'outq90_0') : -2, ('anc2', 'q90_0') : 2, ('q1_13', 'q89_0') : 1, ('outq90_0', 'q90_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_13']==q1_13 and sample['q89_0']==q89_0 and sample['q90_0']==q90_0 and int(energy)==0:
        q1_13=sample['q1_13']
        q89_0=sample['q89_0']
        q90_0=sample['outq90_0']
        tgt_before = sample['q90_0']
        break

print('#' * 80)
print("CCNOT operation on q1_13 (control1), q89_0 (control2) and q90_0 (target):")
print("    in:  q1_13={0}, q89_0={1}, q90_0={2}".format(q1_13,q89_0,tgt_before))
print("    out: q1_13={0}, q89_0={1}, q90_0={2}".format(q1_13,q89_0,q90_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q90_0 target: q91_0 ##
################################################################################
if 'q90_0' not in globals():
    q90_0=0
if 'q91_0' not in globals():
    q91_0=0

bqm = dimod.BinaryQuadraticModel({'q90_0' : 1, 'q91_0' : 1, 'outq91_0' : 1, 'anc' : 4}, {('q90_0', 'q91_0') : 2, ('q90_0', 'outq91_0') : -2, ('q91_0', 'outq91_0') : -2, ('q90_0', 'anc') : -4, ('q91_0', 'anc') : -4, ('outq91_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q90_0']==q90_0 and sample['q91_0']==q91_0 and int(energy)==0:
        q90_0=sample['q90_0']
        q91_0=sample['outq91_0']
        tgt_before = sample['q91_0']
        break

print('#' * 80)
print("CNOT operation on q90_0 (control) and q91_0 (target):")
print("    in:  q90_0={0}, q91_0={1}".format(q90_0,tgt_before))
print("    out: q90_0={0}, q91_0={1}".format(q90_0,q91_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_12 control2: q90_0 target: q91_0 ##
################################################################################
if 'q0_12' not in globals():
    q0_12=0
if 'q90_0' not in globals():
    q90_0=0
if 'q91_0' not in globals():
    q91_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq91_0' : 1, 'q91_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq91_0') : 4, ('anc1','q91_0') : -4, ('anc2', 'q0_12') : -2, ('anc2', 'q90_0') : -2, ('anc2', 'outq91_0') : -2, ('anc2', 'q91_0') : 2, ('q0_12', 'q90_0') : 1, ('outq91_0', 'q91_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_12']==q0_12 and sample['q90_0']==q90_0 and sample['q91_0']==q91_0 and int(energy)==0:
        q0_12=sample['q0_12']
        q90_0=sample['q90_0']
        q91_0=sample['outq91_0']
        tgt_before = sample['q91_0']
        break

print('#' * 80)
print("CCNOT operation on q0_12 (control1), q90_0 (control2) and q91_0 (target):")
print("    in:  q0_12={0}, q90_0={1}, q91_0={2}".format(q0_12,q90_0,tgt_before))
print("    out: q0_12={0}, q90_0={1}, q91_0={2}".format(q0_12,q90_0,q91_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_12 control2: q90_0 target: q91_0 ##
################################################################################
if 'q1_12' not in globals():
    q1_12=0
if 'q90_0' not in globals():
    q90_0=0
if 'q91_0' not in globals():
    q91_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq91_0' : 1, 'q91_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq91_0') : 4, ('anc1','q91_0') : -4, ('anc2', 'q1_12') : -2, ('anc2', 'q90_0') : -2, ('anc2', 'outq91_0') : -2, ('anc2', 'q91_0') : 2, ('q1_12', 'q90_0') : 1, ('outq91_0', 'q91_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_12']==q1_12 and sample['q90_0']==q90_0 and sample['q91_0']==q91_0 and int(energy)==0:
        q1_12=sample['q1_12']
        q90_0=sample['q90_0']
        q91_0=sample['outq91_0']
        tgt_before = sample['q91_0']
        break

print('#' * 80)
print("CCNOT operation on q1_12 (control1), q90_0 (control2) and q91_0 (target):")
print("    in:  q1_12={0}, q90_0={1}, q91_0={2}".format(q1_12,q90_0,tgt_before))
print("    out: q1_12={0}, q90_0={1}, q91_0={2}".format(q1_12,q90_0,q91_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q91_0 target: q92_0 ##
################################################################################
if 'q91_0' not in globals():
    q91_0=0
if 'q92_0' not in globals():
    q92_0=0

bqm = dimod.BinaryQuadraticModel({'q91_0' : 1, 'q92_0' : 1, 'outq92_0' : 1, 'anc' : 4}, {('q91_0', 'q92_0') : 2, ('q91_0', 'outq92_0') : -2, ('q92_0', 'outq92_0') : -2, ('q91_0', 'anc') : -4, ('q92_0', 'anc') : -4, ('outq92_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q91_0']==q91_0 and sample['q92_0']==q92_0 and int(energy)==0:
        q91_0=sample['q91_0']
        q92_0=sample['outq92_0']
        tgt_before = sample['q92_0']
        break

print('#' * 80)
print("CNOT operation on q91_0 (control) and q92_0 (target):")
print("    in:  q91_0={0}, q92_0={1}".format(q91_0,tgt_before))
print("    out: q91_0={0}, q92_0={1}".format(q91_0,q92_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_11 control2: q91_0 target: q92_0 ##
################################################################################
if 'q0_11' not in globals():
    q0_11=0
if 'q91_0' not in globals():
    q91_0=0
if 'q92_0' not in globals():
    q92_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq92_0' : 1, 'q92_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq92_0') : 4, ('anc1','q92_0') : -4, ('anc2', 'q0_11') : -2, ('anc2', 'q91_0') : -2, ('anc2', 'outq92_0') : -2, ('anc2', 'q92_0') : 2, ('q0_11', 'q91_0') : 1, ('outq92_0', 'q92_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_11']==q0_11 and sample['q91_0']==q91_0 and sample['q92_0']==q92_0 and int(energy)==0:
        q0_11=sample['q0_11']
        q91_0=sample['q91_0']
        q92_0=sample['outq92_0']
        tgt_before = sample['q92_0']
        break

print('#' * 80)
print("CCNOT operation on q0_11 (control1), q91_0 (control2) and q92_0 (target):")
print("    in:  q0_11={0}, q91_0={1}, q92_0={2}".format(q0_11,q91_0,tgt_before))
print("    out: q0_11={0}, q91_0={1}, q92_0={2}".format(q0_11,q91_0,q92_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_11 control2: q91_0 target: q92_0 ##
################################################################################
if 'q1_11' not in globals():
    q1_11=0
if 'q91_0' not in globals():
    q91_0=0
if 'q92_0' not in globals():
    q92_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq92_0' : 1, 'q92_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq92_0') : 4, ('anc1','q92_0') : -4, ('anc2', 'q1_11') : -2, ('anc2', 'q91_0') : -2, ('anc2', 'outq92_0') : -2, ('anc2', 'q92_0') : 2, ('q1_11', 'q91_0') : 1, ('outq92_0', 'q92_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_11']==q1_11 and sample['q91_0']==q91_0 and sample['q92_0']==q92_0 and int(energy)==0:
        q1_11=sample['q1_11']
        q91_0=sample['q91_0']
        q92_0=sample['outq92_0']
        tgt_before = sample['q92_0']
        break

print('#' * 80)
print("CCNOT operation on q1_11 (control1), q91_0 (control2) and q92_0 (target):")
print("    in:  q1_11={0}, q91_0={1}, q92_0={2}".format(q1_11,q91_0,tgt_before))
print("    out: q1_11={0}, q91_0={1}, q92_0={2}".format(q1_11,q91_0,q92_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q92_0 target: q93_0 ##
################################################################################
if 'q92_0' not in globals():
    q92_0=0
if 'q93_0' not in globals():
    q93_0=0

bqm = dimod.BinaryQuadraticModel({'q92_0' : 1, 'q93_0' : 1, 'outq93_0' : 1, 'anc' : 4}, {('q92_0', 'q93_0') : 2, ('q92_0', 'outq93_0') : -2, ('q93_0', 'outq93_0') : -2, ('q92_0', 'anc') : -4, ('q93_0', 'anc') : -4, ('outq93_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q92_0']==q92_0 and sample['q93_0']==q93_0 and int(energy)==0:
        q92_0=sample['q92_0']
        q93_0=sample['outq93_0']
        tgt_before = sample['q93_0']
        break

print('#' * 80)
print("CNOT operation on q92_0 (control) and q93_0 (target):")
print("    in:  q92_0={0}, q93_0={1}".format(q92_0,tgt_before))
print("    out: q92_0={0}, q93_0={1}".format(q92_0,q93_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_10 control2: q92_0 target: q93_0 ##
################################################################################
if 'q0_10' not in globals():
    q0_10=0
if 'q92_0' not in globals():
    q92_0=0
if 'q93_0' not in globals():
    q93_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq93_0' : 1, 'q93_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq93_0') : 4, ('anc1','q93_0') : -4, ('anc2', 'q0_10') : -2, ('anc2', 'q92_0') : -2, ('anc2', 'outq93_0') : -2, ('anc2', 'q93_0') : 2, ('q0_10', 'q92_0') : 1, ('outq93_0', 'q93_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_10']==q0_10 and sample['q92_0']==q92_0 and sample['q93_0']==q93_0 and int(energy)==0:
        q0_10=sample['q0_10']
        q92_0=sample['q92_0']
        q93_0=sample['outq93_0']
        tgt_before = sample['q93_0']
        break

print('#' * 80)
print("CCNOT operation on q0_10 (control1), q92_0 (control2) and q93_0 (target):")
print("    in:  q0_10={0}, q92_0={1}, q93_0={2}".format(q0_10,q92_0,tgt_before))
print("    out: q0_10={0}, q92_0={1}, q93_0={2}".format(q0_10,q92_0,q93_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_10 control2: q92_0 target: q93_0 ##
################################################################################
if 'q1_10' not in globals():
    q1_10=0
if 'q92_0' not in globals():
    q92_0=0
if 'q93_0' not in globals():
    q93_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq93_0' : 1, 'q93_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq93_0') : 4, ('anc1','q93_0') : -4, ('anc2', 'q1_10') : -2, ('anc2', 'q92_0') : -2, ('anc2', 'outq93_0') : -2, ('anc2', 'q93_0') : 2, ('q1_10', 'q92_0') : 1, ('outq93_0', 'q93_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_10']==q1_10 and sample['q92_0']==q92_0 and sample['q93_0']==q93_0 and int(energy)==0:
        q1_10=sample['q1_10']
        q92_0=sample['q92_0']
        q93_0=sample['outq93_0']
        tgt_before = sample['q93_0']
        break

print('#' * 80)
print("CCNOT operation on q1_10 (control1), q92_0 (control2) and q93_0 (target):")
print("    in:  q1_10={0}, q92_0={1}, q93_0={2}".format(q1_10,q92_0,tgt_before))
print("    out: q1_10={0}, q92_0={1}, q93_0={2}".format(q1_10,q92_0,q93_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q93_0 target: q94_0 ##
################################################################################
if 'q93_0' not in globals():
    q93_0=0
if 'q94_0' not in globals():
    q94_0=0

bqm = dimod.BinaryQuadraticModel({'q93_0' : 1, 'q94_0' : 1, 'outq94_0' : 1, 'anc' : 4}, {('q93_0', 'q94_0') : 2, ('q93_0', 'outq94_0') : -2, ('q94_0', 'outq94_0') : -2, ('q93_0', 'anc') : -4, ('q94_0', 'anc') : -4, ('outq94_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q93_0']==q93_0 and sample['q94_0']==q94_0 and int(energy)==0:
        q93_0=sample['q93_0']
        q94_0=sample['outq94_0']
        tgt_before = sample['q94_0']
        break

print('#' * 80)
print("CNOT operation on q93_0 (control) and q94_0 (target):")
print("    in:  q93_0={0}, q94_0={1}".format(q93_0,tgt_before))
print("    out: q93_0={0}, q94_0={1}".format(q93_0,q94_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_9 control2: q93_0 target: q94_0 ##
################################################################################
if 'q0_9' not in globals():
    q0_9=0
if 'q93_0' not in globals():
    q93_0=0
if 'q94_0' not in globals():
    q94_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq94_0' : 1, 'q94_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq94_0') : 4, ('anc1','q94_0') : -4, ('anc2', 'q0_9') : -2, ('anc2', 'q93_0') : -2, ('anc2', 'outq94_0') : -2, ('anc2', 'q94_0') : 2, ('q0_9', 'q93_0') : 1, ('outq94_0', 'q94_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_9']==q0_9 and sample['q93_0']==q93_0 and sample['q94_0']==q94_0 and int(energy)==0:
        q0_9=sample['q0_9']
        q93_0=sample['q93_0']
        q94_0=sample['outq94_0']
        tgt_before = sample['q94_0']
        break

print('#' * 80)
print("CCNOT operation on q0_9 (control1), q93_0 (control2) and q94_0 (target):")
print("    in:  q0_9={0}, q93_0={1}, q94_0={2}".format(q0_9,q93_0,tgt_before))
print("    out: q0_9={0}, q93_0={1}, q94_0={2}".format(q0_9,q93_0,q94_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_9 control2: q93_0 target: q94_0 ##
################################################################################
if 'q1_9' not in globals():
    q1_9=0
if 'q93_0' not in globals():
    q93_0=0
if 'q94_0' not in globals():
    q94_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq94_0' : 1, 'q94_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq94_0') : 4, ('anc1','q94_0') : -4, ('anc2', 'q1_9') : -2, ('anc2', 'q93_0') : -2, ('anc2', 'outq94_0') : -2, ('anc2', 'q94_0') : 2, ('q1_9', 'q93_0') : 1, ('outq94_0', 'q94_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_9']==q1_9 and sample['q93_0']==q93_0 and sample['q94_0']==q94_0 and int(energy)==0:
        q1_9=sample['q1_9']
        q93_0=sample['q93_0']
        q94_0=sample['outq94_0']
        tgt_before = sample['q94_0']
        break

print('#' * 80)
print("CCNOT operation on q1_9 (control1), q93_0 (control2) and q94_0 (target):")
print("    in:  q1_9={0}, q93_0={1}, q94_0={2}".format(q1_9,q93_0,tgt_before))
print("    out: q1_9={0}, q93_0={1}, q94_0={2}".format(q1_9,q93_0,q94_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q94_0 target: q95_0 ##
################################################################################
if 'q94_0' not in globals():
    q94_0=0
if 'q95_0' not in globals():
    q95_0=0

bqm = dimod.BinaryQuadraticModel({'q94_0' : 1, 'q95_0' : 1, 'outq95_0' : 1, 'anc' : 4}, {('q94_0', 'q95_0') : 2, ('q94_0', 'outq95_0') : -2, ('q95_0', 'outq95_0') : -2, ('q94_0', 'anc') : -4, ('q95_0', 'anc') : -4, ('outq95_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q94_0']==q94_0 and sample['q95_0']==q95_0 and int(energy)==0:
        q94_0=sample['q94_0']
        q95_0=sample['outq95_0']
        tgt_before = sample['q95_0']
        break

print('#' * 80)
print("CNOT operation on q94_0 (control) and q95_0 (target):")
print("    in:  q94_0={0}, q95_0={1}".format(q94_0,tgt_before))
print("    out: q94_0={0}, q95_0={1}".format(q94_0,q95_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_8 control2: q94_0 target: q95_0 ##
################################################################################
if 'q0_8' not in globals():
    q0_8=0
if 'q94_0' not in globals():
    q94_0=0
if 'q95_0' not in globals():
    q95_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq95_0' : 1, 'q95_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq95_0') : 4, ('anc1','q95_0') : -4, ('anc2', 'q0_8') : -2, ('anc2', 'q94_0') : -2, ('anc2', 'outq95_0') : -2, ('anc2', 'q95_0') : 2, ('q0_8', 'q94_0') : 1, ('outq95_0', 'q95_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_8']==q0_8 and sample['q94_0']==q94_0 and sample['q95_0']==q95_0 and int(energy)==0:
        q0_8=sample['q0_8']
        q94_0=sample['q94_0']
        q95_0=sample['outq95_0']
        tgt_before = sample['q95_0']
        break

print('#' * 80)
print("CCNOT operation on q0_8 (control1), q94_0 (control2) and q95_0 (target):")
print("    in:  q0_8={0}, q94_0={1}, q95_0={2}".format(q0_8,q94_0,tgt_before))
print("    out: q0_8={0}, q94_0={1}, q95_0={2}".format(q0_8,q94_0,q95_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_8 control2: q94_0 target: q95_0 ##
################################################################################
if 'q1_8' not in globals():
    q1_8=0
if 'q94_0' not in globals():
    q94_0=0
if 'q95_0' not in globals():
    q95_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq95_0' : 1, 'q95_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq95_0') : 4, ('anc1','q95_0') : -4, ('anc2', 'q1_8') : -2, ('anc2', 'q94_0') : -2, ('anc2', 'outq95_0') : -2, ('anc2', 'q95_0') : 2, ('q1_8', 'q94_0') : 1, ('outq95_0', 'q95_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_8']==q1_8 and sample['q94_0']==q94_0 and sample['q95_0']==q95_0 and int(energy)==0:
        q1_8=sample['q1_8']
        q94_0=sample['q94_0']
        q95_0=sample['outq95_0']
        tgt_before = sample['q95_0']
        break

print('#' * 80)
print("CCNOT operation on q1_8 (control1), q94_0 (control2) and q95_0 (target):")
print("    in:  q1_8={0}, q94_0={1}, q95_0={2}".format(q1_8,q94_0,tgt_before))
print("    out: q1_8={0}, q94_0={1}, q95_0={2}".format(q1_8,q94_0,q95_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q95_0 target: q96_0 ##
################################################################################
if 'q95_0' not in globals():
    q95_0=0
if 'q96_0' not in globals():
    q96_0=0

bqm = dimod.BinaryQuadraticModel({'q95_0' : 1, 'q96_0' : 1, 'outq96_0' : 1, 'anc' : 4}, {('q95_0', 'q96_0') : 2, ('q95_0', 'outq96_0') : -2, ('q96_0', 'outq96_0') : -2, ('q95_0', 'anc') : -4, ('q96_0', 'anc') : -4, ('outq96_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q95_0']==q95_0 and sample['q96_0']==q96_0 and int(energy)==0:
        q95_0=sample['q95_0']
        q96_0=sample['outq96_0']
        tgt_before = sample['q96_0']
        break

print('#' * 80)
print("CNOT operation on q95_0 (control) and q96_0 (target):")
print("    in:  q95_0={0}, q96_0={1}".format(q95_0,tgt_before))
print("    out: q95_0={0}, q96_0={1}".format(q95_0,q96_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_7 control2: q95_0 target: q96_0 ##
################################################################################
if 'q0_7' not in globals():
    q0_7=0
if 'q95_0' not in globals():
    q95_0=0
if 'q96_0' not in globals():
    q96_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq96_0' : 1, 'q96_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq96_0') : 4, ('anc1','q96_0') : -4, ('anc2', 'q0_7') : -2, ('anc2', 'q95_0') : -2, ('anc2', 'outq96_0') : -2, ('anc2', 'q96_0') : 2, ('q0_7', 'q95_0') : 1, ('outq96_0', 'q96_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_7']==q0_7 and sample['q95_0']==q95_0 and sample['q96_0']==q96_0 and int(energy)==0:
        q0_7=sample['q0_7']
        q95_0=sample['q95_0']
        q96_0=sample['outq96_0']
        tgt_before = sample['q96_0']
        break

print('#' * 80)
print("CCNOT operation on q0_7 (control1), q95_0 (control2) and q96_0 (target):")
print("    in:  q0_7={0}, q95_0={1}, q96_0={2}".format(q0_7,q95_0,tgt_before))
print("    out: q0_7={0}, q95_0={1}, q96_0={2}".format(q0_7,q95_0,q96_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_7 control2: q95_0 target: q96_0 ##
################################################################################
if 'q1_7' not in globals():
    q1_7=0
if 'q95_0' not in globals():
    q95_0=0
if 'q96_0' not in globals():
    q96_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq96_0' : 1, 'q96_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq96_0') : 4, ('anc1','q96_0') : -4, ('anc2', 'q1_7') : -2, ('anc2', 'q95_0') : -2, ('anc2', 'outq96_0') : -2, ('anc2', 'q96_0') : 2, ('q1_7', 'q95_0') : 1, ('outq96_0', 'q96_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_7']==q1_7 and sample['q95_0']==q95_0 and sample['q96_0']==q96_0 and int(energy)==0:
        q1_7=sample['q1_7']
        q95_0=sample['q95_0']
        q96_0=sample['outq96_0']
        tgt_before = sample['q96_0']
        break

print('#' * 80)
print("CCNOT operation on q1_7 (control1), q95_0 (control2) and q96_0 (target):")
print("    in:  q1_7={0}, q95_0={1}, q96_0={2}".format(q1_7,q95_0,tgt_before))
print("    out: q1_7={0}, q95_0={1}, q96_0={2}".format(q1_7,q95_0,q96_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q96_0 target: q97_0 ##
################################################################################
if 'q96_0' not in globals():
    q96_0=0
if 'q97_0' not in globals():
    q97_0=0

bqm = dimod.BinaryQuadraticModel({'q96_0' : 1, 'q97_0' : 1, 'outq97_0' : 1, 'anc' : 4}, {('q96_0', 'q97_0') : 2, ('q96_0', 'outq97_0') : -2, ('q97_0', 'outq97_0') : -2, ('q96_0', 'anc') : -4, ('q97_0', 'anc') : -4, ('outq97_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q96_0']==q96_0 and sample['q97_0']==q97_0 and int(energy)==0:
        q96_0=sample['q96_0']
        q97_0=sample['outq97_0']
        tgt_before = sample['q97_0']
        break

print('#' * 80)
print("CNOT operation on q96_0 (control) and q97_0 (target):")
print("    in:  q96_0={0}, q97_0={1}".format(q96_0,tgt_before))
print("    out: q96_0={0}, q97_0={1}".format(q96_0,q97_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_6 control2: q96_0 target: q97_0 ##
################################################################################
if 'q0_6' not in globals():
    q0_6=0
if 'q96_0' not in globals():
    q96_0=0
if 'q97_0' not in globals():
    q97_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq97_0' : 1, 'q97_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq97_0') : 4, ('anc1','q97_0') : -4, ('anc2', 'q0_6') : -2, ('anc2', 'q96_0') : -2, ('anc2', 'outq97_0') : -2, ('anc2', 'q97_0') : 2, ('q0_6', 'q96_0') : 1, ('outq97_0', 'q97_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_6']==q0_6 and sample['q96_0']==q96_0 and sample['q97_0']==q97_0 and int(energy)==0:
        q0_6=sample['q0_6']
        q96_0=sample['q96_0']
        q97_0=sample['outq97_0']
        tgt_before = sample['q97_0']
        break

print('#' * 80)
print("CCNOT operation on q0_6 (control1), q96_0 (control2) and q97_0 (target):")
print("    in:  q0_6={0}, q96_0={1}, q97_0={2}".format(q0_6,q96_0,tgt_before))
print("    out: q0_6={0}, q96_0={1}, q97_0={2}".format(q0_6,q96_0,q97_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_6 control2: q96_0 target: q97_0 ##
################################################################################
if 'q1_6' not in globals():
    q1_6=0
if 'q96_0' not in globals():
    q96_0=0
if 'q97_0' not in globals():
    q97_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq97_0' : 1, 'q97_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq97_0') : 4, ('anc1','q97_0') : -4, ('anc2', 'q1_6') : -2, ('anc2', 'q96_0') : -2, ('anc2', 'outq97_0') : -2, ('anc2', 'q97_0') : 2, ('q1_6', 'q96_0') : 1, ('outq97_0', 'q97_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_6']==q1_6 and sample['q96_0']==q96_0 and sample['q97_0']==q97_0 and int(energy)==0:
        q1_6=sample['q1_6']
        q96_0=sample['q96_0']
        q97_0=sample['outq97_0']
        tgt_before = sample['q97_0']
        break

print('#' * 80)
print("CCNOT operation on q1_6 (control1), q96_0 (control2) and q97_0 (target):")
print("    in:  q1_6={0}, q96_0={1}, q97_0={2}".format(q1_6,q96_0,tgt_before))
print("    out: q1_6={0}, q96_0={1}, q97_0={2}".format(q1_6,q96_0,q97_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q97_0 target: q98_0 ##
################################################################################
if 'q97_0' not in globals():
    q97_0=0
if 'q98_0' not in globals():
    q98_0=0

bqm = dimod.BinaryQuadraticModel({'q97_0' : 1, 'q98_0' : 1, 'outq98_0' : 1, 'anc' : 4}, {('q97_0', 'q98_0') : 2, ('q97_0', 'outq98_0') : -2, ('q98_0', 'outq98_0') : -2, ('q97_0', 'anc') : -4, ('q98_0', 'anc') : -4, ('outq98_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q97_0']==q97_0 and sample['q98_0']==q98_0 and int(energy)==0:
        q97_0=sample['q97_0']
        q98_0=sample['outq98_0']
        tgt_before = sample['q98_0']
        break

print('#' * 80)
print("CNOT operation on q97_0 (control) and q98_0 (target):")
print("    in:  q97_0={0}, q98_0={1}".format(q97_0,tgt_before))
print("    out: q97_0={0}, q98_0={1}".format(q97_0,q98_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_5 control2: q97_0 target: q98_0 ##
################################################################################
if 'q0_5' not in globals():
    q0_5=0
if 'q97_0' not in globals():
    q97_0=0
if 'q98_0' not in globals():
    q98_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq98_0' : 1, 'q98_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq98_0') : 4, ('anc1','q98_0') : -4, ('anc2', 'q0_5') : -2, ('anc2', 'q97_0') : -2, ('anc2', 'outq98_0') : -2, ('anc2', 'q98_0') : 2, ('q0_5', 'q97_0') : 1, ('outq98_0', 'q98_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_5']==q0_5 and sample['q97_0']==q97_0 and sample['q98_0']==q98_0 and int(energy)==0:
        q0_5=sample['q0_5']
        q97_0=sample['q97_0']
        q98_0=sample['outq98_0']
        tgt_before = sample['q98_0']
        break

print('#' * 80)
print("CCNOT operation on q0_5 (control1), q97_0 (control2) and q98_0 (target):")
print("    in:  q0_5={0}, q97_0={1}, q98_0={2}".format(q0_5,q97_0,tgt_before))
print("    out: q0_5={0}, q97_0={1}, q98_0={2}".format(q0_5,q97_0,q98_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_5 control2: q97_0 target: q98_0 ##
################################################################################
if 'q1_5' not in globals():
    q1_5=0
if 'q97_0' not in globals():
    q97_0=0
if 'q98_0' not in globals():
    q98_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq98_0' : 1, 'q98_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq98_0') : 4, ('anc1','q98_0') : -4, ('anc2', 'q1_5') : -2, ('anc2', 'q97_0') : -2, ('anc2', 'outq98_0') : -2, ('anc2', 'q98_0') : 2, ('q1_5', 'q97_0') : 1, ('outq98_0', 'q98_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_5']==q1_5 and sample['q97_0']==q97_0 and sample['q98_0']==q98_0 and int(energy)==0:
        q1_5=sample['q1_5']
        q97_0=sample['q97_0']
        q98_0=sample['outq98_0']
        tgt_before = sample['q98_0']
        break

print('#' * 80)
print("CCNOT operation on q1_5 (control1), q97_0 (control2) and q98_0 (target):")
print("    in:  q1_5={0}, q97_0={1}, q98_0={2}".format(q1_5,q97_0,tgt_before))
print("    out: q1_5={0}, q97_0={1}, q98_0={2}".format(q1_5,q97_0,q98_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q98_0 target: q99_0 ##
################################################################################
if 'q98_0' not in globals():
    q98_0=0
if 'q99_0' not in globals():
    q99_0=0

bqm = dimod.BinaryQuadraticModel({'q98_0' : 1, 'q99_0' : 1, 'outq99_0' : 1, 'anc' : 4}, {('q98_0', 'q99_0') : 2, ('q98_0', 'outq99_0') : -2, ('q99_0', 'outq99_0') : -2, ('q98_0', 'anc') : -4, ('q99_0', 'anc') : -4, ('outq99_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q98_0']==q98_0 and sample['q99_0']==q99_0 and int(energy)==0:
        q98_0=sample['q98_0']
        q99_0=sample['outq99_0']
        tgt_before = sample['q99_0']
        break

print('#' * 80)
print("CNOT operation on q98_0 (control) and q99_0 (target):")
print("    in:  q98_0={0}, q99_0={1}".format(q98_0,tgt_before))
print("    out: q98_0={0}, q99_0={1}".format(q98_0,q99_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_4 control2: q98_0 target: q99_0 ##
################################################################################
if 'q0_4' not in globals():
    q0_4=0
if 'q98_0' not in globals():
    q98_0=0
if 'q99_0' not in globals():
    q99_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq99_0' : 1, 'q99_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq99_0') : 4, ('anc1','q99_0') : -4, ('anc2', 'q0_4') : -2, ('anc2', 'q98_0') : -2, ('anc2', 'outq99_0') : -2, ('anc2', 'q99_0') : 2, ('q0_4', 'q98_0') : 1, ('outq99_0', 'q99_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_4']==q0_4 and sample['q98_0']==q98_0 and sample['q99_0']==q99_0 and int(energy)==0:
        q0_4=sample['q0_4']
        q98_0=sample['q98_0']
        q99_0=sample['outq99_0']
        tgt_before = sample['q99_0']
        break

print('#' * 80)
print("CCNOT operation on q0_4 (control1), q98_0 (control2) and q99_0 (target):")
print("    in:  q0_4={0}, q98_0={1}, q99_0={2}".format(q0_4,q98_0,tgt_before))
print("    out: q0_4={0}, q98_0={1}, q99_0={2}".format(q0_4,q98_0,q99_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_4 control2: q98_0 target: q99_0 ##
################################################################################
if 'q1_4' not in globals():
    q1_4=0
if 'q98_0' not in globals():
    q98_0=0
if 'q99_0' not in globals():
    q99_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq99_0' : 1, 'q99_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq99_0') : 4, ('anc1','q99_0') : -4, ('anc2', 'q1_4') : -2, ('anc2', 'q98_0') : -2, ('anc2', 'outq99_0') : -2, ('anc2', 'q99_0') : 2, ('q1_4', 'q98_0') : 1, ('outq99_0', 'q99_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_4']==q1_4 and sample['q98_0']==q98_0 and sample['q99_0']==q99_0 and int(energy)==0:
        q1_4=sample['q1_4']
        q98_0=sample['q98_0']
        q99_0=sample['outq99_0']
        tgt_before = sample['q99_0']
        break

print('#' * 80)
print("CCNOT operation on q1_4 (control1), q98_0 (control2) and q99_0 (target):")
print("    in:  q1_4={0}, q98_0={1}, q99_0={2}".format(q1_4,q98_0,tgt_before))
print("    out: q1_4={0}, q98_0={1}, q99_0={2}".format(q1_4,q98_0,q99_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q99_0 target: q100_0 ##
################################################################################
if 'q99_0' not in globals():
    q99_0=0
if 'q100_0' not in globals():
    q100_0=0

bqm = dimod.BinaryQuadraticModel({'q99_0' : 1, 'q100_0' : 1, 'outq100_0' : 1, 'anc' : 4}, {('q99_0', 'q100_0') : 2, ('q99_0', 'outq100_0') : -2, ('q100_0', 'outq100_0') : -2, ('q99_0', 'anc') : -4, ('q100_0', 'anc') : -4, ('outq100_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q99_0']==q99_0 and sample['q100_0']==q100_0 and int(energy)==0:
        q99_0=sample['q99_0']
        q100_0=sample['outq100_0']
        tgt_before = sample['q100_0']
        break

print('#' * 80)
print("CNOT operation on q99_0 (control) and q100_0 (target):")
print("    in:  q99_0={0}, q100_0={1}".format(q99_0,tgt_before))
print("    out: q99_0={0}, q100_0={1}".format(q99_0,q100_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_3 control2: q99_0 target: q100_0 ##
################################################################################
if 'q0_3' not in globals():
    q0_3=0
if 'q99_0' not in globals():
    q99_0=0
if 'q100_0' not in globals():
    q100_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq100_0' : 1, 'q100_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq100_0') : 4, ('anc1','q100_0') : -4, ('anc2', 'q0_3') : -2, ('anc2', 'q99_0') : -2, ('anc2', 'outq100_0') : -2, ('anc2', 'q100_0') : 2, ('q0_3', 'q99_0') : 1, ('outq100_0', 'q100_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_3']==q0_3 and sample['q99_0']==q99_0 and sample['q100_0']==q100_0 and int(energy)==0:
        q0_3=sample['q0_3']
        q99_0=sample['q99_0']
        q100_0=sample['outq100_0']
        tgt_before = sample['q100_0']
        break

print('#' * 80)
print("CCNOT operation on q0_3 (control1), q99_0 (control2) and q100_0 (target):")
print("    in:  q0_3={0}, q99_0={1}, q100_0={2}".format(q0_3,q99_0,tgt_before))
print("    out: q0_3={0}, q99_0={1}, q100_0={2}".format(q0_3,q99_0,q100_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_3 control2: q99_0 target: q100_0 ##
################################################################################
if 'q1_3' not in globals():
    q1_3=0
if 'q99_0' not in globals():
    q99_0=0
if 'q100_0' not in globals():
    q100_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq100_0' : 1, 'q100_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq100_0') : 4, ('anc1','q100_0') : -4, ('anc2', 'q1_3') : -2, ('anc2', 'q99_0') : -2, ('anc2', 'outq100_0') : -2, ('anc2', 'q100_0') : 2, ('q1_3', 'q99_0') : 1, ('outq100_0', 'q100_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_3']==q1_3 and sample['q99_0']==q99_0 and sample['q100_0']==q100_0 and int(energy)==0:
        q1_3=sample['q1_3']
        q99_0=sample['q99_0']
        q100_0=sample['outq100_0']
        tgt_before = sample['q100_0']
        break

print('#' * 80)
print("CCNOT operation on q1_3 (control1), q99_0 (control2) and q100_0 (target):")
print("    in:  q1_3={0}, q99_0={1}, q100_0={2}".format(q1_3,q99_0,tgt_before))
print("    out: q1_3={0}, q99_0={1}, q100_0={2}".format(q1_3,q99_0,q100_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q100_0 target: q101_0 ##
################################################################################
if 'q100_0' not in globals():
    q100_0=0
if 'q101_0' not in globals():
    q101_0=0

bqm = dimod.BinaryQuadraticModel({'q100_0' : 1, 'q101_0' : 1, 'outq101_0' : 1, 'anc' : 4}, {('q100_0', 'q101_0') : 2, ('q100_0', 'outq101_0') : -2, ('q101_0', 'outq101_0') : -2, ('q100_0', 'anc') : -4, ('q101_0', 'anc') : -4, ('outq101_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q100_0']==q100_0 and sample['q101_0']==q101_0 and int(energy)==0:
        q100_0=sample['q100_0']
        q101_0=sample['outq101_0']
        tgt_before = sample['q101_0']
        break

print('#' * 80)
print("CNOT operation on q100_0 (control) and q101_0 (target):")
print("    in:  q100_0={0}, q101_0={1}".format(q100_0,tgt_before))
print("    out: q100_0={0}, q101_0={1}".format(q100_0,q101_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_2 control2: q100_0 target: q101_0 ##
################################################################################
if 'q0_2' not in globals():
    q0_2=0
if 'q100_0' not in globals():
    q100_0=0
if 'q101_0' not in globals():
    q101_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq101_0' : 1, 'q101_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq101_0') : 4, ('anc1','q101_0') : -4, ('anc2', 'q0_2') : -2, ('anc2', 'q100_0') : -2, ('anc2', 'outq101_0') : -2, ('anc2', 'q101_0') : 2, ('q0_2', 'q100_0') : 1, ('outq101_0', 'q101_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_2']==q0_2 and sample['q100_0']==q100_0 and sample['q101_0']==q101_0 and int(energy)==0:
        q0_2=sample['q0_2']
        q100_0=sample['q100_0']
        q101_0=sample['outq101_0']
        tgt_before = sample['q101_0']
        break

print('#' * 80)
print("CCNOT operation on q0_2 (control1), q100_0 (control2) and q101_0 (target):")
print("    in:  q0_2={0}, q100_0={1}, q101_0={2}".format(q0_2,q100_0,tgt_before))
print("    out: q0_2={0}, q100_0={1}, q101_0={2}".format(q0_2,q100_0,q101_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_2 control2: q100_0 target: q101_0 ##
################################################################################
if 'q1_2' not in globals():
    q1_2=0
if 'q100_0' not in globals():
    q100_0=0
if 'q101_0' not in globals():
    q101_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq101_0' : 1, 'q101_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq101_0') : 4, ('anc1','q101_0') : -4, ('anc2', 'q1_2') : -2, ('anc2', 'q100_0') : -2, ('anc2', 'outq101_0') : -2, ('anc2', 'q101_0') : 2, ('q1_2', 'q100_0') : 1, ('outq101_0', 'q101_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_2']==q1_2 and sample['q100_0']==q100_0 and sample['q101_0']==q101_0 and int(energy)==0:
        q1_2=sample['q1_2']
        q100_0=sample['q100_0']
        q101_0=sample['outq101_0']
        tgt_before = sample['q101_0']
        break

print('#' * 80)
print("CCNOT operation on q1_2 (control1), q100_0 (control2) and q101_0 (target):")
print("    in:  q1_2={0}, q100_0={1}, q101_0={2}".format(q1_2,q100_0,tgt_before))
print("    out: q1_2={0}, q100_0={1}, q101_0={2}".format(q1_2,q100_0,q101_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q101_0 target: q102_0 ##
################################################################################
if 'q101_0' not in globals():
    q101_0=0
if 'q102_0' not in globals():
    q102_0=0

bqm = dimod.BinaryQuadraticModel({'q101_0' : 1, 'q102_0' : 1, 'outq102_0' : 1, 'anc' : 4}, {('q101_0', 'q102_0') : 2, ('q101_0', 'outq102_0') : -2, ('q102_0', 'outq102_0') : -2, ('q101_0', 'anc') : -4, ('q102_0', 'anc') : -4, ('outq102_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q101_0']==q101_0 and sample['q102_0']==q102_0 and int(energy)==0:
        q101_0=sample['q101_0']
        q102_0=sample['outq102_0']
        tgt_before = sample['q102_0']
        break

print('#' * 80)
print("CNOT operation on q101_0 (control) and q102_0 (target):")
print("    in:  q101_0={0}, q102_0={1}".format(q101_0,tgt_before))
print("    out: q101_0={0}, q102_0={1}".format(q101_0,q102_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_1 control2: q101_0 target: q102_0 ##
################################################################################
if 'q0_1' not in globals():
    q0_1=0
if 'q101_0' not in globals():
    q101_0=0
if 'q102_0' not in globals():
    q102_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq102_0' : 1, 'q102_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq102_0') : 4, ('anc1','q102_0') : -4, ('anc2', 'q0_1') : -2, ('anc2', 'q101_0') : -2, ('anc2', 'outq102_0') : -2, ('anc2', 'q102_0') : 2, ('q0_1', 'q101_0') : 1, ('outq102_0', 'q102_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_1']==q0_1 and sample['q101_0']==q101_0 and sample['q102_0']==q102_0 and int(energy)==0:
        q0_1=sample['q0_1']
        q101_0=sample['q101_0']
        q102_0=sample['outq102_0']
        tgt_before = sample['q102_0']
        break

print('#' * 80)
print("CCNOT operation on q0_1 (control1), q101_0 (control2) and q102_0 (target):")
print("    in:  q0_1={0}, q101_0={1}, q102_0={2}".format(q0_1,q101_0,tgt_before))
print("    out: q0_1={0}, q101_0={1}, q102_0={2}".format(q0_1,q101_0,q102_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_1 control2: q101_0 target: q102_0 ##
################################################################################
if 'q1_1' not in globals():
    q1_1=0
if 'q101_0' not in globals():
    q101_0=0
if 'q102_0' not in globals():
    q102_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq102_0' : 1, 'q102_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq102_0') : 4, ('anc1','q102_0') : -4, ('anc2', 'q1_1') : -2, ('anc2', 'q101_0') : -2, ('anc2', 'outq102_0') : -2, ('anc2', 'q102_0') : 2, ('q1_1', 'q101_0') : 1, ('outq102_0', 'q102_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_1']==q1_1 and sample['q101_0']==q101_0 and sample['q102_0']==q102_0 and int(energy)==0:
        q1_1=sample['q1_1']
        q101_0=sample['q101_0']
        q102_0=sample['outq102_0']
        tgt_before = sample['q102_0']
        break

print('#' * 80)
print("CCNOT operation on q1_1 (control1), q101_0 (control2) and q102_0 (target):")
print("    in:  q1_1={0}, q101_0={1}, q102_0={2}".format(q1_1,q101_0,tgt_before))
print("    out: q1_1={0}, q101_0={1}, q102_0={2}".format(q1_1,q101_0,q102_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q102_0 target: q2_0 ##
################################################################################
if 'q102_0' not in globals():
    q102_0=0
if 'q2_0' not in globals():
    q2_0=0

bqm = dimod.BinaryQuadraticModel({'q102_0' : 1, 'q2_0' : 1, 'outq2_0' : 1, 'anc' : 4}, {('q102_0', 'q2_0') : 2, ('q102_0', 'outq2_0') : -2, ('q2_0', 'outq2_0') : -2, ('q102_0', 'anc') : -4, ('q2_0', 'anc') : -4, ('outq2_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q102_0']==q102_0 and sample['q2_0']==q2_0 and int(energy)==0:
        q102_0=sample['q102_0']
        q2_0=sample['outq2_0']
        tgt_before = sample['q2_0']
        break

print('#' * 80)
print("CNOT operation on q102_0 (control) and q2_0 (target):")
print("    in:  q102_0={0}, q2_0={1}".format(q102_0,tgt_before))
print("    out: q102_0={0}, q2_0={1}".format(q102_0,q2_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_0 control2: q102_0 target: q2_0 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q102_0' not in globals():
    q102_0=0
if 'q2_0' not in globals():
    q2_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq2_0' : 1, 'q2_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq2_0') : 4, ('anc1','q2_0') : -4, ('anc2', 'q0_0') : -2, ('anc2', 'q102_0') : -2, ('anc2', 'outq2_0') : -2, ('anc2', 'q2_0') : 2, ('q0_0', 'q102_0') : 1, ('outq2_0', 'q2_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_0']==q0_0 and sample['q102_0']==q102_0 and sample['q2_0']==q2_0 and int(energy)==0:
        q0_0=sample['q0_0']
        q102_0=sample['q102_0']
        q2_0=sample['outq2_0']
        tgt_before = sample['q2_0']
        break

print('#' * 80)
print("CCNOT operation on q0_0 (control1), q102_0 (control2) and q2_0 (target):")
print("    in:  q0_0={0}, q102_0={1}, q2_0={2}".format(q0_0,q102_0,tgt_before))
print("    out: q0_0={0}, q102_0={1}, q2_0={2}".format(q0_0,q102_0,q2_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_0 control2: q102_0 target: q2_0 ##
################################################################################
if 'q1_0' not in globals():
    q1_0=0
if 'q102_0' not in globals():
    q102_0=0
if 'q2_0' not in globals():
    q2_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq2_0' : 1, 'q2_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq2_0') : 4, ('anc1','q2_0') : -4, ('anc2', 'q1_0') : -2, ('anc2', 'q102_0') : -2, ('anc2', 'outq2_0') : -2, ('anc2', 'q2_0') : 2, ('q1_0', 'q102_0') : 1, ('outq2_0', 'q2_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_0']==q1_0 and sample['q102_0']==q102_0 and sample['q2_0']==q2_0 and int(energy)==0:
        q1_0=sample['q1_0']
        q102_0=sample['q102_0']
        q2_0=sample['outq2_0']
        tgt_before = sample['q2_0']
        break

print('#' * 80)
print("CCNOT operation on q1_0 (control1), q102_0 (control2) and q2_0 (target):")
print("    in:  q1_0={0}, q102_0={1}, q2_0={2}".format(q1_0,q102_0,tgt_before))
print("    out: q1_0={0}, q102_0={1}, q2_0={2}".format(q1_0,q102_0,q2_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_1 control2: q101_0 target: q102_0 ##
################################################################################
if 'q1_1' not in globals():
    q1_1=0
if 'q101_0' not in globals():
    q101_0=0
if 'q102_0' not in globals():
    q102_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq102_0' : 1, 'q102_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq102_0') : 4, ('anc1','q102_0') : -4, ('anc2', 'q1_1') : -2, ('anc2', 'q101_0') : -2, ('anc2', 'outq102_0') : -2, ('anc2', 'q102_0') : 2, ('q1_1', 'q101_0') : 1, ('outq102_0', 'q102_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_1']==q1_1 and sample['q101_0']==q101_0 and sample['q102_0']==q102_0 and int(energy)==0:
        q1_1=sample['q1_1']
        q101_0=sample['q101_0']
        q102_0=sample['outq102_0']
        tgt_before = sample['q102_0']
        break

print('#' * 80)
print("CCNOT operation on q1_1 (control1), q101_0 (control2) and q102_0 (target):")
print("    in:  q1_1={0}, q101_0={1}, q102_0={2}".format(q1_1,q101_0,tgt_before))
print("    out: q1_1={0}, q101_0={1}, q102_0={2}".format(q1_1,q101_0,q102_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_1 control2: q101_0 target: q102_0 ##
################################################################################
if 'q0_1' not in globals():
    q0_1=0
if 'q101_0' not in globals():
    q101_0=0
if 'q102_0' not in globals():
    q102_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq102_0' : 1, 'q102_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq102_0') : 4, ('anc1','q102_0') : -4, ('anc2', 'q0_1') : -2, ('anc2', 'q101_0') : -2, ('anc2', 'outq102_0') : -2, ('anc2', 'q102_0') : 2, ('q0_1', 'q101_0') : 1, ('outq102_0', 'q102_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_1']==q0_1 and sample['q101_0']==q101_0 and sample['q102_0']==q102_0 and int(energy)==0:
        q0_1=sample['q0_1']
        q101_0=sample['q101_0']
        q102_0=sample['outq102_0']
        tgt_before = sample['q102_0']
        break

print('#' * 80)
print("CCNOT operation on q0_1 (control1), q101_0 (control2) and q102_0 (target):")
print("    in:  q0_1={0}, q101_0={1}, q102_0={2}".format(q0_1,q101_0,tgt_before))
print("    out: q0_1={0}, q101_0={1}, q102_0={2}".format(q0_1,q101_0,q102_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q101_0 target: q102_0 ##
################################################################################
if 'q101_0' not in globals():
    q101_0=0
if 'q102_0' not in globals():
    q102_0=0

bqm = dimod.BinaryQuadraticModel({'q101_0' : 1, 'q102_0' : 1, 'outq102_0' : 1, 'anc' : 4}, {('q101_0', 'q102_0') : 2, ('q101_0', 'outq102_0') : -2, ('q102_0', 'outq102_0') : -2, ('q101_0', 'anc') : -4, ('q102_0', 'anc') : -4, ('outq102_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q101_0']==q101_0 and sample['q102_0']==q102_0 and int(energy)==0:
        q101_0=sample['q101_0']
        q102_0=sample['outq102_0']
        tgt_before = sample['q102_0']
        break

print('#' * 80)
print("CNOT operation on q101_0 (control) and q102_0 (target):")
print("    in:  q101_0={0}, q102_0={1}".format(q101_0,tgt_before))
print("    out: q101_0={0}, q102_0={1}".format(q101_0,q102_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_2 control2: q100_0 target: q101_0 ##
################################################################################
if 'q1_2' not in globals():
    q1_2=0
if 'q100_0' not in globals():
    q100_0=0
if 'q101_0' not in globals():
    q101_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq101_0' : 1, 'q101_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq101_0') : 4, ('anc1','q101_0') : -4, ('anc2', 'q1_2') : -2, ('anc2', 'q100_0') : -2, ('anc2', 'outq101_0') : -2, ('anc2', 'q101_0') : 2, ('q1_2', 'q100_0') : 1, ('outq101_0', 'q101_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_2']==q1_2 and sample['q100_0']==q100_0 and sample['q101_0']==q101_0 and int(energy)==0:
        q1_2=sample['q1_2']
        q100_0=sample['q100_0']
        q101_0=sample['outq101_0']
        tgt_before = sample['q101_0']
        break

print('#' * 80)
print("CCNOT operation on q1_2 (control1), q100_0 (control2) and q101_0 (target):")
print("    in:  q1_2={0}, q100_0={1}, q101_0={2}".format(q1_2,q100_0,tgt_before))
print("    out: q1_2={0}, q100_0={1}, q101_0={2}".format(q1_2,q100_0,q101_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_2 control2: q100_0 target: q101_0 ##
################################################################################
if 'q0_2' not in globals():
    q0_2=0
if 'q100_0' not in globals():
    q100_0=0
if 'q101_0' not in globals():
    q101_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq101_0' : 1, 'q101_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq101_0') : 4, ('anc1','q101_0') : -4, ('anc2', 'q0_2') : -2, ('anc2', 'q100_0') : -2, ('anc2', 'outq101_0') : -2, ('anc2', 'q101_0') : 2, ('q0_2', 'q100_0') : 1, ('outq101_0', 'q101_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_2']==q0_2 and sample['q100_0']==q100_0 and sample['q101_0']==q101_0 and int(energy)==0:
        q0_2=sample['q0_2']
        q100_0=sample['q100_0']
        q101_0=sample['outq101_0']
        tgt_before = sample['q101_0']
        break

print('#' * 80)
print("CCNOT operation on q0_2 (control1), q100_0 (control2) and q101_0 (target):")
print("    in:  q0_2={0}, q100_0={1}, q101_0={2}".format(q0_2,q100_0,tgt_before))
print("    out: q0_2={0}, q100_0={1}, q101_0={2}".format(q0_2,q100_0,q101_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q100_0 target: q101_0 ##
################################################################################
if 'q100_0' not in globals():
    q100_0=0
if 'q101_0' not in globals():
    q101_0=0

bqm = dimod.BinaryQuadraticModel({'q100_0' : 1, 'q101_0' : 1, 'outq101_0' : 1, 'anc' : 4}, {('q100_0', 'q101_0') : 2, ('q100_0', 'outq101_0') : -2, ('q101_0', 'outq101_0') : -2, ('q100_0', 'anc') : -4, ('q101_0', 'anc') : -4, ('outq101_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q100_0']==q100_0 and sample['q101_0']==q101_0 and int(energy)==0:
        q100_0=sample['q100_0']
        q101_0=sample['outq101_0']
        tgt_before = sample['q101_0']
        break

print('#' * 80)
print("CNOT operation on q100_0 (control) and q101_0 (target):")
print("    in:  q100_0={0}, q101_0={1}".format(q100_0,tgt_before))
print("    out: q100_0={0}, q101_0={1}".format(q100_0,q101_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_3 control2: q99_0 target: q100_0 ##
################################################################################
if 'q1_3' not in globals():
    q1_3=0
if 'q99_0' not in globals():
    q99_0=0
if 'q100_0' not in globals():
    q100_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq100_0' : 1, 'q100_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq100_0') : 4, ('anc1','q100_0') : -4, ('anc2', 'q1_3') : -2, ('anc2', 'q99_0') : -2, ('anc2', 'outq100_0') : -2, ('anc2', 'q100_0') : 2, ('q1_3', 'q99_0') : 1, ('outq100_0', 'q100_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_3']==q1_3 and sample['q99_0']==q99_0 and sample['q100_0']==q100_0 and int(energy)==0:
        q1_3=sample['q1_3']
        q99_0=sample['q99_0']
        q100_0=sample['outq100_0']
        tgt_before = sample['q100_0']
        break

print('#' * 80)
print("CCNOT operation on q1_3 (control1), q99_0 (control2) and q100_0 (target):")
print("    in:  q1_3={0}, q99_0={1}, q100_0={2}".format(q1_3,q99_0,tgt_before))
print("    out: q1_3={0}, q99_0={1}, q100_0={2}".format(q1_3,q99_0,q100_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_3 control2: q99_0 target: q100_0 ##
################################################################################
if 'q0_3' not in globals():
    q0_3=0
if 'q99_0' not in globals():
    q99_0=0
if 'q100_0' not in globals():
    q100_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq100_0' : 1, 'q100_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq100_0') : 4, ('anc1','q100_0') : -4, ('anc2', 'q0_3') : -2, ('anc2', 'q99_0') : -2, ('anc2', 'outq100_0') : -2, ('anc2', 'q100_0') : 2, ('q0_3', 'q99_0') : 1, ('outq100_0', 'q100_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_3']==q0_3 and sample['q99_0']==q99_0 and sample['q100_0']==q100_0 and int(energy)==0:
        q0_3=sample['q0_3']
        q99_0=sample['q99_0']
        q100_0=sample['outq100_0']
        tgt_before = sample['q100_0']
        break

print('#' * 80)
print("CCNOT operation on q0_3 (control1), q99_0 (control2) and q100_0 (target):")
print("    in:  q0_3={0}, q99_0={1}, q100_0={2}".format(q0_3,q99_0,tgt_before))
print("    out: q0_3={0}, q99_0={1}, q100_0={2}".format(q0_3,q99_0,q100_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q99_0 target: q100_0 ##
################################################################################
if 'q99_0' not in globals():
    q99_0=0
if 'q100_0' not in globals():
    q100_0=0

bqm = dimod.BinaryQuadraticModel({'q99_0' : 1, 'q100_0' : 1, 'outq100_0' : 1, 'anc' : 4}, {('q99_0', 'q100_0') : 2, ('q99_0', 'outq100_0') : -2, ('q100_0', 'outq100_0') : -2, ('q99_0', 'anc') : -4, ('q100_0', 'anc') : -4, ('outq100_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q99_0']==q99_0 and sample['q100_0']==q100_0 and int(energy)==0:
        q99_0=sample['q99_0']
        q100_0=sample['outq100_0']
        tgt_before = sample['q100_0']
        break

print('#' * 80)
print("CNOT operation on q99_0 (control) and q100_0 (target):")
print("    in:  q99_0={0}, q100_0={1}".format(q99_0,tgt_before))
print("    out: q99_0={0}, q100_0={1}".format(q99_0,q100_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_4 control2: q98_0 target: q99_0 ##
################################################################################
if 'q1_4' not in globals():
    q1_4=0
if 'q98_0' not in globals():
    q98_0=0
if 'q99_0' not in globals():
    q99_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq99_0' : 1, 'q99_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq99_0') : 4, ('anc1','q99_0') : -4, ('anc2', 'q1_4') : -2, ('anc2', 'q98_0') : -2, ('anc2', 'outq99_0') : -2, ('anc2', 'q99_0') : 2, ('q1_4', 'q98_0') : 1, ('outq99_0', 'q99_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_4']==q1_4 and sample['q98_0']==q98_0 and sample['q99_0']==q99_0 and int(energy)==0:
        q1_4=sample['q1_4']
        q98_0=sample['q98_0']
        q99_0=sample['outq99_0']
        tgt_before = sample['q99_0']
        break

print('#' * 80)
print("CCNOT operation on q1_4 (control1), q98_0 (control2) and q99_0 (target):")
print("    in:  q1_4={0}, q98_0={1}, q99_0={2}".format(q1_4,q98_0,tgt_before))
print("    out: q1_4={0}, q98_0={1}, q99_0={2}".format(q1_4,q98_0,q99_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_4 control2: q98_0 target: q99_0 ##
################################################################################
if 'q0_4' not in globals():
    q0_4=0
if 'q98_0' not in globals():
    q98_0=0
if 'q99_0' not in globals():
    q99_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq99_0' : 1, 'q99_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq99_0') : 4, ('anc1','q99_0') : -4, ('anc2', 'q0_4') : -2, ('anc2', 'q98_0') : -2, ('anc2', 'outq99_0') : -2, ('anc2', 'q99_0') : 2, ('q0_4', 'q98_0') : 1, ('outq99_0', 'q99_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_4']==q0_4 and sample['q98_0']==q98_0 and sample['q99_0']==q99_0 and int(energy)==0:
        q0_4=sample['q0_4']
        q98_0=sample['q98_0']
        q99_0=sample['outq99_0']
        tgt_before = sample['q99_0']
        break

print('#' * 80)
print("CCNOT operation on q0_4 (control1), q98_0 (control2) and q99_0 (target):")
print("    in:  q0_4={0}, q98_0={1}, q99_0={2}".format(q0_4,q98_0,tgt_before))
print("    out: q0_4={0}, q98_0={1}, q99_0={2}".format(q0_4,q98_0,q99_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q98_0 target: q99_0 ##
################################################################################
if 'q98_0' not in globals():
    q98_0=0
if 'q99_0' not in globals():
    q99_0=0

bqm = dimod.BinaryQuadraticModel({'q98_0' : 1, 'q99_0' : 1, 'outq99_0' : 1, 'anc' : 4}, {('q98_0', 'q99_0') : 2, ('q98_0', 'outq99_0') : -2, ('q99_0', 'outq99_0') : -2, ('q98_0', 'anc') : -4, ('q99_0', 'anc') : -4, ('outq99_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q98_0']==q98_0 and sample['q99_0']==q99_0 and int(energy)==0:
        q98_0=sample['q98_0']
        q99_0=sample['outq99_0']
        tgt_before = sample['q99_0']
        break

print('#' * 80)
print("CNOT operation on q98_0 (control) and q99_0 (target):")
print("    in:  q98_0={0}, q99_0={1}".format(q98_0,tgt_before))
print("    out: q98_0={0}, q99_0={1}".format(q98_0,q99_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_5 control2: q97_0 target: q98_0 ##
################################################################################
if 'q1_5' not in globals():
    q1_5=0
if 'q97_0' not in globals():
    q97_0=0
if 'q98_0' not in globals():
    q98_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq98_0' : 1, 'q98_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq98_0') : 4, ('anc1','q98_0') : -4, ('anc2', 'q1_5') : -2, ('anc2', 'q97_0') : -2, ('anc2', 'outq98_0') : -2, ('anc2', 'q98_0') : 2, ('q1_5', 'q97_0') : 1, ('outq98_0', 'q98_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_5']==q1_5 and sample['q97_0']==q97_0 and sample['q98_0']==q98_0 and int(energy)==0:
        q1_5=sample['q1_5']
        q97_0=sample['q97_0']
        q98_0=sample['outq98_0']
        tgt_before = sample['q98_0']
        break

print('#' * 80)
print("CCNOT operation on q1_5 (control1), q97_0 (control2) and q98_0 (target):")
print("    in:  q1_5={0}, q97_0={1}, q98_0={2}".format(q1_5,q97_0,tgt_before))
print("    out: q1_5={0}, q97_0={1}, q98_0={2}".format(q1_5,q97_0,q98_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_5 control2: q97_0 target: q98_0 ##
################################################################################
if 'q0_5' not in globals():
    q0_5=0
if 'q97_0' not in globals():
    q97_0=0
if 'q98_0' not in globals():
    q98_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq98_0' : 1, 'q98_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq98_0') : 4, ('anc1','q98_0') : -4, ('anc2', 'q0_5') : -2, ('anc2', 'q97_0') : -2, ('anc2', 'outq98_0') : -2, ('anc2', 'q98_0') : 2, ('q0_5', 'q97_0') : 1, ('outq98_0', 'q98_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_5']==q0_5 and sample['q97_0']==q97_0 and sample['q98_0']==q98_0 and int(energy)==0:
        q0_5=sample['q0_5']
        q97_0=sample['q97_0']
        q98_0=sample['outq98_0']
        tgt_before = sample['q98_0']
        break

print('#' * 80)
print("CCNOT operation on q0_5 (control1), q97_0 (control2) and q98_0 (target):")
print("    in:  q0_5={0}, q97_0={1}, q98_0={2}".format(q0_5,q97_0,tgt_before))
print("    out: q0_5={0}, q97_0={1}, q98_0={2}".format(q0_5,q97_0,q98_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q97_0 target: q98_0 ##
################################################################################
if 'q97_0' not in globals():
    q97_0=0
if 'q98_0' not in globals():
    q98_0=0

bqm = dimod.BinaryQuadraticModel({'q97_0' : 1, 'q98_0' : 1, 'outq98_0' : 1, 'anc' : 4}, {('q97_0', 'q98_0') : 2, ('q97_0', 'outq98_0') : -2, ('q98_0', 'outq98_0') : -2, ('q97_0', 'anc') : -4, ('q98_0', 'anc') : -4, ('outq98_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q97_0']==q97_0 and sample['q98_0']==q98_0 and int(energy)==0:
        q97_0=sample['q97_0']
        q98_0=sample['outq98_0']
        tgt_before = sample['q98_0']
        break

print('#' * 80)
print("CNOT operation on q97_0 (control) and q98_0 (target):")
print("    in:  q97_0={0}, q98_0={1}".format(q97_0,tgt_before))
print("    out: q97_0={0}, q98_0={1}".format(q97_0,q98_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_6 control2: q96_0 target: q97_0 ##
################################################################################
if 'q1_6' not in globals():
    q1_6=0
if 'q96_0' not in globals():
    q96_0=0
if 'q97_0' not in globals():
    q97_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq97_0' : 1, 'q97_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq97_0') : 4, ('anc1','q97_0') : -4, ('anc2', 'q1_6') : -2, ('anc2', 'q96_0') : -2, ('anc2', 'outq97_0') : -2, ('anc2', 'q97_0') : 2, ('q1_6', 'q96_0') : 1, ('outq97_0', 'q97_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_6']==q1_6 and sample['q96_0']==q96_0 and sample['q97_0']==q97_0 and int(energy)==0:
        q1_6=sample['q1_6']
        q96_0=sample['q96_0']
        q97_0=sample['outq97_0']
        tgt_before = sample['q97_0']
        break

print('#' * 80)
print("CCNOT operation on q1_6 (control1), q96_0 (control2) and q97_0 (target):")
print("    in:  q1_6={0}, q96_0={1}, q97_0={2}".format(q1_6,q96_0,tgt_before))
print("    out: q1_6={0}, q96_0={1}, q97_0={2}".format(q1_6,q96_0,q97_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_6 control2: q96_0 target: q97_0 ##
################################################################################
if 'q0_6' not in globals():
    q0_6=0
if 'q96_0' not in globals():
    q96_0=0
if 'q97_0' not in globals():
    q97_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq97_0' : 1, 'q97_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq97_0') : 4, ('anc1','q97_0') : -4, ('anc2', 'q0_6') : -2, ('anc2', 'q96_0') : -2, ('anc2', 'outq97_0') : -2, ('anc2', 'q97_0') : 2, ('q0_6', 'q96_0') : 1, ('outq97_0', 'q97_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_6']==q0_6 and sample['q96_0']==q96_0 and sample['q97_0']==q97_0 and int(energy)==0:
        q0_6=sample['q0_6']
        q96_0=sample['q96_0']
        q97_0=sample['outq97_0']
        tgt_before = sample['q97_0']
        break

print('#' * 80)
print("CCNOT operation on q0_6 (control1), q96_0 (control2) and q97_0 (target):")
print("    in:  q0_6={0}, q96_0={1}, q97_0={2}".format(q0_6,q96_0,tgt_before))
print("    out: q0_6={0}, q96_0={1}, q97_0={2}".format(q0_6,q96_0,q97_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q96_0 target: q97_0 ##
################################################################################
if 'q96_0' not in globals():
    q96_0=0
if 'q97_0' not in globals():
    q97_0=0

bqm = dimod.BinaryQuadraticModel({'q96_0' : 1, 'q97_0' : 1, 'outq97_0' : 1, 'anc' : 4}, {('q96_0', 'q97_0') : 2, ('q96_0', 'outq97_0') : -2, ('q97_0', 'outq97_0') : -2, ('q96_0', 'anc') : -4, ('q97_0', 'anc') : -4, ('outq97_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q96_0']==q96_0 and sample['q97_0']==q97_0 and int(energy)==0:
        q96_0=sample['q96_0']
        q97_0=sample['outq97_0']
        tgt_before = sample['q97_0']
        break

print('#' * 80)
print("CNOT operation on q96_0 (control) and q97_0 (target):")
print("    in:  q96_0={0}, q97_0={1}".format(q96_0,tgt_before))
print("    out: q96_0={0}, q97_0={1}".format(q96_0,q97_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_7 control2: q95_0 target: q96_0 ##
################################################################################
if 'q1_7' not in globals():
    q1_7=0
if 'q95_0' not in globals():
    q95_0=0
if 'q96_0' not in globals():
    q96_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq96_0' : 1, 'q96_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq96_0') : 4, ('anc1','q96_0') : -4, ('anc2', 'q1_7') : -2, ('anc2', 'q95_0') : -2, ('anc2', 'outq96_0') : -2, ('anc2', 'q96_0') : 2, ('q1_7', 'q95_0') : 1, ('outq96_0', 'q96_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_7']==q1_7 and sample['q95_0']==q95_0 and sample['q96_0']==q96_0 and int(energy)==0:
        q1_7=sample['q1_7']
        q95_0=sample['q95_0']
        q96_0=sample['outq96_0']
        tgt_before = sample['q96_0']
        break

print('#' * 80)
print("CCNOT operation on q1_7 (control1), q95_0 (control2) and q96_0 (target):")
print("    in:  q1_7={0}, q95_0={1}, q96_0={2}".format(q1_7,q95_0,tgt_before))
print("    out: q1_7={0}, q95_0={1}, q96_0={2}".format(q1_7,q95_0,q96_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_7 control2: q95_0 target: q96_0 ##
################################################################################
if 'q0_7' not in globals():
    q0_7=0
if 'q95_0' not in globals():
    q95_0=0
if 'q96_0' not in globals():
    q96_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq96_0' : 1, 'q96_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq96_0') : 4, ('anc1','q96_0') : -4, ('anc2', 'q0_7') : -2, ('anc2', 'q95_0') : -2, ('anc2', 'outq96_0') : -2, ('anc2', 'q96_0') : 2, ('q0_7', 'q95_0') : 1, ('outq96_0', 'q96_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_7']==q0_7 and sample['q95_0']==q95_0 and sample['q96_0']==q96_0 and int(energy)==0:
        q0_7=sample['q0_7']
        q95_0=sample['q95_0']
        q96_0=sample['outq96_0']
        tgt_before = sample['q96_0']
        break

print('#' * 80)
print("CCNOT operation on q0_7 (control1), q95_0 (control2) and q96_0 (target):")
print("    in:  q0_7={0}, q95_0={1}, q96_0={2}".format(q0_7,q95_0,tgt_before))
print("    out: q0_7={0}, q95_0={1}, q96_0={2}".format(q0_7,q95_0,q96_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q95_0 target: q96_0 ##
################################################################################
if 'q95_0' not in globals():
    q95_0=0
if 'q96_0' not in globals():
    q96_0=0

bqm = dimod.BinaryQuadraticModel({'q95_0' : 1, 'q96_0' : 1, 'outq96_0' : 1, 'anc' : 4}, {('q95_0', 'q96_0') : 2, ('q95_0', 'outq96_0') : -2, ('q96_0', 'outq96_0') : -2, ('q95_0', 'anc') : -4, ('q96_0', 'anc') : -4, ('outq96_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q95_0']==q95_0 and sample['q96_0']==q96_0 and int(energy)==0:
        q95_0=sample['q95_0']
        q96_0=sample['outq96_0']
        tgt_before = sample['q96_0']
        break

print('#' * 80)
print("CNOT operation on q95_0 (control) and q96_0 (target):")
print("    in:  q95_0={0}, q96_0={1}".format(q95_0,tgt_before))
print("    out: q95_0={0}, q96_0={1}".format(q95_0,q96_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_8 control2: q94_0 target: q95_0 ##
################################################################################
if 'q1_8' not in globals():
    q1_8=0
if 'q94_0' not in globals():
    q94_0=0
if 'q95_0' not in globals():
    q95_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq95_0' : 1, 'q95_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq95_0') : 4, ('anc1','q95_0') : -4, ('anc2', 'q1_8') : -2, ('anc2', 'q94_0') : -2, ('anc2', 'outq95_0') : -2, ('anc2', 'q95_0') : 2, ('q1_8', 'q94_0') : 1, ('outq95_0', 'q95_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_8']==q1_8 and sample['q94_0']==q94_0 and sample['q95_0']==q95_0 and int(energy)==0:
        q1_8=sample['q1_8']
        q94_0=sample['q94_0']
        q95_0=sample['outq95_0']
        tgt_before = sample['q95_0']
        break

print('#' * 80)
print("CCNOT operation on q1_8 (control1), q94_0 (control2) and q95_0 (target):")
print("    in:  q1_8={0}, q94_0={1}, q95_0={2}".format(q1_8,q94_0,tgt_before))
print("    out: q1_8={0}, q94_0={1}, q95_0={2}".format(q1_8,q94_0,q95_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_8 control2: q94_0 target: q95_0 ##
################################################################################
if 'q0_8' not in globals():
    q0_8=0
if 'q94_0' not in globals():
    q94_0=0
if 'q95_0' not in globals():
    q95_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq95_0' : 1, 'q95_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq95_0') : 4, ('anc1','q95_0') : -4, ('anc2', 'q0_8') : -2, ('anc2', 'q94_0') : -2, ('anc2', 'outq95_0') : -2, ('anc2', 'q95_0') : 2, ('q0_8', 'q94_0') : 1, ('outq95_0', 'q95_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_8']==q0_8 and sample['q94_0']==q94_0 and sample['q95_0']==q95_0 and int(energy)==0:
        q0_8=sample['q0_8']
        q94_0=sample['q94_0']
        q95_0=sample['outq95_0']
        tgt_before = sample['q95_0']
        break

print('#' * 80)
print("CCNOT operation on q0_8 (control1), q94_0 (control2) and q95_0 (target):")
print("    in:  q0_8={0}, q94_0={1}, q95_0={2}".format(q0_8,q94_0,tgt_before))
print("    out: q0_8={0}, q94_0={1}, q95_0={2}".format(q0_8,q94_0,q95_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q94_0 target: q95_0 ##
################################################################################
if 'q94_0' not in globals():
    q94_0=0
if 'q95_0' not in globals():
    q95_0=0

bqm = dimod.BinaryQuadraticModel({'q94_0' : 1, 'q95_0' : 1, 'outq95_0' : 1, 'anc' : 4}, {('q94_0', 'q95_0') : 2, ('q94_0', 'outq95_0') : -2, ('q95_0', 'outq95_0') : -2, ('q94_0', 'anc') : -4, ('q95_0', 'anc') : -4, ('outq95_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q94_0']==q94_0 and sample['q95_0']==q95_0 and int(energy)==0:
        q94_0=sample['q94_0']
        q95_0=sample['outq95_0']
        tgt_before = sample['q95_0']
        break

print('#' * 80)
print("CNOT operation on q94_0 (control) and q95_0 (target):")
print("    in:  q94_0={0}, q95_0={1}".format(q94_0,tgt_before))
print("    out: q94_0={0}, q95_0={1}".format(q94_0,q95_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_9 control2: q93_0 target: q94_0 ##
################################################################################
if 'q1_9' not in globals():
    q1_9=0
if 'q93_0' not in globals():
    q93_0=0
if 'q94_0' not in globals():
    q94_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq94_0' : 1, 'q94_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq94_0') : 4, ('anc1','q94_0') : -4, ('anc2', 'q1_9') : -2, ('anc2', 'q93_0') : -2, ('anc2', 'outq94_0') : -2, ('anc2', 'q94_0') : 2, ('q1_9', 'q93_0') : 1, ('outq94_0', 'q94_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_9']==q1_9 and sample['q93_0']==q93_0 and sample['q94_0']==q94_0 and int(energy)==0:
        q1_9=sample['q1_9']
        q93_0=sample['q93_0']
        q94_0=sample['outq94_0']
        tgt_before = sample['q94_0']
        break

print('#' * 80)
print("CCNOT operation on q1_9 (control1), q93_0 (control2) and q94_0 (target):")
print("    in:  q1_9={0}, q93_0={1}, q94_0={2}".format(q1_9,q93_0,tgt_before))
print("    out: q1_9={0}, q93_0={1}, q94_0={2}".format(q1_9,q93_0,q94_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_9 control2: q93_0 target: q94_0 ##
################################################################################
if 'q0_9' not in globals():
    q0_9=0
if 'q93_0' not in globals():
    q93_0=0
if 'q94_0' not in globals():
    q94_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq94_0' : 1, 'q94_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq94_0') : 4, ('anc1','q94_0') : -4, ('anc2', 'q0_9') : -2, ('anc2', 'q93_0') : -2, ('anc2', 'outq94_0') : -2, ('anc2', 'q94_0') : 2, ('q0_9', 'q93_0') : 1, ('outq94_0', 'q94_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_9']==q0_9 and sample['q93_0']==q93_0 and sample['q94_0']==q94_0 and int(energy)==0:
        q0_9=sample['q0_9']
        q93_0=sample['q93_0']
        q94_0=sample['outq94_0']
        tgt_before = sample['q94_0']
        break

print('#' * 80)
print("CCNOT operation on q0_9 (control1), q93_0 (control2) and q94_0 (target):")
print("    in:  q0_9={0}, q93_0={1}, q94_0={2}".format(q0_9,q93_0,tgt_before))
print("    out: q0_9={0}, q93_0={1}, q94_0={2}".format(q0_9,q93_0,q94_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q93_0 target: q94_0 ##
################################################################################
if 'q93_0' not in globals():
    q93_0=0
if 'q94_0' not in globals():
    q94_0=0

bqm = dimod.BinaryQuadraticModel({'q93_0' : 1, 'q94_0' : 1, 'outq94_0' : 1, 'anc' : 4}, {('q93_0', 'q94_0') : 2, ('q93_0', 'outq94_0') : -2, ('q94_0', 'outq94_0') : -2, ('q93_0', 'anc') : -4, ('q94_0', 'anc') : -4, ('outq94_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q93_0']==q93_0 and sample['q94_0']==q94_0 and int(energy)==0:
        q93_0=sample['q93_0']
        q94_0=sample['outq94_0']
        tgt_before = sample['q94_0']
        break

print('#' * 80)
print("CNOT operation on q93_0 (control) and q94_0 (target):")
print("    in:  q93_0={0}, q94_0={1}".format(q93_0,tgt_before))
print("    out: q93_0={0}, q94_0={1}".format(q93_0,q94_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_10 control2: q92_0 target: q93_0 ##
################################################################################
if 'q1_10' not in globals():
    q1_10=0
if 'q92_0' not in globals():
    q92_0=0
if 'q93_0' not in globals():
    q93_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq93_0' : 1, 'q93_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq93_0') : 4, ('anc1','q93_0') : -4, ('anc2', 'q1_10') : -2, ('anc2', 'q92_0') : -2, ('anc2', 'outq93_0') : -2, ('anc2', 'q93_0') : 2, ('q1_10', 'q92_0') : 1, ('outq93_0', 'q93_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_10']==q1_10 and sample['q92_0']==q92_0 and sample['q93_0']==q93_0 and int(energy)==0:
        q1_10=sample['q1_10']
        q92_0=sample['q92_0']
        q93_0=sample['outq93_0']
        tgt_before = sample['q93_0']
        break

print('#' * 80)
print("CCNOT operation on q1_10 (control1), q92_0 (control2) and q93_0 (target):")
print("    in:  q1_10={0}, q92_0={1}, q93_0={2}".format(q1_10,q92_0,tgt_before))
print("    out: q1_10={0}, q92_0={1}, q93_0={2}".format(q1_10,q92_0,q93_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_10 control2: q92_0 target: q93_0 ##
################################################################################
if 'q0_10' not in globals():
    q0_10=0
if 'q92_0' not in globals():
    q92_0=0
if 'q93_0' not in globals():
    q93_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq93_0' : 1, 'q93_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq93_0') : 4, ('anc1','q93_0') : -4, ('anc2', 'q0_10') : -2, ('anc2', 'q92_0') : -2, ('anc2', 'outq93_0') : -2, ('anc2', 'q93_0') : 2, ('q0_10', 'q92_0') : 1, ('outq93_0', 'q93_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_10']==q0_10 and sample['q92_0']==q92_0 and sample['q93_0']==q93_0 and int(energy)==0:
        q0_10=sample['q0_10']
        q92_0=sample['q92_0']
        q93_0=sample['outq93_0']
        tgt_before = sample['q93_0']
        break

print('#' * 80)
print("CCNOT operation on q0_10 (control1), q92_0 (control2) and q93_0 (target):")
print("    in:  q0_10={0}, q92_0={1}, q93_0={2}".format(q0_10,q92_0,tgt_before))
print("    out: q0_10={0}, q92_0={1}, q93_0={2}".format(q0_10,q92_0,q93_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q92_0 target: q93_0 ##
################################################################################
if 'q92_0' not in globals():
    q92_0=0
if 'q93_0' not in globals():
    q93_0=0

bqm = dimod.BinaryQuadraticModel({'q92_0' : 1, 'q93_0' : 1, 'outq93_0' : 1, 'anc' : 4}, {('q92_0', 'q93_0') : 2, ('q92_0', 'outq93_0') : -2, ('q93_0', 'outq93_0') : -2, ('q92_0', 'anc') : -4, ('q93_0', 'anc') : -4, ('outq93_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q92_0']==q92_0 and sample['q93_0']==q93_0 and int(energy)==0:
        q92_0=sample['q92_0']
        q93_0=sample['outq93_0']
        tgt_before = sample['q93_0']
        break

print('#' * 80)
print("CNOT operation on q92_0 (control) and q93_0 (target):")
print("    in:  q92_0={0}, q93_0={1}".format(q92_0,tgt_before))
print("    out: q92_0={0}, q93_0={1}".format(q92_0,q93_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_11 control2: q91_0 target: q92_0 ##
################################################################################
if 'q1_11' not in globals():
    q1_11=0
if 'q91_0' not in globals():
    q91_0=0
if 'q92_0' not in globals():
    q92_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq92_0' : 1, 'q92_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq92_0') : 4, ('anc1','q92_0') : -4, ('anc2', 'q1_11') : -2, ('anc2', 'q91_0') : -2, ('anc2', 'outq92_0') : -2, ('anc2', 'q92_0') : 2, ('q1_11', 'q91_0') : 1, ('outq92_0', 'q92_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_11']==q1_11 and sample['q91_0']==q91_0 and sample['q92_0']==q92_0 and int(energy)==0:
        q1_11=sample['q1_11']
        q91_0=sample['q91_0']
        q92_0=sample['outq92_0']
        tgt_before = sample['q92_0']
        break

print('#' * 80)
print("CCNOT operation on q1_11 (control1), q91_0 (control2) and q92_0 (target):")
print("    in:  q1_11={0}, q91_0={1}, q92_0={2}".format(q1_11,q91_0,tgt_before))
print("    out: q1_11={0}, q91_0={1}, q92_0={2}".format(q1_11,q91_0,q92_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_11 control2: q91_0 target: q92_0 ##
################################################################################
if 'q0_11' not in globals():
    q0_11=0
if 'q91_0' not in globals():
    q91_0=0
if 'q92_0' not in globals():
    q92_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq92_0' : 1, 'q92_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq92_0') : 4, ('anc1','q92_0') : -4, ('anc2', 'q0_11') : -2, ('anc2', 'q91_0') : -2, ('anc2', 'outq92_0') : -2, ('anc2', 'q92_0') : 2, ('q0_11', 'q91_0') : 1, ('outq92_0', 'q92_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_11']==q0_11 and sample['q91_0']==q91_0 and sample['q92_0']==q92_0 and int(energy)==0:
        q0_11=sample['q0_11']
        q91_0=sample['q91_0']
        q92_0=sample['outq92_0']
        tgt_before = sample['q92_0']
        break

print('#' * 80)
print("CCNOT operation on q0_11 (control1), q91_0 (control2) and q92_0 (target):")
print("    in:  q0_11={0}, q91_0={1}, q92_0={2}".format(q0_11,q91_0,tgt_before))
print("    out: q0_11={0}, q91_0={1}, q92_0={2}".format(q0_11,q91_0,q92_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q91_0 target: q92_0 ##
################################################################################
if 'q91_0' not in globals():
    q91_0=0
if 'q92_0' not in globals():
    q92_0=0

bqm = dimod.BinaryQuadraticModel({'q91_0' : 1, 'q92_0' : 1, 'outq92_0' : 1, 'anc' : 4}, {('q91_0', 'q92_0') : 2, ('q91_0', 'outq92_0') : -2, ('q92_0', 'outq92_0') : -2, ('q91_0', 'anc') : -4, ('q92_0', 'anc') : -4, ('outq92_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q91_0']==q91_0 and sample['q92_0']==q92_0 and int(energy)==0:
        q91_0=sample['q91_0']
        q92_0=sample['outq92_0']
        tgt_before = sample['q92_0']
        break

print('#' * 80)
print("CNOT operation on q91_0 (control) and q92_0 (target):")
print("    in:  q91_0={0}, q92_0={1}".format(q91_0,tgt_before))
print("    out: q91_0={0}, q92_0={1}".format(q91_0,q92_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_12 control2: q90_0 target: q91_0 ##
################################################################################
if 'q1_12' not in globals():
    q1_12=0
if 'q90_0' not in globals():
    q90_0=0
if 'q91_0' not in globals():
    q91_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq91_0' : 1, 'q91_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq91_0') : 4, ('anc1','q91_0') : -4, ('anc2', 'q1_12') : -2, ('anc2', 'q90_0') : -2, ('anc2', 'outq91_0') : -2, ('anc2', 'q91_0') : 2, ('q1_12', 'q90_0') : 1, ('outq91_0', 'q91_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_12']==q1_12 and sample['q90_0']==q90_0 and sample['q91_0']==q91_0 and int(energy)==0:
        q1_12=sample['q1_12']
        q90_0=sample['q90_0']
        q91_0=sample['outq91_0']
        tgt_before = sample['q91_0']
        break

print('#' * 80)
print("CCNOT operation on q1_12 (control1), q90_0 (control2) and q91_0 (target):")
print("    in:  q1_12={0}, q90_0={1}, q91_0={2}".format(q1_12,q90_0,tgt_before))
print("    out: q1_12={0}, q90_0={1}, q91_0={2}".format(q1_12,q90_0,q91_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_12 control2: q90_0 target: q91_0 ##
################################################################################
if 'q0_12' not in globals():
    q0_12=0
if 'q90_0' not in globals():
    q90_0=0
if 'q91_0' not in globals():
    q91_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq91_0' : 1, 'q91_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq91_0') : 4, ('anc1','q91_0') : -4, ('anc2', 'q0_12') : -2, ('anc2', 'q90_0') : -2, ('anc2', 'outq91_0') : -2, ('anc2', 'q91_0') : 2, ('q0_12', 'q90_0') : 1, ('outq91_0', 'q91_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_12']==q0_12 and sample['q90_0']==q90_0 and sample['q91_0']==q91_0 and int(energy)==0:
        q0_12=sample['q0_12']
        q90_0=sample['q90_0']
        q91_0=sample['outq91_0']
        tgt_before = sample['q91_0']
        break

print('#' * 80)
print("CCNOT operation on q0_12 (control1), q90_0 (control2) and q91_0 (target):")
print("    in:  q0_12={0}, q90_0={1}, q91_0={2}".format(q0_12,q90_0,tgt_before))
print("    out: q0_12={0}, q90_0={1}, q91_0={2}".format(q0_12,q90_0,q91_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q90_0 target: q91_0 ##
################################################################################
if 'q90_0' not in globals():
    q90_0=0
if 'q91_0' not in globals():
    q91_0=0

bqm = dimod.BinaryQuadraticModel({'q90_0' : 1, 'q91_0' : 1, 'outq91_0' : 1, 'anc' : 4}, {('q90_0', 'q91_0') : 2, ('q90_0', 'outq91_0') : -2, ('q91_0', 'outq91_0') : -2, ('q90_0', 'anc') : -4, ('q91_0', 'anc') : -4, ('outq91_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q90_0']==q90_0 and sample['q91_0']==q91_0 and int(energy)==0:
        q90_0=sample['q90_0']
        q91_0=sample['outq91_0']
        tgt_before = sample['q91_0']
        break

print('#' * 80)
print("CNOT operation on q90_0 (control) and q91_0 (target):")
print("    in:  q90_0={0}, q91_0={1}".format(q90_0,tgt_before))
print("    out: q90_0={0}, q91_0={1}".format(q90_0,q91_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_13 control2: q89_0 target: q90_0 ##
################################################################################
if 'q1_13' not in globals():
    q1_13=0
if 'q89_0' not in globals():
    q89_0=0
if 'q90_0' not in globals():
    q90_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq90_0' : 1, 'q90_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq90_0') : 4, ('anc1','q90_0') : -4, ('anc2', 'q1_13') : -2, ('anc2', 'q89_0') : -2, ('anc2', 'outq90_0') : -2, ('anc2', 'q90_0') : 2, ('q1_13', 'q89_0') : 1, ('outq90_0', 'q90_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_13']==q1_13 and sample['q89_0']==q89_0 and sample['q90_0']==q90_0 and int(energy)==0:
        q1_13=sample['q1_13']
        q89_0=sample['q89_0']
        q90_0=sample['outq90_0']
        tgt_before = sample['q90_0']
        break

print('#' * 80)
print("CCNOT operation on q1_13 (control1), q89_0 (control2) and q90_0 (target):")
print("    in:  q1_13={0}, q89_0={1}, q90_0={2}".format(q1_13,q89_0,tgt_before))
print("    out: q1_13={0}, q89_0={1}, q90_0={2}".format(q1_13,q89_0,q90_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_13 control2: q89_0 target: q90_0 ##
################################################################################
if 'q0_13' not in globals():
    q0_13=0
if 'q89_0' not in globals():
    q89_0=0
if 'q90_0' not in globals():
    q90_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq90_0' : 1, 'q90_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq90_0') : 4, ('anc1','q90_0') : -4, ('anc2', 'q0_13') : -2, ('anc2', 'q89_0') : -2, ('anc2', 'outq90_0') : -2, ('anc2', 'q90_0') : 2, ('q0_13', 'q89_0') : 1, ('outq90_0', 'q90_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_13']==q0_13 and sample['q89_0']==q89_0 and sample['q90_0']==q90_0 and int(energy)==0:
        q0_13=sample['q0_13']
        q89_0=sample['q89_0']
        q90_0=sample['outq90_0']
        tgt_before = sample['q90_0']
        break

print('#' * 80)
print("CCNOT operation on q0_13 (control1), q89_0 (control2) and q90_0 (target):")
print("    in:  q0_13={0}, q89_0={1}, q90_0={2}".format(q0_13,q89_0,tgt_before))
print("    out: q0_13={0}, q89_0={1}, q90_0={2}".format(q0_13,q89_0,q90_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q89_0 target: q90_0 ##
################################################################################
if 'q89_0' not in globals():
    q89_0=0
if 'q90_0' not in globals():
    q90_0=0

bqm = dimod.BinaryQuadraticModel({'q89_0' : 1, 'q90_0' : 1, 'outq90_0' : 1, 'anc' : 4}, {('q89_0', 'q90_0') : 2, ('q89_0', 'outq90_0') : -2, ('q90_0', 'outq90_0') : -2, ('q89_0', 'anc') : -4, ('q90_0', 'anc') : -4, ('outq90_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q89_0']==q89_0 and sample['q90_0']==q90_0 and int(energy)==0:
        q89_0=sample['q89_0']
        q90_0=sample['outq90_0']
        tgt_before = sample['q90_0']
        break

print('#' * 80)
print("CNOT operation on q89_0 (control) and q90_0 (target):")
print("    in:  q89_0={0}, q90_0={1}".format(q89_0,tgt_before))
print("    out: q89_0={0}, q90_0={1}".format(q89_0,q90_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_14 control2: q88_0 target: q89_0 ##
################################################################################
if 'q1_14' not in globals():
    q1_14=0
if 'q88_0' not in globals():
    q88_0=0
if 'q89_0' not in globals():
    q89_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq89_0' : 1, 'q89_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq89_0') : 4, ('anc1','q89_0') : -4, ('anc2', 'q1_14') : -2, ('anc2', 'q88_0') : -2, ('anc2', 'outq89_0') : -2, ('anc2', 'q89_0') : 2, ('q1_14', 'q88_0') : 1, ('outq89_0', 'q89_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_14']==q1_14 and sample['q88_0']==q88_0 and sample['q89_0']==q89_0 and int(energy)==0:
        q1_14=sample['q1_14']
        q88_0=sample['q88_0']
        q89_0=sample['outq89_0']
        tgt_before = sample['q89_0']
        break

print('#' * 80)
print("CCNOT operation on q1_14 (control1), q88_0 (control2) and q89_0 (target):")
print("    in:  q1_14={0}, q88_0={1}, q89_0={2}".format(q1_14,q88_0,tgt_before))
print("    out: q1_14={0}, q88_0={1}, q89_0={2}".format(q1_14,q88_0,q89_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_14 control2: q88_0 target: q89_0 ##
################################################################################
if 'q0_14' not in globals():
    q0_14=0
if 'q88_0' not in globals():
    q88_0=0
if 'q89_0' not in globals():
    q89_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq89_0' : 1, 'q89_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq89_0') : 4, ('anc1','q89_0') : -4, ('anc2', 'q0_14') : -2, ('anc2', 'q88_0') : -2, ('anc2', 'outq89_0') : -2, ('anc2', 'q89_0') : 2, ('q0_14', 'q88_0') : 1, ('outq89_0', 'q89_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_14']==q0_14 and sample['q88_0']==q88_0 and sample['q89_0']==q89_0 and int(energy)==0:
        q0_14=sample['q0_14']
        q88_0=sample['q88_0']
        q89_0=sample['outq89_0']
        tgt_before = sample['q89_0']
        break

print('#' * 80)
print("CCNOT operation on q0_14 (control1), q88_0 (control2) and q89_0 (target):")
print("    in:  q0_14={0}, q88_0={1}, q89_0={2}".format(q0_14,q88_0,tgt_before))
print("    out: q0_14={0}, q88_0={1}, q89_0={2}".format(q0_14,q88_0,q89_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q88_0 target: q89_0 ##
################################################################################
if 'q88_0' not in globals():
    q88_0=0
if 'q89_0' not in globals():
    q89_0=0

bqm = dimod.BinaryQuadraticModel({'q88_0' : 1, 'q89_0' : 1, 'outq89_0' : 1, 'anc' : 4}, {('q88_0', 'q89_0') : 2, ('q88_0', 'outq89_0') : -2, ('q89_0', 'outq89_0') : -2, ('q88_0', 'anc') : -4, ('q89_0', 'anc') : -4, ('outq89_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q88_0']==q88_0 and sample['q89_0']==q89_0 and int(energy)==0:
        q88_0=sample['q88_0']
        q89_0=sample['outq89_0']
        tgt_before = sample['q89_0']
        break

print('#' * 80)
print("CNOT operation on q88_0 (control) and q89_0 (target):")
print("    in:  q88_0={0}, q89_0={1}".format(q88_0,tgt_before))
print("    out: q88_0={0}, q89_0={1}".format(q88_0,q89_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_15 control2: q87_0 target: q88_0 ##
################################################################################
if 'q1_15' not in globals():
    q1_15=0
if 'q87_0' not in globals():
    q87_0=0
if 'q88_0' not in globals():
    q88_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq88_0' : 1, 'q88_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq88_0') : 4, ('anc1','q88_0') : -4, ('anc2', 'q1_15') : -2, ('anc2', 'q87_0') : -2, ('anc2', 'outq88_0') : -2, ('anc2', 'q88_0') : 2, ('q1_15', 'q87_0') : 1, ('outq88_0', 'q88_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_15']==q1_15 and sample['q87_0']==q87_0 and sample['q88_0']==q88_0 and int(energy)==0:
        q1_15=sample['q1_15']
        q87_0=sample['q87_0']
        q88_0=sample['outq88_0']
        tgt_before = sample['q88_0']
        break

print('#' * 80)
print("CCNOT operation on q1_15 (control1), q87_0 (control2) and q88_0 (target):")
print("    in:  q1_15={0}, q87_0={1}, q88_0={2}".format(q1_15,q87_0,tgt_before))
print("    out: q1_15={0}, q87_0={1}, q88_0={2}".format(q1_15,q87_0,q88_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_15 control2: q87_0 target: q88_0 ##
################################################################################
if 'q0_15' not in globals():
    q0_15=0
if 'q87_0' not in globals():
    q87_0=0
if 'q88_0' not in globals():
    q88_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq88_0' : 1, 'q88_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq88_0') : 4, ('anc1','q88_0') : -4, ('anc2', 'q0_15') : -2, ('anc2', 'q87_0') : -2, ('anc2', 'outq88_0') : -2, ('anc2', 'q88_0') : 2, ('q0_15', 'q87_0') : 1, ('outq88_0', 'q88_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_15']==q0_15 and sample['q87_0']==q87_0 and sample['q88_0']==q88_0 and int(energy)==0:
        q0_15=sample['q0_15']
        q87_0=sample['q87_0']
        q88_0=sample['outq88_0']
        tgt_before = sample['q88_0']
        break

print('#' * 80)
print("CCNOT operation on q0_15 (control1), q87_0 (control2) and q88_0 (target):")
print("    in:  q0_15={0}, q87_0={1}, q88_0={2}".format(q0_15,q87_0,tgt_before))
print("    out: q0_15={0}, q87_0={1}, q88_0={2}".format(q0_15,q87_0,q88_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q87_0 target: q88_0 ##
################################################################################
if 'q87_0' not in globals():
    q87_0=0
if 'q88_0' not in globals():
    q88_0=0

bqm = dimod.BinaryQuadraticModel({'q87_0' : 1, 'q88_0' : 1, 'outq88_0' : 1, 'anc' : 4}, {('q87_0', 'q88_0') : 2, ('q87_0', 'outq88_0') : -2, ('q88_0', 'outq88_0') : -2, ('q87_0', 'anc') : -4, ('q88_0', 'anc') : -4, ('outq88_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q87_0']==q87_0 and sample['q88_0']==q88_0 and int(energy)==0:
        q87_0=sample['q87_0']
        q88_0=sample['outq88_0']
        tgt_before = sample['q88_0']
        break

print('#' * 80)
print("CNOT operation on q87_0 (control) and q88_0 (target):")
print("    in:  q87_0={0}, q88_0={1}".format(q87_0,tgt_before))
print("    out: q87_0={0}, q88_0={1}".format(q87_0,q88_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_16 control2: q86_0 target: q87_0 ##
################################################################################
if 'q1_16' not in globals():
    q1_16=0
if 'q86_0' not in globals():
    q86_0=0
if 'q87_0' not in globals():
    q87_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq87_0' : 1, 'q87_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq87_0') : 4, ('anc1','q87_0') : -4, ('anc2', 'q1_16') : -2, ('anc2', 'q86_0') : -2, ('anc2', 'outq87_0') : -2, ('anc2', 'q87_0') : 2, ('q1_16', 'q86_0') : 1, ('outq87_0', 'q87_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_16']==q1_16 and sample['q86_0']==q86_0 and sample['q87_0']==q87_0 and int(energy)==0:
        q1_16=sample['q1_16']
        q86_0=sample['q86_0']
        q87_0=sample['outq87_0']
        tgt_before = sample['q87_0']
        break

print('#' * 80)
print("CCNOT operation on q1_16 (control1), q86_0 (control2) and q87_0 (target):")
print("    in:  q1_16={0}, q86_0={1}, q87_0={2}".format(q1_16,q86_0,tgt_before))
print("    out: q1_16={0}, q86_0={1}, q87_0={2}".format(q1_16,q86_0,q87_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_16 control2: q86_0 target: q87_0 ##
################################################################################
if 'q0_16' not in globals():
    q0_16=0
if 'q86_0' not in globals():
    q86_0=0
if 'q87_0' not in globals():
    q87_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq87_0' : 1, 'q87_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq87_0') : 4, ('anc1','q87_0') : -4, ('anc2', 'q0_16') : -2, ('anc2', 'q86_0') : -2, ('anc2', 'outq87_0') : -2, ('anc2', 'q87_0') : 2, ('q0_16', 'q86_0') : 1, ('outq87_0', 'q87_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_16']==q0_16 and sample['q86_0']==q86_0 and sample['q87_0']==q87_0 and int(energy)==0:
        q0_16=sample['q0_16']
        q86_0=sample['q86_0']
        q87_0=sample['outq87_0']
        tgt_before = sample['q87_0']
        break

print('#' * 80)
print("CCNOT operation on q0_16 (control1), q86_0 (control2) and q87_0 (target):")
print("    in:  q0_16={0}, q86_0={1}, q87_0={2}".format(q0_16,q86_0,tgt_before))
print("    out: q0_16={0}, q86_0={1}, q87_0={2}".format(q0_16,q86_0,q87_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q86_0 target: q87_0 ##
################################################################################
if 'q86_0' not in globals():
    q86_0=0
if 'q87_0' not in globals():
    q87_0=0

bqm = dimod.BinaryQuadraticModel({'q86_0' : 1, 'q87_0' : 1, 'outq87_0' : 1, 'anc' : 4}, {('q86_0', 'q87_0') : 2, ('q86_0', 'outq87_0') : -2, ('q87_0', 'outq87_0') : -2, ('q86_0', 'anc') : -4, ('q87_0', 'anc') : -4, ('outq87_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q86_0']==q86_0 and sample['q87_0']==q87_0 and int(energy)==0:
        q86_0=sample['q86_0']
        q87_0=sample['outq87_0']
        tgt_before = sample['q87_0']
        break

print('#' * 80)
print("CNOT operation on q86_0 (control) and q87_0 (target):")
print("    in:  q86_0={0}, q87_0={1}".format(q86_0,tgt_before))
print("    out: q86_0={0}, q87_0={1}".format(q86_0,q87_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_17 control2: q85_0 target: q86_0 ##
################################################################################
if 'q1_17' not in globals():
    q1_17=0
if 'q85_0' not in globals():
    q85_0=0
if 'q86_0' not in globals():
    q86_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq86_0' : 1, 'q86_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq86_0') : 4, ('anc1','q86_0') : -4, ('anc2', 'q1_17') : -2, ('anc2', 'q85_0') : -2, ('anc2', 'outq86_0') : -2, ('anc2', 'q86_0') : 2, ('q1_17', 'q85_0') : 1, ('outq86_0', 'q86_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_17']==q1_17 and sample['q85_0']==q85_0 and sample['q86_0']==q86_0 and int(energy)==0:
        q1_17=sample['q1_17']
        q85_0=sample['q85_0']
        q86_0=sample['outq86_0']
        tgt_before = sample['q86_0']
        break

print('#' * 80)
print("CCNOT operation on q1_17 (control1), q85_0 (control2) and q86_0 (target):")
print("    in:  q1_17={0}, q85_0={1}, q86_0={2}".format(q1_17,q85_0,tgt_before))
print("    out: q1_17={0}, q85_0={1}, q86_0={2}".format(q1_17,q85_0,q86_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_17 control2: q85_0 target: q86_0 ##
################################################################################
if 'q0_17' not in globals():
    q0_17=0
if 'q85_0' not in globals():
    q85_0=0
if 'q86_0' not in globals():
    q86_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq86_0' : 1, 'q86_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq86_0') : 4, ('anc1','q86_0') : -4, ('anc2', 'q0_17') : -2, ('anc2', 'q85_0') : -2, ('anc2', 'outq86_0') : -2, ('anc2', 'q86_0') : 2, ('q0_17', 'q85_0') : 1, ('outq86_0', 'q86_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_17']==q0_17 and sample['q85_0']==q85_0 and sample['q86_0']==q86_0 and int(energy)==0:
        q0_17=sample['q0_17']
        q85_0=sample['q85_0']
        q86_0=sample['outq86_0']
        tgt_before = sample['q86_0']
        break

print('#' * 80)
print("CCNOT operation on q0_17 (control1), q85_0 (control2) and q86_0 (target):")
print("    in:  q0_17={0}, q85_0={1}, q86_0={2}".format(q0_17,q85_0,tgt_before))
print("    out: q0_17={0}, q85_0={1}, q86_0={2}".format(q0_17,q85_0,q86_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q85_0 target: q86_0 ##
################################################################################
if 'q85_0' not in globals():
    q85_0=0
if 'q86_0' not in globals():
    q86_0=0

bqm = dimod.BinaryQuadraticModel({'q85_0' : 1, 'q86_0' : 1, 'outq86_0' : 1, 'anc' : 4}, {('q85_0', 'q86_0') : 2, ('q85_0', 'outq86_0') : -2, ('q86_0', 'outq86_0') : -2, ('q85_0', 'anc') : -4, ('q86_0', 'anc') : -4, ('outq86_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q85_0']==q85_0 and sample['q86_0']==q86_0 and int(energy)==0:
        q85_0=sample['q85_0']
        q86_0=sample['outq86_0']
        tgt_before = sample['q86_0']
        break

print('#' * 80)
print("CNOT operation on q85_0 (control) and q86_0 (target):")
print("    in:  q85_0={0}, q86_0={1}".format(q85_0,tgt_before))
print("    out: q85_0={0}, q86_0={1}".format(q85_0,q86_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_18 control2: q84_0 target: q85_0 ##
################################################################################
if 'q1_18' not in globals():
    q1_18=0
if 'q84_0' not in globals():
    q84_0=0
if 'q85_0' not in globals():
    q85_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq85_0' : 1, 'q85_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq85_0') : 4, ('anc1','q85_0') : -4, ('anc2', 'q1_18') : -2, ('anc2', 'q84_0') : -2, ('anc2', 'outq85_0') : -2, ('anc2', 'q85_0') : 2, ('q1_18', 'q84_0') : 1, ('outq85_0', 'q85_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_18']==q1_18 and sample['q84_0']==q84_0 and sample['q85_0']==q85_0 and int(energy)==0:
        q1_18=sample['q1_18']
        q84_0=sample['q84_0']
        q85_0=sample['outq85_0']
        tgt_before = sample['q85_0']
        break

print('#' * 80)
print("CCNOT operation on q1_18 (control1), q84_0 (control2) and q85_0 (target):")
print("    in:  q1_18={0}, q84_0={1}, q85_0={2}".format(q1_18,q84_0,tgt_before))
print("    out: q1_18={0}, q84_0={1}, q85_0={2}".format(q1_18,q84_0,q85_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_18 control2: q84_0 target: q85_0 ##
################################################################################
if 'q0_18' not in globals():
    q0_18=0
if 'q84_0' not in globals():
    q84_0=0
if 'q85_0' not in globals():
    q85_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq85_0' : 1, 'q85_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq85_0') : 4, ('anc1','q85_0') : -4, ('anc2', 'q0_18') : -2, ('anc2', 'q84_0') : -2, ('anc2', 'outq85_0') : -2, ('anc2', 'q85_0') : 2, ('q0_18', 'q84_0') : 1, ('outq85_0', 'q85_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_18']==q0_18 and sample['q84_0']==q84_0 and sample['q85_0']==q85_0 and int(energy)==0:
        q0_18=sample['q0_18']
        q84_0=sample['q84_0']
        q85_0=sample['outq85_0']
        tgt_before = sample['q85_0']
        break

print('#' * 80)
print("CCNOT operation on q0_18 (control1), q84_0 (control2) and q85_0 (target):")
print("    in:  q0_18={0}, q84_0={1}, q85_0={2}".format(q0_18,q84_0,tgt_before))
print("    out: q0_18={0}, q84_0={1}, q85_0={2}".format(q0_18,q84_0,q85_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q84_0 target: q85_0 ##
################################################################################
if 'q84_0' not in globals():
    q84_0=0
if 'q85_0' not in globals():
    q85_0=0

bqm = dimod.BinaryQuadraticModel({'q84_0' : 1, 'q85_0' : 1, 'outq85_0' : 1, 'anc' : 4}, {('q84_0', 'q85_0') : 2, ('q84_0', 'outq85_0') : -2, ('q85_0', 'outq85_0') : -2, ('q84_0', 'anc') : -4, ('q85_0', 'anc') : -4, ('outq85_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q84_0']==q84_0 and sample['q85_0']==q85_0 and int(energy)==0:
        q84_0=sample['q84_0']
        q85_0=sample['outq85_0']
        tgt_before = sample['q85_0']
        break

print('#' * 80)
print("CNOT operation on q84_0 (control) and q85_0 (target):")
print("    in:  q84_0={0}, q85_0={1}".format(q84_0,tgt_before))
print("    out: q84_0={0}, q85_0={1}".format(q84_0,q85_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_19 control2: q83_0 target: q84_0 ##
################################################################################
if 'q1_19' not in globals():
    q1_19=0
if 'q83_0' not in globals():
    q83_0=0
if 'q84_0' not in globals():
    q84_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq84_0' : 1, 'q84_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq84_0') : 4, ('anc1','q84_0') : -4, ('anc2', 'q1_19') : -2, ('anc2', 'q83_0') : -2, ('anc2', 'outq84_0') : -2, ('anc2', 'q84_0') : 2, ('q1_19', 'q83_0') : 1, ('outq84_0', 'q84_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_19']==q1_19 and sample['q83_0']==q83_0 and sample['q84_0']==q84_0 and int(energy)==0:
        q1_19=sample['q1_19']
        q83_0=sample['q83_0']
        q84_0=sample['outq84_0']
        tgt_before = sample['q84_0']
        break

print('#' * 80)
print("CCNOT operation on q1_19 (control1), q83_0 (control2) and q84_0 (target):")
print("    in:  q1_19={0}, q83_0={1}, q84_0={2}".format(q1_19,q83_0,tgt_before))
print("    out: q1_19={0}, q83_0={1}, q84_0={2}".format(q1_19,q83_0,q84_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_19 control2: q83_0 target: q84_0 ##
################################################################################
if 'q0_19' not in globals():
    q0_19=0
if 'q83_0' not in globals():
    q83_0=0
if 'q84_0' not in globals():
    q84_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq84_0' : 1, 'q84_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq84_0') : 4, ('anc1','q84_0') : -4, ('anc2', 'q0_19') : -2, ('anc2', 'q83_0') : -2, ('anc2', 'outq84_0') : -2, ('anc2', 'q84_0') : 2, ('q0_19', 'q83_0') : 1, ('outq84_0', 'q84_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_19']==q0_19 and sample['q83_0']==q83_0 and sample['q84_0']==q84_0 and int(energy)==0:
        q0_19=sample['q0_19']
        q83_0=sample['q83_0']
        q84_0=sample['outq84_0']
        tgt_before = sample['q84_0']
        break

print('#' * 80)
print("CCNOT operation on q0_19 (control1), q83_0 (control2) and q84_0 (target):")
print("    in:  q0_19={0}, q83_0={1}, q84_0={2}".format(q0_19,q83_0,tgt_before))
print("    out: q0_19={0}, q83_0={1}, q84_0={2}".format(q0_19,q83_0,q84_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q83_0 target: q84_0 ##
################################################################################
if 'q83_0' not in globals():
    q83_0=0
if 'q84_0' not in globals():
    q84_0=0

bqm = dimod.BinaryQuadraticModel({'q83_0' : 1, 'q84_0' : 1, 'outq84_0' : 1, 'anc' : 4}, {('q83_0', 'q84_0') : 2, ('q83_0', 'outq84_0') : -2, ('q84_0', 'outq84_0') : -2, ('q83_0', 'anc') : -4, ('q84_0', 'anc') : -4, ('outq84_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q83_0']==q83_0 and sample['q84_0']==q84_0 and int(energy)==0:
        q83_0=sample['q83_0']
        q84_0=sample['outq84_0']
        tgt_before = sample['q84_0']
        break

print('#' * 80)
print("CNOT operation on q83_0 (control) and q84_0 (target):")
print("    in:  q83_0={0}, q84_0={1}".format(q83_0,tgt_before))
print("    out: q83_0={0}, q84_0={1}".format(q83_0,q84_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_20 control2: q82_0 target: q83_0 ##
################################################################################
if 'q1_20' not in globals():
    q1_20=0
if 'q82_0' not in globals():
    q82_0=0
if 'q83_0' not in globals():
    q83_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq83_0' : 1, 'q83_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq83_0') : 4, ('anc1','q83_0') : -4, ('anc2', 'q1_20') : -2, ('anc2', 'q82_0') : -2, ('anc2', 'outq83_0') : -2, ('anc2', 'q83_0') : 2, ('q1_20', 'q82_0') : 1, ('outq83_0', 'q83_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_20']==q1_20 and sample['q82_0']==q82_0 and sample['q83_0']==q83_0 and int(energy)==0:
        q1_20=sample['q1_20']
        q82_0=sample['q82_0']
        q83_0=sample['outq83_0']
        tgt_before = sample['q83_0']
        break

print('#' * 80)
print("CCNOT operation on q1_20 (control1), q82_0 (control2) and q83_0 (target):")
print("    in:  q1_20={0}, q82_0={1}, q83_0={2}".format(q1_20,q82_0,tgt_before))
print("    out: q1_20={0}, q82_0={1}, q83_0={2}".format(q1_20,q82_0,q83_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_20 control2: q82_0 target: q83_0 ##
################################################################################
if 'q0_20' not in globals():
    q0_20=0
if 'q82_0' not in globals():
    q82_0=0
if 'q83_0' not in globals():
    q83_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq83_0' : 1, 'q83_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq83_0') : 4, ('anc1','q83_0') : -4, ('anc2', 'q0_20') : -2, ('anc2', 'q82_0') : -2, ('anc2', 'outq83_0') : -2, ('anc2', 'q83_0') : 2, ('q0_20', 'q82_0') : 1, ('outq83_0', 'q83_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_20']==q0_20 and sample['q82_0']==q82_0 and sample['q83_0']==q83_0 and int(energy)==0:
        q0_20=sample['q0_20']
        q82_0=sample['q82_0']
        q83_0=sample['outq83_0']
        tgt_before = sample['q83_0']
        break

print('#' * 80)
print("CCNOT operation on q0_20 (control1), q82_0 (control2) and q83_0 (target):")
print("    in:  q0_20={0}, q82_0={1}, q83_0={2}".format(q0_20,q82_0,tgt_before))
print("    out: q0_20={0}, q82_0={1}, q83_0={2}".format(q0_20,q82_0,q83_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q82_0 target: q83_0 ##
################################################################################
if 'q82_0' not in globals():
    q82_0=0
if 'q83_0' not in globals():
    q83_0=0

bqm = dimod.BinaryQuadraticModel({'q82_0' : 1, 'q83_0' : 1, 'outq83_0' : 1, 'anc' : 4}, {('q82_0', 'q83_0') : 2, ('q82_0', 'outq83_0') : -2, ('q83_0', 'outq83_0') : -2, ('q82_0', 'anc') : -4, ('q83_0', 'anc') : -4, ('outq83_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q82_0']==q82_0 and sample['q83_0']==q83_0 and int(energy)==0:
        q82_0=sample['q82_0']
        q83_0=sample['outq83_0']
        tgt_before = sample['q83_0']
        break

print('#' * 80)
print("CNOT operation on q82_0 (control) and q83_0 (target):")
print("    in:  q82_0={0}, q83_0={1}".format(q82_0,tgt_before))
print("    out: q82_0={0}, q83_0={1}".format(q82_0,q83_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_21 control2: q81_0 target: q82_0 ##
################################################################################
if 'q1_21' not in globals():
    q1_21=0
if 'q81_0' not in globals():
    q81_0=0
if 'q82_0' not in globals():
    q82_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq82_0' : 1, 'q82_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq82_0') : 4, ('anc1','q82_0') : -4, ('anc2', 'q1_21') : -2, ('anc2', 'q81_0') : -2, ('anc2', 'outq82_0') : -2, ('anc2', 'q82_0') : 2, ('q1_21', 'q81_0') : 1, ('outq82_0', 'q82_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_21']==q1_21 and sample['q81_0']==q81_0 and sample['q82_0']==q82_0 and int(energy)==0:
        q1_21=sample['q1_21']
        q81_0=sample['q81_0']
        q82_0=sample['outq82_0']
        tgt_before = sample['q82_0']
        break

print('#' * 80)
print("CCNOT operation on q1_21 (control1), q81_0 (control2) and q82_0 (target):")
print("    in:  q1_21={0}, q81_0={1}, q82_0={2}".format(q1_21,q81_0,tgt_before))
print("    out: q1_21={0}, q81_0={1}, q82_0={2}".format(q1_21,q81_0,q82_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_21 control2: q81_0 target: q82_0 ##
################################################################################
if 'q0_21' not in globals():
    q0_21=0
if 'q81_0' not in globals():
    q81_0=0
if 'q82_0' not in globals():
    q82_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq82_0' : 1, 'q82_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq82_0') : 4, ('anc1','q82_0') : -4, ('anc2', 'q0_21') : -2, ('anc2', 'q81_0') : -2, ('anc2', 'outq82_0') : -2, ('anc2', 'q82_0') : 2, ('q0_21', 'q81_0') : 1, ('outq82_0', 'q82_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_21']==q0_21 and sample['q81_0']==q81_0 and sample['q82_0']==q82_0 and int(energy)==0:
        q0_21=sample['q0_21']
        q81_0=sample['q81_0']
        q82_0=sample['outq82_0']
        tgt_before = sample['q82_0']
        break

print('#' * 80)
print("CCNOT operation on q0_21 (control1), q81_0 (control2) and q82_0 (target):")
print("    in:  q0_21={0}, q81_0={1}, q82_0={2}".format(q0_21,q81_0,tgt_before))
print("    out: q0_21={0}, q81_0={1}, q82_0={2}".format(q0_21,q81_0,q82_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q81_0 target: q82_0 ##
################################################################################
if 'q81_0' not in globals():
    q81_0=0
if 'q82_0' not in globals():
    q82_0=0

bqm = dimod.BinaryQuadraticModel({'q81_0' : 1, 'q82_0' : 1, 'outq82_0' : 1, 'anc' : 4}, {('q81_0', 'q82_0') : 2, ('q81_0', 'outq82_0') : -2, ('q82_0', 'outq82_0') : -2, ('q81_0', 'anc') : -4, ('q82_0', 'anc') : -4, ('outq82_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q81_0']==q81_0 and sample['q82_0']==q82_0 and int(energy)==0:
        q81_0=sample['q81_0']
        q82_0=sample['outq82_0']
        tgt_before = sample['q82_0']
        break

print('#' * 80)
print("CNOT operation on q81_0 (control) and q82_0 (target):")
print("    in:  q81_0={0}, q82_0={1}".format(q81_0,tgt_before))
print("    out: q81_0={0}, q82_0={1}".format(q81_0,q82_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_22 control2: q80_0 target: q81_0 ##
################################################################################
if 'q1_22' not in globals():
    q1_22=0
if 'q80_0' not in globals():
    q80_0=0
if 'q81_0' not in globals():
    q81_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq81_0' : 1, 'q81_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq81_0') : 4, ('anc1','q81_0') : -4, ('anc2', 'q1_22') : -2, ('anc2', 'q80_0') : -2, ('anc2', 'outq81_0') : -2, ('anc2', 'q81_0') : 2, ('q1_22', 'q80_0') : 1, ('outq81_0', 'q81_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_22']==q1_22 and sample['q80_0']==q80_0 and sample['q81_0']==q81_0 and int(energy)==0:
        q1_22=sample['q1_22']
        q80_0=sample['q80_0']
        q81_0=sample['outq81_0']
        tgt_before = sample['q81_0']
        break

print('#' * 80)
print("CCNOT operation on q1_22 (control1), q80_0 (control2) and q81_0 (target):")
print("    in:  q1_22={0}, q80_0={1}, q81_0={2}".format(q1_22,q80_0,tgt_before))
print("    out: q1_22={0}, q80_0={1}, q81_0={2}".format(q1_22,q80_0,q81_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_22 control2: q80_0 target: q81_0 ##
################################################################################
if 'q0_22' not in globals():
    q0_22=0
if 'q80_0' not in globals():
    q80_0=0
if 'q81_0' not in globals():
    q81_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq81_0' : 1, 'q81_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq81_0') : 4, ('anc1','q81_0') : -4, ('anc2', 'q0_22') : -2, ('anc2', 'q80_0') : -2, ('anc2', 'outq81_0') : -2, ('anc2', 'q81_0') : 2, ('q0_22', 'q80_0') : 1, ('outq81_0', 'q81_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_22']==q0_22 and sample['q80_0']==q80_0 and sample['q81_0']==q81_0 and int(energy)==0:
        q0_22=sample['q0_22']
        q80_0=sample['q80_0']
        q81_0=sample['outq81_0']
        tgt_before = sample['q81_0']
        break

print('#' * 80)
print("CCNOT operation on q0_22 (control1), q80_0 (control2) and q81_0 (target):")
print("    in:  q0_22={0}, q80_0={1}, q81_0={2}".format(q0_22,q80_0,tgt_before))
print("    out: q0_22={0}, q80_0={1}, q81_0={2}".format(q0_22,q80_0,q81_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q80_0 target: q81_0 ##
################################################################################
if 'q80_0' not in globals():
    q80_0=0
if 'q81_0' not in globals():
    q81_0=0

bqm = dimod.BinaryQuadraticModel({'q80_0' : 1, 'q81_0' : 1, 'outq81_0' : 1, 'anc' : 4}, {('q80_0', 'q81_0') : 2, ('q80_0', 'outq81_0') : -2, ('q81_0', 'outq81_0') : -2, ('q80_0', 'anc') : -4, ('q81_0', 'anc') : -4, ('outq81_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q80_0']==q80_0 and sample['q81_0']==q81_0 and int(energy)==0:
        q80_0=sample['q80_0']
        q81_0=sample['outq81_0']
        tgt_before = sample['q81_0']
        break

print('#' * 80)
print("CNOT operation on q80_0 (control) and q81_0 (target):")
print("    in:  q80_0={0}, q81_0={1}".format(q80_0,tgt_before))
print("    out: q80_0={0}, q81_0={1}".format(q80_0,q81_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_23 control2: q79_0 target: q80_0 ##
################################################################################
if 'q1_23' not in globals():
    q1_23=0
if 'q79_0' not in globals():
    q79_0=0
if 'q80_0' not in globals():
    q80_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq80_0' : 1, 'q80_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq80_0') : 4, ('anc1','q80_0') : -4, ('anc2', 'q1_23') : -2, ('anc2', 'q79_0') : -2, ('anc2', 'outq80_0') : -2, ('anc2', 'q80_0') : 2, ('q1_23', 'q79_0') : 1, ('outq80_0', 'q80_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_23']==q1_23 and sample['q79_0']==q79_0 and sample['q80_0']==q80_0 and int(energy)==0:
        q1_23=sample['q1_23']
        q79_0=sample['q79_0']
        q80_0=sample['outq80_0']
        tgt_before = sample['q80_0']
        break

print('#' * 80)
print("CCNOT operation on q1_23 (control1), q79_0 (control2) and q80_0 (target):")
print("    in:  q1_23={0}, q79_0={1}, q80_0={2}".format(q1_23,q79_0,tgt_before))
print("    out: q1_23={0}, q79_0={1}, q80_0={2}".format(q1_23,q79_0,q80_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_23 control2: q79_0 target: q80_0 ##
################################################################################
if 'q0_23' not in globals():
    q0_23=0
if 'q79_0' not in globals():
    q79_0=0
if 'q80_0' not in globals():
    q80_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq80_0' : 1, 'q80_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq80_0') : 4, ('anc1','q80_0') : -4, ('anc2', 'q0_23') : -2, ('anc2', 'q79_0') : -2, ('anc2', 'outq80_0') : -2, ('anc2', 'q80_0') : 2, ('q0_23', 'q79_0') : 1, ('outq80_0', 'q80_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_23']==q0_23 and sample['q79_0']==q79_0 and sample['q80_0']==q80_0 and int(energy)==0:
        q0_23=sample['q0_23']
        q79_0=sample['q79_0']
        q80_0=sample['outq80_0']
        tgt_before = sample['q80_0']
        break

print('#' * 80)
print("CCNOT operation on q0_23 (control1), q79_0 (control2) and q80_0 (target):")
print("    in:  q0_23={0}, q79_0={1}, q80_0={2}".format(q0_23,q79_0,tgt_before))
print("    out: q0_23={0}, q79_0={1}, q80_0={2}".format(q0_23,q79_0,q80_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q79_0 target: q80_0 ##
################################################################################
if 'q79_0' not in globals():
    q79_0=0
if 'q80_0' not in globals():
    q80_0=0

bqm = dimod.BinaryQuadraticModel({'q79_0' : 1, 'q80_0' : 1, 'outq80_0' : 1, 'anc' : 4}, {('q79_0', 'q80_0') : 2, ('q79_0', 'outq80_0') : -2, ('q80_0', 'outq80_0') : -2, ('q79_0', 'anc') : -4, ('q80_0', 'anc') : -4, ('outq80_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q79_0']==q79_0 and sample['q80_0']==q80_0 and int(energy)==0:
        q79_0=sample['q79_0']
        q80_0=sample['outq80_0']
        tgt_before = sample['q80_0']
        break

print('#' * 80)
print("CNOT operation on q79_0 (control) and q80_0 (target):")
print("    in:  q79_0={0}, q80_0={1}".format(q79_0,tgt_before))
print("    out: q79_0={0}, q80_0={1}".format(q79_0,q80_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_24 control2: q78_0 target: q79_0 ##
################################################################################
if 'q1_24' not in globals():
    q1_24=0
if 'q78_0' not in globals():
    q78_0=0
if 'q79_0' not in globals():
    q79_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq79_0' : 1, 'q79_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq79_0') : 4, ('anc1','q79_0') : -4, ('anc2', 'q1_24') : -2, ('anc2', 'q78_0') : -2, ('anc2', 'outq79_0') : -2, ('anc2', 'q79_0') : 2, ('q1_24', 'q78_0') : 1, ('outq79_0', 'q79_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_24']==q1_24 and sample['q78_0']==q78_0 and sample['q79_0']==q79_0 and int(energy)==0:
        q1_24=sample['q1_24']
        q78_0=sample['q78_0']
        q79_0=sample['outq79_0']
        tgt_before = sample['q79_0']
        break

print('#' * 80)
print("CCNOT operation on q1_24 (control1), q78_0 (control2) and q79_0 (target):")
print("    in:  q1_24={0}, q78_0={1}, q79_0={2}".format(q1_24,q78_0,tgt_before))
print("    out: q1_24={0}, q78_0={1}, q79_0={2}".format(q1_24,q78_0,q79_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_24 control2: q78_0 target: q79_0 ##
################################################################################
if 'q0_24' not in globals():
    q0_24=0
if 'q78_0' not in globals():
    q78_0=0
if 'q79_0' not in globals():
    q79_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq79_0' : 1, 'q79_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq79_0') : 4, ('anc1','q79_0') : -4, ('anc2', 'q0_24') : -2, ('anc2', 'q78_0') : -2, ('anc2', 'outq79_0') : -2, ('anc2', 'q79_0') : 2, ('q0_24', 'q78_0') : 1, ('outq79_0', 'q79_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_24']==q0_24 and sample['q78_0']==q78_0 and sample['q79_0']==q79_0 and int(energy)==0:
        q0_24=sample['q0_24']
        q78_0=sample['q78_0']
        q79_0=sample['outq79_0']
        tgt_before = sample['q79_0']
        break

print('#' * 80)
print("CCNOT operation on q0_24 (control1), q78_0 (control2) and q79_0 (target):")
print("    in:  q0_24={0}, q78_0={1}, q79_0={2}".format(q0_24,q78_0,tgt_before))
print("    out: q0_24={0}, q78_0={1}, q79_0={2}".format(q0_24,q78_0,q79_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q78_0 target: q79_0 ##
################################################################################
if 'q78_0' not in globals():
    q78_0=0
if 'q79_0' not in globals():
    q79_0=0

bqm = dimod.BinaryQuadraticModel({'q78_0' : 1, 'q79_0' : 1, 'outq79_0' : 1, 'anc' : 4}, {('q78_0', 'q79_0') : 2, ('q78_0', 'outq79_0') : -2, ('q79_0', 'outq79_0') : -2, ('q78_0', 'anc') : -4, ('q79_0', 'anc') : -4, ('outq79_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q78_0']==q78_0 and sample['q79_0']==q79_0 and int(energy)==0:
        q78_0=sample['q78_0']
        q79_0=sample['outq79_0']
        tgt_before = sample['q79_0']
        break

print('#' * 80)
print("CNOT operation on q78_0 (control) and q79_0 (target):")
print("    in:  q78_0={0}, q79_0={1}".format(q78_0,tgt_before))
print("    out: q78_0={0}, q79_0={1}".format(q78_0,q79_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_25 control2: q77_0 target: q78_0 ##
################################################################################
if 'q1_25' not in globals():
    q1_25=0
if 'q77_0' not in globals():
    q77_0=0
if 'q78_0' not in globals():
    q78_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq78_0' : 1, 'q78_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq78_0') : 4, ('anc1','q78_0') : -4, ('anc2', 'q1_25') : -2, ('anc2', 'q77_0') : -2, ('anc2', 'outq78_0') : -2, ('anc2', 'q78_0') : 2, ('q1_25', 'q77_0') : 1, ('outq78_0', 'q78_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_25']==q1_25 and sample['q77_0']==q77_0 and sample['q78_0']==q78_0 and int(energy)==0:
        q1_25=sample['q1_25']
        q77_0=sample['q77_0']
        q78_0=sample['outq78_0']
        tgt_before = sample['q78_0']
        break

print('#' * 80)
print("CCNOT operation on q1_25 (control1), q77_0 (control2) and q78_0 (target):")
print("    in:  q1_25={0}, q77_0={1}, q78_0={2}".format(q1_25,q77_0,tgt_before))
print("    out: q1_25={0}, q77_0={1}, q78_0={2}".format(q1_25,q77_0,q78_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_25 control2: q77_0 target: q78_0 ##
################################################################################
if 'q0_25' not in globals():
    q0_25=0
if 'q77_0' not in globals():
    q77_0=0
if 'q78_0' not in globals():
    q78_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq78_0' : 1, 'q78_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq78_0') : 4, ('anc1','q78_0') : -4, ('anc2', 'q0_25') : -2, ('anc2', 'q77_0') : -2, ('anc2', 'outq78_0') : -2, ('anc2', 'q78_0') : 2, ('q0_25', 'q77_0') : 1, ('outq78_0', 'q78_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_25']==q0_25 and sample['q77_0']==q77_0 and sample['q78_0']==q78_0 and int(energy)==0:
        q0_25=sample['q0_25']
        q77_0=sample['q77_0']
        q78_0=sample['outq78_0']
        tgt_before = sample['q78_0']
        break

print('#' * 80)
print("CCNOT operation on q0_25 (control1), q77_0 (control2) and q78_0 (target):")
print("    in:  q0_25={0}, q77_0={1}, q78_0={2}".format(q0_25,q77_0,tgt_before))
print("    out: q0_25={0}, q77_0={1}, q78_0={2}".format(q0_25,q77_0,q78_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q77_0 target: q78_0 ##
################################################################################
if 'q77_0' not in globals():
    q77_0=0
if 'q78_0' not in globals():
    q78_0=0

bqm = dimod.BinaryQuadraticModel({'q77_0' : 1, 'q78_0' : 1, 'outq78_0' : 1, 'anc' : 4}, {('q77_0', 'q78_0') : 2, ('q77_0', 'outq78_0') : -2, ('q78_0', 'outq78_0') : -2, ('q77_0', 'anc') : -4, ('q78_0', 'anc') : -4, ('outq78_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q77_0']==q77_0 and sample['q78_0']==q78_0 and int(energy)==0:
        q77_0=sample['q77_0']
        q78_0=sample['outq78_0']
        tgt_before = sample['q78_0']
        break

print('#' * 80)
print("CNOT operation on q77_0 (control) and q78_0 (target):")
print("    in:  q77_0={0}, q78_0={1}".format(q77_0,tgt_before))
print("    out: q77_0={0}, q78_0={1}".format(q77_0,q78_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_26 control2: q76_0 target: q77_0 ##
################################################################################
if 'q1_26' not in globals():
    q1_26=0
if 'q76_0' not in globals():
    q76_0=0
if 'q77_0' not in globals():
    q77_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq77_0' : 1, 'q77_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq77_0') : 4, ('anc1','q77_0') : -4, ('anc2', 'q1_26') : -2, ('anc2', 'q76_0') : -2, ('anc2', 'outq77_0') : -2, ('anc2', 'q77_0') : 2, ('q1_26', 'q76_0') : 1, ('outq77_0', 'q77_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_26']==q1_26 and sample['q76_0']==q76_0 and sample['q77_0']==q77_0 and int(energy)==0:
        q1_26=sample['q1_26']
        q76_0=sample['q76_0']
        q77_0=sample['outq77_0']
        tgt_before = sample['q77_0']
        break

print('#' * 80)
print("CCNOT operation on q1_26 (control1), q76_0 (control2) and q77_0 (target):")
print("    in:  q1_26={0}, q76_0={1}, q77_0={2}".format(q1_26,q76_0,tgt_before))
print("    out: q1_26={0}, q76_0={1}, q77_0={2}".format(q1_26,q76_0,q77_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_26 control2: q76_0 target: q77_0 ##
################################################################################
if 'q0_26' not in globals():
    q0_26=0
if 'q76_0' not in globals():
    q76_0=0
if 'q77_0' not in globals():
    q77_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq77_0' : 1, 'q77_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq77_0') : 4, ('anc1','q77_0') : -4, ('anc2', 'q0_26') : -2, ('anc2', 'q76_0') : -2, ('anc2', 'outq77_0') : -2, ('anc2', 'q77_0') : 2, ('q0_26', 'q76_0') : 1, ('outq77_0', 'q77_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_26']==q0_26 and sample['q76_0']==q76_0 and sample['q77_0']==q77_0 and int(energy)==0:
        q0_26=sample['q0_26']
        q76_0=sample['q76_0']
        q77_0=sample['outq77_0']
        tgt_before = sample['q77_0']
        break

print('#' * 80)
print("CCNOT operation on q0_26 (control1), q76_0 (control2) and q77_0 (target):")
print("    in:  q0_26={0}, q76_0={1}, q77_0={2}".format(q0_26,q76_0,tgt_before))
print("    out: q0_26={0}, q76_0={1}, q77_0={2}".format(q0_26,q76_0,q77_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q76_0 target: q77_0 ##
################################################################################
if 'q76_0' not in globals():
    q76_0=0
if 'q77_0' not in globals():
    q77_0=0

bqm = dimod.BinaryQuadraticModel({'q76_0' : 1, 'q77_0' : 1, 'outq77_0' : 1, 'anc' : 4}, {('q76_0', 'q77_0') : 2, ('q76_0', 'outq77_0') : -2, ('q77_0', 'outq77_0') : -2, ('q76_0', 'anc') : -4, ('q77_0', 'anc') : -4, ('outq77_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q76_0']==q76_0 and sample['q77_0']==q77_0 and int(energy)==0:
        q76_0=sample['q76_0']
        q77_0=sample['outq77_0']
        tgt_before = sample['q77_0']
        break

print('#' * 80)
print("CNOT operation on q76_0 (control) and q77_0 (target):")
print("    in:  q76_0={0}, q77_0={1}".format(q76_0,tgt_before))
print("    out: q76_0={0}, q77_0={1}".format(q76_0,q77_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_27 control2: q75_0 target: q76_0 ##
################################################################################
if 'q1_27' not in globals():
    q1_27=0
if 'q75_0' not in globals():
    q75_0=0
if 'q76_0' not in globals():
    q76_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq76_0' : 1, 'q76_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq76_0') : 4, ('anc1','q76_0') : -4, ('anc2', 'q1_27') : -2, ('anc2', 'q75_0') : -2, ('anc2', 'outq76_0') : -2, ('anc2', 'q76_0') : 2, ('q1_27', 'q75_0') : 1, ('outq76_0', 'q76_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_27']==q1_27 and sample['q75_0']==q75_0 and sample['q76_0']==q76_0 and int(energy)==0:
        q1_27=sample['q1_27']
        q75_0=sample['q75_0']
        q76_0=sample['outq76_0']
        tgt_before = sample['q76_0']
        break

print('#' * 80)
print("CCNOT operation on q1_27 (control1), q75_0 (control2) and q76_0 (target):")
print("    in:  q1_27={0}, q75_0={1}, q76_0={2}".format(q1_27,q75_0,tgt_before))
print("    out: q1_27={0}, q75_0={1}, q76_0={2}".format(q1_27,q75_0,q76_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_27 control2: q75_0 target: q76_0 ##
################################################################################
if 'q0_27' not in globals():
    q0_27=0
if 'q75_0' not in globals():
    q75_0=0
if 'q76_0' not in globals():
    q76_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq76_0' : 1, 'q76_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq76_0') : 4, ('anc1','q76_0') : -4, ('anc2', 'q0_27') : -2, ('anc2', 'q75_0') : -2, ('anc2', 'outq76_0') : -2, ('anc2', 'q76_0') : 2, ('q0_27', 'q75_0') : 1, ('outq76_0', 'q76_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_27']==q0_27 and sample['q75_0']==q75_0 and sample['q76_0']==q76_0 and int(energy)==0:
        q0_27=sample['q0_27']
        q75_0=sample['q75_0']
        q76_0=sample['outq76_0']
        tgt_before = sample['q76_0']
        break

print('#' * 80)
print("CCNOT operation on q0_27 (control1), q75_0 (control2) and q76_0 (target):")
print("    in:  q0_27={0}, q75_0={1}, q76_0={2}".format(q0_27,q75_0,tgt_before))
print("    out: q0_27={0}, q75_0={1}, q76_0={2}".format(q0_27,q75_0,q76_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q75_0 target: q76_0 ##
################################################################################
if 'q75_0' not in globals():
    q75_0=0
if 'q76_0' not in globals():
    q76_0=0

bqm = dimod.BinaryQuadraticModel({'q75_0' : 1, 'q76_0' : 1, 'outq76_0' : 1, 'anc' : 4}, {('q75_0', 'q76_0') : 2, ('q75_0', 'outq76_0') : -2, ('q76_0', 'outq76_0') : -2, ('q75_0', 'anc') : -4, ('q76_0', 'anc') : -4, ('outq76_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q75_0']==q75_0 and sample['q76_0']==q76_0 and int(energy)==0:
        q75_0=sample['q75_0']
        q76_0=sample['outq76_0']
        tgt_before = sample['q76_0']
        break

print('#' * 80)
print("CNOT operation on q75_0 (control) and q76_0 (target):")
print("    in:  q75_0={0}, q76_0={1}".format(q75_0,tgt_before))
print("    out: q75_0={0}, q76_0={1}".format(q75_0,q76_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_28 control2: q74_0 target: q75_0 ##
################################################################################
if 'q1_28' not in globals():
    q1_28=0
if 'q74_0' not in globals():
    q74_0=0
if 'q75_0' not in globals():
    q75_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq75_0' : 1, 'q75_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq75_0') : 4, ('anc1','q75_0') : -4, ('anc2', 'q1_28') : -2, ('anc2', 'q74_0') : -2, ('anc2', 'outq75_0') : -2, ('anc2', 'q75_0') : 2, ('q1_28', 'q74_0') : 1, ('outq75_0', 'q75_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_28']==q1_28 and sample['q74_0']==q74_0 and sample['q75_0']==q75_0 and int(energy)==0:
        q1_28=sample['q1_28']
        q74_0=sample['q74_0']
        q75_0=sample['outq75_0']
        tgt_before = sample['q75_0']
        break

print('#' * 80)
print("CCNOT operation on q1_28 (control1), q74_0 (control2) and q75_0 (target):")
print("    in:  q1_28={0}, q74_0={1}, q75_0={2}".format(q1_28,q74_0,tgt_before))
print("    out: q1_28={0}, q74_0={1}, q75_0={2}".format(q1_28,q74_0,q75_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_28 control2: q74_0 target: q75_0 ##
################################################################################
if 'q0_28' not in globals():
    q0_28=0
if 'q74_0' not in globals():
    q74_0=0
if 'q75_0' not in globals():
    q75_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq75_0' : 1, 'q75_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq75_0') : 4, ('anc1','q75_0') : -4, ('anc2', 'q0_28') : -2, ('anc2', 'q74_0') : -2, ('anc2', 'outq75_0') : -2, ('anc2', 'q75_0') : 2, ('q0_28', 'q74_0') : 1, ('outq75_0', 'q75_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_28']==q0_28 and sample['q74_0']==q74_0 and sample['q75_0']==q75_0 and int(energy)==0:
        q0_28=sample['q0_28']
        q74_0=sample['q74_0']
        q75_0=sample['outq75_0']
        tgt_before = sample['q75_0']
        break

print('#' * 80)
print("CCNOT operation on q0_28 (control1), q74_0 (control2) and q75_0 (target):")
print("    in:  q0_28={0}, q74_0={1}, q75_0={2}".format(q0_28,q74_0,tgt_before))
print("    out: q0_28={0}, q74_0={1}, q75_0={2}".format(q0_28,q74_0,q75_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q74_0 target: q75_0 ##
################################################################################
if 'q74_0' not in globals():
    q74_0=0
if 'q75_0' not in globals():
    q75_0=0

bqm = dimod.BinaryQuadraticModel({'q74_0' : 1, 'q75_0' : 1, 'outq75_0' : 1, 'anc' : 4}, {('q74_0', 'q75_0') : 2, ('q74_0', 'outq75_0') : -2, ('q75_0', 'outq75_0') : -2, ('q74_0', 'anc') : -4, ('q75_0', 'anc') : -4, ('outq75_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q74_0']==q74_0 and sample['q75_0']==q75_0 and int(energy)==0:
        q74_0=sample['q74_0']
        q75_0=sample['outq75_0']
        tgt_before = sample['q75_0']
        break

print('#' * 80)
print("CNOT operation on q74_0 (control) and q75_0 (target):")
print("    in:  q74_0={0}, q75_0={1}".format(q74_0,tgt_before))
print("    out: q74_0={0}, q75_0={1}".format(q74_0,q75_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_29 control2: q73_0 target: q74_0 ##
################################################################################
if 'q1_29' not in globals():
    q1_29=0
if 'q73_0' not in globals():
    q73_0=0
if 'q74_0' not in globals():
    q74_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq74_0' : 1, 'q74_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq74_0') : 4, ('anc1','q74_0') : -4, ('anc2', 'q1_29') : -2, ('anc2', 'q73_0') : -2, ('anc2', 'outq74_0') : -2, ('anc2', 'q74_0') : 2, ('q1_29', 'q73_0') : 1, ('outq74_0', 'q74_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_29']==q1_29 and sample['q73_0']==q73_0 and sample['q74_0']==q74_0 and int(energy)==0:
        q1_29=sample['q1_29']
        q73_0=sample['q73_0']
        q74_0=sample['outq74_0']
        tgt_before = sample['q74_0']
        break

print('#' * 80)
print("CCNOT operation on q1_29 (control1), q73_0 (control2) and q74_0 (target):")
print("    in:  q1_29={0}, q73_0={1}, q74_0={2}".format(q1_29,q73_0,tgt_before))
print("    out: q1_29={0}, q73_0={1}, q74_0={2}".format(q1_29,q73_0,q74_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_29 control2: q73_0 target: q74_0 ##
################################################################################
if 'q0_29' not in globals():
    q0_29=0
if 'q73_0' not in globals():
    q73_0=0
if 'q74_0' not in globals():
    q74_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq74_0' : 1, 'q74_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq74_0') : 4, ('anc1','q74_0') : -4, ('anc2', 'q0_29') : -2, ('anc2', 'q73_0') : -2, ('anc2', 'outq74_0') : -2, ('anc2', 'q74_0') : 2, ('q0_29', 'q73_0') : 1, ('outq74_0', 'q74_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_29']==q0_29 and sample['q73_0']==q73_0 and sample['q74_0']==q74_0 and int(energy)==0:
        q0_29=sample['q0_29']
        q73_0=sample['q73_0']
        q74_0=sample['outq74_0']
        tgt_before = sample['q74_0']
        break

print('#' * 80)
print("CCNOT operation on q0_29 (control1), q73_0 (control2) and q74_0 (target):")
print("    in:  q0_29={0}, q73_0={1}, q74_0={2}".format(q0_29,q73_0,tgt_before))
print("    out: q0_29={0}, q73_0={1}, q74_0={2}".format(q0_29,q73_0,q74_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q73_0 target: q74_0 ##
################################################################################
if 'q73_0' not in globals():
    q73_0=0
if 'q74_0' not in globals():
    q74_0=0

bqm = dimod.BinaryQuadraticModel({'q73_0' : 1, 'q74_0' : 1, 'outq74_0' : 1, 'anc' : 4}, {('q73_0', 'q74_0') : 2, ('q73_0', 'outq74_0') : -2, ('q74_0', 'outq74_0') : -2, ('q73_0', 'anc') : -4, ('q74_0', 'anc') : -4, ('outq74_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q73_0']==q73_0 and sample['q74_0']==q74_0 and int(energy)==0:
        q73_0=sample['q73_0']
        q74_0=sample['outq74_0']
        tgt_before = sample['q74_0']
        break

print('#' * 80)
print("CNOT operation on q73_0 (control) and q74_0 (target):")
print("    in:  q73_0={0}, q74_0={1}".format(q73_0,tgt_before))
print("    out: q73_0={0}, q74_0={1}".format(q73_0,q74_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_30 control2: q72_0 target: q73_0 ##
################################################################################
if 'q1_30' not in globals():
    q1_30=0
if 'q72_0' not in globals():
    q72_0=0
if 'q73_0' not in globals():
    q73_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq73_0' : 1, 'q73_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq73_0') : 4, ('anc1','q73_0') : -4, ('anc2', 'q1_30') : -2, ('anc2', 'q72_0') : -2, ('anc2', 'outq73_0') : -2, ('anc2', 'q73_0') : 2, ('q1_30', 'q72_0') : 1, ('outq73_0', 'q73_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_30']==q1_30 and sample['q72_0']==q72_0 and sample['q73_0']==q73_0 and int(energy)==0:
        q1_30=sample['q1_30']
        q72_0=sample['q72_0']
        q73_0=sample['outq73_0']
        tgt_before = sample['q73_0']
        break

print('#' * 80)
print("CCNOT operation on q1_30 (control1), q72_0 (control2) and q73_0 (target):")
print("    in:  q1_30={0}, q72_0={1}, q73_0={2}".format(q1_30,q72_0,tgt_before))
print("    out: q1_30={0}, q72_0={1}, q73_0={2}".format(q1_30,q72_0,q73_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_30 control2: q72_0 target: q73_0 ##
################################################################################
if 'q0_30' not in globals():
    q0_30=0
if 'q72_0' not in globals():
    q72_0=0
if 'q73_0' not in globals():
    q73_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq73_0' : 1, 'q73_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq73_0') : 4, ('anc1','q73_0') : -4, ('anc2', 'q0_30') : -2, ('anc2', 'q72_0') : -2, ('anc2', 'outq73_0') : -2, ('anc2', 'q73_0') : 2, ('q0_30', 'q72_0') : 1, ('outq73_0', 'q73_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_30']==q0_30 and sample['q72_0']==q72_0 and sample['q73_0']==q73_0 and int(energy)==0:
        q0_30=sample['q0_30']
        q72_0=sample['q72_0']
        q73_0=sample['outq73_0']
        tgt_before = sample['q73_0']
        break

print('#' * 80)
print("CCNOT operation on q0_30 (control1), q72_0 (control2) and q73_0 (target):")
print("    in:  q0_30={0}, q72_0={1}, q73_0={2}".format(q0_30,q72_0,tgt_before))
print("    out: q0_30={0}, q72_0={1}, q73_0={2}".format(q0_30,q72_0,q73_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q72_0 target: q73_0 ##
################################################################################
if 'q72_0' not in globals():
    q72_0=0
if 'q73_0' not in globals():
    q73_0=0

bqm = dimod.BinaryQuadraticModel({'q72_0' : 1, 'q73_0' : 1, 'outq73_0' : 1, 'anc' : 4}, {('q72_0', 'q73_0') : 2, ('q72_0', 'outq73_0') : -2, ('q73_0', 'outq73_0') : -2, ('q72_0', 'anc') : -4, ('q73_0', 'anc') : -4, ('outq73_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q72_0']==q72_0 and sample['q73_0']==q73_0 and int(energy)==0:
        q72_0=sample['q72_0']
        q73_0=sample['outq73_0']
        tgt_before = sample['q73_0']
        break

print('#' * 80)
print("CNOT operation on q72_0 (control) and q73_0 (target):")
print("    in:  q72_0={0}, q73_0={1}".format(q72_0,tgt_before))
print("    out: q72_0={0}, q73_0={1}".format(q72_0,q73_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_31 control2: q71_0 target: q72_0 ##
################################################################################
if 'q1_31' not in globals():
    q1_31=0
if 'q71_0' not in globals():
    q71_0=0
if 'q72_0' not in globals():
    q72_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq72_0' : 1, 'q72_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq72_0') : 4, ('anc1','q72_0') : -4, ('anc2', 'q1_31') : -2, ('anc2', 'q71_0') : -2, ('anc2', 'outq72_0') : -2, ('anc2', 'q72_0') : 2, ('q1_31', 'q71_0') : 1, ('outq72_0', 'q72_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_31']==q1_31 and sample['q71_0']==q71_0 and sample['q72_0']==q72_0 and int(energy)==0:
        q1_31=sample['q1_31']
        q71_0=sample['q71_0']
        q72_0=sample['outq72_0']
        tgt_before = sample['q72_0']
        break

print('#' * 80)
print("CCNOT operation on q1_31 (control1), q71_0 (control2) and q72_0 (target):")
print("    in:  q1_31={0}, q71_0={1}, q72_0={2}".format(q1_31,q71_0,tgt_before))
print("    out: q1_31={0}, q71_0={1}, q72_0={2}".format(q1_31,q71_0,q72_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_31 control2: q71_0 target: q72_0 ##
################################################################################
if 'q0_31' not in globals():
    q0_31=0
if 'q71_0' not in globals():
    q71_0=0
if 'q72_0' not in globals():
    q72_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq72_0' : 1, 'q72_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq72_0') : 4, ('anc1','q72_0') : -4, ('anc2', 'q0_31') : -2, ('anc2', 'q71_0') : -2, ('anc2', 'outq72_0') : -2, ('anc2', 'q72_0') : 2, ('q0_31', 'q71_0') : 1, ('outq72_0', 'q72_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_31']==q0_31 and sample['q71_0']==q71_0 and sample['q72_0']==q72_0 and int(energy)==0:
        q0_31=sample['q0_31']
        q71_0=sample['q71_0']
        q72_0=sample['outq72_0']
        tgt_before = sample['q72_0']
        break

print('#' * 80)
print("CCNOT operation on q0_31 (control1), q71_0 (control2) and q72_0 (target):")
print("    in:  q0_31={0}, q71_0={1}, q72_0={2}".format(q0_31,q71_0,tgt_before))
print("    out: q0_31={0}, q71_0={1}, q72_0={2}".format(q0_31,q71_0,q72_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q71_0 target: q72_0 ##
################################################################################
if 'q71_0' not in globals():
    q71_0=0
if 'q72_0' not in globals():
    q72_0=0

bqm = dimod.BinaryQuadraticModel({'q71_0' : 1, 'q72_0' : 1, 'outq72_0' : 1, 'anc' : 4}, {('q71_0', 'q72_0') : 2, ('q71_0', 'outq72_0') : -2, ('q72_0', 'outq72_0') : -2, ('q71_0', 'anc') : -4, ('q72_0', 'anc') : -4, ('outq72_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q71_0']==q71_0 and sample['q72_0']==q72_0 and int(energy)==0:
        q71_0=sample['q71_0']
        q72_0=sample['outq72_0']
        tgt_before = sample['q72_0']
        break

print('#' * 80)
print("CNOT operation on q71_0 (control) and q72_0 (target):")
print("    in:  q71_0={0}, q72_0={1}".format(q71_0,tgt_before))
print("    out: q71_0={0}, q72_0={1}".format(q71_0,q72_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_32 control2: q70_0 target: q71_0 ##
################################################################################
if 'q1_32' not in globals():
    q1_32=0
if 'q70_0' not in globals():
    q70_0=0
if 'q71_0' not in globals():
    q71_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq71_0' : 1, 'q71_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq71_0') : 4, ('anc1','q71_0') : -4, ('anc2', 'q1_32') : -2, ('anc2', 'q70_0') : -2, ('anc2', 'outq71_0') : -2, ('anc2', 'q71_0') : 2, ('q1_32', 'q70_0') : 1, ('outq71_0', 'q71_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_32']==q1_32 and sample['q70_0']==q70_0 and sample['q71_0']==q71_0 and int(energy)==0:
        q1_32=sample['q1_32']
        q70_0=sample['q70_0']
        q71_0=sample['outq71_0']
        tgt_before = sample['q71_0']
        break

print('#' * 80)
print("CCNOT operation on q1_32 (control1), q70_0 (control2) and q71_0 (target):")
print("    in:  q1_32={0}, q70_0={1}, q71_0={2}".format(q1_32,q70_0,tgt_before))
print("    out: q1_32={0}, q70_0={1}, q71_0={2}".format(q1_32,q70_0,q71_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_32 control2: q70_0 target: q71_0 ##
################################################################################
if 'q0_32' not in globals():
    q0_32=0
if 'q70_0' not in globals():
    q70_0=0
if 'q71_0' not in globals():
    q71_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq71_0' : 1, 'q71_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq71_0') : 4, ('anc1','q71_0') : -4, ('anc2', 'q0_32') : -2, ('anc2', 'q70_0') : -2, ('anc2', 'outq71_0') : -2, ('anc2', 'q71_0') : 2, ('q0_32', 'q70_0') : 1, ('outq71_0', 'q71_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_32']==q0_32 and sample['q70_0']==q70_0 and sample['q71_0']==q71_0 and int(energy)==0:
        q0_32=sample['q0_32']
        q70_0=sample['q70_0']
        q71_0=sample['outq71_0']
        tgt_before = sample['q71_0']
        break

print('#' * 80)
print("CCNOT operation on q0_32 (control1), q70_0 (control2) and q71_0 (target):")
print("    in:  q0_32={0}, q70_0={1}, q71_0={2}".format(q0_32,q70_0,tgt_before))
print("    out: q0_32={0}, q70_0={1}, q71_0={2}".format(q0_32,q70_0,q71_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q70_0 target: q71_0 ##
################################################################################
if 'q70_0' not in globals():
    q70_0=0
if 'q71_0' not in globals():
    q71_0=0

bqm = dimod.BinaryQuadraticModel({'q70_0' : 1, 'q71_0' : 1, 'outq71_0' : 1, 'anc' : 4}, {('q70_0', 'q71_0') : 2, ('q70_0', 'outq71_0') : -2, ('q71_0', 'outq71_0') : -2, ('q70_0', 'anc') : -4, ('q71_0', 'anc') : -4, ('outq71_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q70_0']==q70_0 and sample['q71_0']==q71_0 and int(energy)==0:
        q70_0=sample['q70_0']
        q71_0=sample['outq71_0']
        tgt_before = sample['q71_0']
        break

print('#' * 80)
print("CNOT operation on q70_0 (control) and q71_0 (target):")
print("    in:  q70_0={0}, q71_0={1}".format(q70_0,tgt_before))
print("    out: q70_0={0}, q71_0={1}".format(q70_0,q71_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_33 control2: q69_0 target: q70_0 ##
################################################################################
if 'q1_33' not in globals():
    q1_33=0
if 'q69_0' not in globals():
    q69_0=0
if 'q70_0' not in globals():
    q70_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq70_0' : 1, 'q70_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq70_0') : 4, ('anc1','q70_0') : -4, ('anc2', 'q1_33') : -2, ('anc2', 'q69_0') : -2, ('anc2', 'outq70_0') : -2, ('anc2', 'q70_0') : 2, ('q1_33', 'q69_0') : 1, ('outq70_0', 'q70_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_33']==q1_33 and sample['q69_0']==q69_0 and sample['q70_0']==q70_0 and int(energy)==0:
        q1_33=sample['q1_33']
        q69_0=sample['q69_0']
        q70_0=sample['outq70_0']
        tgt_before = sample['q70_0']
        break

print('#' * 80)
print("CCNOT operation on q1_33 (control1), q69_0 (control2) and q70_0 (target):")
print("    in:  q1_33={0}, q69_0={1}, q70_0={2}".format(q1_33,q69_0,tgt_before))
print("    out: q1_33={0}, q69_0={1}, q70_0={2}".format(q1_33,q69_0,q70_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_33 control2: q69_0 target: q70_0 ##
################################################################################
if 'q0_33' not in globals():
    q0_33=0
if 'q69_0' not in globals():
    q69_0=0
if 'q70_0' not in globals():
    q70_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq70_0' : 1, 'q70_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq70_0') : 4, ('anc1','q70_0') : -4, ('anc2', 'q0_33') : -2, ('anc2', 'q69_0') : -2, ('anc2', 'outq70_0') : -2, ('anc2', 'q70_0') : 2, ('q0_33', 'q69_0') : 1, ('outq70_0', 'q70_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_33']==q0_33 and sample['q69_0']==q69_0 and sample['q70_0']==q70_0 and int(energy)==0:
        q0_33=sample['q0_33']
        q69_0=sample['q69_0']
        q70_0=sample['outq70_0']
        tgt_before = sample['q70_0']
        break

print('#' * 80)
print("CCNOT operation on q0_33 (control1), q69_0 (control2) and q70_0 (target):")
print("    in:  q0_33={0}, q69_0={1}, q70_0={2}".format(q0_33,q69_0,tgt_before))
print("    out: q0_33={0}, q69_0={1}, q70_0={2}".format(q0_33,q69_0,q70_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q69_0 target: q70_0 ##
################################################################################
if 'q69_0' not in globals():
    q69_0=0
if 'q70_0' not in globals():
    q70_0=0

bqm = dimod.BinaryQuadraticModel({'q69_0' : 1, 'q70_0' : 1, 'outq70_0' : 1, 'anc' : 4}, {('q69_0', 'q70_0') : 2, ('q69_0', 'outq70_0') : -2, ('q70_0', 'outq70_0') : -2, ('q69_0', 'anc') : -4, ('q70_0', 'anc') : -4, ('outq70_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q69_0']==q69_0 and sample['q70_0']==q70_0 and int(energy)==0:
        q69_0=sample['q69_0']
        q70_0=sample['outq70_0']
        tgt_before = sample['q70_0']
        break

print('#' * 80)
print("CNOT operation on q69_0 (control) and q70_0 (target):")
print("    in:  q69_0={0}, q70_0={1}".format(q69_0,tgt_before))
print("    out: q69_0={0}, q70_0={1}".format(q69_0,q70_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_34 control2: q68_0 target: q69_0 ##
################################################################################
if 'q1_34' not in globals():
    q1_34=0
if 'q68_0' not in globals():
    q68_0=0
if 'q69_0' not in globals():
    q69_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq69_0' : 1, 'q69_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq69_0') : 4, ('anc1','q69_0') : -4, ('anc2', 'q1_34') : -2, ('anc2', 'q68_0') : -2, ('anc2', 'outq69_0') : -2, ('anc2', 'q69_0') : 2, ('q1_34', 'q68_0') : 1, ('outq69_0', 'q69_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_34']==q1_34 and sample['q68_0']==q68_0 and sample['q69_0']==q69_0 and int(energy)==0:
        q1_34=sample['q1_34']
        q68_0=sample['q68_0']
        q69_0=sample['outq69_0']
        tgt_before = sample['q69_0']
        break

print('#' * 80)
print("CCNOT operation on q1_34 (control1), q68_0 (control2) and q69_0 (target):")
print("    in:  q1_34={0}, q68_0={1}, q69_0={2}".format(q1_34,q68_0,tgt_before))
print("    out: q1_34={0}, q68_0={1}, q69_0={2}".format(q1_34,q68_0,q69_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_34 control2: q68_0 target: q69_0 ##
################################################################################
if 'q0_34' not in globals():
    q0_34=0
if 'q68_0' not in globals():
    q68_0=0
if 'q69_0' not in globals():
    q69_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq69_0' : 1, 'q69_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq69_0') : 4, ('anc1','q69_0') : -4, ('anc2', 'q0_34') : -2, ('anc2', 'q68_0') : -2, ('anc2', 'outq69_0') : -2, ('anc2', 'q69_0') : 2, ('q0_34', 'q68_0') : 1, ('outq69_0', 'q69_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_34']==q0_34 and sample['q68_0']==q68_0 and sample['q69_0']==q69_0 and int(energy)==0:
        q0_34=sample['q0_34']
        q68_0=sample['q68_0']
        q69_0=sample['outq69_0']
        tgt_before = sample['q69_0']
        break

print('#' * 80)
print("CCNOT operation on q0_34 (control1), q68_0 (control2) and q69_0 (target):")
print("    in:  q0_34={0}, q68_0={1}, q69_0={2}".format(q0_34,q68_0,tgt_before))
print("    out: q0_34={0}, q68_0={1}, q69_0={2}".format(q0_34,q68_0,q69_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q68_0 target: q69_0 ##
################################################################################
if 'q68_0' not in globals():
    q68_0=0
if 'q69_0' not in globals():
    q69_0=0

bqm = dimod.BinaryQuadraticModel({'q68_0' : 1, 'q69_0' : 1, 'outq69_0' : 1, 'anc' : 4}, {('q68_0', 'q69_0') : 2, ('q68_0', 'outq69_0') : -2, ('q69_0', 'outq69_0') : -2, ('q68_0', 'anc') : -4, ('q69_0', 'anc') : -4, ('outq69_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q68_0']==q68_0 and sample['q69_0']==q69_0 and int(energy)==0:
        q68_0=sample['q68_0']
        q69_0=sample['outq69_0']
        tgt_before = sample['q69_0']
        break

print('#' * 80)
print("CNOT operation on q68_0 (control) and q69_0 (target):")
print("    in:  q68_0={0}, q69_0={1}".format(q68_0,tgt_before))
print("    out: q68_0={0}, q69_0={1}".format(q68_0,q69_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_35 control2: q67_0 target: q68_0 ##
################################################################################
if 'q1_35' not in globals():
    q1_35=0
if 'q67_0' not in globals():
    q67_0=0
if 'q68_0' not in globals():
    q68_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq68_0' : 1, 'q68_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq68_0') : 4, ('anc1','q68_0') : -4, ('anc2', 'q1_35') : -2, ('anc2', 'q67_0') : -2, ('anc2', 'outq68_0') : -2, ('anc2', 'q68_0') : 2, ('q1_35', 'q67_0') : 1, ('outq68_0', 'q68_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_35']==q1_35 and sample['q67_0']==q67_0 and sample['q68_0']==q68_0 and int(energy)==0:
        q1_35=sample['q1_35']
        q67_0=sample['q67_0']
        q68_0=sample['outq68_0']
        tgt_before = sample['q68_0']
        break

print('#' * 80)
print("CCNOT operation on q1_35 (control1), q67_0 (control2) and q68_0 (target):")
print("    in:  q1_35={0}, q67_0={1}, q68_0={2}".format(q1_35,q67_0,tgt_before))
print("    out: q1_35={0}, q67_0={1}, q68_0={2}".format(q1_35,q67_0,q68_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_35 control2: q67_0 target: q68_0 ##
################################################################################
if 'q0_35' not in globals():
    q0_35=0
if 'q67_0' not in globals():
    q67_0=0
if 'q68_0' not in globals():
    q68_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq68_0' : 1, 'q68_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq68_0') : 4, ('anc1','q68_0') : -4, ('anc2', 'q0_35') : -2, ('anc2', 'q67_0') : -2, ('anc2', 'outq68_0') : -2, ('anc2', 'q68_0') : 2, ('q0_35', 'q67_0') : 1, ('outq68_0', 'q68_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_35']==q0_35 and sample['q67_0']==q67_0 and sample['q68_0']==q68_0 and int(energy)==0:
        q0_35=sample['q0_35']
        q67_0=sample['q67_0']
        q68_0=sample['outq68_0']
        tgt_before = sample['q68_0']
        break

print('#' * 80)
print("CCNOT operation on q0_35 (control1), q67_0 (control2) and q68_0 (target):")
print("    in:  q0_35={0}, q67_0={1}, q68_0={2}".format(q0_35,q67_0,tgt_before))
print("    out: q0_35={0}, q67_0={1}, q68_0={2}".format(q0_35,q67_0,q68_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q67_0 target: q68_0 ##
################################################################################
if 'q67_0' not in globals():
    q67_0=0
if 'q68_0' not in globals():
    q68_0=0

bqm = dimod.BinaryQuadraticModel({'q67_0' : 1, 'q68_0' : 1, 'outq68_0' : 1, 'anc' : 4}, {('q67_0', 'q68_0') : 2, ('q67_0', 'outq68_0') : -2, ('q68_0', 'outq68_0') : -2, ('q67_0', 'anc') : -4, ('q68_0', 'anc') : -4, ('outq68_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q67_0']==q67_0 and sample['q68_0']==q68_0 and int(energy)==0:
        q67_0=sample['q67_0']
        q68_0=sample['outq68_0']
        tgt_before = sample['q68_0']
        break

print('#' * 80)
print("CNOT operation on q67_0 (control) and q68_0 (target):")
print("    in:  q67_0={0}, q68_0={1}".format(q67_0,tgt_before))
print("    out: q67_0={0}, q68_0={1}".format(q67_0,q68_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_36 control2: q66_0 target: q67_0 ##
################################################################################
if 'q1_36' not in globals():
    q1_36=0
if 'q66_0' not in globals():
    q66_0=0
if 'q67_0' not in globals():
    q67_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq67_0' : 1, 'q67_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq67_0') : 4, ('anc1','q67_0') : -4, ('anc2', 'q1_36') : -2, ('anc2', 'q66_0') : -2, ('anc2', 'outq67_0') : -2, ('anc2', 'q67_0') : 2, ('q1_36', 'q66_0') : 1, ('outq67_0', 'q67_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_36']==q1_36 and sample['q66_0']==q66_0 and sample['q67_0']==q67_0 and int(energy)==0:
        q1_36=sample['q1_36']
        q66_0=sample['q66_0']
        q67_0=sample['outq67_0']
        tgt_before = sample['q67_0']
        break

print('#' * 80)
print("CCNOT operation on q1_36 (control1), q66_0 (control2) and q67_0 (target):")
print("    in:  q1_36={0}, q66_0={1}, q67_0={2}".format(q1_36,q66_0,tgt_before))
print("    out: q1_36={0}, q66_0={1}, q67_0={2}".format(q1_36,q66_0,q67_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_36 control2: q66_0 target: q67_0 ##
################################################################################
if 'q0_36' not in globals():
    q0_36=0
if 'q66_0' not in globals():
    q66_0=0
if 'q67_0' not in globals():
    q67_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq67_0' : 1, 'q67_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq67_0') : 4, ('anc1','q67_0') : -4, ('anc2', 'q0_36') : -2, ('anc2', 'q66_0') : -2, ('anc2', 'outq67_0') : -2, ('anc2', 'q67_0') : 2, ('q0_36', 'q66_0') : 1, ('outq67_0', 'q67_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_36']==q0_36 and sample['q66_0']==q66_0 and sample['q67_0']==q67_0 and int(energy)==0:
        q0_36=sample['q0_36']
        q66_0=sample['q66_0']
        q67_0=sample['outq67_0']
        tgt_before = sample['q67_0']
        break

print('#' * 80)
print("CCNOT operation on q0_36 (control1), q66_0 (control2) and q67_0 (target):")
print("    in:  q0_36={0}, q66_0={1}, q67_0={2}".format(q0_36,q66_0,tgt_before))
print("    out: q0_36={0}, q66_0={1}, q67_0={2}".format(q0_36,q66_0,q67_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q66_0 target: q67_0 ##
################################################################################
if 'q66_0' not in globals():
    q66_0=0
if 'q67_0' not in globals():
    q67_0=0

bqm = dimod.BinaryQuadraticModel({'q66_0' : 1, 'q67_0' : 1, 'outq67_0' : 1, 'anc' : 4}, {('q66_0', 'q67_0') : 2, ('q66_0', 'outq67_0') : -2, ('q67_0', 'outq67_0') : -2, ('q66_0', 'anc') : -4, ('q67_0', 'anc') : -4, ('outq67_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q66_0']==q66_0 and sample['q67_0']==q67_0 and int(energy)==0:
        q66_0=sample['q66_0']
        q67_0=sample['outq67_0']
        tgt_before = sample['q67_0']
        break

print('#' * 80)
print("CNOT operation on q66_0 (control) and q67_0 (target):")
print("    in:  q66_0={0}, q67_0={1}".format(q66_0,tgt_before))
print("    out: q66_0={0}, q67_0={1}".format(q66_0,q67_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_37 control2: q65_0 target: q66_0 ##
################################################################################
if 'q1_37' not in globals():
    q1_37=0
if 'q65_0' not in globals():
    q65_0=0
if 'q66_0' not in globals():
    q66_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq66_0' : 1, 'q66_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq66_0') : 4, ('anc1','q66_0') : -4, ('anc2', 'q1_37') : -2, ('anc2', 'q65_0') : -2, ('anc2', 'outq66_0') : -2, ('anc2', 'q66_0') : 2, ('q1_37', 'q65_0') : 1, ('outq66_0', 'q66_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_37']==q1_37 and sample['q65_0']==q65_0 and sample['q66_0']==q66_0 and int(energy)==0:
        q1_37=sample['q1_37']
        q65_0=sample['q65_0']
        q66_0=sample['outq66_0']
        tgt_before = sample['q66_0']
        break

print('#' * 80)
print("CCNOT operation on q1_37 (control1), q65_0 (control2) and q66_0 (target):")
print("    in:  q1_37={0}, q65_0={1}, q66_0={2}".format(q1_37,q65_0,tgt_before))
print("    out: q1_37={0}, q65_0={1}, q66_0={2}".format(q1_37,q65_0,q66_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_37 control2: q65_0 target: q66_0 ##
################################################################################
if 'q0_37' not in globals():
    q0_37=0
if 'q65_0' not in globals():
    q65_0=0
if 'q66_0' not in globals():
    q66_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq66_0' : 1, 'q66_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq66_0') : 4, ('anc1','q66_0') : -4, ('anc2', 'q0_37') : -2, ('anc2', 'q65_0') : -2, ('anc2', 'outq66_0') : -2, ('anc2', 'q66_0') : 2, ('q0_37', 'q65_0') : 1, ('outq66_0', 'q66_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_37']==q0_37 and sample['q65_0']==q65_0 and sample['q66_0']==q66_0 and int(energy)==0:
        q0_37=sample['q0_37']
        q65_0=sample['q65_0']
        q66_0=sample['outq66_0']
        tgt_before = sample['q66_0']
        break

print('#' * 80)
print("CCNOT operation on q0_37 (control1), q65_0 (control2) and q66_0 (target):")
print("    in:  q0_37={0}, q65_0={1}, q66_0={2}".format(q0_37,q65_0,tgt_before))
print("    out: q0_37={0}, q65_0={1}, q66_0={2}".format(q0_37,q65_0,q66_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q65_0 target: q66_0 ##
################################################################################
if 'q65_0' not in globals():
    q65_0=0
if 'q66_0' not in globals():
    q66_0=0

bqm = dimod.BinaryQuadraticModel({'q65_0' : 1, 'q66_0' : 1, 'outq66_0' : 1, 'anc' : 4}, {('q65_0', 'q66_0') : 2, ('q65_0', 'outq66_0') : -2, ('q66_0', 'outq66_0') : -2, ('q65_0', 'anc') : -4, ('q66_0', 'anc') : -4, ('outq66_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q65_0']==q65_0 and sample['q66_0']==q66_0 and int(energy)==0:
        q65_0=sample['q65_0']
        q66_0=sample['outq66_0']
        tgt_before = sample['q66_0']
        break

print('#' * 80)
print("CNOT operation on q65_0 (control) and q66_0 (target):")
print("    in:  q65_0={0}, q66_0={1}".format(q65_0,tgt_before))
print("    out: q65_0={0}, q66_0={1}".format(q65_0,q66_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_38 control2: q64_0 target: q65_0 ##
################################################################################
if 'q1_38' not in globals():
    q1_38=0
if 'q64_0' not in globals():
    q64_0=0
if 'q65_0' not in globals():
    q65_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq65_0' : 1, 'q65_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq65_0') : 4, ('anc1','q65_0') : -4, ('anc2', 'q1_38') : -2, ('anc2', 'q64_0') : -2, ('anc2', 'outq65_0') : -2, ('anc2', 'q65_0') : 2, ('q1_38', 'q64_0') : 1, ('outq65_0', 'q65_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_38']==q1_38 and sample['q64_0']==q64_0 and sample['q65_0']==q65_0 and int(energy)==0:
        q1_38=sample['q1_38']
        q64_0=sample['q64_0']
        q65_0=sample['outq65_0']
        tgt_before = sample['q65_0']
        break

print('#' * 80)
print("CCNOT operation on q1_38 (control1), q64_0 (control2) and q65_0 (target):")
print("    in:  q1_38={0}, q64_0={1}, q65_0={2}".format(q1_38,q64_0,tgt_before))
print("    out: q1_38={0}, q64_0={1}, q65_0={2}".format(q1_38,q64_0,q65_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_38 control2: q64_0 target: q65_0 ##
################################################################################
if 'q0_38' not in globals():
    q0_38=0
if 'q64_0' not in globals():
    q64_0=0
if 'q65_0' not in globals():
    q65_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq65_0' : 1, 'q65_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq65_0') : 4, ('anc1','q65_0') : -4, ('anc2', 'q0_38') : -2, ('anc2', 'q64_0') : -2, ('anc2', 'outq65_0') : -2, ('anc2', 'q65_0') : 2, ('q0_38', 'q64_0') : 1, ('outq65_0', 'q65_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_38']==q0_38 and sample['q64_0']==q64_0 and sample['q65_0']==q65_0 and int(energy)==0:
        q0_38=sample['q0_38']
        q64_0=sample['q64_0']
        q65_0=sample['outq65_0']
        tgt_before = sample['q65_0']
        break

print('#' * 80)
print("CCNOT operation on q0_38 (control1), q64_0 (control2) and q65_0 (target):")
print("    in:  q0_38={0}, q64_0={1}, q65_0={2}".format(q0_38,q64_0,tgt_before))
print("    out: q0_38={0}, q64_0={1}, q65_0={2}".format(q0_38,q64_0,q65_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q64_0 target: q65_0 ##
################################################################################
if 'q64_0' not in globals():
    q64_0=0
if 'q65_0' not in globals():
    q65_0=0

bqm = dimod.BinaryQuadraticModel({'q64_0' : 1, 'q65_0' : 1, 'outq65_0' : 1, 'anc' : 4}, {('q64_0', 'q65_0') : 2, ('q64_0', 'outq65_0') : -2, ('q65_0', 'outq65_0') : -2, ('q64_0', 'anc') : -4, ('q65_0', 'anc') : -4, ('outq65_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q64_0']==q64_0 and sample['q65_0']==q65_0 and int(energy)==0:
        q64_0=sample['q64_0']
        q65_0=sample['outq65_0']
        tgt_before = sample['q65_0']
        break

print('#' * 80)
print("CNOT operation on q64_0 (control) and q65_0 (target):")
print("    in:  q64_0={0}, q65_0={1}".format(q64_0,tgt_before))
print("    out: q64_0={0}, q65_0={1}".format(q64_0,q65_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_39 control2: q63_0 target: q64_0 ##
################################################################################
if 'q1_39' not in globals():
    q1_39=0
if 'q63_0' not in globals():
    q63_0=0
if 'q64_0' not in globals():
    q64_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq64_0' : 1, 'q64_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq64_0') : 4, ('anc1','q64_0') : -4, ('anc2', 'q1_39') : -2, ('anc2', 'q63_0') : -2, ('anc2', 'outq64_0') : -2, ('anc2', 'q64_0') : 2, ('q1_39', 'q63_0') : 1, ('outq64_0', 'q64_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_39']==q1_39 and sample['q63_0']==q63_0 and sample['q64_0']==q64_0 and int(energy)==0:
        q1_39=sample['q1_39']
        q63_0=sample['q63_0']
        q64_0=sample['outq64_0']
        tgt_before = sample['q64_0']
        break

print('#' * 80)
print("CCNOT operation on q1_39 (control1), q63_0 (control2) and q64_0 (target):")
print("    in:  q1_39={0}, q63_0={1}, q64_0={2}".format(q1_39,q63_0,tgt_before))
print("    out: q1_39={0}, q63_0={1}, q64_0={2}".format(q1_39,q63_0,q64_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_39 control2: q63_0 target: q64_0 ##
################################################################################
if 'q0_39' not in globals():
    q0_39=0
if 'q63_0' not in globals():
    q63_0=0
if 'q64_0' not in globals():
    q64_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq64_0' : 1, 'q64_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq64_0') : 4, ('anc1','q64_0') : -4, ('anc2', 'q0_39') : -2, ('anc2', 'q63_0') : -2, ('anc2', 'outq64_0') : -2, ('anc2', 'q64_0') : 2, ('q0_39', 'q63_0') : 1, ('outq64_0', 'q64_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_39']==q0_39 and sample['q63_0']==q63_0 and sample['q64_0']==q64_0 and int(energy)==0:
        q0_39=sample['q0_39']
        q63_0=sample['q63_0']
        q64_0=sample['outq64_0']
        tgt_before = sample['q64_0']
        break

print('#' * 80)
print("CCNOT operation on q0_39 (control1), q63_0 (control2) and q64_0 (target):")
print("    in:  q0_39={0}, q63_0={1}, q64_0={2}".format(q0_39,q63_0,tgt_before))
print("    out: q0_39={0}, q63_0={1}, q64_0={2}".format(q0_39,q63_0,q64_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q63_0 target: q64_0 ##
################################################################################
if 'q63_0' not in globals():
    q63_0=0
if 'q64_0' not in globals():
    q64_0=0

bqm = dimod.BinaryQuadraticModel({'q63_0' : 1, 'q64_0' : 1, 'outq64_0' : 1, 'anc' : 4}, {('q63_0', 'q64_0') : 2, ('q63_0', 'outq64_0') : -2, ('q64_0', 'outq64_0') : -2, ('q63_0', 'anc') : -4, ('q64_0', 'anc') : -4, ('outq64_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q63_0']==q63_0 and sample['q64_0']==q64_0 and int(energy)==0:
        q63_0=sample['q63_0']
        q64_0=sample['outq64_0']
        tgt_before = sample['q64_0']
        break

print('#' * 80)
print("CNOT operation on q63_0 (control) and q64_0 (target):")
print("    in:  q63_0={0}, q64_0={1}".format(q63_0,tgt_before))
print("    out: q63_0={0}, q64_0={1}".format(q63_0,q64_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_40 control2: q62_0 target: q63_0 ##
################################################################################
if 'q1_40' not in globals():
    q1_40=0
if 'q62_0' not in globals():
    q62_0=0
if 'q63_0' not in globals():
    q63_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq63_0' : 1, 'q63_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq63_0') : 4, ('anc1','q63_0') : -4, ('anc2', 'q1_40') : -2, ('anc2', 'q62_0') : -2, ('anc2', 'outq63_0') : -2, ('anc2', 'q63_0') : 2, ('q1_40', 'q62_0') : 1, ('outq63_0', 'q63_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_40']==q1_40 and sample['q62_0']==q62_0 and sample['q63_0']==q63_0 and int(energy)==0:
        q1_40=sample['q1_40']
        q62_0=sample['q62_0']
        q63_0=sample['outq63_0']
        tgt_before = sample['q63_0']
        break

print('#' * 80)
print("CCNOT operation on q1_40 (control1), q62_0 (control2) and q63_0 (target):")
print("    in:  q1_40={0}, q62_0={1}, q63_0={2}".format(q1_40,q62_0,tgt_before))
print("    out: q1_40={0}, q62_0={1}, q63_0={2}".format(q1_40,q62_0,q63_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_40 control2: q62_0 target: q63_0 ##
################################################################################
if 'q0_40' not in globals():
    q0_40=0
if 'q62_0' not in globals():
    q62_0=0
if 'q63_0' not in globals():
    q63_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq63_0' : 1, 'q63_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq63_0') : 4, ('anc1','q63_0') : -4, ('anc2', 'q0_40') : -2, ('anc2', 'q62_0') : -2, ('anc2', 'outq63_0') : -2, ('anc2', 'q63_0') : 2, ('q0_40', 'q62_0') : 1, ('outq63_0', 'q63_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_40']==q0_40 and sample['q62_0']==q62_0 and sample['q63_0']==q63_0 and int(energy)==0:
        q0_40=sample['q0_40']
        q62_0=sample['q62_0']
        q63_0=sample['outq63_0']
        tgt_before = sample['q63_0']
        break

print('#' * 80)
print("CCNOT operation on q0_40 (control1), q62_0 (control2) and q63_0 (target):")
print("    in:  q0_40={0}, q62_0={1}, q63_0={2}".format(q0_40,q62_0,tgt_before))
print("    out: q0_40={0}, q62_0={1}, q63_0={2}".format(q0_40,q62_0,q63_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q62_0 target: q63_0 ##
################################################################################
if 'q62_0' not in globals():
    q62_0=0
if 'q63_0' not in globals():
    q63_0=0

bqm = dimod.BinaryQuadraticModel({'q62_0' : 1, 'q63_0' : 1, 'outq63_0' : 1, 'anc' : 4}, {('q62_0', 'q63_0') : 2, ('q62_0', 'outq63_0') : -2, ('q63_0', 'outq63_0') : -2, ('q62_0', 'anc') : -4, ('q63_0', 'anc') : -4, ('outq63_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q62_0']==q62_0 and sample['q63_0']==q63_0 and int(energy)==0:
        q62_0=sample['q62_0']
        q63_0=sample['outq63_0']
        tgt_before = sample['q63_0']
        break

print('#' * 80)
print("CNOT operation on q62_0 (control) and q63_0 (target):")
print("    in:  q62_0={0}, q63_0={1}".format(q62_0,tgt_before))
print("    out: q62_0={0}, q63_0={1}".format(q62_0,q63_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_41 control2: q61_0 target: q62_0 ##
################################################################################
if 'q1_41' not in globals():
    q1_41=0
if 'q61_0' not in globals():
    q61_0=0
if 'q62_0' not in globals():
    q62_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq62_0' : 1, 'q62_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq62_0') : 4, ('anc1','q62_0') : -4, ('anc2', 'q1_41') : -2, ('anc2', 'q61_0') : -2, ('anc2', 'outq62_0') : -2, ('anc2', 'q62_0') : 2, ('q1_41', 'q61_0') : 1, ('outq62_0', 'q62_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_41']==q1_41 and sample['q61_0']==q61_0 and sample['q62_0']==q62_0 and int(energy)==0:
        q1_41=sample['q1_41']
        q61_0=sample['q61_0']
        q62_0=sample['outq62_0']
        tgt_before = sample['q62_0']
        break

print('#' * 80)
print("CCNOT operation on q1_41 (control1), q61_0 (control2) and q62_0 (target):")
print("    in:  q1_41={0}, q61_0={1}, q62_0={2}".format(q1_41,q61_0,tgt_before))
print("    out: q1_41={0}, q61_0={1}, q62_0={2}".format(q1_41,q61_0,q62_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_41 control2: q61_0 target: q62_0 ##
################################################################################
if 'q0_41' not in globals():
    q0_41=0
if 'q61_0' not in globals():
    q61_0=0
if 'q62_0' not in globals():
    q62_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq62_0' : 1, 'q62_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq62_0') : 4, ('anc1','q62_0') : -4, ('anc2', 'q0_41') : -2, ('anc2', 'q61_0') : -2, ('anc2', 'outq62_0') : -2, ('anc2', 'q62_0') : 2, ('q0_41', 'q61_0') : 1, ('outq62_0', 'q62_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_41']==q0_41 and sample['q61_0']==q61_0 and sample['q62_0']==q62_0 and int(energy)==0:
        q0_41=sample['q0_41']
        q61_0=sample['q61_0']
        q62_0=sample['outq62_0']
        tgt_before = sample['q62_0']
        break

print('#' * 80)
print("CCNOT operation on q0_41 (control1), q61_0 (control2) and q62_0 (target):")
print("    in:  q0_41={0}, q61_0={1}, q62_0={2}".format(q0_41,q61_0,tgt_before))
print("    out: q0_41={0}, q61_0={1}, q62_0={2}".format(q0_41,q61_0,q62_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q61_0 target: q62_0 ##
################################################################################
if 'q61_0' not in globals():
    q61_0=0
if 'q62_0' not in globals():
    q62_0=0

bqm = dimod.BinaryQuadraticModel({'q61_0' : 1, 'q62_0' : 1, 'outq62_0' : 1, 'anc' : 4}, {('q61_0', 'q62_0') : 2, ('q61_0', 'outq62_0') : -2, ('q62_0', 'outq62_0') : -2, ('q61_0', 'anc') : -4, ('q62_0', 'anc') : -4, ('outq62_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q61_0']==q61_0 and sample['q62_0']==q62_0 and int(energy)==0:
        q61_0=sample['q61_0']
        q62_0=sample['outq62_0']
        tgt_before = sample['q62_0']
        break

print('#' * 80)
print("CNOT operation on q61_0 (control) and q62_0 (target):")
print("    in:  q61_0={0}, q62_0={1}".format(q61_0,tgt_before))
print("    out: q61_0={0}, q62_0={1}".format(q61_0,q62_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_42 control2: q60_0 target: q61_0 ##
################################################################################
if 'q1_42' not in globals():
    q1_42=0
if 'q60_0' not in globals():
    q60_0=0
if 'q61_0' not in globals():
    q61_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq61_0' : 1, 'q61_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq61_0') : 4, ('anc1','q61_0') : -4, ('anc2', 'q1_42') : -2, ('anc2', 'q60_0') : -2, ('anc2', 'outq61_0') : -2, ('anc2', 'q61_0') : 2, ('q1_42', 'q60_0') : 1, ('outq61_0', 'q61_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_42']==q1_42 and sample['q60_0']==q60_0 and sample['q61_0']==q61_0 and int(energy)==0:
        q1_42=sample['q1_42']
        q60_0=sample['q60_0']
        q61_0=sample['outq61_0']
        tgt_before = sample['q61_0']
        break

print('#' * 80)
print("CCNOT operation on q1_42 (control1), q60_0 (control2) and q61_0 (target):")
print("    in:  q1_42={0}, q60_0={1}, q61_0={2}".format(q1_42,q60_0,tgt_before))
print("    out: q1_42={0}, q60_0={1}, q61_0={2}".format(q1_42,q60_0,q61_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_42 control2: q60_0 target: q61_0 ##
################################################################################
if 'q0_42' not in globals():
    q0_42=0
if 'q60_0' not in globals():
    q60_0=0
if 'q61_0' not in globals():
    q61_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq61_0' : 1, 'q61_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq61_0') : 4, ('anc1','q61_0') : -4, ('anc2', 'q0_42') : -2, ('anc2', 'q60_0') : -2, ('anc2', 'outq61_0') : -2, ('anc2', 'q61_0') : 2, ('q0_42', 'q60_0') : 1, ('outq61_0', 'q61_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_42']==q0_42 and sample['q60_0']==q60_0 and sample['q61_0']==q61_0 and int(energy)==0:
        q0_42=sample['q0_42']
        q60_0=sample['q60_0']
        q61_0=sample['outq61_0']
        tgt_before = sample['q61_0']
        break

print('#' * 80)
print("CCNOT operation on q0_42 (control1), q60_0 (control2) and q61_0 (target):")
print("    in:  q0_42={0}, q60_0={1}, q61_0={2}".format(q0_42,q60_0,tgt_before))
print("    out: q0_42={0}, q60_0={1}, q61_0={2}".format(q0_42,q60_0,q61_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q60_0 target: q61_0 ##
################################################################################
if 'q60_0' not in globals():
    q60_0=0
if 'q61_0' not in globals():
    q61_0=0

bqm = dimod.BinaryQuadraticModel({'q60_0' : 1, 'q61_0' : 1, 'outq61_0' : 1, 'anc' : 4}, {('q60_0', 'q61_0') : 2, ('q60_0', 'outq61_0') : -2, ('q61_0', 'outq61_0') : -2, ('q60_0', 'anc') : -4, ('q61_0', 'anc') : -4, ('outq61_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q60_0']==q60_0 and sample['q61_0']==q61_0 and int(energy)==0:
        q60_0=sample['q60_0']
        q61_0=sample['outq61_0']
        tgt_before = sample['q61_0']
        break

print('#' * 80)
print("CNOT operation on q60_0 (control) and q61_0 (target):")
print("    in:  q60_0={0}, q61_0={1}".format(q60_0,tgt_before))
print("    out: q60_0={0}, q61_0={1}".format(q60_0,q61_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_43 control2: q59_0 target: q60_0 ##
################################################################################
if 'q1_43' not in globals():
    q1_43=0
if 'q59_0' not in globals():
    q59_0=0
if 'q60_0' not in globals():
    q60_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq60_0' : 1, 'q60_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq60_0') : 4, ('anc1','q60_0') : -4, ('anc2', 'q1_43') : -2, ('anc2', 'q59_0') : -2, ('anc2', 'outq60_0') : -2, ('anc2', 'q60_0') : 2, ('q1_43', 'q59_0') : 1, ('outq60_0', 'q60_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_43']==q1_43 and sample['q59_0']==q59_0 and sample['q60_0']==q60_0 and int(energy)==0:
        q1_43=sample['q1_43']
        q59_0=sample['q59_0']
        q60_0=sample['outq60_0']
        tgt_before = sample['q60_0']
        break

print('#' * 80)
print("CCNOT operation on q1_43 (control1), q59_0 (control2) and q60_0 (target):")
print("    in:  q1_43={0}, q59_0={1}, q60_0={2}".format(q1_43,q59_0,tgt_before))
print("    out: q1_43={0}, q59_0={1}, q60_0={2}".format(q1_43,q59_0,q60_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_43 control2: q59_0 target: q60_0 ##
################################################################################
if 'q0_43' not in globals():
    q0_43=0
if 'q59_0' not in globals():
    q59_0=0
if 'q60_0' not in globals():
    q60_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq60_0' : 1, 'q60_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq60_0') : 4, ('anc1','q60_0') : -4, ('anc2', 'q0_43') : -2, ('anc2', 'q59_0') : -2, ('anc2', 'outq60_0') : -2, ('anc2', 'q60_0') : 2, ('q0_43', 'q59_0') : 1, ('outq60_0', 'q60_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_43']==q0_43 and sample['q59_0']==q59_0 and sample['q60_0']==q60_0 and int(energy)==0:
        q0_43=sample['q0_43']
        q59_0=sample['q59_0']
        q60_0=sample['outq60_0']
        tgt_before = sample['q60_0']
        break

print('#' * 80)
print("CCNOT operation on q0_43 (control1), q59_0 (control2) and q60_0 (target):")
print("    in:  q0_43={0}, q59_0={1}, q60_0={2}".format(q0_43,q59_0,tgt_before))
print("    out: q0_43={0}, q59_0={1}, q60_0={2}".format(q0_43,q59_0,q60_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q59_0 target: q60_0 ##
################################################################################
if 'q59_0' not in globals():
    q59_0=0
if 'q60_0' not in globals():
    q60_0=0

bqm = dimod.BinaryQuadraticModel({'q59_0' : 1, 'q60_0' : 1, 'outq60_0' : 1, 'anc' : 4}, {('q59_0', 'q60_0') : 2, ('q59_0', 'outq60_0') : -2, ('q60_0', 'outq60_0') : -2, ('q59_0', 'anc') : -4, ('q60_0', 'anc') : -4, ('outq60_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q59_0']==q59_0 and sample['q60_0']==q60_0 and int(energy)==0:
        q59_0=sample['q59_0']
        q60_0=sample['outq60_0']
        tgt_before = sample['q60_0']
        break

print('#' * 80)
print("CNOT operation on q59_0 (control) and q60_0 (target):")
print("    in:  q59_0={0}, q60_0={1}".format(q59_0,tgt_before))
print("    out: q59_0={0}, q60_0={1}".format(q59_0,q60_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_44 control2: q58_0 target: q59_0 ##
################################################################################
if 'q1_44' not in globals():
    q1_44=0
if 'q58_0' not in globals():
    q58_0=0
if 'q59_0' not in globals():
    q59_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq59_0' : 1, 'q59_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq59_0') : 4, ('anc1','q59_0') : -4, ('anc2', 'q1_44') : -2, ('anc2', 'q58_0') : -2, ('anc2', 'outq59_0') : -2, ('anc2', 'q59_0') : 2, ('q1_44', 'q58_0') : 1, ('outq59_0', 'q59_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_44']==q1_44 and sample['q58_0']==q58_0 and sample['q59_0']==q59_0 and int(energy)==0:
        q1_44=sample['q1_44']
        q58_0=sample['q58_0']
        q59_0=sample['outq59_0']
        tgt_before = sample['q59_0']
        break

print('#' * 80)
print("CCNOT operation on q1_44 (control1), q58_0 (control2) and q59_0 (target):")
print("    in:  q1_44={0}, q58_0={1}, q59_0={2}".format(q1_44,q58_0,tgt_before))
print("    out: q1_44={0}, q58_0={1}, q59_0={2}".format(q1_44,q58_0,q59_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_44 control2: q58_0 target: q59_0 ##
################################################################################
if 'q0_44' not in globals():
    q0_44=0
if 'q58_0' not in globals():
    q58_0=0
if 'q59_0' not in globals():
    q59_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq59_0' : 1, 'q59_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq59_0') : 4, ('anc1','q59_0') : -4, ('anc2', 'q0_44') : -2, ('anc2', 'q58_0') : -2, ('anc2', 'outq59_0') : -2, ('anc2', 'q59_0') : 2, ('q0_44', 'q58_0') : 1, ('outq59_0', 'q59_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_44']==q0_44 and sample['q58_0']==q58_0 and sample['q59_0']==q59_0 and int(energy)==0:
        q0_44=sample['q0_44']
        q58_0=sample['q58_0']
        q59_0=sample['outq59_0']
        tgt_before = sample['q59_0']
        break

print('#' * 80)
print("CCNOT operation on q0_44 (control1), q58_0 (control2) and q59_0 (target):")
print("    in:  q0_44={0}, q58_0={1}, q59_0={2}".format(q0_44,q58_0,tgt_before))
print("    out: q0_44={0}, q58_0={1}, q59_0={2}".format(q0_44,q58_0,q59_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q58_0 target: q59_0 ##
################################################################################
if 'q58_0' not in globals():
    q58_0=0
if 'q59_0' not in globals():
    q59_0=0

bqm = dimod.BinaryQuadraticModel({'q58_0' : 1, 'q59_0' : 1, 'outq59_0' : 1, 'anc' : 4}, {('q58_0', 'q59_0') : 2, ('q58_0', 'outq59_0') : -2, ('q59_0', 'outq59_0') : -2, ('q58_0', 'anc') : -4, ('q59_0', 'anc') : -4, ('outq59_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q58_0']==q58_0 and sample['q59_0']==q59_0 and int(energy)==0:
        q58_0=sample['q58_0']
        q59_0=sample['outq59_0']
        tgt_before = sample['q59_0']
        break

print('#' * 80)
print("CNOT operation on q58_0 (control) and q59_0 (target):")
print("    in:  q58_0={0}, q59_0={1}".format(q58_0,tgt_before))
print("    out: q58_0={0}, q59_0={1}".format(q58_0,q59_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_45 control2: q57_0 target: q58_0 ##
################################################################################
if 'q1_45' not in globals():
    q1_45=0
if 'q57_0' not in globals():
    q57_0=0
if 'q58_0' not in globals():
    q58_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq58_0' : 1, 'q58_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq58_0') : 4, ('anc1','q58_0') : -4, ('anc2', 'q1_45') : -2, ('anc2', 'q57_0') : -2, ('anc2', 'outq58_0') : -2, ('anc2', 'q58_0') : 2, ('q1_45', 'q57_0') : 1, ('outq58_0', 'q58_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_45']==q1_45 and sample['q57_0']==q57_0 and sample['q58_0']==q58_0 and int(energy)==0:
        q1_45=sample['q1_45']
        q57_0=sample['q57_0']
        q58_0=sample['outq58_0']
        tgt_before = sample['q58_0']
        break

print('#' * 80)
print("CCNOT operation on q1_45 (control1), q57_0 (control2) and q58_0 (target):")
print("    in:  q1_45={0}, q57_0={1}, q58_0={2}".format(q1_45,q57_0,tgt_before))
print("    out: q1_45={0}, q57_0={1}, q58_0={2}".format(q1_45,q57_0,q58_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_45 control2: q57_0 target: q58_0 ##
################################################################################
if 'q0_45' not in globals():
    q0_45=0
if 'q57_0' not in globals():
    q57_0=0
if 'q58_0' not in globals():
    q58_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq58_0' : 1, 'q58_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq58_0') : 4, ('anc1','q58_0') : -4, ('anc2', 'q0_45') : -2, ('anc2', 'q57_0') : -2, ('anc2', 'outq58_0') : -2, ('anc2', 'q58_0') : 2, ('q0_45', 'q57_0') : 1, ('outq58_0', 'q58_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_45']==q0_45 and sample['q57_0']==q57_0 and sample['q58_0']==q58_0 and int(energy)==0:
        q0_45=sample['q0_45']
        q57_0=sample['q57_0']
        q58_0=sample['outq58_0']
        tgt_before = sample['q58_0']
        break

print('#' * 80)
print("CCNOT operation on q0_45 (control1), q57_0 (control2) and q58_0 (target):")
print("    in:  q0_45={0}, q57_0={1}, q58_0={2}".format(q0_45,q57_0,tgt_before))
print("    out: q0_45={0}, q57_0={1}, q58_0={2}".format(q0_45,q57_0,q58_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q57_0 target: q58_0 ##
################################################################################
if 'q57_0' not in globals():
    q57_0=0
if 'q58_0' not in globals():
    q58_0=0

bqm = dimod.BinaryQuadraticModel({'q57_0' : 1, 'q58_0' : 1, 'outq58_0' : 1, 'anc' : 4}, {('q57_0', 'q58_0') : 2, ('q57_0', 'outq58_0') : -2, ('q58_0', 'outq58_0') : -2, ('q57_0', 'anc') : -4, ('q58_0', 'anc') : -4, ('outq58_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q57_0']==q57_0 and sample['q58_0']==q58_0 and int(energy)==0:
        q57_0=sample['q57_0']
        q58_0=sample['outq58_0']
        tgt_before = sample['q58_0']
        break

print('#' * 80)
print("CNOT operation on q57_0 (control) and q58_0 (target):")
print("    in:  q57_0={0}, q58_0={1}".format(q57_0,tgt_before))
print("    out: q57_0={0}, q58_0={1}".format(q57_0,q58_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_46 control2: q56_0 target: q57_0 ##
################################################################################
if 'q1_46' not in globals():
    q1_46=0
if 'q56_0' not in globals():
    q56_0=0
if 'q57_0' not in globals():
    q57_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq57_0' : 1, 'q57_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq57_0') : 4, ('anc1','q57_0') : -4, ('anc2', 'q1_46') : -2, ('anc2', 'q56_0') : -2, ('anc2', 'outq57_0') : -2, ('anc2', 'q57_0') : 2, ('q1_46', 'q56_0') : 1, ('outq57_0', 'q57_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_46']==q1_46 and sample['q56_0']==q56_0 and sample['q57_0']==q57_0 and int(energy)==0:
        q1_46=sample['q1_46']
        q56_0=sample['q56_0']
        q57_0=sample['outq57_0']
        tgt_before = sample['q57_0']
        break

print('#' * 80)
print("CCNOT operation on q1_46 (control1), q56_0 (control2) and q57_0 (target):")
print("    in:  q1_46={0}, q56_0={1}, q57_0={2}".format(q1_46,q56_0,tgt_before))
print("    out: q1_46={0}, q56_0={1}, q57_0={2}".format(q1_46,q56_0,q57_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_46 control2: q56_0 target: q57_0 ##
################################################################################
if 'q0_46' not in globals():
    q0_46=0
if 'q56_0' not in globals():
    q56_0=0
if 'q57_0' not in globals():
    q57_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq57_0' : 1, 'q57_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq57_0') : 4, ('anc1','q57_0') : -4, ('anc2', 'q0_46') : -2, ('anc2', 'q56_0') : -2, ('anc2', 'outq57_0') : -2, ('anc2', 'q57_0') : 2, ('q0_46', 'q56_0') : 1, ('outq57_0', 'q57_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_46']==q0_46 and sample['q56_0']==q56_0 and sample['q57_0']==q57_0 and int(energy)==0:
        q0_46=sample['q0_46']
        q56_0=sample['q56_0']
        q57_0=sample['outq57_0']
        tgt_before = sample['q57_0']
        break

print('#' * 80)
print("CCNOT operation on q0_46 (control1), q56_0 (control2) and q57_0 (target):")
print("    in:  q0_46={0}, q56_0={1}, q57_0={2}".format(q0_46,q56_0,tgt_before))
print("    out: q0_46={0}, q56_0={1}, q57_0={2}".format(q0_46,q56_0,q57_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q56_0 target: q57_0 ##
################################################################################
if 'q56_0' not in globals():
    q56_0=0
if 'q57_0' not in globals():
    q57_0=0

bqm = dimod.BinaryQuadraticModel({'q56_0' : 1, 'q57_0' : 1, 'outq57_0' : 1, 'anc' : 4}, {('q56_0', 'q57_0') : 2, ('q56_0', 'outq57_0') : -2, ('q57_0', 'outq57_0') : -2, ('q56_0', 'anc') : -4, ('q57_0', 'anc') : -4, ('outq57_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q56_0']==q56_0 and sample['q57_0']==q57_0 and int(energy)==0:
        q56_0=sample['q56_0']
        q57_0=sample['outq57_0']
        tgt_before = sample['q57_0']
        break

print('#' * 80)
print("CNOT operation on q56_0 (control) and q57_0 (target):")
print("    in:  q56_0={0}, q57_0={1}".format(q56_0,tgt_before))
print("    out: q56_0={0}, q57_0={1}".format(q56_0,q57_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_47 control2: q55_0 target: q56_0 ##
################################################################################
if 'q1_47' not in globals():
    q1_47=0
if 'q55_0' not in globals():
    q55_0=0
if 'q56_0' not in globals():
    q56_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq56_0' : 1, 'q56_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq56_0') : 4, ('anc1','q56_0') : -4, ('anc2', 'q1_47') : -2, ('anc2', 'q55_0') : -2, ('anc2', 'outq56_0') : -2, ('anc2', 'q56_0') : 2, ('q1_47', 'q55_0') : 1, ('outq56_0', 'q56_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_47']==q1_47 and sample['q55_0']==q55_0 and sample['q56_0']==q56_0 and int(energy)==0:
        q1_47=sample['q1_47']
        q55_0=sample['q55_0']
        q56_0=sample['outq56_0']
        tgt_before = sample['q56_0']
        break

print('#' * 80)
print("CCNOT operation on q1_47 (control1), q55_0 (control2) and q56_0 (target):")
print("    in:  q1_47={0}, q55_0={1}, q56_0={2}".format(q1_47,q55_0,tgt_before))
print("    out: q1_47={0}, q55_0={1}, q56_0={2}".format(q1_47,q55_0,q56_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_47 control2: q55_0 target: q56_0 ##
################################################################################
if 'q0_47' not in globals():
    q0_47=0
if 'q55_0' not in globals():
    q55_0=0
if 'q56_0' not in globals():
    q56_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq56_0' : 1, 'q56_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq56_0') : 4, ('anc1','q56_0') : -4, ('anc2', 'q0_47') : -2, ('anc2', 'q55_0') : -2, ('anc2', 'outq56_0') : -2, ('anc2', 'q56_0') : 2, ('q0_47', 'q55_0') : 1, ('outq56_0', 'q56_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_47']==q0_47 and sample['q55_0']==q55_0 and sample['q56_0']==q56_0 and int(energy)==0:
        q0_47=sample['q0_47']
        q55_0=sample['q55_0']
        q56_0=sample['outq56_0']
        tgt_before = sample['q56_0']
        break

print('#' * 80)
print("CCNOT operation on q0_47 (control1), q55_0 (control2) and q56_0 (target):")
print("    in:  q0_47={0}, q55_0={1}, q56_0={2}".format(q0_47,q55_0,tgt_before))
print("    out: q0_47={0}, q55_0={1}, q56_0={2}".format(q0_47,q55_0,q56_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q55_0 target: q56_0 ##
################################################################################
if 'q55_0' not in globals():
    q55_0=0
if 'q56_0' not in globals():
    q56_0=0

bqm = dimod.BinaryQuadraticModel({'q55_0' : 1, 'q56_0' : 1, 'outq56_0' : 1, 'anc' : 4}, {('q55_0', 'q56_0') : 2, ('q55_0', 'outq56_0') : -2, ('q56_0', 'outq56_0') : -2, ('q55_0', 'anc') : -4, ('q56_0', 'anc') : -4, ('outq56_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q55_0']==q55_0 and sample['q56_0']==q56_0 and int(energy)==0:
        q55_0=sample['q55_0']
        q56_0=sample['outq56_0']
        tgt_before = sample['q56_0']
        break

print('#' * 80)
print("CNOT operation on q55_0 (control) and q56_0 (target):")
print("    in:  q55_0={0}, q56_0={1}".format(q55_0,tgt_before))
print("    out: q55_0={0}, q56_0={1}".format(q55_0,q56_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_48 control2: q54_0 target: q55_0 ##
################################################################################
if 'q1_48' not in globals():
    q1_48=0
if 'q54_0' not in globals():
    q54_0=0
if 'q55_0' not in globals():
    q55_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq55_0' : 1, 'q55_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq55_0') : 4, ('anc1','q55_0') : -4, ('anc2', 'q1_48') : -2, ('anc2', 'q54_0') : -2, ('anc2', 'outq55_0') : -2, ('anc2', 'q55_0') : 2, ('q1_48', 'q54_0') : 1, ('outq55_0', 'q55_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_48']==q1_48 and sample['q54_0']==q54_0 and sample['q55_0']==q55_0 and int(energy)==0:
        q1_48=sample['q1_48']
        q54_0=sample['q54_0']
        q55_0=sample['outq55_0']
        tgt_before = sample['q55_0']
        break

print('#' * 80)
print("CCNOT operation on q1_48 (control1), q54_0 (control2) and q55_0 (target):")
print("    in:  q1_48={0}, q54_0={1}, q55_0={2}".format(q1_48,q54_0,tgt_before))
print("    out: q1_48={0}, q54_0={1}, q55_0={2}".format(q1_48,q54_0,q55_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_48 control2: q54_0 target: q55_0 ##
################################################################################
if 'q0_48' not in globals():
    q0_48=0
if 'q54_0' not in globals():
    q54_0=0
if 'q55_0' not in globals():
    q55_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq55_0' : 1, 'q55_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq55_0') : 4, ('anc1','q55_0') : -4, ('anc2', 'q0_48') : -2, ('anc2', 'q54_0') : -2, ('anc2', 'outq55_0') : -2, ('anc2', 'q55_0') : 2, ('q0_48', 'q54_0') : 1, ('outq55_0', 'q55_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_48']==q0_48 and sample['q54_0']==q54_0 and sample['q55_0']==q55_0 and int(energy)==0:
        q0_48=sample['q0_48']
        q54_0=sample['q54_0']
        q55_0=sample['outq55_0']
        tgt_before = sample['q55_0']
        break

print('#' * 80)
print("CCNOT operation on q0_48 (control1), q54_0 (control2) and q55_0 (target):")
print("    in:  q0_48={0}, q54_0={1}, q55_0={2}".format(q0_48,q54_0,tgt_before))
print("    out: q0_48={0}, q54_0={1}, q55_0={2}".format(q0_48,q54_0,q55_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q54_0 target: q55_0 ##
################################################################################
if 'q54_0' not in globals():
    q54_0=0
if 'q55_0' not in globals():
    q55_0=0

bqm = dimod.BinaryQuadraticModel({'q54_0' : 1, 'q55_0' : 1, 'outq55_0' : 1, 'anc' : 4}, {('q54_0', 'q55_0') : 2, ('q54_0', 'outq55_0') : -2, ('q55_0', 'outq55_0') : -2, ('q54_0', 'anc') : -4, ('q55_0', 'anc') : -4, ('outq55_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q54_0']==q54_0 and sample['q55_0']==q55_0 and int(energy)==0:
        q54_0=sample['q54_0']
        q55_0=sample['outq55_0']
        tgt_before = sample['q55_0']
        break

print('#' * 80)
print("CNOT operation on q54_0 (control) and q55_0 (target):")
print("    in:  q54_0={0}, q55_0={1}".format(q54_0,tgt_before))
print("    out: q54_0={0}, q55_0={1}".format(q54_0,q55_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_49 control2: q53_0 target: q54_0 ##
################################################################################
if 'q1_49' not in globals():
    q1_49=0
if 'q53_0' not in globals():
    q53_0=0
if 'q54_0' not in globals():
    q54_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq54_0' : 1, 'q54_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq54_0') : 4, ('anc1','q54_0') : -4, ('anc2', 'q1_49') : -2, ('anc2', 'q53_0') : -2, ('anc2', 'outq54_0') : -2, ('anc2', 'q54_0') : 2, ('q1_49', 'q53_0') : 1, ('outq54_0', 'q54_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_49']==q1_49 and sample['q53_0']==q53_0 and sample['q54_0']==q54_0 and int(energy)==0:
        q1_49=sample['q1_49']
        q53_0=sample['q53_0']
        q54_0=sample['outq54_0']
        tgt_before = sample['q54_0']
        break

print('#' * 80)
print("CCNOT operation on q1_49 (control1), q53_0 (control2) and q54_0 (target):")
print("    in:  q1_49={0}, q53_0={1}, q54_0={2}".format(q1_49,q53_0,tgt_before))
print("    out: q1_49={0}, q53_0={1}, q54_0={2}".format(q1_49,q53_0,q54_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_49 control2: q53_0 target: q54_0 ##
################################################################################
if 'q0_49' not in globals():
    q0_49=0
if 'q53_0' not in globals():
    q53_0=0
if 'q54_0' not in globals():
    q54_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq54_0' : 1, 'q54_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq54_0') : 4, ('anc1','q54_0') : -4, ('anc2', 'q0_49') : -2, ('anc2', 'q53_0') : -2, ('anc2', 'outq54_0') : -2, ('anc2', 'q54_0') : 2, ('q0_49', 'q53_0') : 1, ('outq54_0', 'q54_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_49']==q0_49 and sample['q53_0']==q53_0 and sample['q54_0']==q54_0 and int(energy)==0:
        q0_49=sample['q0_49']
        q53_0=sample['q53_0']
        q54_0=sample['outq54_0']
        tgt_before = sample['q54_0']
        break

print('#' * 80)
print("CCNOT operation on q0_49 (control1), q53_0 (control2) and q54_0 (target):")
print("    in:  q0_49={0}, q53_0={1}, q54_0={2}".format(q0_49,q53_0,tgt_before))
print("    out: q0_49={0}, q53_0={1}, q54_0={2}".format(q0_49,q53_0,q54_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q53_0 target: q54_0 ##
################################################################################
if 'q53_0' not in globals():
    q53_0=0
if 'q54_0' not in globals():
    q54_0=0

bqm = dimod.BinaryQuadraticModel({'q53_0' : 1, 'q54_0' : 1, 'outq54_0' : 1, 'anc' : 4}, {('q53_0', 'q54_0') : 2, ('q53_0', 'outq54_0') : -2, ('q54_0', 'outq54_0') : -2, ('q53_0', 'anc') : -4, ('q54_0', 'anc') : -4, ('outq54_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q53_0']==q53_0 and sample['q54_0']==q54_0 and int(energy)==0:
        q53_0=sample['q53_0']
        q54_0=sample['outq54_0']
        tgt_before = sample['q54_0']
        break

print('#' * 80)
print("CNOT operation on q53_0 (control) and q54_0 (target):")
print("    in:  q53_0={0}, q54_0={1}".format(q53_0,tgt_before))
print("    out: q53_0={0}, q54_0={1}".format(q53_0,q54_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_50 control2: q52_0 target: q53_0 ##
################################################################################
if 'q1_50' not in globals():
    q1_50=0
if 'q52_0' not in globals():
    q52_0=0
if 'q53_0' not in globals():
    q53_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq53_0' : 1, 'q53_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq53_0') : 4, ('anc1','q53_0') : -4, ('anc2', 'q1_50') : -2, ('anc2', 'q52_0') : -2, ('anc2', 'outq53_0') : -2, ('anc2', 'q53_0') : 2, ('q1_50', 'q52_0') : 1, ('outq53_0', 'q53_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_50']==q1_50 and sample['q52_0']==q52_0 and sample['q53_0']==q53_0 and int(energy)==0:
        q1_50=sample['q1_50']
        q52_0=sample['q52_0']
        q53_0=sample['outq53_0']
        tgt_before = sample['q53_0']
        break

print('#' * 80)
print("CCNOT operation on q1_50 (control1), q52_0 (control2) and q53_0 (target):")
print("    in:  q1_50={0}, q52_0={1}, q53_0={2}".format(q1_50,q52_0,tgt_before))
print("    out: q1_50={0}, q52_0={1}, q53_0={2}".format(q1_50,q52_0,q53_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_50 control2: q52_0 target: q53_0 ##
################################################################################
if 'q0_50' not in globals():
    q0_50=0
if 'q52_0' not in globals():
    q52_0=0
if 'q53_0' not in globals():
    q53_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq53_0' : 1, 'q53_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq53_0') : 4, ('anc1','q53_0') : -4, ('anc2', 'q0_50') : -2, ('anc2', 'q52_0') : -2, ('anc2', 'outq53_0') : -2, ('anc2', 'q53_0') : 2, ('q0_50', 'q52_0') : 1, ('outq53_0', 'q53_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_50']==q0_50 and sample['q52_0']==q52_0 and sample['q53_0']==q53_0 and int(energy)==0:
        q0_50=sample['q0_50']
        q52_0=sample['q52_0']
        q53_0=sample['outq53_0']
        tgt_before = sample['q53_0']
        break

print('#' * 80)
print("CCNOT operation on q0_50 (control1), q52_0 (control2) and q53_0 (target):")
print("    in:  q0_50={0}, q52_0={1}, q53_0={2}".format(q0_50,q52_0,tgt_before))
print("    out: q0_50={0}, q52_0={1}, q53_0={2}".format(q0_50,q52_0,q53_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q52_0 target: q53_0 ##
################################################################################
if 'q52_0' not in globals():
    q52_0=0
if 'q53_0' not in globals():
    q53_0=0

bqm = dimod.BinaryQuadraticModel({'q52_0' : 1, 'q53_0' : 1, 'outq53_0' : 1, 'anc' : 4}, {('q52_0', 'q53_0') : 2, ('q52_0', 'outq53_0') : -2, ('q53_0', 'outq53_0') : -2, ('q52_0', 'anc') : -4, ('q53_0', 'anc') : -4, ('outq53_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q52_0']==q52_0 and sample['q53_0']==q53_0 and int(energy)==0:
        q52_0=sample['q52_0']
        q53_0=sample['outq53_0']
        tgt_before = sample['q53_0']
        break

print('#' * 80)
print("CNOT operation on q52_0 (control) and q53_0 (target):")
print("    in:  q52_0={0}, q53_0={1}".format(q52_0,tgt_before))
print("    out: q52_0={0}, q53_0={1}".format(q52_0,q53_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_51 control2: q51_0 target: q52_0 ##
################################################################################
if 'q1_51' not in globals():
    q1_51=0
if 'q51_0' not in globals():
    q51_0=0
if 'q52_0' not in globals():
    q52_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq52_0' : 1, 'q52_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq52_0') : 4, ('anc1','q52_0') : -4, ('anc2', 'q1_51') : -2, ('anc2', 'q51_0') : -2, ('anc2', 'outq52_0') : -2, ('anc2', 'q52_0') : 2, ('q1_51', 'q51_0') : 1, ('outq52_0', 'q52_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_51']==q1_51 and sample['q51_0']==q51_0 and sample['q52_0']==q52_0 and int(energy)==0:
        q1_51=sample['q1_51']
        q51_0=sample['q51_0']
        q52_0=sample['outq52_0']
        tgt_before = sample['q52_0']
        break

print('#' * 80)
print("CCNOT operation on q1_51 (control1), q51_0 (control2) and q52_0 (target):")
print("    in:  q1_51={0}, q51_0={1}, q52_0={2}".format(q1_51,q51_0,tgt_before))
print("    out: q1_51={0}, q51_0={1}, q52_0={2}".format(q1_51,q51_0,q52_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_51 control2: q51_0 target: q52_0 ##
################################################################################
if 'q0_51' not in globals():
    q0_51=0
if 'q51_0' not in globals():
    q51_0=0
if 'q52_0' not in globals():
    q52_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq52_0' : 1, 'q52_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq52_0') : 4, ('anc1','q52_0') : -4, ('anc2', 'q0_51') : -2, ('anc2', 'q51_0') : -2, ('anc2', 'outq52_0') : -2, ('anc2', 'q52_0') : 2, ('q0_51', 'q51_0') : 1, ('outq52_0', 'q52_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_51']==q0_51 and sample['q51_0']==q51_0 and sample['q52_0']==q52_0 and int(energy)==0:
        q0_51=sample['q0_51']
        q51_0=sample['q51_0']
        q52_0=sample['outq52_0']
        tgt_before = sample['q52_0']
        break

print('#' * 80)
print("CCNOT operation on q0_51 (control1), q51_0 (control2) and q52_0 (target):")
print("    in:  q0_51={0}, q51_0={1}, q52_0={2}".format(q0_51,q51_0,tgt_before))
print("    out: q0_51={0}, q51_0={1}, q52_0={2}".format(q0_51,q51_0,q52_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q51_0 target: q52_0 ##
################################################################################
if 'q51_0' not in globals():
    q51_0=0
if 'q52_0' not in globals():
    q52_0=0

bqm = dimod.BinaryQuadraticModel({'q51_0' : 1, 'q52_0' : 1, 'outq52_0' : 1, 'anc' : 4}, {('q51_0', 'q52_0') : 2, ('q51_0', 'outq52_0') : -2, ('q52_0', 'outq52_0') : -2, ('q51_0', 'anc') : -4, ('q52_0', 'anc') : -4, ('outq52_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q51_0']==q51_0 and sample['q52_0']==q52_0 and int(energy)==0:
        q51_0=sample['q51_0']
        q52_0=sample['outq52_0']
        tgt_before = sample['q52_0']
        break

print('#' * 80)
print("CNOT operation on q51_0 (control) and q52_0 (target):")
print("    in:  q51_0={0}, q52_0={1}".format(q51_0,tgt_before))
print("    out: q51_0={0}, q52_0={1}".format(q51_0,q52_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_52 control2: q50_0 target: q51_0 ##
################################################################################
if 'q1_52' not in globals():
    q1_52=0
if 'q50_0' not in globals():
    q50_0=0
if 'q51_0' not in globals():
    q51_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq51_0' : 1, 'q51_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq51_0') : 4, ('anc1','q51_0') : -4, ('anc2', 'q1_52') : -2, ('anc2', 'q50_0') : -2, ('anc2', 'outq51_0') : -2, ('anc2', 'q51_0') : 2, ('q1_52', 'q50_0') : 1, ('outq51_0', 'q51_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_52']==q1_52 and sample['q50_0']==q50_0 and sample['q51_0']==q51_0 and int(energy)==0:
        q1_52=sample['q1_52']
        q50_0=sample['q50_0']
        q51_0=sample['outq51_0']
        tgt_before = sample['q51_0']
        break

print('#' * 80)
print("CCNOT operation on q1_52 (control1), q50_0 (control2) and q51_0 (target):")
print("    in:  q1_52={0}, q50_0={1}, q51_0={2}".format(q1_52,q50_0,tgt_before))
print("    out: q1_52={0}, q50_0={1}, q51_0={2}".format(q1_52,q50_0,q51_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_52 control2: q50_0 target: q51_0 ##
################################################################################
if 'q0_52' not in globals():
    q0_52=0
if 'q50_0' not in globals():
    q50_0=0
if 'q51_0' not in globals():
    q51_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq51_0' : 1, 'q51_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq51_0') : 4, ('anc1','q51_0') : -4, ('anc2', 'q0_52') : -2, ('anc2', 'q50_0') : -2, ('anc2', 'outq51_0') : -2, ('anc2', 'q51_0') : 2, ('q0_52', 'q50_0') : 1, ('outq51_0', 'q51_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_52']==q0_52 and sample['q50_0']==q50_0 and sample['q51_0']==q51_0 and int(energy)==0:
        q0_52=sample['q0_52']
        q50_0=sample['q50_0']
        q51_0=sample['outq51_0']
        tgt_before = sample['q51_0']
        break

print('#' * 80)
print("CCNOT operation on q0_52 (control1), q50_0 (control2) and q51_0 (target):")
print("    in:  q0_52={0}, q50_0={1}, q51_0={2}".format(q0_52,q50_0,tgt_before))
print("    out: q0_52={0}, q50_0={1}, q51_0={2}".format(q0_52,q50_0,q51_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q50_0 target: q51_0 ##
################################################################################
if 'q50_0' not in globals():
    q50_0=0
if 'q51_0' not in globals():
    q51_0=0

bqm = dimod.BinaryQuadraticModel({'q50_0' : 1, 'q51_0' : 1, 'outq51_0' : 1, 'anc' : 4}, {('q50_0', 'q51_0') : 2, ('q50_0', 'outq51_0') : -2, ('q51_0', 'outq51_0') : -2, ('q50_0', 'anc') : -4, ('q51_0', 'anc') : -4, ('outq51_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q50_0']==q50_0 and sample['q51_0']==q51_0 and int(energy)==0:
        q50_0=sample['q50_0']
        q51_0=sample['outq51_0']
        tgt_before = sample['q51_0']
        break

print('#' * 80)
print("CNOT operation on q50_0 (control) and q51_0 (target):")
print("    in:  q50_0={0}, q51_0={1}".format(q50_0,tgt_before))
print("    out: q50_0={0}, q51_0={1}".format(q50_0,q51_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_53 control2: q49_0 target: q50_0 ##
################################################################################
if 'q1_53' not in globals():
    q1_53=0
if 'q49_0' not in globals():
    q49_0=0
if 'q50_0' not in globals():
    q50_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq50_0' : 1, 'q50_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq50_0') : 4, ('anc1','q50_0') : -4, ('anc2', 'q1_53') : -2, ('anc2', 'q49_0') : -2, ('anc2', 'outq50_0') : -2, ('anc2', 'q50_0') : 2, ('q1_53', 'q49_0') : 1, ('outq50_0', 'q50_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_53']==q1_53 and sample['q49_0']==q49_0 and sample['q50_0']==q50_0 and int(energy)==0:
        q1_53=sample['q1_53']
        q49_0=sample['q49_0']
        q50_0=sample['outq50_0']
        tgt_before = sample['q50_0']
        break

print('#' * 80)
print("CCNOT operation on q1_53 (control1), q49_0 (control2) and q50_0 (target):")
print("    in:  q1_53={0}, q49_0={1}, q50_0={2}".format(q1_53,q49_0,tgt_before))
print("    out: q1_53={0}, q49_0={1}, q50_0={2}".format(q1_53,q49_0,q50_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_53 control2: q49_0 target: q50_0 ##
################################################################################
if 'q0_53' not in globals():
    q0_53=0
if 'q49_0' not in globals():
    q49_0=0
if 'q50_0' not in globals():
    q50_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq50_0' : 1, 'q50_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq50_0') : 4, ('anc1','q50_0') : -4, ('anc2', 'q0_53') : -2, ('anc2', 'q49_0') : -2, ('anc2', 'outq50_0') : -2, ('anc2', 'q50_0') : 2, ('q0_53', 'q49_0') : 1, ('outq50_0', 'q50_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_53']==q0_53 and sample['q49_0']==q49_0 and sample['q50_0']==q50_0 and int(energy)==0:
        q0_53=sample['q0_53']
        q49_0=sample['q49_0']
        q50_0=sample['outq50_0']
        tgt_before = sample['q50_0']
        break

print('#' * 80)
print("CCNOT operation on q0_53 (control1), q49_0 (control2) and q50_0 (target):")
print("    in:  q0_53={0}, q49_0={1}, q50_0={2}".format(q0_53,q49_0,tgt_before))
print("    out: q0_53={0}, q49_0={1}, q50_0={2}".format(q0_53,q49_0,q50_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q49_0 target: q50_0 ##
################################################################################
if 'q49_0' not in globals():
    q49_0=0
if 'q50_0' not in globals():
    q50_0=0

bqm = dimod.BinaryQuadraticModel({'q49_0' : 1, 'q50_0' : 1, 'outq50_0' : 1, 'anc' : 4}, {('q49_0', 'q50_0') : 2, ('q49_0', 'outq50_0') : -2, ('q50_0', 'outq50_0') : -2, ('q49_0', 'anc') : -4, ('q50_0', 'anc') : -4, ('outq50_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q49_0']==q49_0 and sample['q50_0']==q50_0 and int(energy)==0:
        q49_0=sample['q49_0']
        q50_0=sample['outq50_0']
        tgt_before = sample['q50_0']
        break

print('#' * 80)
print("CNOT operation on q49_0 (control) and q50_0 (target):")
print("    in:  q49_0={0}, q50_0={1}".format(q49_0,tgt_before))
print("    out: q49_0={0}, q50_0={1}".format(q49_0,q50_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_54 control2: q48_0 target: q49_0 ##
################################################################################
if 'q1_54' not in globals():
    q1_54=0
if 'q48_0' not in globals():
    q48_0=0
if 'q49_0' not in globals():
    q49_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq49_0' : 1, 'q49_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq49_0') : 4, ('anc1','q49_0') : -4, ('anc2', 'q1_54') : -2, ('anc2', 'q48_0') : -2, ('anc2', 'outq49_0') : -2, ('anc2', 'q49_0') : 2, ('q1_54', 'q48_0') : 1, ('outq49_0', 'q49_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_54']==q1_54 and sample['q48_0']==q48_0 and sample['q49_0']==q49_0 and int(energy)==0:
        q1_54=sample['q1_54']
        q48_0=sample['q48_0']
        q49_0=sample['outq49_0']
        tgt_before = sample['q49_0']
        break

print('#' * 80)
print("CCNOT operation on q1_54 (control1), q48_0 (control2) and q49_0 (target):")
print("    in:  q1_54={0}, q48_0={1}, q49_0={2}".format(q1_54,q48_0,tgt_before))
print("    out: q1_54={0}, q48_0={1}, q49_0={2}".format(q1_54,q48_0,q49_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_54 control2: q48_0 target: q49_0 ##
################################################################################
if 'q0_54' not in globals():
    q0_54=0
if 'q48_0' not in globals():
    q48_0=0
if 'q49_0' not in globals():
    q49_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq49_0' : 1, 'q49_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq49_0') : 4, ('anc1','q49_0') : -4, ('anc2', 'q0_54') : -2, ('anc2', 'q48_0') : -2, ('anc2', 'outq49_0') : -2, ('anc2', 'q49_0') : 2, ('q0_54', 'q48_0') : 1, ('outq49_0', 'q49_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_54']==q0_54 and sample['q48_0']==q48_0 and sample['q49_0']==q49_0 and int(energy)==0:
        q0_54=sample['q0_54']
        q48_0=sample['q48_0']
        q49_0=sample['outq49_0']
        tgt_before = sample['q49_0']
        break

print('#' * 80)
print("CCNOT operation on q0_54 (control1), q48_0 (control2) and q49_0 (target):")
print("    in:  q0_54={0}, q48_0={1}, q49_0={2}".format(q0_54,q48_0,tgt_before))
print("    out: q0_54={0}, q48_0={1}, q49_0={2}".format(q0_54,q48_0,q49_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q48_0 target: q49_0 ##
################################################################################
if 'q48_0' not in globals():
    q48_0=0
if 'q49_0' not in globals():
    q49_0=0

bqm = dimod.BinaryQuadraticModel({'q48_0' : 1, 'q49_0' : 1, 'outq49_0' : 1, 'anc' : 4}, {('q48_0', 'q49_0') : 2, ('q48_0', 'outq49_0') : -2, ('q49_0', 'outq49_0') : -2, ('q48_0', 'anc') : -4, ('q49_0', 'anc') : -4, ('outq49_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q48_0']==q48_0 and sample['q49_0']==q49_0 and int(energy)==0:
        q48_0=sample['q48_0']
        q49_0=sample['outq49_0']
        tgt_before = sample['q49_0']
        break

print('#' * 80)
print("CNOT operation on q48_0 (control) and q49_0 (target):")
print("    in:  q48_0={0}, q49_0={1}".format(q48_0,tgt_before))
print("    out: q48_0={0}, q49_0={1}".format(q48_0,q49_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_55 control2: q47_0 target: q48_0 ##
################################################################################
if 'q1_55' not in globals():
    q1_55=0
if 'q47_0' not in globals():
    q47_0=0
if 'q48_0' not in globals():
    q48_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq48_0' : 1, 'q48_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq48_0') : 4, ('anc1','q48_0') : -4, ('anc2', 'q1_55') : -2, ('anc2', 'q47_0') : -2, ('anc2', 'outq48_0') : -2, ('anc2', 'q48_0') : 2, ('q1_55', 'q47_0') : 1, ('outq48_0', 'q48_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_55']==q1_55 and sample['q47_0']==q47_0 and sample['q48_0']==q48_0 and int(energy)==0:
        q1_55=sample['q1_55']
        q47_0=sample['q47_0']
        q48_0=sample['outq48_0']
        tgt_before = sample['q48_0']
        break

print('#' * 80)
print("CCNOT operation on q1_55 (control1), q47_0 (control2) and q48_0 (target):")
print("    in:  q1_55={0}, q47_0={1}, q48_0={2}".format(q1_55,q47_0,tgt_before))
print("    out: q1_55={0}, q47_0={1}, q48_0={2}".format(q1_55,q47_0,q48_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_55 control2: q47_0 target: q48_0 ##
################################################################################
if 'q0_55' not in globals():
    q0_55=0
if 'q47_0' not in globals():
    q47_0=0
if 'q48_0' not in globals():
    q48_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq48_0' : 1, 'q48_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq48_0') : 4, ('anc1','q48_0') : -4, ('anc2', 'q0_55') : -2, ('anc2', 'q47_0') : -2, ('anc2', 'outq48_0') : -2, ('anc2', 'q48_0') : 2, ('q0_55', 'q47_0') : 1, ('outq48_0', 'q48_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_55']==q0_55 and sample['q47_0']==q47_0 and sample['q48_0']==q48_0 and int(energy)==0:
        q0_55=sample['q0_55']
        q47_0=sample['q47_0']
        q48_0=sample['outq48_0']
        tgt_before = sample['q48_0']
        break

print('#' * 80)
print("CCNOT operation on q0_55 (control1), q47_0 (control2) and q48_0 (target):")
print("    in:  q0_55={0}, q47_0={1}, q48_0={2}".format(q0_55,q47_0,tgt_before))
print("    out: q0_55={0}, q47_0={1}, q48_0={2}".format(q0_55,q47_0,q48_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q47_0 target: q48_0 ##
################################################################################
if 'q47_0' not in globals():
    q47_0=0
if 'q48_0' not in globals():
    q48_0=0

bqm = dimod.BinaryQuadraticModel({'q47_0' : 1, 'q48_0' : 1, 'outq48_0' : 1, 'anc' : 4}, {('q47_0', 'q48_0') : 2, ('q47_0', 'outq48_0') : -2, ('q48_0', 'outq48_0') : -2, ('q47_0', 'anc') : -4, ('q48_0', 'anc') : -4, ('outq48_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q47_0']==q47_0 and sample['q48_0']==q48_0 and int(energy)==0:
        q47_0=sample['q47_0']
        q48_0=sample['outq48_0']
        tgt_before = sample['q48_0']
        break

print('#' * 80)
print("CNOT operation on q47_0 (control) and q48_0 (target):")
print("    in:  q47_0={0}, q48_0={1}".format(q47_0,tgt_before))
print("    out: q47_0={0}, q48_0={1}".format(q47_0,q48_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_56 control2: q46_0 target: q47_0 ##
################################################################################
if 'q1_56' not in globals():
    q1_56=0
if 'q46_0' not in globals():
    q46_0=0
if 'q47_0' not in globals():
    q47_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq47_0' : 1, 'q47_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq47_0') : 4, ('anc1','q47_0') : -4, ('anc2', 'q1_56') : -2, ('anc2', 'q46_0') : -2, ('anc2', 'outq47_0') : -2, ('anc2', 'q47_0') : 2, ('q1_56', 'q46_0') : 1, ('outq47_0', 'q47_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_56']==q1_56 and sample['q46_0']==q46_0 and sample['q47_0']==q47_0 and int(energy)==0:
        q1_56=sample['q1_56']
        q46_0=sample['q46_0']
        q47_0=sample['outq47_0']
        tgt_before = sample['q47_0']
        break

print('#' * 80)
print("CCNOT operation on q1_56 (control1), q46_0 (control2) and q47_0 (target):")
print("    in:  q1_56={0}, q46_0={1}, q47_0={2}".format(q1_56,q46_0,tgt_before))
print("    out: q1_56={0}, q46_0={1}, q47_0={2}".format(q1_56,q46_0,q47_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_56 control2: q46_0 target: q47_0 ##
################################################################################
if 'q0_56' not in globals():
    q0_56=0
if 'q46_0' not in globals():
    q46_0=0
if 'q47_0' not in globals():
    q47_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq47_0' : 1, 'q47_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq47_0') : 4, ('anc1','q47_0') : -4, ('anc2', 'q0_56') : -2, ('anc2', 'q46_0') : -2, ('anc2', 'outq47_0') : -2, ('anc2', 'q47_0') : 2, ('q0_56', 'q46_0') : 1, ('outq47_0', 'q47_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_56']==q0_56 and sample['q46_0']==q46_0 and sample['q47_0']==q47_0 and int(energy)==0:
        q0_56=sample['q0_56']
        q46_0=sample['q46_0']
        q47_0=sample['outq47_0']
        tgt_before = sample['q47_0']
        break

print('#' * 80)
print("CCNOT operation on q0_56 (control1), q46_0 (control2) and q47_0 (target):")
print("    in:  q0_56={0}, q46_0={1}, q47_0={2}".format(q0_56,q46_0,tgt_before))
print("    out: q0_56={0}, q46_0={1}, q47_0={2}".format(q0_56,q46_0,q47_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q46_0 target: q47_0 ##
################################################################################
if 'q46_0' not in globals():
    q46_0=0
if 'q47_0' not in globals():
    q47_0=0

bqm = dimod.BinaryQuadraticModel({'q46_0' : 1, 'q47_0' : 1, 'outq47_0' : 1, 'anc' : 4}, {('q46_0', 'q47_0') : 2, ('q46_0', 'outq47_0') : -2, ('q47_0', 'outq47_0') : -2, ('q46_0', 'anc') : -4, ('q47_0', 'anc') : -4, ('outq47_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q46_0']==q46_0 and sample['q47_0']==q47_0 and int(energy)==0:
        q46_0=sample['q46_0']
        q47_0=sample['outq47_0']
        tgt_before = sample['q47_0']
        break

print('#' * 80)
print("CNOT operation on q46_0 (control) and q47_0 (target):")
print("    in:  q46_0={0}, q47_0={1}".format(q46_0,tgt_before))
print("    out: q46_0={0}, q47_0={1}".format(q46_0,q47_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_57 control2: q45_0 target: q46_0 ##
################################################################################
if 'q1_57' not in globals():
    q1_57=0
if 'q45_0' not in globals():
    q45_0=0
if 'q46_0' not in globals():
    q46_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq46_0' : 1, 'q46_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq46_0') : 4, ('anc1','q46_0') : -4, ('anc2', 'q1_57') : -2, ('anc2', 'q45_0') : -2, ('anc2', 'outq46_0') : -2, ('anc2', 'q46_0') : 2, ('q1_57', 'q45_0') : 1, ('outq46_0', 'q46_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_57']==q1_57 and sample['q45_0']==q45_0 and sample['q46_0']==q46_0 and int(energy)==0:
        q1_57=sample['q1_57']
        q45_0=sample['q45_0']
        q46_0=sample['outq46_0']
        tgt_before = sample['q46_0']
        break

print('#' * 80)
print("CCNOT operation on q1_57 (control1), q45_0 (control2) and q46_0 (target):")
print("    in:  q1_57={0}, q45_0={1}, q46_0={2}".format(q1_57,q45_0,tgt_before))
print("    out: q1_57={0}, q45_0={1}, q46_0={2}".format(q1_57,q45_0,q46_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_57 control2: q45_0 target: q46_0 ##
################################################################################
if 'q0_57' not in globals():
    q0_57=0
if 'q45_0' not in globals():
    q45_0=0
if 'q46_0' not in globals():
    q46_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq46_0' : 1, 'q46_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq46_0') : 4, ('anc1','q46_0') : -4, ('anc2', 'q0_57') : -2, ('anc2', 'q45_0') : -2, ('anc2', 'outq46_0') : -2, ('anc2', 'q46_0') : 2, ('q0_57', 'q45_0') : 1, ('outq46_0', 'q46_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_57']==q0_57 and sample['q45_0']==q45_0 and sample['q46_0']==q46_0 and int(energy)==0:
        q0_57=sample['q0_57']
        q45_0=sample['q45_0']
        q46_0=sample['outq46_0']
        tgt_before = sample['q46_0']
        break

print('#' * 80)
print("CCNOT operation on q0_57 (control1), q45_0 (control2) and q46_0 (target):")
print("    in:  q0_57={0}, q45_0={1}, q46_0={2}".format(q0_57,q45_0,tgt_before))
print("    out: q0_57={0}, q45_0={1}, q46_0={2}".format(q0_57,q45_0,q46_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q45_0 target: q46_0 ##
################################################################################
if 'q45_0' not in globals():
    q45_0=0
if 'q46_0' not in globals():
    q46_0=0

bqm = dimod.BinaryQuadraticModel({'q45_0' : 1, 'q46_0' : 1, 'outq46_0' : 1, 'anc' : 4}, {('q45_0', 'q46_0') : 2, ('q45_0', 'outq46_0') : -2, ('q46_0', 'outq46_0') : -2, ('q45_0', 'anc') : -4, ('q46_0', 'anc') : -4, ('outq46_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q45_0']==q45_0 and sample['q46_0']==q46_0 and int(energy)==0:
        q45_0=sample['q45_0']
        q46_0=sample['outq46_0']
        tgt_before = sample['q46_0']
        break

print('#' * 80)
print("CNOT operation on q45_0 (control) and q46_0 (target):")
print("    in:  q45_0={0}, q46_0={1}".format(q45_0,tgt_before))
print("    out: q45_0={0}, q46_0={1}".format(q45_0,q46_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_58 control2: q44_0 target: q45_0 ##
################################################################################
if 'q1_58' not in globals():
    q1_58=0
if 'q44_0' not in globals():
    q44_0=0
if 'q45_0' not in globals():
    q45_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq45_0' : 1, 'q45_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq45_0') : 4, ('anc1','q45_0') : -4, ('anc2', 'q1_58') : -2, ('anc2', 'q44_0') : -2, ('anc2', 'outq45_0') : -2, ('anc2', 'q45_0') : 2, ('q1_58', 'q44_0') : 1, ('outq45_0', 'q45_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_58']==q1_58 and sample['q44_0']==q44_0 and sample['q45_0']==q45_0 and int(energy)==0:
        q1_58=sample['q1_58']
        q44_0=sample['q44_0']
        q45_0=sample['outq45_0']
        tgt_before = sample['q45_0']
        break

print('#' * 80)
print("CCNOT operation on q1_58 (control1), q44_0 (control2) and q45_0 (target):")
print("    in:  q1_58={0}, q44_0={1}, q45_0={2}".format(q1_58,q44_0,tgt_before))
print("    out: q1_58={0}, q44_0={1}, q45_0={2}".format(q1_58,q44_0,q45_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_58 control2: q44_0 target: q45_0 ##
################################################################################
if 'q0_58' not in globals():
    q0_58=0
if 'q44_0' not in globals():
    q44_0=0
if 'q45_0' not in globals():
    q45_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq45_0' : 1, 'q45_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq45_0') : 4, ('anc1','q45_0') : -4, ('anc2', 'q0_58') : -2, ('anc2', 'q44_0') : -2, ('anc2', 'outq45_0') : -2, ('anc2', 'q45_0') : 2, ('q0_58', 'q44_0') : 1, ('outq45_0', 'q45_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_58']==q0_58 and sample['q44_0']==q44_0 and sample['q45_0']==q45_0 and int(energy)==0:
        q0_58=sample['q0_58']
        q44_0=sample['q44_0']
        q45_0=sample['outq45_0']
        tgt_before = sample['q45_0']
        break

print('#' * 80)
print("CCNOT operation on q0_58 (control1), q44_0 (control2) and q45_0 (target):")
print("    in:  q0_58={0}, q44_0={1}, q45_0={2}".format(q0_58,q44_0,tgt_before))
print("    out: q0_58={0}, q44_0={1}, q45_0={2}".format(q0_58,q44_0,q45_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q44_0 target: q45_0 ##
################################################################################
if 'q44_0' not in globals():
    q44_0=0
if 'q45_0' not in globals():
    q45_0=0

bqm = dimod.BinaryQuadraticModel({'q44_0' : 1, 'q45_0' : 1, 'outq45_0' : 1, 'anc' : 4}, {('q44_0', 'q45_0') : 2, ('q44_0', 'outq45_0') : -2, ('q45_0', 'outq45_0') : -2, ('q44_0', 'anc') : -4, ('q45_0', 'anc') : -4, ('outq45_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q44_0']==q44_0 and sample['q45_0']==q45_0 and int(energy)==0:
        q44_0=sample['q44_0']
        q45_0=sample['outq45_0']
        tgt_before = sample['q45_0']
        break

print('#' * 80)
print("CNOT operation on q44_0 (control) and q45_0 (target):")
print("    in:  q44_0={0}, q45_0={1}".format(q44_0,tgt_before))
print("    out: q44_0={0}, q45_0={1}".format(q44_0,q45_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_59 control2: q43_0 target: q44_0 ##
################################################################################
if 'q1_59' not in globals():
    q1_59=0
if 'q43_0' not in globals():
    q43_0=0
if 'q44_0' not in globals():
    q44_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq44_0' : 1, 'q44_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq44_0') : 4, ('anc1','q44_0') : -4, ('anc2', 'q1_59') : -2, ('anc2', 'q43_0') : -2, ('anc2', 'outq44_0') : -2, ('anc2', 'q44_0') : 2, ('q1_59', 'q43_0') : 1, ('outq44_0', 'q44_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_59']==q1_59 and sample['q43_0']==q43_0 and sample['q44_0']==q44_0 and int(energy)==0:
        q1_59=sample['q1_59']
        q43_0=sample['q43_0']
        q44_0=sample['outq44_0']
        tgt_before = sample['q44_0']
        break

print('#' * 80)
print("CCNOT operation on q1_59 (control1), q43_0 (control2) and q44_0 (target):")
print("    in:  q1_59={0}, q43_0={1}, q44_0={2}".format(q1_59,q43_0,tgt_before))
print("    out: q1_59={0}, q43_0={1}, q44_0={2}".format(q1_59,q43_0,q44_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_59 control2: q43_0 target: q44_0 ##
################################################################################
if 'q0_59' not in globals():
    q0_59=0
if 'q43_0' not in globals():
    q43_0=0
if 'q44_0' not in globals():
    q44_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq44_0' : 1, 'q44_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq44_0') : 4, ('anc1','q44_0') : -4, ('anc2', 'q0_59') : -2, ('anc2', 'q43_0') : -2, ('anc2', 'outq44_0') : -2, ('anc2', 'q44_0') : 2, ('q0_59', 'q43_0') : 1, ('outq44_0', 'q44_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_59']==q0_59 and sample['q43_0']==q43_0 and sample['q44_0']==q44_0 and int(energy)==0:
        q0_59=sample['q0_59']
        q43_0=sample['q43_0']
        q44_0=sample['outq44_0']
        tgt_before = sample['q44_0']
        break

print('#' * 80)
print("CCNOT operation on q0_59 (control1), q43_0 (control2) and q44_0 (target):")
print("    in:  q0_59={0}, q43_0={1}, q44_0={2}".format(q0_59,q43_0,tgt_before))
print("    out: q0_59={0}, q43_0={1}, q44_0={2}".format(q0_59,q43_0,q44_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q43_0 target: q44_0 ##
################################################################################
if 'q43_0' not in globals():
    q43_0=0
if 'q44_0' not in globals():
    q44_0=0

bqm = dimod.BinaryQuadraticModel({'q43_0' : 1, 'q44_0' : 1, 'outq44_0' : 1, 'anc' : 4}, {('q43_0', 'q44_0') : 2, ('q43_0', 'outq44_0') : -2, ('q44_0', 'outq44_0') : -2, ('q43_0', 'anc') : -4, ('q44_0', 'anc') : -4, ('outq44_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q43_0']==q43_0 and sample['q44_0']==q44_0 and int(energy)==0:
        q43_0=sample['q43_0']
        q44_0=sample['outq44_0']
        tgt_before = sample['q44_0']
        break

print('#' * 80)
print("CNOT operation on q43_0 (control) and q44_0 (target):")
print("    in:  q43_0={0}, q44_0={1}".format(q43_0,tgt_before))
print("    out: q43_0={0}, q44_0={1}".format(q43_0,q44_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_60 control2: q42_0 target: q43_0 ##
################################################################################
if 'q1_60' not in globals():
    q1_60=0
if 'q42_0' not in globals():
    q42_0=0
if 'q43_0' not in globals():
    q43_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq43_0' : 1, 'q43_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq43_0') : 4, ('anc1','q43_0') : -4, ('anc2', 'q1_60') : -2, ('anc2', 'q42_0') : -2, ('anc2', 'outq43_0') : -2, ('anc2', 'q43_0') : 2, ('q1_60', 'q42_0') : 1, ('outq43_0', 'q43_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_60']==q1_60 and sample['q42_0']==q42_0 and sample['q43_0']==q43_0 and int(energy)==0:
        q1_60=sample['q1_60']
        q42_0=sample['q42_0']
        q43_0=sample['outq43_0']
        tgt_before = sample['q43_0']
        break

print('#' * 80)
print("CCNOT operation on q1_60 (control1), q42_0 (control2) and q43_0 (target):")
print("    in:  q1_60={0}, q42_0={1}, q43_0={2}".format(q1_60,q42_0,tgt_before))
print("    out: q1_60={0}, q42_0={1}, q43_0={2}".format(q1_60,q42_0,q43_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_60 control2: q42_0 target: q43_0 ##
################################################################################
if 'q0_60' not in globals():
    q0_60=0
if 'q42_0' not in globals():
    q42_0=0
if 'q43_0' not in globals():
    q43_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq43_0' : 1, 'q43_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq43_0') : 4, ('anc1','q43_0') : -4, ('anc2', 'q0_60') : -2, ('anc2', 'q42_0') : -2, ('anc2', 'outq43_0') : -2, ('anc2', 'q43_0') : 2, ('q0_60', 'q42_0') : 1, ('outq43_0', 'q43_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_60']==q0_60 and sample['q42_0']==q42_0 and sample['q43_0']==q43_0 and int(energy)==0:
        q0_60=sample['q0_60']
        q42_0=sample['q42_0']
        q43_0=sample['outq43_0']
        tgt_before = sample['q43_0']
        break

print('#' * 80)
print("CCNOT operation on q0_60 (control1), q42_0 (control2) and q43_0 (target):")
print("    in:  q0_60={0}, q42_0={1}, q43_0={2}".format(q0_60,q42_0,tgt_before))
print("    out: q0_60={0}, q42_0={1}, q43_0={2}".format(q0_60,q42_0,q43_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q42_0 target: q43_0 ##
################################################################################
if 'q42_0' not in globals():
    q42_0=0
if 'q43_0' not in globals():
    q43_0=0

bqm = dimod.BinaryQuadraticModel({'q42_0' : 1, 'q43_0' : 1, 'outq43_0' : 1, 'anc' : 4}, {('q42_0', 'q43_0') : 2, ('q42_0', 'outq43_0') : -2, ('q43_0', 'outq43_0') : -2, ('q42_0', 'anc') : -4, ('q43_0', 'anc') : -4, ('outq43_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q42_0']==q42_0 and sample['q43_0']==q43_0 and int(energy)==0:
        q42_0=sample['q42_0']
        q43_0=sample['outq43_0']
        tgt_before = sample['q43_0']
        break

print('#' * 80)
print("CNOT operation on q42_0 (control) and q43_0 (target):")
print("    in:  q42_0={0}, q43_0={1}".format(q42_0,tgt_before))
print("    out: q42_0={0}, q43_0={1}".format(q42_0,q43_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_61 control2: q41_0 target: q42_0 ##
################################################################################
if 'q1_61' not in globals():
    q1_61=0
if 'q41_0' not in globals():
    q41_0=0
if 'q42_0' not in globals():
    q42_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq42_0' : 1, 'q42_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq42_0') : 4, ('anc1','q42_0') : -4, ('anc2', 'q1_61') : -2, ('anc2', 'q41_0') : -2, ('anc2', 'outq42_0') : -2, ('anc2', 'q42_0') : 2, ('q1_61', 'q41_0') : 1, ('outq42_0', 'q42_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_61']==q1_61 and sample['q41_0']==q41_0 and sample['q42_0']==q42_0 and int(energy)==0:
        q1_61=sample['q1_61']
        q41_0=sample['q41_0']
        q42_0=sample['outq42_0']
        tgt_before = sample['q42_0']
        break

print('#' * 80)
print("CCNOT operation on q1_61 (control1), q41_0 (control2) and q42_0 (target):")
print("    in:  q1_61={0}, q41_0={1}, q42_0={2}".format(q1_61,q41_0,tgt_before))
print("    out: q1_61={0}, q41_0={1}, q42_0={2}".format(q1_61,q41_0,q42_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_61 control2: q41_0 target: q42_0 ##
################################################################################
if 'q0_61' not in globals():
    q0_61=0
if 'q41_0' not in globals():
    q41_0=0
if 'q42_0' not in globals():
    q42_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq42_0' : 1, 'q42_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq42_0') : 4, ('anc1','q42_0') : -4, ('anc2', 'q0_61') : -2, ('anc2', 'q41_0') : -2, ('anc2', 'outq42_0') : -2, ('anc2', 'q42_0') : 2, ('q0_61', 'q41_0') : 1, ('outq42_0', 'q42_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_61']==q0_61 and sample['q41_0']==q41_0 and sample['q42_0']==q42_0 and int(energy)==0:
        q0_61=sample['q0_61']
        q41_0=sample['q41_0']
        q42_0=sample['outq42_0']
        tgt_before = sample['q42_0']
        break

print('#' * 80)
print("CCNOT operation on q0_61 (control1), q41_0 (control2) and q42_0 (target):")
print("    in:  q0_61={0}, q41_0={1}, q42_0={2}".format(q0_61,q41_0,tgt_before))
print("    out: q0_61={0}, q41_0={1}, q42_0={2}".format(q0_61,q41_0,q42_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q41_0 target: q42_0 ##
################################################################################
if 'q41_0' not in globals():
    q41_0=0
if 'q42_0' not in globals():
    q42_0=0

bqm = dimod.BinaryQuadraticModel({'q41_0' : 1, 'q42_0' : 1, 'outq42_0' : 1, 'anc' : 4}, {('q41_0', 'q42_0') : 2, ('q41_0', 'outq42_0') : -2, ('q42_0', 'outq42_0') : -2, ('q41_0', 'anc') : -4, ('q42_0', 'anc') : -4, ('outq42_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q41_0']==q41_0 and sample['q42_0']==q42_0 and int(energy)==0:
        q41_0=sample['q41_0']
        q42_0=sample['outq42_0']
        tgt_before = sample['q42_0']
        break

print('#' * 80)
print("CNOT operation on q41_0 (control) and q42_0 (target):")
print("    in:  q41_0={0}, q42_0={1}".format(q41_0,tgt_before))
print("    out: q41_0={0}, q42_0={1}".format(q41_0,q42_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_62 control2: q40_0 target: q41_0 ##
################################################################################
if 'q1_62' not in globals():
    q1_62=0
if 'q40_0' not in globals():
    q40_0=0
if 'q41_0' not in globals():
    q41_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq41_0' : 1, 'q41_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq41_0') : 4, ('anc1','q41_0') : -4, ('anc2', 'q1_62') : -2, ('anc2', 'q40_0') : -2, ('anc2', 'outq41_0') : -2, ('anc2', 'q41_0') : 2, ('q1_62', 'q40_0') : 1, ('outq41_0', 'q41_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_62']==q1_62 and sample['q40_0']==q40_0 and sample['q41_0']==q41_0 and int(energy)==0:
        q1_62=sample['q1_62']
        q40_0=sample['q40_0']
        q41_0=sample['outq41_0']
        tgt_before = sample['q41_0']
        break

print('#' * 80)
print("CCNOT operation on q1_62 (control1), q40_0 (control2) and q41_0 (target):")
print("    in:  q1_62={0}, q40_0={1}, q41_0={2}".format(q1_62,q40_0,tgt_before))
print("    out: q1_62={0}, q40_0={1}, q41_0={2}".format(q1_62,q40_0,q41_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_62 control2: q40_0 target: q41_0 ##
################################################################################
if 'q0_62' not in globals():
    q0_62=0
if 'q40_0' not in globals():
    q40_0=0
if 'q41_0' not in globals():
    q41_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq41_0' : 1, 'q41_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq41_0') : 4, ('anc1','q41_0') : -4, ('anc2', 'q0_62') : -2, ('anc2', 'q40_0') : -2, ('anc2', 'outq41_0') : -2, ('anc2', 'q41_0') : 2, ('q0_62', 'q40_0') : 1, ('outq41_0', 'q41_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_62']==q0_62 and sample['q40_0']==q40_0 and sample['q41_0']==q41_0 and int(energy)==0:
        q0_62=sample['q0_62']
        q40_0=sample['q40_0']
        q41_0=sample['outq41_0']
        tgt_before = sample['q41_0']
        break

print('#' * 80)
print("CCNOT operation on q0_62 (control1), q40_0 (control2) and q41_0 (target):")
print("    in:  q0_62={0}, q40_0={1}, q41_0={2}".format(q0_62,q40_0,tgt_before))
print("    out: q0_62={0}, q40_0={1}, q41_0={2}".format(q0_62,q40_0,q41_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q40_0 target: q41_0 ##
################################################################################
if 'q40_0' not in globals():
    q40_0=0
if 'q41_0' not in globals():
    q41_0=0

bqm = dimod.BinaryQuadraticModel({'q40_0' : 1, 'q41_0' : 1, 'outq41_0' : 1, 'anc' : 4}, {('q40_0', 'q41_0') : 2, ('q40_0', 'outq41_0') : -2, ('q41_0', 'outq41_0') : -2, ('q40_0', 'anc') : -4, ('q41_0', 'anc') : -4, ('outq41_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q40_0']==q40_0 and sample['q41_0']==q41_0 and int(energy)==0:
        q40_0=sample['q40_0']
        q41_0=sample['outq41_0']
        tgt_before = sample['q41_0']
        break

print('#' * 80)
print("CNOT operation on q40_0 (control) and q41_0 (target):")
print("    in:  q40_0={0}, q41_0={1}".format(q40_0,tgt_before))
print("    out: q40_0={0}, q41_0={1}".format(q40_0,q41_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_63 control2: q39_0 target: q40_0 ##
################################################################################
if 'q1_63' not in globals():
    q1_63=0
if 'q39_0' not in globals():
    q39_0=0
if 'q40_0' not in globals():
    q40_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq40_0' : 1, 'q40_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq40_0') : 4, ('anc1','q40_0') : -4, ('anc2', 'q1_63') : -2, ('anc2', 'q39_0') : -2, ('anc2', 'outq40_0') : -2, ('anc2', 'q40_0') : 2, ('q1_63', 'q39_0') : 1, ('outq40_0', 'q40_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_63']==q1_63 and sample['q39_0']==q39_0 and sample['q40_0']==q40_0 and int(energy)==0:
        q1_63=sample['q1_63']
        q39_0=sample['q39_0']
        q40_0=sample['outq40_0']
        tgt_before = sample['q40_0']
        break

print('#' * 80)
print("CCNOT operation on q1_63 (control1), q39_0 (control2) and q40_0 (target):")
print("    in:  q1_63={0}, q39_0={1}, q40_0={2}".format(q1_63,q39_0,tgt_before))
print("    out: q1_63={0}, q39_0={1}, q40_0={2}".format(q1_63,q39_0,q40_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_63 control2: q39_0 target: q40_0 ##
################################################################################
if 'q0_63' not in globals():
    q0_63=0
if 'q39_0' not in globals():
    q39_0=0
if 'q40_0' not in globals():
    q40_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq40_0' : 1, 'q40_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq40_0') : 4, ('anc1','q40_0') : -4, ('anc2', 'q0_63') : -2, ('anc2', 'q39_0') : -2, ('anc2', 'outq40_0') : -2, ('anc2', 'q40_0') : 2, ('q0_63', 'q39_0') : 1, ('outq40_0', 'q40_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_63']==q0_63 and sample['q39_0']==q39_0 and sample['q40_0']==q40_0 and int(energy)==0:
        q0_63=sample['q0_63']
        q39_0=sample['q39_0']
        q40_0=sample['outq40_0']
        tgt_before = sample['q40_0']
        break

print('#' * 80)
print("CCNOT operation on q0_63 (control1), q39_0 (control2) and q40_0 (target):")
print("    in:  q0_63={0}, q39_0={1}, q40_0={2}".format(q0_63,q39_0,tgt_before))
print("    out: q0_63={0}, q39_0={1}, q40_0={2}".format(q0_63,q39_0,q40_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q39_0 target: q40_0 ##
################################################################################
if 'q39_0' not in globals():
    q39_0=0
if 'q40_0' not in globals():
    q40_0=0

bqm = dimod.BinaryQuadraticModel({'q39_0' : 1, 'q40_0' : 1, 'outq40_0' : 1, 'anc' : 4}, {('q39_0', 'q40_0') : 2, ('q39_0', 'outq40_0') : -2, ('q40_0', 'outq40_0') : -2, ('q39_0', 'anc') : -4, ('q40_0', 'anc') : -4, ('outq40_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q39_0']==q39_0 and sample['q40_0']==q40_0 and int(energy)==0:
        q39_0=sample['q39_0']
        q40_0=sample['outq40_0']
        tgt_before = sample['q40_0']
        break

print('#' * 80)
print("CNOT operation on q39_0 (control) and q40_0 (target):")
print("    in:  q39_0={0}, q40_0={1}".format(q39_0,tgt_before))
print("    out: q39_0={0}, q40_0={1}".format(q39_0,q40_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_64 control2: q38_0 target: q39_0 ##
################################################################################
if 'q1_64' not in globals():
    q1_64=0
if 'q38_0' not in globals():
    q38_0=0
if 'q39_0' not in globals():
    q39_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq39_0' : 1, 'q39_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq39_0') : 4, ('anc1','q39_0') : -4, ('anc2', 'q1_64') : -2, ('anc2', 'q38_0') : -2, ('anc2', 'outq39_0') : -2, ('anc2', 'q39_0') : 2, ('q1_64', 'q38_0') : 1, ('outq39_0', 'q39_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_64']==q1_64 and sample['q38_0']==q38_0 and sample['q39_0']==q39_0 and int(energy)==0:
        q1_64=sample['q1_64']
        q38_0=sample['q38_0']
        q39_0=sample['outq39_0']
        tgt_before = sample['q39_0']
        break

print('#' * 80)
print("CCNOT operation on q1_64 (control1), q38_0 (control2) and q39_0 (target):")
print("    in:  q1_64={0}, q38_0={1}, q39_0={2}".format(q1_64,q38_0,tgt_before))
print("    out: q1_64={0}, q38_0={1}, q39_0={2}".format(q1_64,q38_0,q39_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_64 control2: q38_0 target: q39_0 ##
################################################################################
if 'q0_64' not in globals():
    q0_64=0
if 'q38_0' not in globals():
    q38_0=0
if 'q39_0' not in globals():
    q39_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq39_0' : 1, 'q39_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq39_0') : 4, ('anc1','q39_0') : -4, ('anc2', 'q0_64') : -2, ('anc2', 'q38_0') : -2, ('anc2', 'outq39_0') : -2, ('anc2', 'q39_0') : 2, ('q0_64', 'q38_0') : 1, ('outq39_0', 'q39_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_64']==q0_64 and sample['q38_0']==q38_0 and sample['q39_0']==q39_0 and int(energy)==0:
        q0_64=sample['q0_64']
        q38_0=sample['q38_0']
        q39_0=sample['outq39_0']
        tgt_before = sample['q39_0']
        break

print('#' * 80)
print("CCNOT operation on q0_64 (control1), q38_0 (control2) and q39_0 (target):")
print("    in:  q0_64={0}, q38_0={1}, q39_0={2}".format(q0_64,q38_0,tgt_before))
print("    out: q0_64={0}, q38_0={1}, q39_0={2}".format(q0_64,q38_0,q39_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q38_0 target: q39_0 ##
################################################################################
if 'q38_0' not in globals():
    q38_0=0
if 'q39_0' not in globals():
    q39_0=0

bqm = dimod.BinaryQuadraticModel({'q38_0' : 1, 'q39_0' : 1, 'outq39_0' : 1, 'anc' : 4}, {('q38_0', 'q39_0') : 2, ('q38_0', 'outq39_0') : -2, ('q39_0', 'outq39_0') : -2, ('q38_0', 'anc') : -4, ('q39_0', 'anc') : -4, ('outq39_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q38_0']==q38_0 and sample['q39_0']==q39_0 and int(energy)==0:
        q38_0=sample['q38_0']
        q39_0=sample['outq39_0']
        tgt_before = sample['q39_0']
        break

print('#' * 80)
print("CNOT operation on q38_0 (control) and q39_0 (target):")
print("    in:  q38_0={0}, q39_0={1}".format(q38_0,tgt_before))
print("    out: q38_0={0}, q39_0={1}".format(q38_0,q39_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_65 control2: q37_0 target: q38_0 ##
################################################################################
if 'q1_65' not in globals():
    q1_65=0
if 'q37_0' not in globals():
    q37_0=0
if 'q38_0' not in globals():
    q38_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq38_0' : 1, 'q38_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq38_0') : 4, ('anc1','q38_0') : -4, ('anc2', 'q1_65') : -2, ('anc2', 'q37_0') : -2, ('anc2', 'outq38_0') : -2, ('anc2', 'q38_0') : 2, ('q1_65', 'q37_0') : 1, ('outq38_0', 'q38_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_65']==q1_65 and sample['q37_0']==q37_0 and sample['q38_0']==q38_0 and int(energy)==0:
        q1_65=sample['q1_65']
        q37_0=sample['q37_0']
        q38_0=sample['outq38_0']
        tgt_before = sample['q38_0']
        break

print('#' * 80)
print("CCNOT operation on q1_65 (control1), q37_0 (control2) and q38_0 (target):")
print("    in:  q1_65={0}, q37_0={1}, q38_0={2}".format(q1_65,q37_0,tgt_before))
print("    out: q1_65={0}, q37_0={1}, q38_0={2}".format(q1_65,q37_0,q38_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_65 control2: q37_0 target: q38_0 ##
################################################################################
if 'q0_65' not in globals():
    q0_65=0
if 'q37_0' not in globals():
    q37_0=0
if 'q38_0' not in globals():
    q38_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq38_0' : 1, 'q38_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq38_0') : 4, ('anc1','q38_0') : -4, ('anc2', 'q0_65') : -2, ('anc2', 'q37_0') : -2, ('anc2', 'outq38_0') : -2, ('anc2', 'q38_0') : 2, ('q0_65', 'q37_0') : 1, ('outq38_0', 'q38_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_65']==q0_65 and sample['q37_0']==q37_0 and sample['q38_0']==q38_0 and int(energy)==0:
        q0_65=sample['q0_65']
        q37_0=sample['q37_0']
        q38_0=sample['outq38_0']
        tgt_before = sample['q38_0']
        break

print('#' * 80)
print("CCNOT operation on q0_65 (control1), q37_0 (control2) and q38_0 (target):")
print("    in:  q0_65={0}, q37_0={1}, q38_0={2}".format(q0_65,q37_0,tgt_before))
print("    out: q0_65={0}, q37_0={1}, q38_0={2}".format(q0_65,q37_0,q38_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q37_0 target: q38_0 ##
################################################################################
if 'q37_0' not in globals():
    q37_0=0
if 'q38_0' not in globals():
    q38_0=0

bqm = dimod.BinaryQuadraticModel({'q37_0' : 1, 'q38_0' : 1, 'outq38_0' : 1, 'anc' : 4}, {('q37_0', 'q38_0') : 2, ('q37_0', 'outq38_0') : -2, ('q38_0', 'outq38_0') : -2, ('q37_0', 'anc') : -4, ('q38_0', 'anc') : -4, ('outq38_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q37_0']==q37_0 and sample['q38_0']==q38_0 and int(energy)==0:
        q37_0=sample['q37_0']
        q38_0=sample['outq38_0']
        tgt_before = sample['q38_0']
        break

print('#' * 80)
print("CNOT operation on q37_0 (control) and q38_0 (target):")
print("    in:  q37_0={0}, q38_0={1}".format(q37_0,tgt_before))
print("    out: q37_0={0}, q38_0={1}".format(q37_0,q38_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_66 control2: q36_0 target: q37_0 ##
################################################################################
if 'q1_66' not in globals():
    q1_66=0
if 'q36_0' not in globals():
    q36_0=0
if 'q37_0' not in globals():
    q37_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq37_0' : 1, 'q37_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq37_0') : 4, ('anc1','q37_0') : -4, ('anc2', 'q1_66') : -2, ('anc2', 'q36_0') : -2, ('anc2', 'outq37_0') : -2, ('anc2', 'q37_0') : 2, ('q1_66', 'q36_0') : 1, ('outq37_0', 'q37_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_66']==q1_66 and sample['q36_0']==q36_0 and sample['q37_0']==q37_0 and int(energy)==0:
        q1_66=sample['q1_66']
        q36_0=sample['q36_0']
        q37_0=sample['outq37_0']
        tgt_before = sample['q37_0']
        break

print('#' * 80)
print("CCNOT operation on q1_66 (control1), q36_0 (control2) and q37_0 (target):")
print("    in:  q1_66={0}, q36_0={1}, q37_0={2}".format(q1_66,q36_0,tgt_before))
print("    out: q1_66={0}, q36_0={1}, q37_0={2}".format(q1_66,q36_0,q37_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_66 control2: q36_0 target: q37_0 ##
################################################################################
if 'q0_66' not in globals():
    q0_66=0
if 'q36_0' not in globals():
    q36_0=0
if 'q37_0' not in globals():
    q37_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq37_0' : 1, 'q37_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq37_0') : 4, ('anc1','q37_0') : -4, ('anc2', 'q0_66') : -2, ('anc2', 'q36_0') : -2, ('anc2', 'outq37_0') : -2, ('anc2', 'q37_0') : 2, ('q0_66', 'q36_0') : 1, ('outq37_0', 'q37_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_66']==q0_66 and sample['q36_0']==q36_0 and sample['q37_0']==q37_0 and int(energy)==0:
        q0_66=sample['q0_66']
        q36_0=sample['q36_0']
        q37_0=sample['outq37_0']
        tgt_before = sample['q37_0']
        break

print('#' * 80)
print("CCNOT operation on q0_66 (control1), q36_0 (control2) and q37_0 (target):")
print("    in:  q0_66={0}, q36_0={1}, q37_0={2}".format(q0_66,q36_0,tgt_before))
print("    out: q0_66={0}, q36_0={1}, q37_0={2}".format(q0_66,q36_0,q37_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q36_0 target: q37_0 ##
################################################################################
if 'q36_0' not in globals():
    q36_0=0
if 'q37_0' not in globals():
    q37_0=0

bqm = dimod.BinaryQuadraticModel({'q36_0' : 1, 'q37_0' : 1, 'outq37_0' : 1, 'anc' : 4}, {('q36_0', 'q37_0') : 2, ('q36_0', 'outq37_0') : -2, ('q37_0', 'outq37_0') : -2, ('q36_0', 'anc') : -4, ('q37_0', 'anc') : -4, ('outq37_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q36_0']==q36_0 and sample['q37_0']==q37_0 and int(energy)==0:
        q36_0=sample['q36_0']
        q37_0=sample['outq37_0']
        tgt_before = sample['q37_0']
        break

print('#' * 80)
print("CNOT operation on q36_0 (control) and q37_0 (target):")
print("    in:  q36_0={0}, q37_0={1}".format(q36_0,tgt_before))
print("    out: q36_0={0}, q37_0={1}".format(q36_0,q37_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_67 control2: q35_0 target: q36_0 ##
################################################################################
if 'q1_67' not in globals():
    q1_67=0
if 'q35_0' not in globals():
    q35_0=0
if 'q36_0' not in globals():
    q36_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq36_0' : 1, 'q36_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq36_0') : 4, ('anc1','q36_0') : -4, ('anc2', 'q1_67') : -2, ('anc2', 'q35_0') : -2, ('anc2', 'outq36_0') : -2, ('anc2', 'q36_0') : 2, ('q1_67', 'q35_0') : 1, ('outq36_0', 'q36_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_67']==q1_67 and sample['q35_0']==q35_0 and sample['q36_0']==q36_0 and int(energy)==0:
        q1_67=sample['q1_67']
        q35_0=sample['q35_0']
        q36_0=sample['outq36_0']
        tgt_before = sample['q36_0']
        break

print('#' * 80)
print("CCNOT operation on q1_67 (control1), q35_0 (control2) and q36_0 (target):")
print("    in:  q1_67={0}, q35_0={1}, q36_0={2}".format(q1_67,q35_0,tgt_before))
print("    out: q1_67={0}, q35_0={1}, q36_0={2}".format(q1_67,q35_0,q36_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_67 control2: q35_0 target: q36_0 ##
################################################################################
if 'q0_67' not in globals():
    q0_67=0
if 'q35_0' not in globals():
    q35_0=0
if 'q36_0' not in globals():
    q36_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq36_0' : 1, 'q36_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq36_0') : 4, ('anc1','q36_0') : -4, ('anc2', 'q0_67') : -2, ('anc2', 'q35_0') : -2, ('anc2', 'outq36_0') : -2, ('anc2', 'q36_0') : 2, ('q0_67', 'q35_0') : 1, ('outq36_0', 'q36_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_67']==q0_67 and sample['q35_0']==q35_0 and sample['q36_0']==q36_0 and int(energy)==0:
        q0_67=sample['q0_67']
        q35_0=sample['q35_0']
        q36_0=sample['outq36_0']
        tgt_before = sample['q36_0']
        break

print('#' * 80)
print("CCNOT operation on q0_67 (control1), q35_0 (control2) and q36_0 (target):")
print("    in:  q0_67={0}, q35_0={1}, q36_0={2}".format(q0_67,q35_0,tgt_before))
print("    out: q0_67={0}, q35_0={1}, q36_0={2}".format(q0_67,q35_0,q36_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q35_0 target: q36_0 ##
################################################################################
if 'q35_0' not in globals():
    q35_0=0
if 'q36_0' not in globals():
    q36_0=0

bqm = dimod.BinaryQuadraticModel({'q35_0' : 1, 'q36_0' : 1, 'outq36_0' : 1, 'anc' : 4}, {('q35_0', 'q36_0') : 2, ('q35_0', 'outq36_0') : -2, ('q36_0', 'outq36_0') : -2, ('q35_0', 'anc') : -4, ('q36_0', 'anc') : -4, ('outq36_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q35_0']==q35_0 and sample['q36_0']==q36_0 and int(energy)==0:
        q35_0=sample['q35_0']
        q36_0=sample['outq36_0']
        tgt_before = sample['q36_0']
        break

print('#' * 80)
print("CNOT operation on q35_0 (control) and q36_0 (target):")
print("    in:  q35_0={0}, q36_0={1}".format(q35_0,tgt_before))
print("    out: q35_0={0}, q36_0={1}".format(q35_0,q36_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_68 control2: q34_0 target: q35_0 ##
################################################################################
if 'q1_68' not in globals():
    q1_68=0
if 'q34_0' not in globals():
    q34_0=0
if 'q35_0' not in globals():
    q35_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq35_0' : 1, 'q35_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq35_0') : 4, ('anc1','q35_0') : -4, ('anc2', 'q1_68') : -2, ('anc2', 'q34_0') : -2, ('anc2', 'outq35_0') : -2, ('anc2', 'q35_0') : 2, ('q1_68', 'q34_0') : 1, ('outq35_0', 'q35_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_68']==q1_68 and sample['q34_0']==q34_0 and sample['q35_0']==q35_0 and int(energy)==0:
        q1_68=sample['q1_68']
        q34_0=sample['q34_0']
        q35_0=sample['outq35_0']
        tgt_before = sample['q35_0']
        break

print('#' * 80)
print("CCNOT operation on q1_68 (control1), q34_0 (control2) and q35_0 (target):")
print("    in:  q1_68={0}, q34_0={1}, q35_0={2}".format(q1_68,q34_0,tgt_before))
print("    out: q1_68={0}, q34_0={1}, q35_0={2}".format(q1_68,q34_0,q35_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_68 control2: q34_0 target: q35_0 ##
################################################################################
if 'q0_68' not in globals():
    q0_68=0
if 'q34_0' not in globals():
    q34_0=0
if 'q35_0' not in globals():
    q35_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq35_0' : 1, 'q35_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq35_0') : 4, ('anc1','q35_0') : -4, ('anc2', 'q0_68') : -2, ('anc2', 'q34_0') : -2, ('anc2', 'outq35_0') : -2, ('anc2', 'q35_0') : 2, ('q0_68', 'q34_0') : 1, ('outq35_0', 'q35_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_68']==q0_68 and sample['q34_0']==q34_0 and sample['q35_0']==q35_0 and int(energy)==0:
        q0_68=sample['q0_68']
        q34_0=sample['q34_0']
        q35_0=sample['outq35_0']
        tgt_before = sample['q35_0']
        break

print('#' * 80)
print("CCNOT operation on q0_68 (control1), q34_0 (control2) and q35_0 (target):")
print("    in:  q0_68={0}, q34_0={1}, q35_0={2}".format(q0_68,q34_0,tgt_before))
print("    out: q0_68={0}, q34_0={1}, q35_0={2}".format(q0_68,q34_0,q35_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q34_0 target: q35_0 ##
################################################################################
if 'q34_0' not in globals():
    q34_0=0
if 'q35_0' not in globals():
    q35_0=0

bqm = dimod.BinaryQuadraticModel({'q34_0' : 1, 'q35_0' : 1, 'outq35_0' : 1, 'anc' : 4}, {('q34_0', 'q35_0') : 2, ('q34_0', 'outq35_0') : -2, ('q35_0', 'outq35_0') : -2, ('q34_0', 'anc') : -4, ('q35_0', 'anc') : -4, ('outq35_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q34_0']==q34_0 and sample['q35_0']==q35_0 and int(energy)==0:
        q34_0=sample['q34_0']
        q35_0=sample['outq35_0']
        tgt_before = sample['q35_0']
        break

print('#' * 80)
print("CNOT operation on q34_0 (control) and q35_0 (target):")
print("    in:  q34_0={0}, q35_0={1}".format(q34_0,tgt_before))
print("    out: q34_0={0}, q35_0={1}".format(q34_0,q35_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_69 control2: q33_0 target: q34_0 ##
################################################################################
if 'q1_69' not in globals():
    q1_69=0
if 'q33_0' not in globals():
    q33_0=0
if 'q34_0' not in globals():
    q34_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq34_0' : 1, 'q34_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq34_0') : 4, ('anc1','q34_0') : -4, ('anc2', 'q1_69') : -2, ('anc2', 'q33_0') : -2, ('anc2', 'outq34_0') : -2, ('anc2', 'q34_0') : 2, ('q1_69', 'q33_0') : 1, ('outq34_0', 'q34_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_69']==q1_69 and sample['q33_0']==q33_0 and sample['q34_0']==q34_0 and int(energy)==0:
        q1_69=sample['q1_69']
        q33_0=sample['q33_0']
        q34_0=sample['outq34_0']
        tgt_before = sample['q34_0']
        break

print('#' * 80)
print("CCNOT operation on q1_69 (control1), q33_0 (control2) and q34_0 (target):")
print("    in:  q1_69={0}, q33_0={1}, q34_0={2}".format(q1_69,q33_0,tgt_before))
print("    out: q1_69={0}, q33_0={1}, q34_0={2}".format(q1_69,q33_0,q34_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_69 control2: q33_0 target: q34_0 ##
################################################################################
if 'q0_69' not in globals():
    q0_69=0
if 'q33_0' not in globals():
    q33_0=0
if 'q34_0' not in globals():
    q34_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq34_0' : 1, 'q34_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq34_0') : 4, ('anc1','q34_0') : -4, ('anc2', 'q0_69') : -2, ('anc2', 'q33_0') : -2, ('anc2', 'outq34_0') : -2, ('anc2', 'q34_0') : 2, ('q0_69', 'q33_0') : 1, ('outq34_0', 'q34_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_69']==q0_69 and sample['q33_0']==q33_0 and sample['q34_0']==q34_0 and int(energy)==0:
        q0_69=sample['q0_69']
        q33_0=sample['q33_0']
        q34_0=sample['outq34_0']
        tgt_before = sample['q34_0']
        break

print('#' * 80)
print("CCNOT operation on q0_69 (control1), q33_0 (control2) and q34_0 (target):")
print("    in:  q0_69={0}, q33_0={1}, q34_0={2}".format(q0_69,q33_0,tgt_before))
print("    out: q0_69={0}, q33_0={1}, q34_0={2}".format(q0_69,q33_0,q34_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q33_0 target: q34_0 ##
################################################################################
if 'q33_0' not in globals():
    q33_0=0
if 'q34_0' not in globals():
    q34_0=0

bqm = dimod.BinaryQuadraticModel({'q33_0' : 1, 'q34_0' : 1, 'outq34_0' : 1, 'anc' : 4}, {('q33_0', 'q34_0') : 2, ('q33_0', 'outq34_0') : -2, ('q34_0', 'outq34_0') : -2, ('q33_0', 'anc') : -4, ('q34_0', 'anc') : -4, ('outq34_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q33_0']==q33_0 and sample['q34_0']==q34_0 and int(energy)==0:
        q33_0=sample['q33_0']
        q34_0=sample['outq34_0']
        tgt_before = sample['q34_0']
        break

print('#' * 80)
print("CNOT operation on q33_0 (control) and q34_0 (target):")
print("    in:  q33_0={0}, q34_0={1}".format(q33_0,tgt_before))
print("    out: q33_0={0}, q34_0={1}".format(q33_0,q34_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_70 control2: q32_0 target: q33_0 ##
################################################################################
if 'q1_70' not in globals():
    q1_70=0
if 'q32_0' not in globals():
    q32_0=0
if 'q33_0' not in globals():
    q33_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq33_0' : 1, 'q33_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq33_0') : 4, ('anc1','q33_0') : -4, ('anc2', 'q1_70') : -2, ('anc2', 'q32_0') : -2, ('anc2', 'outq33_0') : -2, ('anc2', 'q33_0') : 2, ('q1_70', 'q32_0') : 1, ('outq33_0', 'q33_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_70']==q1_70 and sample['q32_0']==q32_0 and sample['q33_0']==q33_0 and int(energy)==0:
        q1_70=sample['q1_70']
        q32_0=sample['q32_0']
        q33_0=sample['outq33_0']
        tgt_before = sample['q33_0']
        break

print('#' * 80)
print("CCNOT operation on q1_70 (control1), q32_0 (control2) and q33_0 (target):")
print("    in:  q1_70={0}, q32_0={1}, q33_0={2}".format(q1_70,q32_0,tgt_before))
print("    out: q1_70={0}, q32_0={1}, q33_0={2}".format(q1_70,q32_0,q33_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_70 control2: q32_0 target: q33_0 ##
################################################################################
if 'q0_70' not in globals():
    q0_70=0
if 'q32_0' not in globals():
    q32_0=0
if 'q33_0' not in globals():
    q33_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq33_0' : 1, 'q33_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq33_0') : 4, ('anc1','q33_0') : -4, ('anc2', 'q0_70') : -2, ('anc2', 'q32_0') : -2, ('anc2', 'outq33_0') : -2, ('anc2', 'q33_0') : 2, ('q0_70', 'q32_0') : 1, ('outq33_0', 'q33_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_70']==q0_70 and sample['q32_0']==q32_0 and sample['q33_0']==q33_0 and int(energy)==0:
        q0_70=sample['q0_70']
        q32_0=sample['q32_0']
        q33_0=sample['outq33_0']
        tgt_before = sample['q33_0']
        break

print('#' * 80)
print("CCNOT operation on q0_70 (control1), q32_0 (control2) and q33_0 (target):")
print("    in:  q0_70={0}, q32_0={1}, q33_0={2}".format(q0_70,q32_0,tgt_before))
print("    out: q0_70={0}, q32_0={1}, q33_0={2}".format(q0_70,q32_0,q33_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q32_0 target: q33_0 ##
################################################################################
if 'q32_0' not in globals():
    q32_0=0
if 'q33_0' not in globals():
    q33_0=0

bqm = dimod.BinaryQuadraticModel({'q32_0' : 1, 'q33_0' : 1, 'outq33_0' : 1, 'anc' : 4}, {('q32_0', 'q33_0') : 2, ('q32_0', 'outq33_0') : -2, ('q33_0', 'outq33_0') : -2, ('q32_0', 'anc') : -4, ('q33_0', 'anc') : -4, ('outq33_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q32_0']==q32_0 and sample['q33_0']==q33_0 and int(energy)==0:
        q32_0=sample['q32_0']
        q33_0=sample['outq33_0']
        tgt_before = sample['q33_0']
        break

print('#' * 80)
print("CNOT operation on q32_0 (control) and q33_0 (target):")
print("    in:  q32_0={0}, q33_0={1}".format(q32_0,tgt_before))
print("    out: q32_0={0}, q33_0={1}".format(q32_0,q33_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_71 control2: q31_0 target: q32_0 ##
################################################################################
if 'q1_71' not in globals():
    q1_71=0
if 'q31_0' not in globals():
    q31_0=0
if 'q32_0' not in globals():
    q32_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq32_0' : 1, 'q32_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq32_0') : 4, ('anc1','q32_0') : -4, ('anc2', 'q1_71') : -2, ('anc2', 'q31_0') : -2, ('anc2', 'outq32_0') : -2, ('anc2', 'q32_0') : 2, ('q1_71', 'q31_0') : 1, ('outq32_0', 'q32_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_71']==q1_71 and sample['q31_0']==q31_0 and sample['q32_0']==q32_0 and int(energy)==0:
        q1_71=sample['q1_71']
        q31_0=sample['q31_0']
        q32_0=sample['outq32_0']
        tgt_before = sample['q32_0']
        break

print('#' * 80)
print("CCNOT operation on q1_71 (control1), q31_0 (control2) and q32_0 (target):")
print("    in:  q1_71={0}, q31_0={1}, q32_0={2}".format(q1_71,q31_0,tgt_before))
print("    out: q1_71={0}, q31_0={1}, q32_0={2}".format(q1_71,q31_0,q32_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_71 control2: q31_0 target: q32_0 ##
################################################################################
if 'q0_71' not in globals():
    q0_71=0
if 'q31_0' not in globals():
    q31_0=0
if 'q32_0' not in globals():
    q32_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq32_0' : 1, 'q32_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq32_0') : 4, ('anc1','q32_0') : -4, ('anc2', 'q0_71') : -2, ('anc2', 'q31_0') : -2, ('anc2', 'outq32_0') : -2, ('anc2', 'q32_0') : 2, ('q0_71', 'q31_0') : 1, ('outq32_0', 'q32_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_71']==q0_71 and sample['q31_0']==q31_0 and sample['q32_0']==q32_0 and int(energy)==0:
        q0_71=sample['q0_71']
        q31_0=sample['q31_0']
        q32_0=sample['outq32_0']
        tgt_before = sample['q32_0']
        break

print('#' * 80)
print("CCNOT operation on q0_71 (control1), q31_0 (control2) and q32_0 (target):")
print("    in:  q0_71={0}, q31_0={1}, q32_0={2}".format(q0_71,q31_0,tgt_before))
print("    out: q0_71={0}, q31_0={1}, q32_0={2}".format(q0_71,q31_0,q32_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q31_0 target: q32_0 ##
################################################################################
if 'q31_0' not in globals():
    q31_0=0
if 'q32_0' not in globals():
    q32_0=0

bqm = dimod.BinaryQuadraticModel({'q31_0' : 1, 'q32_0' : 1, 'outq32_0' : 1, 'anc' : 4}, {('q31_0', 'q32_0') : 2, ('q31_0', 'outq32_0') : -2, ('q32_0', 'outq32_0') : -2, ('q31_0', 'anc') : -4, ('q32_0', 'anc') : -4, ('outq32_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q31_0']==q31_0 and sample['q32_0']==q32_0 and int(energy)==0:
        q31_0=sample['q31_0']
        q32_0=sample['outq32_0']
        tgt_before = sample['q32_0']
        break

print('#' * 80)
print("CNOT operation on q31_0 (control) and q32_0 (target):")
print("    in:  q31_0={0}, q32_0={1}".format(q31_0,tgt_before))
print("    out: q31_0={0}, q32_0={1}".format(q31_0,q32_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_72 control2: q30_0 target: q31_0 ##
################################################################################
if 'q1_72' not in globals():
    q1_72=0
if 'q30_0' not in globals():
    q30_0=0
if 'q31_0' not in globals():
    q31_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq31_0' : 1, 'q31_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq31_0') : 4, ('anc1','q31_0') : -4, ('anc2', 'q1_72') : -2, ('anc2', 'q30_0') : -2, ('anc2', 'outq31_0') : -2, ('anc2', 'q31_0') : 2, ('q1_72', 'q30_0') : 1, ('outq31_0', 'q31_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_72']==q1_72 and sample['q30_0']==q30_0 and sample['q31_0']==q31_0 and int(energy)==0:
        q1_72=sample['q1_72']
        q30_0=sample['q30_0']
        q31_0=sample['outq31_0']
        tgt_before = sample['q31_0']
        break

print('#' * 80)
print("CCNOT operation on q1_72 (control1), q30_0 (control2) and q31_0 (target):")
print("    in:  q1_72={0}, q30_0={1}, q31_0={2}".format(q1_72,q30_0,tgt_before))
print("    out: q1_72={0}, q30_0={1}, q31_0={2}".format(q1_72,q30_0,q31_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_72 control2: q30_0 target: q31_0 ##
################################################################################
if 'q0_72' not in globals():
    q0_72=0
if 'q30_0' not in globals():
    q30_0=0
if 'q31_0' not in globals():
    q31_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq31_0' : 1, 'q31_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq31_0') : 4, ('anc1','q31_0') : -4, ('anc2', 'q0_72') : -2, ('anc2', 'q30_0') : -2, ('anc2', 'outq31_0') : -2, ('anc2', 'q31_0') : 2, ('q0_72', 'q30_0') : 1, ('outq31_0', 'q31_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_72']==q0_72 and sample['q30_0']==q30_0 and sample['q31_0']==q31_0 and int(energy)==0:
        q0_72=sample['q0_72']
        q30_0=sample['q30_0']
        q31_0=sample['outq31_0']
        tgt_before = sample['q31_0']
        break

print('#' * 80)
print("CCNOT operation on q0_72 (control1), q30_0 (control2) and q31_0 (target):")
print("    in:  q0_72={0}, q30_0={1}, q31_0={2}".format(q0_72,q30_0,tgt_before))
print("    out: q0_72={0}, q30_0={1}, q31_0={2}".format(q0_72,q30_0,q31_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q30_0 target: q31_0 ##
################################################################################
if 'q30_0' not in globals():
    q30_0=0
if 'q31_0' not in globals():
    q31_0=0

bqm = dimod.BinaryQuadraticModel({'q30_0' : 1, 'q31_0' : 1, 'outq31_0' : 1, 'anc' : 4}, {('q30_0', 'q31_0') : 2, ('q30_0', 'outq31_0') : -2, ('q31_0', 'outq31_0') : -2, ('q30_0', 'anc') : -4, ('q31_0', 'anc') : -4, ('outq31_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q30_0']==q30_0 and sample['q31_0']==q31_0 and int(energy)==0:
        q30_0=sample['q30_0']
        q31_0=sample['outq31_0']
        tgt_before = sample['q31_0']
        break

print('#' * 80)
print("CNOT operation on q30_0 (control) and q31_0 (target):")
print("    in:  q30_0={0}, q31_0={1}".format(q30_0,tgt_before))
print("    out: q30_0={0}, q31_0={1}".format(q30_0,q31_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_73 control2: q29_0 target: q30_0 ##
################################################################################
if 'q1_73' not in globals():
    q1_73=0
if 'q29_0' not in globals():
    q29_0=0
if 'q30_0' not in globals():
    q30_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq30_0' : 1, 'q30_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq30_0') : 4, ('anc1','q30_0') : -4, ('anc2', 'q1_73') : -2, ('anc2', 'q29_0') : -2, ('anc2', 'outq30_0') : -2, ('anc2', 'q30_0') : 2, ('q1_73', 'q29_0') : 1, ('outq30_0', 'q30_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_73']==q1_73 and sample['q29_0']==q29_0 and sample['q30_0']==q30_0 and int(energy)==0:
        q1_73=sample['q1_73']
        q29_0=sample['q29_0']
        q30_0=sample['outq30_0']
        tgt_before = sample['q30_0']
        break

print('#' * 80)
print("CCNOT operation on q1_73 (control1), q29_0 (control2) and q30_0 (target):")
print("    in:  q1_73={0}, q29_0={1}, q30_0={2}".format(q1_73,q29_0,tgt_before))
print("    out: q1_73={0}, q29_0={1}, q30_0={2}".format(q1_73,q29_0,q30_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_73 control2: q29_0 target: q30_0 ##
################################################################################
if 'q0_73' not in globals():
    q0_73=0
if 'q29_0' not in globals():
    q29_0=0
if 'q30_0' not in globals():
    q30_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq30_0' : 1, 'q30_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq30_0') : 4, ('anc1','q30_0') : -4, ('anc2', 'q0_73') : -2, ('anc2', 'q29_0') : -2, ('anc2', 'outq30_0') : -2, ('anc2', 'q30_0') : 2, ('q0_73', 'q29_0') : 1, ('outq30_0', 'q30_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_73']==q0_73 and sample['q29_0']==q29_0 and sample['q30_0']==q30_0 and int(energy)==0:
        q0_73=sample['q0_73']
        q29_0=sample['q29_0']
        q30_0=sample['outq30_0']
        tgt_before = sample['q30_0']
        break

print('#' * 80)
print("CCNOT operation on q0_73 (control1), q29_0 (control2) and q30_0 (target):")
print("    in:  q0_73={0}, q29_0={1}, q30_0={2}".format(q0_73,q29_0,tgt_before))
print("    out: q0_73={0}, q29_0={1}, q30_0={2}".format(q0_73,q29_0,q30_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q29_0 target: q30_0 ##
################################################################################
if 'q29_0' not in globals():
    q29_0=0
if 'q30_0' not in globals():
    q30_0=0

bqm = dimod.BinaryQuadraticModel({'q29_0' : 1, 'q30_0' : 1, 'outq30_0' : 1, 'anc' : 4}, {('q29_0', 'q30_0') : 2, ('q29_0', 'outq30_0') : -2, ('q30_0', 'outq30_0') : -2, ('q29_0', 'anc') : -4, ('q30_0', 'anc') : -4, ('outq30_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q29_0']==q29_0 and sample['q30_0']==q30_0 and int(energy)==0:
        q29_0=sample['q29_0']
        q30_0=sample['outq30_0']
        tgt_before = sample['q30_0']
        break

print('#' * 80)
print("CNOT operation on q29_0 (control) and q30_0 (target):")
print("    in:  q29_0={0}, q30_0={1}".format(q29_0,tgt_before))
print("    out: q29_0={0}, q30_0={1}".format(q29_0,q30_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_74 control2: q28_0 target: q29_0 ##
################################################################################
if 'q1_74' not in globals():
    q1_74=0
if 'q28_0' not in globals():
    q28_0=0
if 'q29_0' not in globals():
    q29_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq29_0' : 1, 'q29_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq29_0') : 4, ('anc1','q29_0') : -4, ('anc2', 'q1_74') : -2, ('anc2', 'q28_0') : -2, ('anc2', 'outq29_0') : -2, ('anc2', 'q29_0') : 2, ('q1_74', 'q28_0') : 1, ('outq29_0', 'q29_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_74']==q1_74 and sample['q28_0']==q28_0 and sample['q29_0']==q29_0 and int(energy)==0:
        q1_74=sample['q1_74']
        q28_0=sample['q28_0']
        q29_0=sample['outq29_0']
        tgt_before = sample['q29_0']
        break

print('#' * 80)
print("CCNOT operation on q1_74 (control1), q28_0 (control2) and q29_0 (target):")
print("    in:  q1_74={0}, q28_0={1}, q29_0={2}".format(q1_74,q28_0,tgt_before))
print("    out: q1_74={0}, q28_0={1}, q29_0={2}".format(q1_74,q28_0,q29_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_74 control2: q28_0 target: q29_0 ##
################################################################################
if 'q0_74' not in globals():
    q0_74=0
if 'q28_0' not in globals():
    q28_0=0
if 'q29_0' not in globals():
    q29_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq29_0' : 1, 'q29_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq29_0') : 4, ('anc1','q29_0') : -4, ('anc2', 'q0_74') : -2, ('anc2', 'q28_0') : -2, ('anc2', 'outq29_0') : -2, ('anc2', 'q29_0') : 2, ('q0_74', 'q28_0') : 1, ('outq29_0', 'q29_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_74']==q0_74 and sample['q28_0']==q28_0 and sample['q29_0']==q29_0 and int(energy)==0:
        q0_74=sample['q0_74']
        q28_0=sample['q28_0']
        q29_0=sample['outq29_0']
        tgt_before = sample['q29_0']
        break

print('#' * 80)
print("CCNOT operation on q0_74 (control1), q28_0 (control2) and q29_0 (target):")
print("    in:  q0_74={0}, q28_0={1}, q29_0={2}".format(q0_74,q28_0,tgt_before))
print("    out: q0_74={0}, q28_0={1}, q29_0={2}".format(q0_74,q28_0,q29_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q28_0 target: q29_0 ##
################################################################################
if 'q28_0' not in globals():
    q28_0=0
if 'q29_0' not in globals():
    q29_0=0

bqm = dimod.BinaryQuadraticModel({'q28_0' : 1, 'q29_0' : 1, 'outq29_0' : 1, 'anc' : 4}, {('q28_0', 'q29_0') : 2, ('q28_0', 'outq29_0') : -2, ('q29_0', 'outq29_0') : -2, ('q28_0', 'anc') : -4, ('q29_0', 'anc') : -4, ('outq29_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q28_0']==q28_0 and sample['q29_0']==q29_0 and int(energy)==0:
        q28_0=sample['q28_0']
        q29_0=sample['outq29_0']
        tgt_before = sample['q29_0']
        break

print('#' * 80)
print("CNOT operation on q28_0 (control) and q29_0 (target):")
print("    in:  q28_0={0}, q29_0={1}".format(q28_0,tgt_before))
print("    out: q28_0={0}, q29_0={1}".format(q28_0,q29_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_75 control2: q27_0 target: q28_0 ##
################################################################################
if 'q1_75' not in globals():
    q1_75=0
if 'q27_0' not in globals():
    q27_0=0
if 'q28_0' not in globals():
    q28_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq28_0' : 1, 'q28_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq28_0') : 4, ('anc1','q28_0') : -4, ('anc2', 'q1_75') : -2, ('anc2', 'q27_0') : -2, ('anc2', 'outq28_0') : -2, ('anc2', 'q28_0') : 2, ('q1_75', 'q27_0') : 1, ('outq28_0', 'q28_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_75']==q1_75 and sample['q27_0']==q27_0 and sample['q28_0']==q28_0 and int(energy)==0:
        q1_75=sample['q1_75']
        q27_0=sample['q27_0']
        q28_0=sample['outq28_0']
        tgt_before = sample['q28_0']
        break

print('#' * 80)
print("CCNOT operation on q1_75 (control1), q27_0 (control2) and q28_0 (target):")
print("    in:  q1_75={0}, q27_0={1}, q28_0={2}".format(q1_75,q27_0,tgt_before))
print("    out: q1_75={0}, q27_0={1}, q28_0={2}".format(q1_75,q27_0,q28_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_75 control2: q27_0 target: q28_0 ##
################################################################################
if 'q0_75' not in globals():
    q0_75=0
if 'q27_0' not in globals():
    q27_0=0
if 'q28_0' not in globals():
    q28_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq28_0' : 1, 'q28_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq28_0') : 4, ('anc1','q28_0') : -4, ('anc2', 'q0_75') : -2, ('anc2', 'q27_0') : -2, ('anc2', 'outq28_0') : -2, ('anc2', 'q28_0') : 2, ('q0_75', 'q27_0') : 1, ('outq28_0', 'q28_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_75']==q0_75 and sample['q27_0']==q27_0 and sample['q28_0']==q28_0 and int(energy)==0:
        q0_75=sample['q0_75']
        q27_0=sample['q27_0']
        q28_0=sample['outq28_0']
        tgt_before = sample['q28_0']
        break

print('#' * 80)
print("CCNOT operation on q0_75 (control1), q27_0 (control2) and q28_0 (target):")
print("    in:  q0_75={0}, q27_0={1}, q28_0={2}".format(q0_75,q27_0,tgt_before))
print("    out: q0_75={0}, q27_0={1}, q28_0={2}".format(q0_75,q27_0,q28_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q27_0 target: q28_0 ##
################################################################################
if 'q27_0' not in globals():
    q27_0=0
if 'q28_0' not in globals():
    q28_0=0

bqm = dimod.BinaryQuadraticModel({'q27_0' : 1, 'q28_0' : 1, 'outq28_0' : 1, 'anc' : 4}, {('q27_0', 'q28_0') : 2, ('q27_0', 'outq28_0') : -2, ('q28_0', 'outq28_0') : -2, ('q27_0', 'anc') : -4, ('q28_0', 'anc') : -4, ('outq28_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q27_0']==q27_0 and sample['q28_0']==q28_0 and int(energy)==0:
        q27_0=sample['q27_0']
        q28_0=sample['outq28_0']
        tgt_before = sample['q28_0']
        break

print('#' * 80)
print("CNOT operation on q27_0 (control) and q28_0 (target):")
print("    in:  q27_0={0}, q28_0={1}".format(q27_0,tgt_before))
print("    out: q27_0={0}, q28_0={1}".format(q27_0,q28_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_76 control2: q26_0 target: q27_0 ##
################################################################################
if 'q1_76' not in globals():
    q1_76=0
if 'q26_0' not in globals():
    q26_0=0
if 'q27_0' not in globals():
    q27_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq27_0' : 1, 'q27_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq27_0') : 4, ('anc1','q27_0') : -4, ('anc2', 'q1_76') : -2, ('anc2', 'q26_0') : -2, ('anc2', 'outq27_0') : -2, ('anc2', 'q27_0') : 2, ('q1_76', 'q26_0') : 1, ('outq27_0', 'q27_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_76']==q1_76 and sample['q26_0']==q26_0 and sample['q27_0']==q27_0 and int(energy)==0:
        q1_76=sample['q1_76']
        q26_0=sample['q26_0']
        q27_0=sample['outq27_0']
        tgt_before = sample['q27_0']
        break

print('#' * 80)
print("CCNOT operation on q1_76 (control1), q26_0 (control2) and q27_0 (target):")
print("    in:  q1_76={0}, q26_0={1}, q27_0={2}".format(q1_76,q26_0,tgt_before))
print("    out: q1_76={0}, q26_0={1}, q27_0={2}".format(q1_76,q26_0,q27_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_76 control2: q26_0 target: q27_0 ##
################################################################################
if 'q0_76' not in globals():
    q0_76=0
if 'q26_0' not in globals():
    q26_0=0
if 'q27_0' not in globals():
    q27_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq27_0' : 1, 'q27_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq27_0') : 4, ('anc1','q27_0') : -4, ('anc2', 'q0_76') : -2, ('anc2', 'q26_0') : -2, ('anc2', 'outq27_0') : -2, ('anc2', 'q27_0') : 2, ('q0_76', 'q26_0') : 1, ('outq27_0', 'q27_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_76']==q0_76 and sample['q26_0']==q26_0 and sample['q27_0']==q27_0 and int(energy)==0:
        q0_76=sample['q0_76']
        q26_0=sample['q26_0']
        q27_0=sample['outq27_0']
        tgt_before = sample['q27_0']
        break

print('#' * 80)
print("CCNOT operation on q0_76 (control1), q26_0 (control2) and q27_0 (target):")
print("    in:  q0_76={0}, q26_0={1}, q27_0={2}".format(q0_76,q26_0,tgt_before))
print("    out: q0_76={0}, q26_0={1}, q27_0={2}".format(q0_76,q26_0,q27_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q26_0 target: q27_0 ##
################################################################################
if 'q26_0' not in globals():
    q26_0=0
if 'q27_0' not in globals():
    q27_0=0

bqm = dimod.BinaryQuadraticModel({'q26_0' : 1, 'q27_0' : 1, 'outq27_0' : 1, 'anc' : 4}, {('q26_0', 'q27_0') : 2, ('q26_0', 'outq27_0') : -2, ('q27_0', 'outq27_0') : -2, ('q26_0', 'anc') : -4, ('q27_0', 'anc') : -4, ('outq27_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q26_0']==q26_0 and sample['q27_0']==q27_0 and int(energy)==0:
        q26_0=sample['q26_0']
        q27_0=sample['outq27_0']
        tgt_before = sample['q27_0']
        break

print('#' * 80)
print("CNOT operation on q26_0 (control) and q27_0 (target):")
print("    in:  q26_0={0}, q27_0={1}".format(q26_0,tgt_before))
print("    out: q26_0={0}, q27_0={1}".format(q26_0,q27_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_77 control2: q25_0 target: q26_0 ##
################################################################################
if 'q1_77' not in globals():
    q1_77=0
if 'q25_0' not in globals():
    q25_0=0
if 'q26_0' not in globals():
    q26_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq26_0' : 1, 'q26_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq26_0') : 4, ('anc1','q26_0') : -4, ('anc2', 'q1_77') : -2, ('anc2', 'q25_0') : -2, ('anc2', 'outq26_0') : -2, ('anc2', 'q26_0') : 2, ('q1_77', 'q25_0') : 1, ('outq26_0', 'q26_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_77']==q1_77 and sample['q25_0']==q25_0 and sample['q26_0']==q26_0 and int(energy)==0:
        q1_77=sample['q1_77']
        q25_0=sample['q25_0']
        q26_0=sample['outq26_0']
        tgt_before = sample['q26_0']
        break

print('#' * 80)
print("CCNOT operation on q1_77 (control1), q25_0 (control2) and q26_0 (target):")
print("    in:  q1_77={0}, q25_0={1}, q26_0={2}".format(q1_77,q25_0,tgt_before))
print("    out: q1_77={0}, q25_0={1}, q26_0={2}".format(q1_77,q25_0,q26_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_77 control2: q25_0 target: q26_0 ##
################################################################################
if 'q0_77' not in globals():
    q0_77=0
if 'q25_0' not in globals():
    q25_0=0
if 'q26_0' not in globals():
    q26_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq26_0' : 1, 'q26_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq26_0') : 4, ('anc1','q26_0') : -4, ('anc2', 'q0_77') : -2, ('anc2', 'q25_0') : -2, ('anc2', 'outq26_0') : -2, ('anc2', 'q26_0') : 2, ('q0_77', 'q25_0') : 1, ('outq26_0', 'q26_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_77']==q0_77 and sample['q25_0']==q25_0 and sample['q26_0']==q26_0 and int(energy)==0:
        q0_77=sample['q0_77']
        q25_0=sample['q25_0']
        q26_0=sample['outq26_0']
        tgt_before = sample['q26_0']
        break

print('#' * 80)
print("CCNOT operation on q0_77 (control1), q25_0 (control2) and q26_0 (target):")
print("    in:  q0_77={0}, q25_0={1}, q26_0={2}".format(q0_77,q25_0,tgt_before))
print("    out: q0_77={0}, q25_0={1}, q26_0={2}".format(q0_77,q25_0,q26_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q25_0 target: q26_0 ##
################################################################################
if 'q25_0' not in globals():
    q25_0=0
if 'q26_0' not in globals():
    q26_0=0

bqm = dimod.BinaryQuadraticModel({'q25_0' : 1, 'q26_0' : 1, 'outq26_0' : 1, 'anc' : 4}, {('q25_0', 'q26_0') : 2, ('q25_0', 'outq26_0') : -2, ('q26_0', 'outq26_0') : -2, ('q25_0', 'anc') : -4, ('q26_0', 'anc') : -4, ('outq26_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q25_0']==q25_0 and sample['q26_0']==q26_0 and int(energy)==0:
        q25_0=sample['q25_0']
        q26_0=sample['outq26_0']
        tgt_before = sample['q26_0']
        break

print('#' * 80)
print("CNOT operation on q25_0 (control) and q26_0 (target):")
print("    in:  q25_0={0}, q26_0={1}".format(q25_0,tgt_before))
print("    out: q25_0={0}, q26_0={1}".format(q25_0,q26_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_78 control2: q24_0 target: q25_0 ##
################################################################################
if 'q1_78' not in globals():
    q1_78=0
if 'q24_0' not in globals():
    q24_0=0
if 'q25_0' not in globals():
    q25_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq25_0' : 1, 'q25_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq25_0') : 4, ('anc1','q25_0') : -4, ('anc2', 'q1_78') : -2, ('anc2', 'q24_0') : -2, ('anc2', 'outq25_0') : -2, ('anc2', 'q25_0') : 2, ('q1_78', 'q24_0') : 1, ('outq25_0', 'q25_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_78']==q1_78 and sample['q24_0']==q24_0 and sample['q25_0']==q25_0 and int(energy)==0:
        q1_78=sample['q1_78']
        q24_0=sample['q24_0']
        q25_0=sample['outq25_0']
        tgt_before = sample['q25_0']
        break

print('#' * 80)
print("CCNOT operation on q1_78 (control1), q24_0 (control2) and q25_0 (target):")
print("    in:  q1_78={0}, q24_0={1}, q25_0={2}".format(q1_78,q24_0,tgt_before))
print("    out: q1_78={0}, q24_0={1}, q25_0={2}".format(q1_78,q24_0,q25_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_78 control2: q24_0 target: q25_0 ##
################################################################################
if 'q0_78' not in globals():
    q0_78=0
if 'q24_0' not in globals():
    q24_0=0
if 'q25_0' not in globals():
    q25_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq25_0' : 1, 'q25_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq25_0') : 4, ('anc1','q25_0') : -4, ('anc2', 'q0_78') : -2, ('anc2', 'q24_0') : -2, ('anc2', 'outq25_0') : -2, ('anc2', 'q25_0') : 2, ('q0_78', 'q24_0') : 1, ('outq25_0', 'q25_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_78']==q0_78 and sample['q24_0']==q24_0 and sample['q25_0']==q25_0 and int(energy)==0:
        q0_78=sample['q0_78']
        q24_0=sample['q24_0']
        q25_0=sample['outq25_0']
        tgt_before = sample['q25_0']
        break

print('#' * 80)
print("CCNOT operation on q0_78 (control1), q24_0 (control2) and q25_0 (target):")
print("    in:  q0_78={0}, q24_0={1}, q25_0={2}".format(q0_78,q24_0,tgt_before))
print("    out: q0_78={0}, q24_0={1}, q25_0={2}".format(q0_78,q24_0,q25_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q24_0 target: q25_0 ##
################################################################################
if 'q24_0' not in globals():
    q24_0=0
if 'q25_0' not in globals():
    q25_0=0

bqm = dimod.BinaryQuadraticModel({'q24_0' : 1, 'q25_0' : 1, 'outq25_0' : 1, 'anc' : 4}, {('q24_0', 'q25_0') : 2, ('q24_0', 'outq25_0') : -2, ('q25_0', 'outq25_0') : -2, ('q24_0', 'anc') : -4, ('q25_0', 'anc') : -4, ('outq25_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q24_0']==q24_0 and sample['q25_0']==q25_0 and int(energy)==0:
        q24_0=sample['q24_0']
        q25_0=sample['outq25_0']
        tgt_before = sample['q25_0']
        break

print('#' * 80)
print("CNOT operation on q24_0 (control) and q25_0 (target):")
print("    in:  q24_0={0}, q25_0={1}".format(q24_0,tgt_before))
print("    out: q24_0={0}, q25_0={1}".format(q24_0,q25_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_79 control2: q23_0 target: q24_0 ##
################################################################################
if 'q1_79' not in globals():
    q1_79=0
if 'q23_0' not in globals():
    q23_0=0
if 'q24_0' not in globals():
    q24_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq24_0' : 1, 'q24_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq24_0') : 4, ('anc1','q24_0') : -4, ('anc2', 'q1_79') : -2, ('anc2', 'q23_0') : -2, ('anc2', 'outq24_0') : -2, ('anc2', 'q24_0') : 2, ('q1_79', 'q23_0') : 1, ('outq24_0', 'q24_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_79']==q1_79 and sample['q23_0']==q23_0 and sample['q24_0']==q24_0 and int(energy)==0:
        q1_79=sample['q1_79']
        q23_0=sample['q23_0']
        q24_0=sample['outq24_0']
        tgt_before = sample['q24_0']
        break

print('#' * 80)
print("CCNOT operation on q1_79 (control1), q23_0 (control2) and q24_0 (target):")
print("    in:  q1_79={0}, q23_0={1}, q24_0={2}".format(q1_79,q23_0,tgt_before))
print("    out: q1_79={0}, q23_0={1}, q24_0={2}".format(q1_79,q23_0,q24_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_79 control2: q23_0 target: q24_0 ##
################################################################################
if 'q0_79' not in globals():
    q0_79=0
if 'q23_0' not in globals():
    q23_0=0
if 'q24_0' not in globals():
    q24_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq24_0' : 1, 'q24_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq24_0') : 4, ('anc1','q24_0') : -4, ('anc2', 'q0_79') : -2, ('anc2', 'q23_0') : -2, ('anc2', 'outq24_0') : -2, ('anc2', 'q24_0') : 2, ('q0_79', 'q23_0') : 1, ('outq24_0', 'q24_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_79']==q0_79 and sample['q23_0']==q23_0 and sample['q24_0']==q24_0 and int(energy)==0:
        q0_79=sample['q0_79']
        q23_0=sample['q23_0']
        q24_0=sample['outq24_0']
        tgt_before = sample['q24_0']
        break

print('#' * 80)
print("CCNOT operation on q0_79 (control1), q23_0 (control2) and q24_0 (target):")
print("    in:  q0_79={0}, q23_0={1}, q24_0={2}".format(q0_79,q23_0,tgt_before))
print("    out: q0_79={0}, q23_0={1}, q24_0={2}".format(q0_79,q23_0,q24_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q23_0 target: q24_0 ##
################################################################################
if 'q23_0' not in globals():
    q23_0=0
if 'q24_0' not in globals():
    q24_0=0

bqm = dimod.BinaryQuadraticModel({'q23_0' : 1, 'q24_0' : 1, 'outq24_0' : 1, 'anc' : 4}, {('q23_0', 'q24_0') : 2, ('q23_0', 'outq24_0') : -2, ('q24_0', 'outq24_0') : -2, ('q23_0', 'anc') : -4, ('q24_0', 'anc') : -4, ('outq24_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q23_0']==q23_0 and sample['q24_0']==q24_0 and int(energy)==0:
        q23_0=sample['q23_0']
        q24_0=sample['outq24_0']
        tgt_before = sample['q24_0']
        break

print('#' * 80)
print("CNOT operation on q23_0 (control) and q24_0 (target):")
print("    in:  q23_0={0}, q24_0={1}".format(q23_0,tgt_before))
print("    out: q23_0={0}, q24_0={1}".format(q23_0,q24_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_80 control2: q22_0 target: q23_0 ##
################################################################################
if 'q1_80' not in globals():
    q1_80=0
if 'q22_0' not in globals():
    q22_0=0
if 'q23_0' not in globals():
    q23_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq23_0' : 1, 'q23_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq23_0') : 4, ('anc1','q23_0') : -4, ('anc2', 'q1_80') : -2, ('anc2', 'q22_0') : -2, ('anc2', 'outq23_0') : -2, ('anc2', 'q23_0') : 2, ('q1_80', 'q22_0') : 1, ('outq23_0', 'q23_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_80']==q1_80 and sample['q22_0']==q22_0 and sample['q23_0']==q23_0 and int(energy)==0:
        q1_80=sample['q1_80']
        q22_0=sample['q22_0']
        q23_0=sample['outq23_0']
        tgt_before = sample['q23_0']
        break

print('#' * 80)
print("CCNOT operation on q1_80 (control1), q22_0 (control2) and q23_0 (target):")
print("    in:  q1_80={0}, q22_0={1}, q23_0={2}".format(q1_80,q22_0,tgt_before))
print("    out: q1_80={0}, q22_0={1}, q23_0={2}".format(q1_80,q22_0,q23_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_80 control2: q22_0 target: q23_0 ##
################################################################################
if 'q0_80' not in globals():
    q0_80=0
if 'q22_0' not in globals():
    q22_0=0
if 'q23_0' not in globals():
    q23_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq23_0' : 1, 'q23_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq23_0') : 4, ('anc1','q23_0') : -4, ('anc2', 'q0_80') : -2, ('anc2', 'q22_0') : -2, ('anc2', 'outq23_0') : -2, ('anc2', 'q23_0') : 2, ('q0_80', 'q22_0') : 1, ('outq23_0', 'q23_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_80']==q0_80 and sample['q22_0']==q22_0 and sample['q23_0']==q23_0 and int(energy)==0:
        q0_80=sample['q0_80']
        q22_0=sample['q22_0']
        q23_0=sample['outq23_0']
        tgt_before = sample['q23_0']
        break

print('#' * 80)
print("CCNOT operation on q0_80 (control1), q22_0 (control2) and q23_0 (target):")
print("    in:  q0_80={0}, q22_0={1}, q23_0={2}".format(q0_80,q22_0,tgt_before))
print("    out: q0_80={0}, q22_0={1}, q23_0={2}".format(q0_80,q22_0,q23_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q22_0 target: q23_0 ##
################################################################################
if 'q22_0' not in globals():
    q22_0=0
if 'q23_0' not in globals():
    q23_0=0

bqm = dimod.BinaryQuadraticModel({'q22_0' : 1, 'q23_0' : 1, 'outq23_0' : 1, 'anc' : 4}, {('q22_0', 'q23_0') : 2, ('q22_0', 'outq23_0') : -2, ('q23_0', 'outq23_0') : -2, ('q22_0', 'anc') : -4, ('q23_0', 'anc') : -4, ('outq23_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q22_0']==q22_0 and sample['q23_0']==q23_0 and int(energy)==0:
        q22_0=sample['q22_0']
        q23_0=sample['outq23_0']
        tgt_before = sample['q23_0']
        break

print('#' * 80)
print("CNOT operation on q22_0 (control) and q23_0 (target):")
print("    in:  q22_0={0}, q23_0={1}".format(q22_0,tgt_before))
print("    out: q22_0={0}, q23_0={1}".format(q22_0,q23_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_81 control2: q21_0 target: q22_0 ##
################################################################################
if 'q1_81' not in globals():
    q1_81=0
if 'q21_0' not in globals():
    q21_0=0
if 'q22_0' not in globals():
    q22_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq22_0' : 1, 'q22_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq22_0') : 4, ('anc1','q22_0') : -4, ('anc2', 'q1_81') : -2, ('anc2', 'q21_0') : -2, ('anc2', 'outq22_0') : -2, ('anc2', 'q22_0') : 2, ('q1_81', 'q21_0') : 1, ('outq22_0', 'q22_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_81']==q1_81 and sample['q21_0']==q21_0 and sample['q22_0']==q22_0 and int(energy)==0:
        q1_81=sample['q1_81']
        q21_0=sample['q21_0']
        q22_0=sample['outq22_0']
        tgt_before = sample['q22_0']
        break

print('#' * 80)
print("CCNOT operation on q1_81 (control1), q21_0 (control2) and q22_0 (target):")
print("    in:  q1_81={0}, q21_0={1}, q22_0={2}".format(q1_81,q21_0,tgt_before))
print("    out: q1_81={0}, q21_0={1}, q22_0={2}".format(q1_81,q21_0,q22_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_81 control2: q21_0 target: q22_0 ##
################################################################################
if 'q0_81' not in globals():
    q0_81=0
if 'q21_0' not in globals():
    q21_0=0
if 'q22_0' not in globals():
    q22_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq22_0' : 1, 'q22_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq22_0') : 4, ('anc1','q22_0') : -4, ('anc2', 'q0_81') : -2, ('anc2', 'q21_0') : -2, ('anc2', 'outq22_0') : -2, ('anc2', 'q22_0') : 2, ('q0_81', 'q21_0') : 1, ('outq22_0', 'q22_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_81']==q0_81 and sample['q21_0']==q21_0 and sample['q22_0']==q22_0 and int(energy)==0:
        q0_81=sample['q0_81']
        q21_0=sample['q21_0']
        q22_0=sample['outq22_0']
        tgt_before = sample['q22_0']
        break

print('#' * 80)
print("CCNOT operation on q0_81 (control1), q21_0 (control2) and q22_0 (target):")
print("    in:  q0_81={0}, q21_0={1}, q22_0={2}".format(q0_81,q21_0,tgt_before))
print("    out: q0_81={0}, q21_0={1}, q22_0={2}".format(q0_81,q21_0,q22_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q21_0 target: q22_0 ##
################################################################################
if 'q21_0' not in globals():
    q21_0=0
if 'q22_0' not in globals():
    q22_0=0

bqm = dimod.BinaryQuadraticModel({'q21_0' : 1, 'q22_0' : 1, 'outq22_0' : 1, 'anc' : 4}, {('q21_0', 'q22_0') : 2, ('q21_0', 'outq22_0') : -2, ('q22_0', 'outq22_0') : -2, ('q21_0', 'anc') : -4, ('q22_0', 'anc') : -4, ('outq22_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q21_0']==q21_0 and sample['q22_0']==q22_0 and int(energy)==0:
        q21_0=sample['q21_0']
        q22_0=sample['outq22_0']
        tgt_before = sample['q22_0']
        break

print('#' * 80)
print("CNOT operation on q21_0 (control) and q22_0 (target):")
print("    in:  q21_0={0}, q22_0={1}".format(q21_0,tgt_before))
print("    out: q21_0={0}, q22_0={1}".format(q21_0,q22_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_82 control2: q20_0 target: q21_0 ##
################################################################################
if 'q1_82' not in globals():
    q1_82=0
if 'q20_0' not in globals():
    q20_0=0
if 'q21_0' not in globals():
    q21_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq21_0' : 1, 'q21_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq21_0') : 4, ('anc1','q21_0') : -4, ('anc2', 'q1_82') : -2, ('anc2', 'q20_0') : -2, ('anc2', 'outq21_0') : -2, ('anc2', 'q21_0') : 2, ('q1_82', 'q20_0') : 1, ('outq21_0', 'q21_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_82']==q1_82 and sample['q20_0']==q20_0 and sample['q21_0']==q21_0 and int(energy)==0:
        q1_82=sample['q1_82']
        q20_0=sample['q20_0']
        q21_0=sample['outq21_0']
        tgt_before = sample['q21_0']
        break

print('#' * 80)
print("CCNOT operation on q1_82 (control1), q20_0 (control2) and q21_0 (target):")
print("    in:  q1_82={0}, q20_0={1}, q21_0={2}".format(q1_82,q20_0,tgt_before))
print("    out: q1_82={0}, q20_0={1}, q21_0={2}".format(q1_82,q20_0,q21_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_82 control2: q20_0 target: q21_0 ##
################################################################################
if 'q0_82' not in globals():
    q0_82=0
if 'q20_0' not in globals():
    q20_0=0
if 'q21_0' not in globals():
    q21_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq21_0' : 1, 'q21_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq21_0') : 4, ('anc1','q21_0') : -4, ('anc2', 'q0_82') : -2, ('anc2', 'q20_0') : -2, ('anc2', 'outq21_0') : -2, ('anc2', 'q21_0') : 2, ('q0_82', 'q20_0') : 1, ('outq21_0', 'q21_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_82']==q0_82 and sample['q20_0']==q20_0 and sample['q21_0']==q21_0 and int(energy)==0:
        q0_82=sample['q0_82']
        q20_0=sample['q20_0']
        q21_0=sample['outq21_0']
        tgt_before = sample['q21_0']
        break

print('#' * 80)
print("CCNOT operation on q0_82 (control1), q20_0 (control2) and q21_0 (target):")
print("    in:  q0_82={0}, q20_0={1}, q21_0={2}".format(q0_82,q20_0,tgt_before))
print("    out: q0_82={0}, q20_0={1}, q21_0={2}".format(q0_82,q20_0,q21_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q20_0 target: q21_0 ##
################################################################################
if 'q20_0' not in globals():
    q20_0=0
if 'q21_0' not in globals():
    q21_0=0

bqm = dimod.BinaryQuadraticModel({'q20_0' : 1, 'q21_0' : 1, 'outq21_0' : 1, 'anc' : 4}, {('q20_0', 'q21_0') : 2, ('q20_0', 'outq21_0') : -2, ('q21_0', 'outq21_0') : -2, ('q20_0', 'anc') : -4, ('q21_0', 'anc') : -4, ('outq21_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q20_0']==q20_0 and sample['q21_0']==q21_0 and int(energy)==0:
        q20_0=sample['q20_0']
        q21_0=sample['outq21_0']
        tgt_before = sample['q21_0']
        break

print('#' * 80)
print("CNOT operation on q20_0 (control) and q21_0 (target):")
print("    in:  q20_0={0}, q21_0={1}".format(q20_0,tgt_before))
print("    out: q20_0={0}, q21_0={1}".format(q20_0,q21_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_83 control2: q19_0 target: q20_0 ##
################################################################################
if 'q1_83' not in globals():
    q1_83=0
if 'q19_0' not in globals():
    q19_0=0
if 'q20_0' not in globals():
    q20_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq20_0' : 1, 'q20_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq20_0') : 4, ('anc1','q20_0') : -4, ('anc2', 'q1_83') : -2, ('anc2', 'q19_0') : -2, ('anc2', 'outq20_0') : -2, ('anc2', 'q20_0') : 2, ('q1_83', 'q19_0') : 1, ('outq20_0', 'q20_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_83']==q1_83 and sample['q19_0']==q19_0 and sample['q20_0']==q20_0 and int(energy)==0:
        q1_83=sample['q1_83']
        q19_0=sample['q19_0']
        q20_0=sample['outq20_0']
        tgt_before = sample['q20_0']
        break

print('#' * 80)
print("CCNOT operation on q1_83 (control1), q19_0 (control2) and q20_0 (target):")
print("    in:  q1_83={0}, q19_0={1}, q20_0={2}".format(q1_83,q19_0,tgt_before))
print("    out: q1_83={0}, q19_0={1}, q20_0={2}".format(q1_83,q19_0,q20_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_83 control2: q19_0 target: q20_0 ##
################################################################################
if 'q0_83' not in globals():
    q0_83=0
if 'q19_0' not in globals():
    q19_0=0
if 'q20_0' not in globals():
    q20_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq20_0' : 1, 'q20_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq20_0') : 4, ('anc1','q20_0') : -4, ('anc2', 'q0_83') : -2, ('anc2', 'q19_0') : -2, ('anc2', 'outq20_0') : -2, ('anc2', 'q20_0') : 2, ('q0_83', 'q19_0') : 1, ('outq20_0', 'q20_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_83']==q0_83 and sample['q19_0']==q19_0 and sample['q20_0']==q20_0 and int(energy)==0:
        q0_83=sample['q0_83']
        q19_0=sample['q19_0']
        q20_0=sample['outq20_0']
        tgt_before = sample['q20_0']
        break

print('#' * 80)
print("CCNOT operation on q0_83 (control1), q19_0 (control2) and q20_0 (target):")
print("    in:  q0_83={0}, q19_0={1}, q20_0={2}".format(q0_83,q19_0,tgt_before))
print("    out: q0_83={0}, q19_0={1}, q20_0={2}".format(q0_83,q19_0,q20_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q19_0 target: q20_0 ##
################################################################################
if 'q19_0' not in globals():
    q19_0=0
if 'q20_0' not in globals():
    q20_0=0

bqm = dimod.BinaryQuadraticModel({'q19_0' : 1, 'q20_0' : 1, 'outq20_0' : 1, 'anc' : 4}, {('q19_0', 'q20_0') : 2, ('q19_0', 'outq20_0') : -2, ('q20_0', 'outq20_0') : -2, ('q19_0', 'anc') : -4, ('q20_0', 'anc') : -4, ('outq20_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q19_0']==q19_0 and sample['q20_0']==q20_0 and int(energy)==0:
        q19_0=sample['q19_0']
        q20_0=sample['outq20_0']
        tgt_before = sample['q20_0']
        break

print('#' * 80)
print("CNOT operation on q19_0 (control) and q20_0 (target):")
print("    in:  q19_0={0}, q20_0={1}".format(q19_0,tgt_before))
print("    out: q19_0={0}, q20_0={1}".format(q19_0,q20_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_84 control2: q18_0 target: q19_0 ##
################################################################################
if 'q1_84' not in globals():
    q1_84=0
if 'q18_0' not in globals():
    q18_0=0
if 'q19_0' not in globals():
    q19_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq19_0' : 1, 'q19_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq19_0') : 4, ('anc1','q19_0') : -4, ('anc2', 'q1_84') : -2, ('anc2', 'q18_0') : -2, ('anc2', 'outq19_0') : -2, ('anc2', 'q19_0') : 2, ('q1_84', 'q18_0') : 1, ('outq19_0', 'q19_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_84']==q1_84 and sample['q18_0']==q18_0 and sample['q19_0']==q19_0 and int(energy)==0:
        q1_84=sample['q1_84']
        q18_0=sample['q18_0']
        q19_0=sample['outq19_0']
        tgt_before = sample['q19_0']
        break

print('#' * 80)
print("CCNOT operation on q1_84 (control1), q18_0 (control2) and q19_0 (target):")
print("    in:  q1_84={0}, q18_0={1}, q19_0={2}".format(q1_84,q18_0,tgt_before))
print("    out: q1_84={0}, q18_0={1}, q19_0={2}".format(q1_84,q18_0,q19_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_84 control2: q18_0 target: q19_0 ##
################################################################################
if 'q0_84' not in globals():
    q0_84=0
if 'q18_0' not in globals():
    q18_0=0
if 'q19_0' not in globals():
    q19_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq19_0' : 1, 'q19_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq19_0') : 4, ('anc1','q19_0') : -4, ('anc2', 'q0_84') : -2, ('anc2', 'q18_0') : -2, ('anc2', 'outq19_0') : -2, ('anc2', 'q19_0') : 2, ('q0_84', 'q18_0') : 1, ('outq19_0', 'q19_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_84']==q0_84 and sample['q18_0']==q18_0 and sample['q19_0']==q19_0 and int(energy)==0:
        q0_84=sample['q0_84']
        q18_0=sample['q18_0']
        q19_0=sample['outq19_0']
        tgt_before = sample['q19_0']
        break

print('#' * 80)
print("CCNOT operation on q0_84 (control1), q18_0 (control2) and q19_0 (target):")
print("    in:  q0_84={0}, q18_0={1}, q19_0={2}".format(q0_84,q18_0,tgt_before))
print("    out: q0_84={0}, q18_0={1}, q19_0={2}".format(q0_84,q18_0,q19_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q18_0 target: q19_0 ##
################################################################################
if 'q18_0' not in globals():
    q18_0=0
if 'q19_0' not in globals():
    q19_0=0

bqm = dimod.BinaryQuadraticModel({'q18_0' : 1, 'q19_0' : 1, 'outq19_0' : 1, 'anc' : 4}, {('q18_0', 'q19_0') : 2, ('q18_0', 'outq19_0') : -2, ('q19_0', 'outq19_0') : -2, ('q18_0', 'anc') : -4, ('q19_0', 'anc') : -4, ('outq19_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q18_0']==q18_0 and sample['q19_0']==q19_0 and int(energy)==0:
        q18_0=sample['q18_0']
        q19_0=sample['outq19_0']
        tgt_before = sample['q19_0']
        break

print('#' * 80)
print("CNOT operation on q18_0 (control) and q19_0 (target):")
print("    in:  q18_0={0}, q19_0={1}".format(q18_0,tgt_before))
print("    out: q18_0={0}, q19_0={1}".format(q18_0,q19_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_85 control2: q17_0 target: q18_0 ##
################################################################################
if 'q1_85' not in globals():
    q1_85=0
if 'q17_0' not in globals():
    q17_0=0
if 'q18_0' not in globals():
    q18_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq18_0' : 1, 'q18_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq18_0') : 4, ('anc1','q18_0') : -4, ('anc2', 'q1_85') : -2, ('anc2', 'q17_0') : -2, ('anc2', 'outq18_0') : -2, ('anc2', 'q18_0') : 2, ('q1_85', 'q17_0') : 1, ('outq18_0', 'q18_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_85']==q1_85 and sample['q17_0']==q17_0 and sample['q18_0']==q18_0 and int(energy)==0:
        q1_85=sample['q1_85']
        q17_0=sample['q17_0']
        q18_0=sample['outq18_0']
        tgt_before = sample['q18_0']
        break

print('#' * 80)
print("CCNOT operation on q1_85 (control1), q17_0 (control2) and q18_0 (target):")
print("    in:  q1_85={0}, q17_0={1}, q18_0={2}".format(q1_85,q17_0,tgt_before))
print("    out: q1_85={0}, q17_0={1}, q18_0={2}".format(q1_85,q17_0,q18_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_85 control2: q17_0 target: q18_0 ##
################################################################################
if 'q0_85' not in globals():
    q0_85=0
if 'q17_0' not in globals():
    q17_0=0
if 'q18_0' not in globals():
    q18_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq18_0' : 1, 'q18_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq18_0') : 4, ('anc1','q18_0') : -4, ('anc2', 'q0_85') : -2, ('anc2', 'q17_0') : -2, ('anc2', 'outq18_0') : -2, ('anc2', 'q18_0') : 2, ('q0_85', 'q17_0') : 1, ('outq18_0', 'q18_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_85']==q0_85 and sample['q17_0']==q17_0 and sample['q18_0']==q18_0 and int(energy)==0:
        q0_85=sample['q0_85']
        q17_0=sample['q17_0']
        q18_0=sample['outq18_0']
        tgt_before = sample['q18_0']
        break

print('#' * 80)
print("CCNOT operation on q0_85 (control1), q17_0 (control2) and q18_0 (target):")
print("    in:  q0_85={0}, q17_0={1}, q18_0={2}".format(q0_85,q17_0,tgt_before))
print("    out: q0_85={0}, q17_0={1}, q18_0={2}".format(q0_85,q17_0,q18_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q17_0 target: q18_0 ##
################################################################################
if 'q17_0' not in globals():
    q17_0=0
if 'q18_0' not in globals():
    q18_0=0

bqm = dimod.BinaryQuadraticModel({'q17_0' : 1, 'q18_0' : 1, 'outq18_0' : 1, 'anc' : 4}, {('q17_0', 'q18_0') : 2, ('q17_0', 'outq18_0') : -2, ('q18_0', 'outq18_0') : -2, ('q17_0', 'anc') : -4, ('q18_0', 'anc') : -4, ('outq18_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q17_0']==q17_0 and sample['q18_0']==q18_0 and int(energy)==0:
        q17_0=sample['q17_0']
        q18_0=sample['outq18_0']
        tgt_before = sample['q18_0']
        break

print('#' * 80)
print("CNOT operation on q17_0 (control) and q18_0 (target):")
print("    in:  q17_0={0}, q18_0={1}".format(q17_0,tgt_before))
print("    out: q17_0={0}, q18_0={1}".format(q17_0,q18_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_86 control2: q16_0 target: q17_0 ##
################################################################################
if 'q1_86' not in globals():
    q1_86=0
if 'q16_0' not in globals():
    q16_0=0
if 'q17_0' not in globals():
    q17_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq17_0' : 1, 'q17_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq17_0') : 4, ('anc1','q17_0') : -4, ('anc2', 'q1_86') : -2, ('anc2', 'q16_0') : -2, ('anc2', 'outq17_0') : -2, ('anc2', 'q17_0') : 2, ('q1_86', 'q16_0') : 1, ('outq17_0', 'q17_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_86']==q1_86 and sample['q16_0']==q16_0 and sample['q17_0']==q17_0 and int(energy)==0:
        q1_86=sample['q1_86']
        q16_0=sample['q16_0']
        q17_0=sample['outq17_0']
        tgt_before = sample['q17_0']
        break

print('#' * 80)
print("CCNOT operation on q1_86 (control1), q16_0 (control2) and q17_0 (target):")
print("    in:  q1_86={0}, q16_0={1}, q17_0={2}".format(q1_86,q16_0,tgt_before))
print("    out: q1_86={0}, q16_0={1}, q17_0={2}".format(q1_86,q16_0,q17_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_86 control2: q16_0 target: q17_0 ##
################################################################################
if 'q0_86' not in globals():
    q0_86=0
if 'q16_0' not in globals():
    q16_0=0
if 'q17_0' not in globals():
    q17_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq17_0' : 1, 'q17_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq17_0') : 4, ('anc1','q17_0') : -4, ('anc2', 'q0_86') : -2, ('anc2', 'q16_0') : -2, ('anc2', 'outq17_0') : -2, ('anc2', 'q17_0') : 2, ('q0_86', 'q16_0') : 1, ('outq17_0', 'q17_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_86']==q0_86 and sample['q16_0']==q16_0 and sample['q17_0']==q17_0 and int(energy)==0:
        q0_86=sample['q0_86']
        q16_0=sample['q16_0']
        q17_0=sample['outq17_0']
        tgt_before = sample['q17_0']
        break

print('#' * 80)
print("CCNOT operation on q0_86 (control1), q16_0 (control2) and q17_0 (target):")
print("    in:  q0_86={0}, q16_0={1}, q17_0={2}".format(q0_86,q16_0,tgt_before))
print("    out: q0_86={0}, q16_0={1}, q17_0={2}".format(q0_86,q16_0,q17_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q16_0 target: q17_0 ##
################################################################################
if 'q16_0' not in globals():
    q16_0=0
if 'q17_0' not in globals():
    q17_0=0

bqm = dimod.BinaryQuadraticModel({'q16_0' : 1, 'q17_0' : 1, 'outq17_0' : 1, 'anc' : 4}, {('q16_0', 'q17_0') : 2, ('q16_0', 'outq17_0') : -2, ('q17_0', 'outq17_0') : -2, ('q16_0', 'anc') : -4, ('q17_0', 'anc') : -4, ('outq17_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q16_0']==q16_0 and sample['q17_0']==q17_0 and int(energy)==0:
        q16_0=sample['q16_0']
        q17_0=sample['outq17_0']
        tgt_before = sample['q17_0']
        break

print('#' * 80)
print("CNOT operation on q16_0 (control) and q17_0 (target):")
print("    in:  q16_0={0}, q17_0={1}".format(q16_0,tgt_before))
print("    out: q16_0={0}, q17_0={1}".format(q16_0,q17_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_87 control2: q15_0 target: q16_0 ##
################################################################################
if 'q1_87' not in globals():
    q1_87=0
if 'q15_0' not in globals():
    q15_0=0
if 'q16_0' not in globals():
    q16_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq16_0' : 1, 'q16_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq16_0') : 4, ('anc1','q16_0') : -4, ('anc2', 'q1_87') : -2, ('anc2', 'q15_0') : -2, ('anc2', 'outq16_0') : -2, ('anc2', 'q16_0') : 2, ('q1_87', 'q15_0') : 1, ('outq16_0', 'q16_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_87']==q1_87 and sample['q15_0']==q15_0 and sample['q16_0']==q16_0 and int(energy)==0:
        q1_87=sample['q1_87']
        q15_0=sample['q15_0']
        q16_0=sample['outq16_0']
        tgt_before = sample['q16_0']
        break

print('#' * 80)
print("CCNOT operation on q1_87 (control1), q15_0 (control2) and q16_0 (target):")
print("    in:  q1_87={0}, q15_0={1}, q16_0={2}".format(q1_87,q15_0,tgt_before))
print("    out: q1_87={0}, q15_0={1}, q16_0={2}".format(q1_87,q15_0,q16_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_87 control2: q15_0 target: q16_0 ##
################################################################################
if 'q0_87' not in globals():
    q0_87=0
if 'q15_0' not in globals():
    q15_0=0
if 'q16_0' not in globals():
    q16_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq16_0' : 1, 'q16_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq16_0') : 4, ('anc1','q16_0') : -4, ('anc2', 'q0_87') : -2, ('anc2', 'q15_0') : -2, ('anc2', 'outq16_0') : -2, ('anc2', 'q16_0') : 2, ('q0_87', 'q15_0') : 1, ('outq16_0', 'q16_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_87']==q0_87 and sample['q15_0']==q15_0 and sample['q16_0']==q16_0 and int(energy)==0:
        q0_87=sample['q0_87']
        q15_0=sample['q15_0']
        q16_0=sample['outq16_0']
        tgt_before = sample['q16_0']
        break

print('#' * 80)
print("CCNOT operation on q0_87 (control1), q15_0 (control2) and q16_0 (target):")
print("    in:  q0_87={0}, q15_0={1}, q16_0={2}".format(q0_87,q15_0,tgt_before))
print("    out: q0_87={0}, q15_0={1}, q16_0={2}".format(q0_87,q15_0,q16_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q15_0 target: q16_0 ##
################################################################################
if 'q15_0' not in globals():
    q15_0=0
if 'q16_0' not in globals():
    q16_0=0

bqm = dimod.BinaryQuadraticModel({'q15_0' : 1, 'q16_0' : 1, 'outq16_0' : 1, 'anc' : 4}, {('q15_0', 'q16_0') : 2, ('q15_0', 'outq16_0') : -2, ('q16_0', 'outq16_0') : -2, ('q15_0', 'anc') : -4, ('q16_0', 'anc') : -4, ('outq16_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q15_0']==q15_0 and sample['q16_0']==q16_0 and int(energy)==0:
        q15_0=sample['q15_0']
        q16_0=sample['outq16_0']
        tgt_before = sample['q16_0']
        break

print('#' * 80)
print("CNOT operation on q15_0 (control) and q16_0 (target):")
print("    in:  q15_0={0}, q16_0={1}".format(q15_0,tgt_before))
print("    out: q15_0={0}, q16_0={1}".format(q15_0,q16_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_88 control2: q14_0 target: q15_0 ##
################################################################################
if 'q1_88' not in globals():
    q1_88=0
if 'q14_0' not in globals():
    q14_0=0
if 'q15_0' not in globals():
    q15_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq15_0' : 1, 'q15_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq15_0') : 4, ('anc1','q15_0') : -4, ('anc2', 'q1_88') : -2, ('anc2', 'q14_0') : -2, ('anc2', 'outq15_0') : -2, ('anc2', 'q15_0') : 2, ('q1_88', 'q14_0') : 1, ('outq15_0', 'q15_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_88']==q1_88 and sample['q14_0']==q14_0 and sample['q15_0']==q15_0 and int(energy)==0:
        q1_88=sample['q1_88']
        q14_0=sample['q14_0']
        q15_0=sample['outq15_0']
        tgt_before = sample['q15_0']
        break

print('#' * 80)
print("CCNOT operation on q1_88 (control1), q14_0 (control2) and q15_0 (target):")
print("    in:  q1_88={0}, q14_0={1}, q15_0={2}".format(q1_88,q14_0,tgt_before))
print("    out: q1_88={0}, q14_0={1}, q15_0={2}".format(q1_88,q14_0,q15_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_88 control2: q14_0 target: q15_0 ##
################################################################################
if 'q0_88' not in globals():
    q0_88=0
if 'q14_0' not in globals():
    q14_0=0
if 'q15_0' not in globals():
    q15_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq15_0' : 1, 'q15_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq15_0') : 4, ('anc1','q15_0') : -4, ('anc2', 'q0_88') : -2, ('anc2', 'q14_0') : -2, ('anc2', 'outq15_0') : -2, ('anc2', 'q15_0') : 2, ('q0_88', 'q14_0') : 1, ('outq15_0', 'q15_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_88']==q0_88 and sample['q14_0']==q14_0 and sample['q15_0']==q15_0 and int(energy)==0:
        q0_88=sample['q0_88']
        q14_0=sample['q14_0']
        q15_0=sample['outq15_0']
        tgt_before = sample['q15_0']
        break

print('#' * 80)
print("CCNOT operation on q0_88 (control1), q14_0 (control2) and q15_0 (target):")
print("    in:  q0_88={0}, q14_0={1}, q15_0={2}".format(q0_88,q14_0,tgt_before))
print("    out: q0_88={0}, q14_0={1}, q15_0={2}".format(q0_88,q14_0,q15_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q14_0 target: q15_0 ##
################################################################################
if 'q14_0' not in globals():
    q14_0=0
if 'q15_0' not in globals():
    q15_0=0

bqm = dimod.BinaryQuadraticModel({'q14_0' : 1, 'q15_0' : 1, 'outq15_0' : 1, 'anc' : 4}, {('q14_0', 'q15_0') : 2, ('q14_0', 'outq15_0') : -2, ('q15_0', 'outq15_0') : -2, ('q14_0', 'anc') : -4, ('q15_0', 'anc') : -4, ('outq15_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q14_0']==q14_0 and sample['q15_0']==q15_0 and int(energy)==0:
        q14_0=sample['q14_0']
        q15_0=sample['outq15_0']
        tgt_before = sample['q15_0']
        break

print('#' * 80)
print("CNOT operation on q14_0 (control) and q15_0 (target):")
print("    in:  q14_0={0}, q15_0={1}".format(q14_0,tgt_before))
print("    out: q14_0={0}, q15_0={1}".format(q14_0,q15_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_89 control2: q13_0 target: q14_0 ##
################################################################################
if 'q1_89' not in globals():
    q1_89=0
if 'q13_0' not in globals():
    q13_0=0
if 'q14_0' not in globals():
    q14_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq14_0' : 1, 'q14_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq14_0') : 4, ('anc1','q14_0') : -4, ('anc2', 'q1_89') : -2, ('anc2', 'q13_0') : -2, ('anc2', 'outq14_0') : -2, ('anc2', 'q14_0') : 2, ('q1_89', 'q13_0') : 1, ('outq14_0', 'q14_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_89']==q1_89 and sample['q13_0']==q13_0 and sample['q14_0']==q14_0 and int(energy)==0:
        q1_89=sample['q1_89']
        q13_0=sample['q13_0']
        q14_0=sample['outq14_0']
        tgt_before = sample['q14_0']
        break

print('#' * 80)
print("CCNOT operation on q1_89 (control1), q13_0 (control2) and q14_0 (target):")
print("    in:  q1_89={0}, q13_0={1}, q14_0={2}".format(q1_89,q13_0,tgt_before))
print("    out: q1_89={0}, q13_0={1}, q14_0={2}".format(q1_89,q13_0,q14_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_89 control2: q13_0 target: q14_0 ##
################################################################################
if 'q0_89' not in globals():
    q0_89=0
if 'q13_0' not in globals():
    q13_0=0
if 'q14_0' not in globals():
    q14_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq14_0' : 1, 'q14_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq14_0') : 4, ('anc1','q14_0') : -4, ('anc2', 'q0_89') : -2, ('anc2', 'q13_0') : -2, ('anc2', 'outq14_0') : -2, ('anc2', 'q14_0') : 2, ('q0_89', 'q13_0') : 1, ('outq14_0', 'q14_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_89']==q0_89 and sample['q13_0']==q13_0 and sample['q14_0']==q14_0 and int(energy)==0:
        q0_89=sample['q0_89']
        q13_0=sample['q13_0']
        q14_0=sample['outq14_0']
        tgt_before = sample['q14_0']
        break

print('#' * 80)
print("CCNOT operation on q0_89 (control1), q13_0 (control2) and q14_0 (target):")
print("    in:  q0_89={0}, q13_0={1}, q14_0={2}".format(q0_89,q13_0,tgt_before))
print("    out: q0_89={0}, q13_0={1}, q14_0={2}".format(q0_89,q13_0,q14_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q13_0 target: q14_0 ##
################################################################################
if 'q13_0' not in globals():
    q13_0=0
if 'q14_0' not in globals():
    q14_0=0

bqm = dimod.BinaryQuadraticModel({'q13_0' : 1, 'q14_0' : 1, 'outq14_0' : 1, 'anc' : 4}, {('q13_0', 'q14_0') : 2, ('q13_0', 'outq14_0') : -2, ('q14_0', 'outq14_0') : -2, ('q13_0', 'anc') : -4, ('q14_0', 'anc') : -4, ('outq14_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q13_0']==q13_0 and sample['q14_0']==q14_0 and int(energy)==0:
        q13_0=sample['q13_0']
        q14_0=sample['outq14_0']
        tgt_before = sample['q14_0']
        break

print('#' * 80)
print("CNOT operation on q13_0 (control) and q14_0 (target):")
print("    in:  q13_0={0}, q14_0={1}".format(q13_0,tgt_before))
print("    out: q13_0={0}, q14_0={1}".format(q13_0,q14_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_90 control2: q12_0 target: q13_0 ##
################################################################################
if 'q1_90' not in globals():
    q1_90=0
if 'q12_0' not in globals():
    q12_0=0
if 'q13_0' not in globals():
    q13_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq13_0' : 1, 'q13_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq13_0') : 4, ('anc1','q13_0') : -4, ('anc2', 'q1_90') : -2, ('anc2', 'q12_0') : -2, ('anc2', 'outq13_0') : -2, ('anc2', 'q13_0') : 2, ('q1_90', 'q12_0') : 1, ('outq13_0', 'q13_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_90']==q1_90 and sample['q12_0']==q12_0 and sample['q13_0']==q13_0 and int(energy)==0:
        q1_90=sample['q1_90']
        q12_0=sample['q12_0']
        q13_0=sample['outq13_0']
        tgt_before = sample['q13_0']
        break

print('#' * 80)
print("CCNOT operation on q1_90 (control1), q12_0 (control2) and q13_0 (target):")
print("    in:  q1_90={0}, q12_0={1}, q13_0={2}".format(q1_90,q12_0,tgt_before))
print("    out: q1_90={0}, q12_0={1}, q13_0={2}".format(q1_90,q12_0,q13_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_90 control2: q12_0 target: q13_0 ##
################################################################################
if 'q0_90' not in globals():
    q0_90=0
if 'q12_0' not in globals():
    q12_0=0
if 'q13_0' not in globals():
    q13_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq13_0' : 1, 'q13_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq13_0') : 4, ('anc1','q13_0') : -4, ('anc2', 'q0_90') : -2, ('anc2', 'q12_0') : -2, ('anc2', 'outq13_0') : -2, ('anc2', 'q13_0') : 2, ('q0_90', 'q12_0') : 1, ('outq13_0', 'q13_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_90']==q0_90 and sample['q12_0']==q12_0 and sample['q13_0']==q13_0 and int(energy)==0:
        q0_90=sample['q0_90']
        q12_0=sample['q12_0']
        q13_0=sample['outq13_0']
        tgt_before = sample['q13_0']
        break

print('#' * 80)
print("CCNOT operation on q0_90 (control1), q12_0 (control2) and q13_0 (target):")
print("    in:  q0_90={0}, q12_0={1}, q13_0={2}".format(q0_90,q12_0,tgt_before))
print("    out: q0_90={0}, q12_0={1}, q13_0={2}".format(q0_90,q12_0,q13_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q12_0 target: q13_0 ##
################################################################################
if 'q12_0' not in globals():
    q12_0=0
if 'q13_0' not in globals():
    q13_0=0

bqm = dimod.BinaryQuadraticModel({'q12_0' : 1, 'q13_0' : 1, 'outq13_0' : 1, 'anc' : 4}, {('q12_0', 'q13_0') : 2, ('q12_0', 'outq13_0') : -2, ('q13_0', 'outq13_0') : -2, ('q12_0', 'anc') : -4, ('q13_0', 'anc') : -4, ('outq13_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q12_0']==q12_0 and sample['q13_0']==q13_0 and int(energy)==0:
        q12_0=sample['q12_0']
        q13_0=sample['outq13_0']
        tgt_before = sample['q13_0']
        break

print('#' * 80)
print("CNOT operation on q12_0 (control) and q13_0 (target):")
print("    in:  q12_0={0}, q13_0={1}".format(q12_0,tgt_before))
print("    out: q12_0={0}, q13_0={1}".format(q12_0,q13_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_91 control2: q11_0 target: q12_0 ##
################################################################################
if 'q1_91' not in globals():
    q1_91=0
if 'q11_0' not in globals():
    q11_0=0
if 'q12_0' not in globals():
    q12_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq12_0' : 1, 'q12_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq12_0') : 4, ('anc1','q12_0') : -4, ('anc2', 'q1_91') : -2, ('anc2', 'q11_0') : -2, ('anc2', 'outq12_0') : -2, ('anc2', 'q12_0') : 2, ('q1_91', 'q11_0') : 1, ('outq12_0', 'q12_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_91']==q1_91 and sample['q11_0']==q11_0 and sample['q12_0']==q12_0 and int(energy)==0:
        q1_91=sample['q1_91']
        q11_0=sample['q11_0']
        q12_0=sample['outq12_0']
        tgt_before = sample['q12_0']
        break

print('#' * 80)
print("CCNOT operation on q1_91 (control1), q11_0 (control2) and q12_0 (target):")
print("    in:  q1_91={0}, q11_0={1}, q12_0={2}".format(q1_91,q11_0,tgt_before))
print("    out: q1_91={0}, q11_0={1}, q12_0={2}".format(q1_91,q11_0,q12_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_91 control2: q11_0 target: q12_0 ##
################################################################################
if 'q0_91' not in globals():
    q0_91=0
if 'q11_0' not in globals():
    q11_0=0
if 'q12_0' not in globals():
    q12_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq12_0' : 1, 'q12_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq12_0') : 4, ('anc1','q12_0') : -4, ('anc2', 'q0_91') : -2, ('anc2', 'q11_0') : -2, ('anc2', 'outq12_0') : -2, ('anc2', 'q12_0') : 2, ('q0_91', 'q11_0') : 1, ('outq12_0', 'q12_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_91']==q0_91 and sample['q11_0']==q11_0 and sample['q12_0']==q12_0 and int(energy)==0:
        q0_91=sample['q0_91']
        q11_0=sample['q11_0']
        q12_0=sample['outq12_0']
        tgt_before = sample['q12_0']
        break

print('#' * 80)
print("CCNOT operation on q0_91 (control1), q11_0 (control2) and q12_0 (target):")
print("    in:  q0_91={0}, q11_0={1}, q12_0={2}".format(q0_91,q11_0,tgt_before))
print("    out: q0_91={0}, q11_0={1}, q12_0={2}".format(q0_91,q11_0,q12_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q11_0 target: q12_0 ##
################################################################################
if 'q11_0' not in globals():
    q11_0=0
if 'q12_0' not in globals():
    q12_0=0

bqm = dimod.BinaryQuadraticModel({'q11_0' : 1, 'q12_0' : 1, 'outq12_0' : 1, 'anc' : 4}, {('q11_0', 'q12_0') : 2, ('q11_0', 'outq12_0') : -2, ('q12_0', 'outq12_0') : -2, ('q11_0', 'anc') : -4, ('q12_0', 'anc') : -4, ('outq12_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q11_0']==q11_0 and sample['q12_0']==q12_0 and int(energy)==0:
        q11_0=sample['q11_0']
        q12_0=sample['outq12_0']
        tgt_before = sample['q12_0']
        break

print('#' * 80)
print("CNOT operation on q11_0 (control) and q12_0 (target):")
print("    in:  q11_0={0}, q12_0={1}".format(q11_0,tgt_before))
print("    out: q11_0={0}, q12_0={1}".format(q11_0,q12_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_92 control2: q10_0 target: q11_0 ##
################################################################################
if 'q1_92' not in globals():
    q1_92=0
if 'q10_0' not in globals():
    q10_0=0
if 'q11_0' not in globals():
    q11_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq11_0' : 1, 'q11_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq11_0') : 4, ('anc1','q11_0') : -4, ('anc2', 'q1_92') : -2, ('anc2', 'q10_0') : -2, ('anc2', 'outq11_0') : -2, ('anc2', 'q11_0') : 2, ('q1_92', 'q10_0') : 1, ('outq11_0', 'q11_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_92']==q1_92 and sample['q10_0']==q10_0 and sample['q11_0']==q11_0 and int(energy)==0:
        q1_92=sample['q1_92']
        q10_0=sample['q10_0']
        q11_0=sample['outq11_0']
        tgt_before = sample['q11_0']
        break

print('#' * 80)
print("CCNOT operation on q1_92 (control1), q10_0 (control2) and q11_0 (target):")
print("    in:  q1_92={0}, q10_0={1}, q11_0={2}".format(q1_92,q10_0,tgt_before))
print("    out: q1_92={0}, q10_0={1}, q11_0={2}".format(q1_92,q10_0,q11_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_92 control2: q10_0 target: q11_0 ##
################################################################################
if 'q0_92' not in globals():
    q0_92=0
if 'q10_0' not in globals():
    q10_0=0
if 'q11_0' not in globals():
    q11_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq11_0' : 1, 'q11_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq11_0') : 4, ('anc1','q11_0') : -4, ('anc2', 'q0_92') : -2, ('anc2', 'q10_0') : -2, ('anc2', 'outq11_0') : -2, ('anc2', 'q11_0') : 2, ('q0_92', 'q10_0') : 1, ('outq11_0', 'q11_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_92']==q0_92 and sample['q10_0']==q10_0 and sample['q11_0']==q11_0 and int(energy)==0:
        q0_92=sample['q0_92']
        q10_0=sample['q10_0']
        q11_0=sample['outq11_0']
        tgt_before = sample['q11_0']
        break

print('#' * 80)
print("CCNOT operation on q0_92 (control1), q10_0 (control2) and q11_0 (target):")
print("    in:  q0_92={0}, q10_0={1}, q11_0={2}".format(q0_92,q10_0,tgt_before))
print("    out: q0_92={0}, q10_0={1}, q11_0={2}".format(q0_92,q10_0,q11_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q10_0 target: q11_0 ##
################################################################################
if 'q10_0' not in globals():
    q10_0=0
if 'q11_0' not in globals():
    q11_0=0

bqm = dimod.BinaryQuadraticModel({'q10_0' : 1, 'q11_0' : 1, 'outq11_0' : 1, 'anc' : 4}, {('q10_0', 'q11_0') : 2, ('q10_0', 'outq11_0') : -2, ('q11_0', 'outq11_0') : -2, ('q10_0', 'anc') : -4, ('q11_0', 'anc') : -4, ('outq11_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q10_0']==q10_0 and sample['q11_0']==q11_0 and int(energy)==0:
        q10_0=sample['q10_0']
        q11_0=sample['outq11_0']
        tgt_before = sample['q11_0']
        break

print('#' * 80)
print("CNOT operation on q10_0 (control) and q11_0 (target):")
print("    in:  q10_0={0}, q11_0={1}".format(q10_0,tgt_before))
print("    out: q10_0={0}, q11_0={1}".format(q10_0,q11_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_93 control2: q9_0 target: q10_0 ##
################################################################################
if 'q1_93' not in globals():
    q1_93=0
if 'q9_0' not in globals():
    q9_0=0
if 'q10_0' not in globals():
    q10_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq10_0' : 1, 'q10_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq10_0') : 4, ('anc1','q10_0') : -4, ('anc2', 'q1_93') : -2, ('anc2', 'q9_0') : -2, ('anc2', 'outq10_0') : -2, ('anc2', 'q10_0') : 2, ('q1_93', 'q9_0') : 1, ('outq10_0', 'q10_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_93']==q1_93 and sample['q9_0']==q9_0 and sample['q10_0']==q10_0 and int(energy)==0:
        q1_93=sample['q1_93']
        q9_0=sample['q9_0']
        q10_0=sample['outq10_0']
        tgt_before = sample['q10_0']
        break

print('#' * 80)
print("CCNOT operation on q1_93 (control1), q9_0 (control2) and q10_0 (target):")
print("    in:  q1_93={0}, q9_0={1}, q10_0={2}".format(q1_93,q9_0,tgt_before))
print("    out: q1_93={0}, q9_0={1}, q10_0={2}".format(q1_93,q9_0,q10_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_93 control2: q9_0 target: q10_0 ##
################################################################################
if 'q0_93' not in globals():
    q0_93=0
if 'q9_0' not in globals():
    q9_0=0
if 'q10_0' not in globals():
    q10_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq10_0' : 1, 'q10_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq10_0') : 4, ('anc1','q10_0') : -4, ('anc2', 'q0_93') : -2, ('anc2', 'q9_0') : -2, ('anc2', 'outq10_0') : -2, ('anc2', 'q10_0') : 2, ('q0_93', 'q9_0') : 1, ('outq10_0', 'q10_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_93']==q0_93 and sample['q9_0']==q9_0 and sample['q10_0']==q10_0 and int(energy)==0:
        q0_93=sample['q0_93']
        q9_0=sample['q9_0']
        q10_0=sample['outq10_0']
        tgt_before = sample['q10_0']
        break

print('#' * 80)
print("CCNOT operation on q0_93 (control1), q9_0 (control2) and q10_0 (target):")
print("    in:  q0_93={0}, q9_0={1}, q10_0={2}".format(q0_93,q9_0,tgt_before))
print("    out: q0_93={0}, q9_0={1}, q10_0={2}".format(q0_93,q9_0,q10_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q9_0 target: q10_0 ##
################################################################################
if 'q9_0' not in globals():
    q9_0=0
if 'q10_0' not in globals():
    q10_0=0

bqm = dimod.BinaryQuadraticModel({'q9_0' : 1, 'q10_0' : 1, 'outq10_0' : 1, 'anc' : 4}, {('q9_0', 'q10_0') : 2, ('q9_0', 'outq10_0') : -2, ('q10_0', 'outq10_0') : -2, ('q9_0', 'anc') : -4, ('q10_0', 'anc') : -4, ('outq10_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q9_0']==q9_0 and sample['q10_0']==q10_0 and int(energy)==0:
        q9_0=sample['q9_0']
        q10_0=sample['outq10_0']
        tgt_before = sample['q10_0']
        break

print('#' * 80)
print("CNOT operation on q9_0 (control) and q10_0 (target):")
print("    in:  q9_0={0}, q10_0={1}".format(q9_0,tgt_before))
print("    out: q9_0={0}, q10_0={1}".format(q9_0,q10_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_94 control2: q8_0 target: q9_0 ##
################################################################################
if 'q1_94' not in globals():
    q1_94=0
if 'q8_0' not in globals():
    q8_0=0
if 'q9_0' not in globals():
    q9_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq9_0' : 1, 'q9_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq9_0') : 4, ('anc1','q9_0') : -4, ('anc2', 'q1_94') : -2, ('anc2', 'q8_0') : -2, ('anc2', 'outq9_0') : -2, ('anc2', 'q9_0') : 2, ('q1_94', 'q8_0') : 1, ('outq9_0', 'q9_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_94']==q1_94 and sample['q8_0']==q8_0 and sample['q9_0']==q9_0 and int(energy)==0:
        q1_94=sample['q1_94']
        q8_0=sample['q8_0']
        q9_0=sample['outq9_0']
        tgt_before = sample['q9_0']
        break

print('#' * 80)
print("CCNOT operation on q1_94 (control1), q8_0 (control2) and q9_0 (target):")
print("    in:  q1_94={0}, q8_0={1}, q9_0={2}".format(q1_94,q8_0,tgt_before))
print("    out: q1_94={0}, q8_0={1}, q9_0={2}".format(q1_94,q8_0,q9_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_94 control2: q8_0 target: q9_0 ##
################################################################################
if 'q0_94' not in globals():
    q0_94=0
if 'q8_0' not in globals():
    q8_0=0
if 'q9_0' not in globals():
    q9_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq9_0' : 1, 'q9_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq9_0') : 4, ('anc1','q9_0') : -4, ('anc2', 'q0_94') : -2, ('anc2', 'q8_0') : -2, ('anc2', 'outq9_0') : -2, ('anc2', 'q9_0') : 2, ('q0_94', 'q8_0') : 1, ('outq9_0', 'q9_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_94']==q0_94 and sample['q8_0']==q8_0 and sample['q9_0']==q9_0 and int(energy)==0:
        q0_94=sample['q0_94']
        q8_0=sample['q8_0']
        q9_0=sample['outq9_0']
        tgt_before = sample['q9_0']
        break

print('#' * 80)
print("CCNOT operation on q0_94 (control1), q8_0 (control2) and q9_0 (target):")
print("    in:  q0_94={0}, q8_0={1}, q9_0={2}".format(q0_94,q8_0,tgt_before))
print("    out: q0_94={0}, q8_0={1}, q9_0={2}".format(q0_94,q8_0,q9_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q8_0 target: q9_0 ##
################################################################################
if 'q8_0' not in globals():
    q8_0=0
if 'q9_0' not in globals():
    q9_0=0

bqm = dimod.BinaryQuadraticModel({'q8_0' : 1, 'q9_0' : 1, 'outq9_0' : 1, 'anc' : 4}, {('q8_0', 'q9_0') : 2, ('q8_0', 'outq9_0') : -2, ('q9_0', 'outq9_0') : -2, ('q8_0', 'anc') : -4, ('q9_0', 'anc') : -4, ('outq9_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q8_0']==q8_0 and sample['q9_0']==q9_0 and int(energy)==0:
        q8_0=sample['q8_0']
        q9_0=sample['outq9_0']
        tgt_before = sample['q9_0']
        break

print('#' * 80)
print("CNOT operation on q8_0 (control) and q9_0 (target):")
print("    in:  q8_0={0}, q9_0={1}".format(q8_0,tgt_before))
print("    out: q8_0={0}, q9_0={1}".format(q8_0,q9_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_95 control2: q7_0 target: q8_0 ##
################################################################################
if 'q1_95' not in globals():
    q1_95=0
if 'q7_0' not in globals():
    q7_0=0
if 'q8_0' not in globals():
    q8_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq8_0' : 1, 'q8_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq8_0') : 4, ('anc1','q8_0') : -4, ('anc2', 'q1_95') : -2, ('anc2', 'q7_0') : -2, ('anc2', 'outq8_0') : -2, ('anc2', 'q8_0') : 2, ('q1_95', 'q7_0') : 1, ('outq8_0', 'q8_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_95']==q1_95 and sample['q7_0']==q7_0 and sample['q8_0']==q8_0 and int(energy)==0:
        q1_95=sample['q1_95']
        q7_0=sample['q7_0']
        q8_0=sample['outq8_0']
        tgt_before = sample['q8_0']
        break

print('#' * 80)
print("CCNOT operation on q1_95 (control1), q7_0 (control2) and q8_0 (target):")
print("    in:  q1_95={0}, q7_0={1}, q8_0={2}".format(q1_95,q7_0,tgt_before))
print("    out: q1_95={0}, q7_0={1}, q8_0={2}".format(q1_95,q7_0,q8_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_95 control2: q7_0 target: q8_0 ##
################################################################################
if 'q0_95' not in globals():
    q0_95=0
if 'q7_0' not in globals():
    q7_0=0
if 'q8_0' not in globals():
    q8_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq8_0' : 1, 'q8_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq8_0') : 4, ('anc1','q8_0') : -4, ('anc2', 'q0_95') : -2, ('anc2', 'q7_0') : -2, ('anc2', 'outq8_0') : -2, ('anc2', 'q8_0') : 2, ('q0_95', 'q7_0') : 1, ('outq8_0', 'q8_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_95']==q0_95 and sample['q7_0']==q7_0 and sample['q8_0']==q8_0 and int(energy)==0:
        q0_95=sample['q0_95']
        q7_0=sample['q7_0']
        q8_0=sample['outq8_0']
        tgt_before = sample['q8_0']
        break

print('#' * 80)
print("CCNOT operation on q0_95 (control1), q7_0 (control2) and q8_0 (target):")
print("    in:  q0_95={0}, q7_0={1}, q8_0={2}".format(q0_95,q7_0,tgt_before))
print("    out: q0_95={0}, q7_0={1}, q8_0={2}".format(q0_95,q7_0,q8_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q7_0 target: q8_0 ##
################################################################################
if 'q7_0' not in globals():
    q7_0=0
if 'q8_0' not in globals():
    q8_0=0

bqm = dimod.BinaryQuadraticModel({'q7_0' : 1, 'q8_0' : 1, 'outq8_0' : 1, 'anc' : 4}, {('q7_0', 'q8_0') : 2, ('q7_0', 'outq8_0') : -2, ('q8_0', 'outq8_0') : -2, ('q7_0', 'anc') : -4, ('q8_0', 'anc') : -4, ('outq8_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q7_0']==q7_0 and sample['q8_0']==q8_0 and int(energy)==0:
        q7_0=sample['q7_0']
        q8_0=sample['outq8_0']
        tgt_before = sample['q8_0']
        break

print('#' * 80)
print("CNOT operation on q7_0 (control) and q8_0 (target):")
print("    in:  q7_0={0}, q8_0={1}".format(q7_0,tgt_before))
print("    out: q7_0={0}, q8_0={1}".format(q7_0,q8_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_96 control2: q6_0 target: q7_0 ##
################################################################################
if 'q1_96' not in globals():
    q1_96=0
if 'q6_0' not in globals():
    q6_0=0
if 'q7_0' not in globals():
    q7_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq7_0' : 1, 'q7_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq7_0') : 4, ('anc1','q7_0') : -4, ('anc2', 'q1_96') : -2, ('anc2', 'q6_0') : -2, ('anc2', 'outq7_0') : -2, ('anc2', 'q7_0') : 2, ('q1_96', 'q6_0') : 1, ('outq7_0', 'q7_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_96']==q1_96 and sample['q6_0']==q6_0 and sample['q7_0']==q7_0 and int(energy)==0:
        q1_96=sample['q1_96']
        q6_0=sample['q6_0']
        q7_0=sample['outq7_0']
        tgt_before = sample['q7_0']
        break

print('#' * 80)
print("CCNOT operation on q1_96 (control1), q6_0 (control2) and q7_0 (target):")
print("    in:  q1_96={0}, q6_0={1}, q7_0={2}".format(q1_96,q6_0,tgt_before))
print("    out: q1_96={0}, q6_0={1}, q7_0={2}".format(q1_96,q6_0,q7_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_96 control2: q6_0 target: q7_0 ##
################################################################################
if 'q0_96' not in globals():
    q0_96=0
if 'q6_0' not in globals():
    q6_0=0
if 'q7_0' not in globals():
    q7_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq7_0' : 1, 'q7_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq7_0') : 4, ('anc1','q7_0') : -4, ('anc2', 'q0_96') : -2, ('anc2', 'q6_0') : -2, ('anc2', 'outq7_0') : -2, ('anc2', 'q7_0') : 2, ('q0_96', 'q6_0') : 1, ('outq7_0', 'q7_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_96']==q0_96 and sample['q6_0']==q6_0 and sample['q7_0']==q7_0 and int(energy)==0:
        q0_96=sample['q0_96']
        q6_0=sample['q6_0']
        q7_0=sample['outq7_0']
        tgt_before = sample['q7_0']
        break

print('#' * 80)
print("CCNOT operation on q0_96 (control1), q6_0 (control2) and q7_0 (target):")
print("    in:  q0_96={0}, q6_0={1}, q7_0={2}".format(q0_96,q6_0,tgt_before))
print("    out: q0_96={0}, q6_0={1}, q7_0={2}".format(q0_96,q6_0,q7_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q6_0 target: q7_0 ##
################################################################################
if 'q6_0' not in globals():
    q6_0=0
if 'q7_0' not in globals():
    q7_0=0

bqm = dimod.BinaryQuadraticModel({'q6_0' : 1, 'q7_0' : 1, 'outq7_0' : 1, 'anc' : 4}, {('q6_0', 'q7_0') : 2, ('q6_0', 'outq7_0') : -2, ('q7_0', 'outq7_0') : -2, ('q6_0', 'anc') : -4, ('q7_0', 'anc') : -4, ('outq7_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q6_0']==q6_0 and sample['q7_0']==q7_0 and int(energy)==0:
        q6_0=sample['q6_0']
        q7_0=sample['outq7_0']
        tgt_before = sample['q7_0']
        break

print('#' * 80)
print("CNOT operation on q6_0 (control) and q7_0 (target):")
print("    in:  q6_0={0}, q7_0={1}".format(q6_0,tgt_before))
print("    out: q6_0={0}, q7_0={1}".format(q6_0,q7_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_97 control2: q5_0 target: q6_0 ##
################################################################################
if 'q1_97' not in globals():
    q1_97=0
if 'q5_0' not in globals():
    q5_0=0
if 'q6_0' not in globals():
    q6_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq6_0' : 1, 'q6_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq6_0') : 4, ('anc1','q6_0') : -4, ('anc2', 'q1_97') : -2, ('anc2', 'q5_0') : -2, ('anc2', 'outq6_0') : -2, ('anc2', 'q6_0') : 2, ('q1_97', 'q5_0') : 1, ('outq6_0', 'q6_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_97']==q1_97 and sample['q5_0']==q5_0 and sample['q6_0']==q6_0 and int(energy)==0:
        q1_97=sample['q1_97']
        q5_0=sample['q5_0']
        q6_0=sample['outq6_0']
        tgt_before = sample['q6_0']
        break

print('#' * 80)
print("CCNOT operation on q1_97 (control1), q5_0 (control2) and q6_0 (target):")
print("    in:  q1_97={0}, q5_0={1}, q6_0={2}".format(q1_97,q5_0,tgt_before))
print("    out: q1_97={0}, q5_0={1}, q6_0={2}".format(q1_97,q5_0,q6_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_97 control2: q5_0 target: q6_0 ##
################################################################################
if 'q0_97' not in globals():
    q0_97=0
if 'q5_0' not in globals():
    q5_0=0
if 'q6_0' not in globals():
    q6_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq6_0' : 1, 'q6_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq6_0') : 4, ('anc1','q6_0') : -4, ('anc2', 'q0_97') : -2, ('anc2', 'q5_0') : -2, ('anc2', 'outq6_0') : -2, ('anc2', 'q6_0') : 2, ('q0_97', 'q5_0') : 1, ('outq6_0', 'q6_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_97']==q0_97 and sample['q5_0']==q5_0 and sample['q6_0']==q6_0 and int(energy)==0:
        q0_97=sample['q0_97']
        q5_0=sample['q5_0']
        q6_0=sample['outq6_0']
        tgt_before = sample['q6_0']
        break

print('#' * 80)
print("CCNOT operation on q0_97 (control1), q5_0 (control2) and q6_0 (target):")
print("    in:  q0_97={0}, q5_0={1}, q6_0={2}".format(q0_97,q5_0,tgt_before))
print("    out: q0_97={0}, q5_0={1}, q6_0={2}".format(q0_97,q5_0,q6_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q5_0 target: q6_0 ##
################################################################################
if 'q5_0' not in globals():
    q5_0=0
if 'q6_0' not in globals():
    q6_0=0

bqm = dimod.BinaryQuadraticModel({'q5_0' : 1, 'q6_0' : 1, 'outq6_0' : 1, 'anc' : 4}, {('q5_0', 'q6_0') : 2, ('q5_0', 'outq6_0') : -2, ('q6_0', 'outq6_0') : -2, ('q5_0', 'anc') : -4, ('q6_0', 'anc') : -4, ('outq6_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q5_0']==q5_0 and sample['q6_0']==q6_0 and int(energy)==0:
        q5_0=sample['q5_0']
        q6_0=sample['outq6_0']
        tgt_before = sample['q6_0']
        break

print('#' * 80)
print("CNOT operation on q5_0 (control) and q6_0 (target):")
print("    in:  q5_0={0}, q6_0={1}".format(q5_0,tgt_before))
print("    out: q5_0={0}, q6_0={1}".format(q5_0,q6_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_98 control2: q4_0 target: q5_0 ##
################################################################################
if 'q1_98' not in globals():
    q1_98=0
if 'q4_0' not in globals():
    q4_0=0
if 'q5_0' not in globals():
    q5_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq5_0' : 1, 'q5_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq5_0') : 4, ('anc1','q5_0') : -4, ('anc2', 'q1_98') : -2, ('anc2', 'q4_0') : -2, ('anc2', 'outq5_0') : -2, ('anc2', 'q5_0') : 2, ('q1_98', 'q4_0') : 1, ('outq5_0', 'q5_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_98']==q1_98 and sample['q4_0']==q4_0 and sample['q5_0']==q5_0 and int(energy)==0:
        q1_98=sample['q1_98']
        q4_0=sample['q4_0']
        q5_0=sample['outq5_0']
        tgt_before = sample['q5_0']
        break

print('#' * 80)
print("CCNOT operation on q1_98 (control1), q4_0 (control2) and q5_0 (target):")
print("    in:  q1_98={0}, q4_0={1}, q5_0={2}".format(q1_98,q4_0,tgt_before))
print("    out: q1_98={0}, q4_0={1}, q5_0={2}".format(q1_98,q4_0,q5_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_98 control2: q4_0 target: q5_0 ##
################################################################################
if 'q0_98' not in globals():
    q0_98=0
if 'q4_0' not in globals():
    q4_0=0
if 'q5_0' not in globals():
    q5_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq5_0' : 1, 'q5_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq5_0') : 4, ('anc1','q5_0') : -4, ('anc2', 'q0_98') : -2, ('anc2', 'q4_0') : -2, ('anc2', 'outq5_0') : -2, ('anc2', 'q5_0') : 2, ('q0_98', 'q4_0') : 1, ('outq5_0', 'q5_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_98']==q0_98 and sample['q4_0']==q4_0 and sample['q5_0']==q5_0 and int(energy)==0:
        q0_98=sample['q0_98']
        q4_0=sample['q4_0']
        q5_0=sample['outq5_0']
        tgt_before = sample['q5_0']
        break

print('#' * 80)
print("CCNOT operation on q0_98 (control1), q4_0 (control2) and q5_0 (target):")
print("    in:  q0_98={0}, q4_0={1}, q5_0={2}".format(q0_98,q4_0,tgt_before))
print("    out: q0_98={0}, q4_0={1}, q5_0={2}".format(q0_98,q4_0,q5_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q4_0 target: q5_0 ##
################################################################################
if 'q4_0' not in globals():
    q4_0=0
if 'q5_0' not in globals():
    q5_0=0

bqm = dimod.BinaryQuadraticModel({'q4_0' : 1, 'q5_0' : 1, 'outq5_0' : 1, 'anc' : 4}, {('q4_0', 'q5_0') : 2, ('q4_0', 'outq5_0') : -2, ('q5_0', 'outq5_0') : -2, ('q4_0', 'anc') : -4, ('q5_0', 'anc') : -4, ('outq5_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q4_0']==q4_0 and sample['q5_0']==q5_0 and int(energy)==0:
        q4_0=sample['q4_0']
        q5_0=sample['outq5_0']
        tgt_before = sample['q5_0']
        break

print('#' * 80)
print("CNOT operation on q4_0 (control) and q5_0 (target):")
print("    in:  q4_0={0}, q5_0={1}".format(q4_0,tgt_before))
print("    out: q4_0={0}, q5_0={1}".format(q4_0,q5_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_99 control2: q3_0 target: q4_0 ##
################################################################################
if 'q1_99' not in globals():
    q1_99=0
if 'q3_0' not in globals():
    q3_0=0
if 'q4_0' not in globals():
    q4_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq4_0' : 1, 'q4_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq4_0') : 4, ('anc1','q4_0') : -4, ('anc2', 'q1_99') : -2, ('anc2', 'q3_0') : -2, ('anc2', 'outq4_0') : -2, ('anc2', 'q4_0') : 2, ('q1_99', 'q3_0') : 1, ('outq4_0', 'q4_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_99']==q1_99 and sample['q3_0']==q3_0 and sample['q4_0']==q4_0 and int(energy)==0:
        q1_99=sample['q1_99']
        q3_0=sample['q3_0']
        q4_0=sample['outq4_0']
        tgt_before = sample['q4_0']
        break

print('#' * 80)
print("CCNOT operation on q1_99 (control1), q3_0 (control2) and q4_0 (target):")
print("    in:  q1_99={0}, q3_0={1}, q4_0={2}".format(q1_99,q3_0,tgt_before))
print("    out: q1_99={0}, q3_0={1}, q4_0={2}".format(q1_99,q3_0,q4_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_99 control2: q3_0 target: q4_0 ##
################################################################################
if 'q0_99' not in globals():
    q0_99=0
if 'q3_0' not in globals():
    q3_0=0
if 'q4_0' not in globals():
    q4_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq4_0' : 1, 'q4_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq4_0') : 4, ('anc1','q4_0') : -4, ('anc2', 'q0_99') : -2, ('anc2', 'q3_0') : -2, ('anc2', 'outq4_0') : -2, ('anc2', 'q4_0') : 2, ('q0_99', 'q3_0') : 1, ('outq4_0', 'q4_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_99']==q0_99 and sample['q3_0']==q3_0 and sample['q4_0']==q4_0 and int(energy)==0:
        q0_99=sample['q0_99']
        q3_0=sample['q3_0']
        q4_0=sample['outq4_0']
        tgt_before = sample['q4_0']
        break

print('#' * 80)
print("CCNOT operation on q0_99 (control1), q3_0 (control2) and q4_0 (target):")
print("    in:  q0_99={0}, q3_0={1}, q4_0={2}".format(q0_99,q3_0,tgt_before))
print("    out: q0_99={0}, q3_0={1}, q4_0={2}".format(q0_99,q3_0,q4_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q3_0 target: q4_0 ##
################################################################################
if 'q3_0' not in globals():
    q3_0=0
if 'q4_0' not in globals():
    q4_0=0

bqm = dimod.BinaryQuadraticModel({'q3_0' : 1, 'q4_0' : 1, 'outq4_0' : 1, 'anc' : 4}, {('q3_0', 'q4_0') : 2, ('q3_0', 'outq4_0') : -2, ('q4_0', 'outq4_0') : -2, ('q3_0', 'anc') : -4, ('q4_0', 'anc') : -4, ('outq4_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q3_0']==q3_0 and sample['q4_0']==q4_0 and int(energy)==0:
        q3_0=sample['q3_0']
        q4_0=sample['outq4_0']
        tgt_before = sample['q4_0']
        break

print('#' * 80)
print("CNOT operation on q3_0 (control) and q4_0 (target):")
print("    in:  q3_0={0}, q4_0={1}".format(q3_0,tgt_before))
print("    out: q3_0={0}, q4_0={1}".format(q3_0,q4_0))
print('#' * 80)
print()
################################################################################
## NOT - target: q3_0 ##
################################################################################
if 'q3_0' not in globals():
    q3_0=0

bqm = dimod.BinaryQuadraticModel({'q3_0' : -4, 'outq3_0' : -4}, {('q3_0', 'outq3_0') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q3_0']==q3_0 and int(energy)==0:
        q3_0_before = sample['q3_0']
        q3_0=sample['outq3_0']
        break

print('#' * 80)
print("NOT operation on q3_0:")
print("    in:  q3_0={0}".format(q3_0_before))
print("    out: q3_0={0}".format(q3_0))
print('#' * 80)
print()
print("Measurement of q0_0 => {0}".format(q0_0))
print("Measurement of q0_1 => {0}".format(q0_1))
print("Measurement of q0_2 => {0}".format(q0_2))
print("Measurement of q0_3 => {0}".format(q0_3))
print("Measurement of q0_4 => {0}".format(q0_4))
print("Measurement of q0_5 => {0}".format(q0_5))
print("Measurement of q0_6 => {0}".format(q0_6))
print("Measurement of q0_7 => {0}".format(q0_7))
print("Measurement of q0_8 => {0}".format(q0_8))
print("Measurement of q0_9 => {0}".format(q0_9))
print("Measurement of q0_10 => {0}".format(q0_10))
print("Measurement of q0_11 => {0}".format(q0_11))
print("Measurement of q0_12 => {0}".format(q0_12))
print("Measurement of q0_13 => {0}".format(q0_13))
print("Measurement of q0_14 => {0}".format(q0_14))
print("Measurement of q0_15 => {0}".format(q0_15))
print("Measurement of q0_16 => {0}".format(q0_16))
print("Measurement of q0_17 => {0}".format(q0_17))
print("Measurement of q0_18 => {0}".format(q0_18))
print("Measurement of q0_19 => {0}".format(q0_19))
print("Measurement of q0_20 => {0}".format(q0_20))
print("Measurement of q0_21 => {0}".format(q0_21))
print("Measurement of q0_22 => {0}".format(q0_22))
print("Measurement of q0_23 => {0}".format(q0_23))
print("Measurement of q0_24 => {0}".format(q0_24))
print("Measurement of q0_25 => {0}".format(q0_25))
print("Measurement of q0_26 => {0}".format(q0_26))
print("Measurement of q0_27 => {0}".format(q0_27))
print("Measurement of q0_28 => {0}".format(q0_28))
print("Measurement of q0_29 => {0}".format(q0_29))
print("Measurement of q0_30 => {0}".format(q0_30))
print("Measurement of q0_31 => {0}".format(q0_31))
print("Measurement of q0_32 => {0}".format(q0_32))
print("Measurement of q0_33 => {0}".format(q0_33))
print("Measurement of q0_34 => {0}".format(q0_34))
print("Measurement of q0_35 => {0}".format(q0_35))
print("Measurement of q0_36 => {0}".format(q0_36))
print("Measurement of q0_37 => {0}".format(q0_37))
print("Measurement of q0_38 => {0}".format(q0_38))
print("Measurement of q0_39 => {0}".format(q0_39))
print("Measurement of q0_40 => {0}".format(q0_40))
print("Measurement of q0_41 => {0}".format(q0_41))
print("Measurement of q0_42 => {0}".format(q0_42))
print("Measurement of q0_43 => {0}".format(q0_43))
print("Measurement of q0_44 => {0}".format(q0_44))
print("Measurement of q0_45 => {0}".format(q0_45))
print("Measurement of q0_46 => {0}".format(q0_46))
print("Measurement of q0_47 => {0}".format(q0_47))
print("Measurement of q0_48 => {0}".format(q0_48))
print("Measurement of q0_49 => {0}".format(q0_49))
print("Measurement of q0_50 => {0}".format(q0_50))
print("Measurement of q0_51 => {0}".format(q0_51))
print("Measurement of q0_52 => {0}".format(q0_52))
print("Measurement of q0_53 => {0}".format(q0_53))
print("Measurement of q0_54 => {0}".format(q0_54))
print("Measurement of q0_55 => {0}".format(q0_55))
print("Measurement of q0_56 => {0}".format(q0_56))
print("Measurement of q0_57 => {0}".format(q0_57))
print("Measurement of q0_58 => {0}".format(q0_58))
print("Measurement of q0_59 => {0}".format(q0_59))
print("Measurement of q0_60 => {0}".format(q0_60))
print("Measurement of q0_61 => {0}".format(q0_61))
print("Measurement of q0_62 => {0}".format(q0_62))
print("Measurement of q0_63 => {0}".format(q0_63))
print("Measurement of q0_64 => {0}".format(q0_64))
print("Measurement of q0_65 => {0}".format(q0_65))
print("Measurement of q0_66 => {0}".format(q0_66))
print("Measurement of q0_67 => {0}".format(q0_67))
print("Measurement of q0_68 => {0}".format(q0_68))
print("Measurement of q0_69 => {0}".format(q0_69))
print("Measurement of q0_70 => {0}".format(q0_70))
print("Measurement of q0_71 => {0}".format(q0_71))
print("Measurement of q0_72 => {0}".format(q0_72))
print("Measurement of q0_73 => {0}".format(q0_73))
print("Measurement of q0_74 => {0}".format(q0_74))
print("Measurement of q0_75 => {0}".format(q0_75))
print("Measurement of q0_76 => {0}".format(q0_76))
print("Measurement of q0_77 => {0}".format(q0_77))
print("Measurement of q0_78 => {0}".format(q0_78))
print("Measurement of q0_79 => {0}".format(q0_79))
print("Measurement of q0_80 => {0}".format(q0_80))
print("Measurement of q0_81 => {0}".format(q0_81))
print("Measurement of q0_82 => {0}".format(q0_82))
print("Measurement of q0_83 => {0}".format(q0_83))
print("Measurement of q0_84 => {0}".format(q0_84))
print("Measurement of q0_85 => {0}".format(q0_85))
print("Measurement of q0_86 => {0}".format(q0_86))
print("Measurement of q0_87 => {0}".format(q0_87))
print("Measurement of q0_88 => {0}".format(q0_88))
print("Measurement of q0_89 => {0}".format(q0_89))
print("Measurement of q0_90 => {0}".format(q0_90))
print("Measurement of q0_91 => {0}".format(q0_91))
print("Measurement of q0_92 => {0}".format(q0_92))
print("Measurement of q0_93 => {0}".format(q0_93))
print("Measurement of q0_94 => {0}".format(q0_94))
print("Measurement of q0_95 => {0}".format(q0_95))
print("Measurement of q0_96 => {0}".format(q0_96))
print("Measurement of q0_97 => {0}".format(q0_97))
print("Measurement of q0_98 => {0}".format(q0_98))
print("Measurement of q0_99 => {0}".format(q0_99))
print("Measurement of q1_0 => {0}".format(q1_0))
print("Measurement of q1_1 => {0}".format(q1_1))
print("Measurement of q1_2 => {0}".format(q1_2))
print("Measurement of q1_3 => {0}".format(q1_3))
print("Measurement of q1_4 => {0}".format(q1_4))
print("Measurement of q1_5 => {0}".format(q1_5))
print("Measurement of q1_6 => {0}".format(q1_6))
print("Measurement of q1_7 => {0}".format(q1_7))
print("Measurement of q1_8 => {0}".format(q1_8))
print("Measurement of q1_9 => {0}".format(q1_9))
print("Measurement of q1_10 => {0}".format(q1_10))
print("Measurement of q1_11 => {0}".format(q1_11))
print("Measurement of q1_12 => {0}".format(q1_12))
print("Measurement of q1_13 => {0}".format(q1_13))
print("Measurement of q1_14 => {0}".format(q1_14))
print("Measurement of q1_15 => {0}".format(q1_15))
print("Measurement of q1_16 => {0}".format(q1_16))
print("Measurement of q1_17 => {0}".format(q1_17))
print("Measurement of q1_18 => {0}".format(q1_18))
print("Measurement of q1_19 => {0}".format(q1_19))
print("Measurement of q1_20 => {0}".format(q1_20))
print("Measurement of q1_21 => {0}".format(q1_21))
print("Measurement of q1_22 => {0}".format(q1_22))
print("Measurement of q1_23 => {0}".format(q1_23))
print("Measurement of q1_24 => {0}".format(q1_24))
print("Measurement of q1_25 => {0}".format(q1_25))
print("Measurement of q1_26 => {0}".format(q1_26))
print("Measurement of q1_27 => {0}".format(q1_27))
print("Measurement of q1_28 => {0}".format(q1_28))
print("Measurement of q1_29 => {0}".format(q1_29))
print("Measurement of q1_30 => {0}".format(q1_30))
print("Measurement of q1_31 => {0}".format(q1_31))
print("Measurement of q1_32 => {0}".format(q1_32))
print("Measurement of q1_33 => {0}".format(q1_33))
print("Measurement of q1_34 => {0}".format(q1_34))
print("Measurement of q1_35 => {0}".format(q1_35))
print("Measurement of q1_36 => {0}".format(q1_36))
print("Measurement of q1_37 => {0}".format(q1_37))
print("Measurement of q1_38 => {0}".format(q1_38))
print("Measurement of q1_39 => {0}".format(q1_39))
print("Measurement of q1_40 => {0}".format(q1_40))
print("Measurement of q1_41 => {0}".format(q1_41))
print("Measurement of q1_42 => {0}".format(q1_42))
print("Measurement of q1_43 => {0}".format(q1_43))
print("Measurement of q1_44 => {0}".format(q1_44))
print("Measurement of q1_45 => {0}".format(q1_45))
print("Measurement of q1_46 => {0}".format(q1_46))
print("Measurement of q1_47 => {0}".format(q1_47))
print("Measurement of q1_48 => {0}".format(q1_48))
print("Measurement of q1_49 => {0}".format(q1_49))
print("Measurement of q1_50 => {0}".format(q1_50))
print("Measurement of q1_51 => {0}".format(q1_51))
print("Measurement of q1_52 => {0}".format(q1_52))
print("Measurement of q1_53 => {0}".format(q1_53))
print("Measurement of q1_54 => {0}".format(q1_54))
print("Measurement of q1_55 => {0}".format(q1_55))
print("Measurement of q1_56 => {0}".format(q1_56))
print("Measurement of q1_57 => {0}".format(q1_57))
print("Measurement of q1_58 => {0}".format(q1_58))
print("Measurement of q1_59 => {0}".format(q1_59))
print("Measurement of q1_60 => {0}".format(q1_60))
print("Measurement of q1_61 => {0}".format(q1_61))
print("Measurement of q1_62 => {0}".format(q1_62))
print("Measurement of q1_63 => {0}".format(q1_63))
print("Measurement of q1_64 => {0}".format(q1_64))
print("Measurement of q1_65 => {0}".format(q1_65))
print("Measurement of q1_66 => {0}".format(q1_66))
print("Measurement of q1_67 => {0}".format(q1_67))
print("Measurement of q1_68 => {0}".format(q1_68))
print("Measurement of q1_69 => {0}".format(q1_69))
print("Measurement of q1_70 => {0}".format(q1_70))
print("Measurement of q1_71 => {0}".format(q1_71))
print("Measurement of q1_72 => {0}".format(q1_72))
print("Measurement of q1_73 => {0}".format(q1_73))
print("Measurement of q1_74 => {0}".format(q1_74))
print("Measurement of q1_75 => {0}".format(q1_75))
print("Measurement of q1_76 => {0}".format(q1_76))
print("Measurement of q1_77 => {0}".format(q1_77))
print("Measurement of q1_78 => {0}".format(q1_78))
print("Measurement of q1_79 => {0}".format(q1_79))
print("Measurement of q1_80 => {0}".format(q1_80))
print("Measurement of q1_81 => {0}".format(q1_81))
print("Measurement of q1_82 => {0}".format(q1_82))
print("Measurement of q1_83 => {0}".format(q1_83))
print("Measurement of q1_84 => {0}".format(q1_84))
print("Measurement of q1_85 => {0}".format(q1_85))
print("Measurement of q1_86 => {0}".format(q1_86))
print("Measurement of q1_87 => {0}".format(q1_87))
print("Measurement of q1_88 => {0}".format(q1_88))
print("Measurement of q1_89 => {0}".format(q1_89))
print("Measurement of q1_90 => {0}".format(q1_90))
print("Measurement of q1_91 => {0}".format(q1_91))
print("Measurement of q1_92 => {0}".format(q1_92))
print("Measurement of q1_93 => {0}".format(q1_93))
print("Measurement of q1_94 => {0}".format(q1_94))
print("Measurement of q1_95 => {0}".format(q1_95))
print("Measurement of q1_96 => {0}".format(q1_96))
print("Measurement of q1_97 => {0}".format(q1_97))
print("Measurement of q1_98 => {0}".format(q1_98))
print("Measurement of q1_99 => {0}".format(q1_99))
print("Measurement of q2_0 => {0}".format(q2_0))
