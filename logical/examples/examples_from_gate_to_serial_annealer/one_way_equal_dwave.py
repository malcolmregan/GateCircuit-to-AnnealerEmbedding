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
## NOT - target: q1_0 ##
################################################################################
if 'q1_0' not in globals():
    q1_0=0

bqm = dimod.BinaryQuadraticModel({'q1_0' : -4, 'outq1_0' : -4}, {('q1_0', 'outq1_0') : 8}, 4, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_0']==q1_0 and int(energy)==0:
        q1_0_before = sample['q1_0']
        q1_0=sample['outq1_0']
        break

print('#' * 80)
print("NOT operation on q1_0:")
print("    in:  q1_0={0}".format(q1_0_before))
print("    out: q1_0={0}".format(q1_0))
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
## CNOT - control: q3_0 target: q2_0 ##
################################################################################
if 'q3_0' not in globals():
    q3_0=0
if 'q2_0' not in globals():
    q2_0=0

bqm = dimod.BinaryQuadraticModel({'q3_0' : 1, 'q2_0' : 1, 'outq2_0' : 1, 'anc' : 4}, {('q3_0', 'q2_0') : 2, ('q3_0', 'outq2_0') : -2, ('q2_0', 'outq2_0') : -2, ('q3_0', 'anc') : -4, ('q2_0', 'anc') : -4, ('outq2_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q3_0']==q3_0 and sample['q2_0']==q2_0 and int(energy)==0:
        q3_0=sample['q3_0']
        q2_0=sample['outq2_0']
        tgt_before = sample['q2_0']
        break

print('#' * 80)
print("CNOT operation on q3_0 (control) and q2_0 (target):")
print("    in:  q3_0={0}, q2_0={1}".format(q3_0,tgt_before))
print("    out: q3_0={0}, q2_0={1}".format(q3_0,q2_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_0 control2: q3_0 target: q2_0 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q3_0' not in globals():
    q3_0=0
if 'q2_0' not in globals():
    q2_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq2_0' : 1, 'q2_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq2_0') : 4, ('anc1','q2_0') : -4, ('anc2', 'q0_0') : -2, ('anc2', 'q3_0') : -2, ('anc2', 'outq2_0') : -2, ('anc2', 'q2_0') : 2, ('q0_0', 'q3_0') : 1, ('outq2_0', 'q2_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_0']==q0_0 and sample['q3_0']==q3_0 and sample['q2_0']==q2_0 and int(energy)==0:
        q0_0=sample['q0_0']
        q3_0=sample['q3_0']
        q2_0=sample['outq2_0']
        tgt_before = sample['q2_0']
        break

print('#' * 80)
print("CCNOT operation on q0_0 (control1), q3_0 (control2) and q2_0 (target):")
print("    in:  q0_0={0}, q3_0={1}, q2_0={2}".format(q0_0,q3_0,tgt_before))
print("    out: q0_0={0}, q3_0={1}, q2_0={2}".format(q0_0,q3_0,q2_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q1_0 control2: q3_0 target: q2_0 ##
################################################################################
if 'q1_0' not in globals():
    q1_0=0
if 'q3_0' not in globals():
    q3_0=0
if 'q2_0' not in globals():
    q2_0=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq2_0' : 1, 'q2_0' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq2_0') : 4, ('anc1','q2_0') : -4, ('anc2', 'q1_0') : -2, ('anc2', 'q3_0') : -2, ('anc2', 'outq2_0') : -2, ('anc2', 'q2_0') : 2, ('q1_0', 'q3_0') : 1, ('outq2_0', 'q2_0') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q1_0']==q1_0 and sample['q3_0']==q3_0 and sample['q2_0']==q2_0 and int(energy)==0:
        q1_0=sample['q1_0']
        q3_0=sample['q3_0']
        q2_0=sample['outq2_0']
        tgt_before = sample['q2_0']
        break

print('#' * 80)
print("CCNOT operation on q1_0 (control1), q3_0 (control2) and q2_0 (target):")
print("    in:  q1_0={0}, q3_0={1}, q2_0={2}".format(q1_0,q3_0,tgt_before))
print("    out: q1_0={0}, q3_0={1}, q2_0={2}".format(q1_0,q3_0,q2_0))
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
print("Measurement of q1_0 => {0}".format(q1_0))
print("Measurement of q2_0 => {0}".format(q2_0))
