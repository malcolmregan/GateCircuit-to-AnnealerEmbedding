#!/usr/bin/python3
import dimod

################################################################################
## NOT - target: q0_0 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0

bqm = dimod.BinaryQuadraticModel({'q0_0' : -4, 'outq0_0' : -4}, {('q0_0', 'outq0_0') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_0']==q0_0 and int(energy)==0:
        q0_0_before = sample['q0_0']
        q0_0=sample['outq0_0']
        break

print('#' * 80)
print("NOT operation on q0_0:")
print("    in:  q0_0={0}".format(q0_0_before))
print("    out: q0_0={0}".format(q0_0))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_1 ##
################################################################################
if 'q0_1' not in globals():
    q0_1=0

bqm = dimod.BinaryQuadraticModel({'q0_1' : -4, 'outq0_1' : -4}, {('q0_1', 'outq0_1') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_1']==q0_1 and int(energy)==0:
        q0_1_before = sample['q0_1']
        q0_1=sample['outq0_1']
        break

print('#' * 80)
print("NOT operation on q0_1:")
print("    in:  q0_1={0}".format(q0_1_before))
print("    out: q0_1={0}".format(q0_1))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_2 ##
################################################################################
if 'q0_2' not in globals():
    q0_2=0

bqm = dimod.BinaryQuadraticModel({'q0_2' : -4, 'outq0_2' : -4}, {('q0_2', 'outq0_2') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_2']==q0_2 and int(energy)==0:
        q0_2_before = sample['q0_2']
        q0_2=sample['outq0_2']
        break

print('#' * 80)
print("NOT operation on q0_2:")
print("    in:  q0_2={0}".format(q0_2_before))
print("    out: q0_2={0}".format(q0_2))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_3 ##
################################################################################
if 'q0_3' not in globals():
    q0_3=0

bqm = dimod.BinaryQuadraticModel({'q0_3' : -4, 'outq0_3' : -4}, {('q0_3', 'outq0_3') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_3']==q0_3 and int(energy)==0:
        q0_3_before = sample['q0_3']
        q0_3=sample['outq0_3']
        break

print('#' * 80)
print("NOT operation on q0_3:")
print("    in:  q0_3={0}".format(q0_3_before))
print("    out: q0_3={0}".format(q0_3))
print('#' * 80)
print()
################################################################################
## NOT - target: q0_4 ##
################################################################################
if 'q0_4' not in globals():
    q0_4=0

bqm = dimod.BinaryQuadraticModel({'q0_4' : -4, 'outq0_4' : -4}, {('q0_4', 'outq0_4') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_4']==q0_4 and int(energy)==0:
        q0_4_before = sample['q0_4']
        q0_4=sample['outq0_4']
        break

print('#' * 80)
print("NOT operation on q0_4:")
print("    in:  q0_4={0}".format(q0_4_before))
print("    out: q0_4={0}".format(q0_4))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_1 ##
################################################################################
if 'q1_1' not in globals():
    q1_1=0

bqm = dimod.BinaryQuadraticModel({'q1_1' : -4, 'outq1_1' : -4}, {('q1_1', 'outq1_1') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_1']==q1_1 and int(energy)==0:
        q1_1_before = sample['q1_1']
        q1_1=sample['outq1_1']
        break

print('#' * 80)
print("NOT operation on q1_1:")
print("    in:  q1_1={0}".format(q1_1_before))
print("    out: q1_1={0}".format(q1_1))
print('#' * 80)
print()
################################################################################
## NOT - target: q1_3 ##
################################################################################
if 'q1_3' not in globals():
    q1_3=0

bqm = dimod.BinaryQuadraticModel({'q1_3' : -4, 'outq1_3' : -4}, {('q1_3', 'outq1_3') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_3']==q1_3 and int(energy)==0:
        q1_3_before = sample['q1_3']
        q1_3=sample['outq1_3']
        break

print('#' * 80)
print("NOT operation on q1_3:")
print("    in:  q1_3={0}".format(q1_3_before))
print("    out: q1_3={0}".format(q1_3))
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
## CCNOT - control1: q0_4 control2: q3_0 target: q4_0 ##
################################################################################
if 'q0_4' not in globals():
    q0_4=0
if 'q3_0' not in globals():
    q3_0=0
if 'q4_0' not in globals():
    q4_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq4_0' : 1, 'q4_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq4_0') : 4, ('anc1','q4_0') : -4, ('anc2', 'q0_4') : -2, ('anc2', 'q3_0') : -2, ('anc2', 'outq4_0') : -2, ('anc2', 'q4_0') : 2, ('q0_4', 'q3_0') : 1, ('outq4_0', 'q4_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_4']==q0_4 and sample['q3_0']==q3_0 and sample['q4_0']==q4_0 and int(energy)==0:
        q0_4=sample['q0_4']
        q3_0=sample['q3_0']
        q4_0=sample['outq4_0']
        tgt_before = sample['q4_0']
        break

print('#' * 80)
print("CCNOT operation on q0_4 (control1), q3_0 (control2) and q4_0 (target):")
print("    in:  q0_4={0}, q3_0={1}, q4_0={2}".format(q0_4,q3_0,tgt_before))
print("    out: q0_4={0}, q3_0={1}, q4_0={2}".format(q0_4,q3_0,q4_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_4 control2: q3_0 target: q4_0 ##
################################################################################
if 'q1_4' not in globals():
    q1_4=0
if 'q3_0' not in globals():
    q3_0=0
if 'q4_0' not in globals():
    q4_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq4_0' : 1, 'q4_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq4_0') : 4, ('anc1','q4_0') : -4, ('anc2', 'q1_4') : -2, ('anc2', 'q3_0') : -2, ('anc2', 'outq4_0') : -2, ('anc2', 'q4_0') : 2, ('q1_4', 'q3_0') : 1, ('outq4_0', 'q4_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_4']==q1_4 and sample['q3_0']==q3_0 and sample['q4_0']==q4_0 and int(energy)==0:
        q1_4=sample['q1_4']
        q3_0=sample['q3_0']
        q4_0=sample['outq4_0']
        tgt_before = sample['q4_0']
        break

print('#' * 80)
print("CCNOT operation on q1_4 (control1), q3_0 (control2) and q4_0 (target):")
print("    in:  q1_4={0}, q3_0={1}, q4_0={2}".format(q1_4,q3_0,tgt_before))
print("    out: q1_4={0}, q3_0={1}, q4_0={2}".format(q1_4,q3_0,q4_0))
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
## CCNOT - control1: q0_3 control2: q4_0 target: q5_0 ##
################################################################################
if 'q0_3' not in globals():
    q0_3=0
if 'q4_0' not in globals():
    q4_0=0
if 'q5_0' not in globals():
    q5_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq5_0' : 1, 'q5_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq5_0') : 4, ('anc1','q5_0') : -4, ('anc2', 'q0_3') : -2, ('anc2', 'q4_0') : -2, ('anc2', 'outq5_0') : -2, ('anc2', 'q5_0') : 2, ('q0_3', 'q4_0') : 1, ('outq5_0', 'q5_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_3']==q0_3 and sample['q4_0']==q4_0 and sample['q5_0']==q5_0 and int(energy)==0:
        q0_3=sample['q0_3']
        q4_0=sample['q4_0']
        q5_0=sample['outq5_0']
        tgt_before = sample['q5_0']
        break

print('#' * 80)
print("CCNOT operation on q0_3 (control1), q4_0 (control2) and q5_0 (target):")
print("    in:  q0_3={0}, q4_0={1}, q5_0={2}".format(q0_3,q4_0,tgt_before))
print("    out: q0_3={0}, q4_0={1}, q5_0={2}".format(q0_3,q4_0,q5_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_3 control2: q4_0 target: q5_0 ##
################################################################################
if 'q1_3' not in globals():
    q1_3=0
if 'q4_0' not in globals():
    q4_0=0
if 'q5_0' not in globals():
    q5_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq5_0' : 1, 'q5_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq5_0') : 4, ('anc1','q5_0') : -4, ('anc2', 'q1_3') : -2, ('anc2', 'q4_0') : -2, ('anc2', 'outq5_0') : -2, ('anc2', 'q5_0') : 2, ('q1_3', 'q4_0') : 1, ('outq5_0', 'q5_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_3']==q1_3 and sample['q4_0']==q4_0 and sample['q5_0']==q5_0 and int(energy)==0:
        q1_3=sample['q1_3']
        q4_0=sample['q4_0']
        q5_0=sample['outq5_0']
        tgt_before = sample['q5_0']
        break

print('#' * 80)
print("CCNOT operation on q1_3 (control1), q4_0 (control2) and q5_0 (target):")
print("    in:  q1_3={0}, q4_0={1}, q5_0={2}".format(q1_3,q4_0,tgt_before))
print("    out: q1_3={0}, q4_0={1}, q5_0={2}".format(q1_3,q4_0,q5_0))
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
## CCNOT - control1: q0_2 control2: q5_0 target: q6_0 ##
################################################################################
if 'q0_2' not in globals():
    q0_2=0
if 'q5_0' not in globals():
    q5_0=0
if 'q6_0' not in globals():
    q6_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq6_0' : 1, 'q6_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq6_0') : 4, ('anc1','q6_0') : -4, ('anc2', 'q0_2') : -2, ('anc2', 'q5_0') : -2, ('anc2', 'outq6_0') : -2, ('anc2', 'q6_0') : 2, ('q0_2', 'q5_0') : 1, ('outq6_0', 'q6_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_2']==q0_2 and sample['q5_0']==q5_0 and sample['q6_0']==q6_0 and int(energy)==0:
        q0_2=sample['q0_2']
        q5_0=sample['q5_0']
        q6_0=sample['outq6_0']
        tgt_before = sample['q6_0']
        break

print('#' * 80)
print("CCNOT operation on q0_2 (control1), q5_0 (control2) and q6_0 (target):")
print("    in:  q0_2={0}, q5_0={1}, q6_0={2}".format(q0_2,q5_0,tgt_before))
print("    out: q0_2={0}, q5_0={1}, q6_0={2}".format(q0_2,q5_0,q6_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_2 control2: q5_0 target: q6_0 ##
################################################################################
if 'q1_2' not in globals():
    q1_2=0
if 'q5_0' not in globals():
    q5_0=0
if 'q6_0' not in globals():
    q6_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq6_0' : 1, 'q6_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq6_0') : 4, ('anc1','q6_0') : -4, ('anc2', 'q1_2') : -2, ('anc2', 'q5_0') : -2, ('anc2', 'outq6_0') : -2, ('anc2', 'q6_0') : 2, ('q1_2', 'q5_0') : 1, ('outq6_0', 'q6_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_2']==q1_2 and sample['q5_0']==q5_0 and sample['q6_0']==q6_0 and int(energy)==0:
        q1_2=sample['q1_2']
        q5_0=sample['q5_0']
        q6_0=sample['outq6_0']
        tgt_before = sample['q6_0']
        break

print('#' * 80)
print("CCNOT operation on q1_2 (control1), q5_0 (control2) and q6_0 (target):")
print("    in:  q1_2={0}, q5_0={1}, q6_0={2}".format(q1_2,q5_0,tgt_before))
print("    out: q1_2={0}, q5_0={1}, q6_0={2}".format(q1_2,q5_0,q6_0))
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
## CCNOT - control1: q0_1 control2: q6_0 target: q7_0 ##
################################################################################
if 'q0_1' not in globals():
    q0_1=0
if 'q6_0' not in globals():
    q6_0=0
if 'q7_0' not in globals():
    q7_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq7_0' : 1, 'q7_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq7_0') : 4, ('anc1','q7_0') : -4, ('anc2', 'q0_1') : -2, ('anc2', 'q6_0') : -2, ('anc2', 'outq7_0') : -2, ('anc2', 'q7_0') : 2, ('q0_1', 'q6_0') : 1, ('outq7_0', 'q7_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_1']==q0_1 and sample['q6_0']==q6_0 and sample['q7_0']==q7_0 and int(energy)==0:
        q0_1=sample['q0_1']
        q6_0=sample['q6_0']
        q7_0=sample['outq7_0']
        tgt_before = sample['q7_0']
        break

print('#' * 80)
print("CCNOT operation on q0_1 (control1), q6_0 (control2) and q7_0 (target):")
print("    in:  q0_1={0}, q6_0={1}, q7_0={2}".format(q0_1,q6_0,tgt_before))
print("    out: q0_1={0}, q6_0={1}, q7_0={2}".format(q0_1,q6_0,q7_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_1 control2: q6_0 target: q7_0 ##
################################################################################
if 'q1_1' not in globals():
    q1_1=0
if 'q6_0' not in globals():
    q6_0=0
if 'q7_0' not in globals():
    q7_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq7_0' : 1, 'q7_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq7_0') : 4, ('anc1','q7_0') : -4, ('anc2', 'q1_1') : -2, ('anc2', 'q6_0') : -2, ('anc2', 'outq7_0') : -2, ('anc2', 'q7_0') : 2, ('q1_1', 'q6_0') : 1, ('outq7_0', 'q7_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_1']==q1_1 and sample['q6_0']==q6_0 and sample['q7_0']==q7_0 and int(energy)==0:
        q1_1=sample['q1_1']
        q6_0=sample['q6_0']
        q7_0=sample['outq7_0']
        tgt_before = sample['q7_0']
        break

print('#' * 80)
print("CCNOT operation on q1_1 (control1), q6_0 (control2) and q7_0 (target):")
print("    in:  q1_1={0}, q6_0={1}, q7_0={2}".format(q1_1,q6_0,tgt_before))
print("    out: q1_1={0}, q6_0={1}, q7_0={2}".format(q1_1,q6_0,q7_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q7_0 target: q2_0 ##
################################################################################
if 'q7_0' not in globals():
    q7_0=0
if 'q2_0' not in globals():
    q2_0=0

bqm = dimod.BinaryQuadraticModel({'q7_0' : 1, 'q2_0' : 1, 'outq2_0' : 1, 'anc' : 4}, {('q7_0', 'q2_0') : 2, ('q7_0', 'outq2_0') : -2, ('q2_0', 'outq2_0') : -2, ('q7_0', 'anc') : -4, ('q2_0', 'anc') : -4, ('outq2_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q7_0']==q7_0 and sample['q2_0']==q2_0 and int(energy)==0:
        q7_0=sample['q7_0']
        q2_0=sample['outq2_0']
        tgt_before = sample['q2_0']
        break

print('#' * 80)
print("CNOT operation on q7_0 (control) and q2_0 (target):")
print("    in:  q7_0={0}, q2_0={1}".format(q7_0,tgt_before))
print("    out: q7_0={0}, q2_0={1}".format(q7_0,q2_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_0 control2: q7_0 target: q2_0 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q7_0' not in globals():
    q7_0=0
if 'q2_0' not in globals():
    q2_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq2_0' : 1, 'q2_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq2_0') : 4, ('anc1','q2_0') : -4, ('anc2', 'q0_0') : -2, ('anc2', 'q7_0') : -2, ('anc2', 'outq2_0') : -2, ('anc2', 'q2_0') : 2, ('q0_0', 'q7_0') : 1, ('outq2_0', 'q2_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_0']==q0_0 and sample['q7_0']==q7_0 and sample['q2_0']==q2_0 and int(energy)==0:
        q0_0=sample['q0_0']
        q7_0=sample['q7_0']
        q2_0=sample['outq2_0']
        tgt_before = sample['q2_0']
        break

print('#' * 80)
print("CCNOT operation on q0_0 (control1), q7_0 (control2) and q2_0 (target):")
print("    in:  q0_0={0}, q7_0={1}, q2_0={2}".format(q0_0,q7_0,tgt_before))
print("    out: q0_0={0}, q7_0={1}, q2_0={2}".format(q0_0,q7_0,q2_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_0 control2: q7_0 target: q2_0 ##
################################################################################
if 'q1_0' not in globals():
    q1_0=0
if 'q7_0' not in globals():
    q7_0=0
if 'q2_0' not in globals():
    q2_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq2_0' : 1, 'q2_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq2_0') : 4, ('anc1','q2_0') : -4, ('anc2', 'q1_0') : -2, ('anc2', 'q7_0') : -2, ('anc2', 'outq2_0') : -2, ('anc2', 'q2_0') : 2, ('q1_0', 'q7_0') : 1, ('outq2_0', 'q2_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_0']==q1_0 and sample['q7_0']==q7_0 and sample['q2_0']==q2_0 and int(energy)==0:
        q1_0=sample['q1_0']
        q7_0=sample['q7_0']
        q2_0=sample['outq2_0']
        tgt_before = sample['q2_0']
        break

print('#' * 80)
print("CCNOT operation on q1_0 (control1), q7_0 (control2) and q2_0 (target):")
print("    in:  q1_0={0}, q7_0={1}, q2_0={2}".format(q1_0,q7_0,tgt_before))
print("    out: q1_0={0}, q7_0={1}, q2_0={2}".format(q1_0,q7_0,q2_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_1 control2: q6_0 target: q7_0 ##
################################################################################
if 'q1_1' not in globals():
    q1_1=0
if 'q6_0' not in globals():
    q6_0=0
if 'q7_0' not in globals():
    q7_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq7_0' : 1, 'q7_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq7_0') : 4, ('anc1','q7_0') : -4, ('anc2', 'q1_1') : -2, ('anc2', 'q6_0') : -2, ('anc2', 'outq7_0') : -2, ('anc2', 'q7_0') : 2, ('q1_1', 'q6_0') : 1, ('outq7_0', 'q7_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_1']==q1_1 and sample['q6_0']==q6_0 and sample['q7_0']==q7_0 and int(energy)==0:
        q1_1=sample['q1_1']
        q6_0=sample['q6_0']
        q7_0=sample['outq7_0']
        tgt_before = sample['q7_0']
        break

print('#' * 80)
print("CCNOT operation on q1_1 (control1), q6_0 (control2) and q7_0 (target):")
print("    in:  q1_1={0}, q6_0={1}, q7_0={2}".format(q1_1,q6_0,tgt_before))
print("    out: q1_1={0}, q6_0={1}, q7_0={2}".format(q1_1,q6_0,q7_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_1 control2: q6_0 target: q7_0 ##
################################################################################
if 'q0_1' not in globals():
    q0_1=0
if 'q6_0' not in globals():
    q6_0=0
if 'q7_0' not in globals():
    q7_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq7_0' : 1, 'q7_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq7_0') : 4, ('anc1','q7_0') : -4, ('anc2', 'q0_1') : -2, ('anc2', 'q6_0') : -2, ('anc2', 'outq7_0') : -2, ('anc2', 'q7_0') : 2, ('q0_1', 'q6_0') : 1, ('outq7_0', 'q7_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_1']==q0_1 and sample['q6_0']==q6_0 and sample['q7_0']==q7_0 and int(energy)==0:
        q0_1=sample['q0_1']
        q6_0=sample['q6_0']
        q7_0=sample['outq7_0']
        tgt_before = sample['q7_0']
        break

print('#' * 80)
print("CCNOT operation on q0_1 (control1), q6_0 (control2) and q7_0 (target):")
print("    in:  q0_1={0}, q6_0={1}, q7_0={2}".format(q0_1,q6_0,tgt_before))
print("    out: q0_1={0}, q6_0={1}, q7_0={2}".format(q0_1,q6_0,q7_0))
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
## CCNOT - control1: q1_2 control2: q5_0 target: q6_0 ##
################################################################################
if 'q1_2' not in globals():
    q1_2=0
if 'q5_0' not in globals():
    q5_0=0
if 'q6_0' not in globals():
    q6_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq6_0' : 1, 'q6_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq6_0') : 4, ('anc1','q6_0') : -4, ('anc2', 'q1_2') : -2, ('anc2', 'q5_0') : -2, ('anc2', 'outq6_0') : -2, ('anc2', 'q6_0') : 2, ('q1_2', 'q5_0') : 1, ('outq6_0', 'q6_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_2']==q1_2 and sample['q5_0']==q5_0 and sample['q6_0']==q6_0 and int(energy)==0:
        q1_2=sample['q1_2']
        q5_0=sample['q5_0']
        q6_0=sample['outq6_0']
        tgt_before = sample['q6_0']
        break

print('#' * 80)
print("CCNOT operation on q1_2 (control1), q5_0 (control2) and q6_0 (target):")
print("    in:  q1_2={0}, q5_0={1}, q6_0={2}".format(q1_2,q5_0,tgt_before))
print("    out: q1_2={0}, q5_0={1}, q6_0={2}".format(q1_2,q5_0,q6_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_2 control2: q5_0 target: q6_0 ##
################################################################################
if 'q0_2' not in globals():
    q0_2=0
if 'q5_0' not in globals():
    q5_0=0
if 'q6_0' not in globals():
    q6_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq6_0' : 1, 'q6_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq6_0') : 4, ('anc1','q6_0') : -4, ('anc2', 'q0_2') : -2, ('anc2', 'q5_0') : -2, ('anc2', 'outq6_0') : -2, ('anc2', 'q6_0') : 2, ('q0_2', 'q5_0') : 1, ('outq6_0', 'q6_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_2']==q0_2 and sample['q5_0']==q5_0 and sample['q6_0']==q6_0 and int(energy)==0:
        q0_2=sample['q0_2']
        q5_0=sample['q5_0']
        q6_0=sample['outq6_0']
        tgt_before = sample['q6_0']
        break

print('#' * 80)
print("CCNOT operation on q0_2 (control1), q5_0 (control2) and q6_0 (target):")
print("    in:  q0_2={0}, q5_0={1}, q6_0={2}".format(q0_2,q5_0,tgt_before))
print("    out: q0_2={0}, q5_0={1}, q6_0={2}".format(q0_2,q5_0,q6_0))
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
## CCNOT - control1: q1_3 control2: q4_0 target: q5_0 ##
################################################################################
if 'q1_3' not in globals():
    q1_3=0
if 'q4_0' not in globals():
    q4_0=0
if 'q5_0' not in globals():
    q5_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq5_0' : 1, 'q5_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq5_0') : 4, ('anc1','q5_0') : -4, ('anc2', 'q1_3') : -2, ('anc2', 'q4_0') : -2, ('anc2', 'outq5_0') : -2, ('anc2', 'q5_0') : 2, ('q1_3', 'q4_0') : 1, ('outq5_0', 'q5_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_3']==q1_3 and sample['q4_0']==q4_0 and sample['q5_0']==q5_0 and int(energy)==0:
        q1_3=sample['q1_3']
        q4_0=sample['q4_0']
        q5_0=sample['outq5_0']
        tgt_before = sample['q5_0']
        break

print('#' * 80)
print("CCNOT operation on q1_3 (control1), q4_0 (control2) and q5_0 (target):")
print("    in:  q1_3={0}, q4_0={1}, q5_0={2}".format(q1_3,q4_0,tgt_before))
print("    out: q1_3={0}, q4_0={1}, q5_0={2}".format(q1_3,q4_0,q5_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_3 control2: q4_0 target: q5_0 ##
################################################################################
if 'q0_3' not in globals():
    q0_3=0
if 'q4_0' not in globals():
    q4_0=0
if 'q5_0' not in globals():
    q5_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq5_0' : 1, 'q5_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq5_0') : 4, ('anc1','q5_0') : -4, ('anc2', 'q0_3') : -2, ('anc2', 'q4_0') : -2, ('anc2', 'outq5_0') : -2, ('anc2', 'q5_0') : 2, ('q0_3', 'q4_0') : 1, ('outq5_0', 'q5_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_3']==q0_3 and sample['q4_0']==q4_0 and sample['q5_0']==q5_0 and int(energy)==0:
        q0_3=sample['q0_3']
        q4_0=sample['q4_0']
        q5_0=sample['outq5_0']
        tgt_before = sample['q5_0']
        break

print('#' * 80)
print("CCNOT operation on q0_3 (control1), q4_0 (control2) and q5_0 (target):")
print("    in:  q0_3={0}, q4_0={1}, q5_0={2}".format(q0_3,q4_0,tgt_before))
print("    out: q0_3={0}, q4_0={1}, q5_0={2}".format(q0_3,q4_0,q5_0))
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
## CCNOT - control1: q1_4 control2: q3_0 target: q4_0 ##
################################################################################
if 'q1_4' not in globals():
    q1_4=0
if 'q3_0' not in globals():
    q3_0=0
if 'q4_0' not in globals():
    q4_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq4_0' : 1, 'q4_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq4_0') : 4, ('anc1','q4_0') : -4, ('anc2', 'q1_4') : -2, ('anc2', 'q3_0') : -2, ('anc2', 'outq4_0') : -2, ('anc2', 'q4_0') : 2, ('q1_4', 'q3_0') : 1, ('outq4_0', 'q4_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_4']==q1_4 and sample['q3_0']==q3_0 and sample['q4_0']==q4_0 and int(energy)==0:
        q1_4=sample['q1_4']
        q3_0=sample['q3_0']
        q4_0=sample['outq4_0']
        tgt_before = sample['q4_0']
        break

print('#' * 80)
print("CCNOT operation on q1_4 (control1), q3_0 (control2) and q4_0 (target):")
print("    in:  q1_4={0}, q3_0={1}, q4_0={2}".format(q1_4,q3_0,tgt_before))
print("    out: q1_4={0}, q3_0={1}, q4_0={2}".format(q1_4,q3_0,q4_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_4 control2: q3_0 target: q4_0 ##
################################################################################
if 'q0_4' not in globals():
    q0_4=0
if 'q3_0' not in globals():
    q3_0=0
if 'q4_0' not in globals():
    q4_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq4_0' : 1, 'q4_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq4_0') : 4, ('anc1','q4_0') : -4, ('anc2', 'q0_4') : -2, ('anc2', 'q3_0') : -2, ('anc2', 'outq4_0') : -2, ('anc2', 'q4_0') : 2, ('q0_4', 'q3_0') : 1, ('outq4_0', 'q4_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_4']==q0_4 and sample['q3_0']==q3_0 and sample['q4_0']==q4_0 and int(energy)==0:
        q0_4=sample['q0_4']
        q3_0=sample['q3_0']
        q4_0=sample['outq4_0']
        tgt_before = sample['q4_0']
        break

print('#' * 80)
print("CCNOT operation on q0_4 (control1), q3_0 (control2) and q4_0 (target):")
print("    in:  q0_4={0}, q3_0={1}, q4_0={2}".format(q0_4,q3_0,tgt_before))
print("    out: q0_4={0}, q3_0={1}, q4_0={2}".format(q0_4,q3_0,q4_0))
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
print("Measurement of q1_0 => {0}".format(q1_0))
print("Measurement of q1_1 => {0}".format(q1_1))
print("Measurement of q1_2 => {0}".format(q1_2))
print("Measurement of q1_3 => {0}".format(q1_3))
print("Measurement of q1_4 => {0}".format(q1_4))
print("Measurement of q2_0 => {0}".format(q2_0))
