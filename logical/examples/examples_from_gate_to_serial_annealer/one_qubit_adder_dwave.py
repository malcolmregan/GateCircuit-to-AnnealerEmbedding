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
## CNOT - control: q0_0 target: q1_0 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q1_0' not in globals():
    q1_0=0

bqm = dimod.BinaryQuadraticModel({'q0_0' : 1, 'q1_0' : 1, 'outq1_0' : 1, 'anc' : 4}, {('q0_0', 'q1_0') : 2, ('q0_0', 'outq1_0') : -2, ('q1_0', 'outq1_0') : -2, ('q0_0', 'anc') : -4, ('q1_0', 'anc') : -4, ('outq1_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_0']==q0_0 and sample['q1_0']==q1_0 and int(energy)==0:
        q0_0=sample['q0_0']
        q1_0=sample['outq1_0']
        tgt_before = sample['q1_0']
        break

print('#' * 80)
print("CNOT operation on q0_0 (control) and q1_0 (target):")
print("    in:  q0_0={0}, q1_0={1}".format(q0_0,tgt_before))
print("    out: q0_0={0}, q1_0={1}".format(q0_0,q1_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q0_1 target: q1_0 ##
################################################################################
if 'q0_1' not in globals():
    q0_1=0
if 'q1_0' not in globals():
    q1_0=0

bqm = dimod.BinaryQuadraticModel({'q0_1' : 1, 'q1_0' : 1, 'outq1_0' : 1, 'anc' : 4}, {('q0_1', 'q1_0') : 2, ('q0_1', 'outq1_0') : -2, ('q1_0', 'outq1_0') : -2, ('q0_1', 'anc') : -4, ('q1_0', 'anc') : -4, ('outq1_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_1']==q0_1 and sample['q1_0']==q1_0 and int(energy)==0:
        q0_1=sample['q0_1']
        q1_0=sample['outq1_0']
        tgt_before = sample['q1_0']
        break

print('#' * 80)
print("CNOT operation on q0_1 (control) and q1_0 (target):")
print("    in:  q0_1={0}, q1_0={1}".format(q0_1,tgt_before))
print("    out: q0_1={0}, q1_0={1}".format(q0_1,q1_0))
print('#' * 80)
print()
################################################################################
## CNOT - control: q0_2 target: q1_0 ##
################################################################################
if 'q0_2' not in globals():
    q0_2=0
if 'q1_0' not in globals():
    q1_0=0

bqm = dimod.BinaryQuadraticModel({'q0_2' : 1, 'q1_0' : 1, 'outq1_0' : 1, 'anc' : 4}, {('q0_2', 'q1_0') : 2, ('q0_2', 'outq1_0') : -2, ('q1_0', 'outq1_0') : -2, ('q0_2', 'anc') : -4, ('q1_0', 'anc') : -4, ('outq1_0', 'anc') : 4}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_2']==q0_2 and sample['q1_0']==q1_0 and int(energy)==0:
        q0_2=sample['q0_2']
        q1_0=sample['outq1_0']
        tgt_before = sample['q1_0']
        break

print('#' * 80)
print("CNOT operation on q0_2 (control) and q1_0 (target):")
print("    in:  q0_2={0}, q1_0={1}".format(q0_2,tgt_before))
print("    out: q0_2={0}, q1_0={1}".format(q0_2,q1_0))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_0 control2: q0_1 target: q1_1 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q0_1' not in globals():
    q0_1=0
if 'q1_1' not in globals():
    q1_1=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq1_1' : 1, 'q1_1' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq1_1') : 4, ('anc1','q1_1') : -4, ('anc2', 'q0_0') : -2, ('anc2', 'q0_1') : -2, ('anc2', 'outq1_1') : -2, ('anc2', 'q1_1') : 2, ('q0_0', 'q0_1') : 1, ('outq1_1', 'q1_1') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_0']==q0_0 and sample['q0_1']==q0_1 and sample['q1_1']==q1_1 and int(energy)==0:
        q0_0=sample['q0_0']
        q0_1=sample['q0_1']
        q1_1=sample['outq1_1']
        tgt_before = sample['q1_1']
        break

print('#' * 80)
print("CCNOT operation on q0_0 (control1), q0_1 (control2) and q1_1 (target):")
print("    in:  q0_0={0}, q0_1={1}, q1_1={2}".format(q0_0,q0_1,tgt_before))
print("    out: q0_0={0}, q0_1={1}, q1_1={2}".format(q0_0,q0_1,q1_1))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_1 control2: q0_2 target: q1_1 ##
################################################################################
if 'q0_1' not in globals():
    q0_1=0
if 'q0_2' not in globals():
    q0_2=0
if 'q1_1' not in globals():
    q1_1=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq1_1' : 1, 'q1_1' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq1_1') : 4, ('anc1','q1_1') : -4, ('anc2', 'q0_1') : -2, ('anc2', 'q0_2') : -2, ('anc2', 'outq1_1') : -2, ('anc2', 'q1_1') : 2, ('q0_1', 'q0_2') : 1, ('outq1_1', 'q1_1') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_1']==q0_1 and sample['q0_2']==q0_2 and sample['q1_1']==q1_1 and int(energy)==0:
        q0_1=sample['q0_1']
        q0_2=sample['q0_2']
        q1_1=sample['outq1_1']
        tgt_before = sample['q1_1']
        break

print('#' * 80)
print("CCNOT operation on q0_1 (control1), q0_2 (control2) and q1_1 (target):")
print("    in:  q0_1={0}, q0_2={1}, q1_1={2}".format(q0_1,q0_2,tgt_before))
print("    out: q0_1={0}, q0_2={1}, q1_1={2}".format(q0_1,q0_2,q1_1))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_2 control2: q0_0 target: q1_1 ##
################################################################################
if 'q0_2' not in globals():
    q0_2=0
if 'q0_0' not in globals():
    q0_0=0
if 'q1_1' not in globals():
    q1_1=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq1_1' : 1, 'q1_1' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq1_1') : 4, ('anc1','q1_1') : -4, ('anc2', 'q0_2') : -2, ('anc2', 'q0_0') : -2, ('anc2', 'outq1_1') : -2, ('anc2', 'q1_1') : 2, ('q0_2', 'q0_0') : 1, ('outq1_1', 'q1_1') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_2']==q0_2 and sample['q0_0']==q0_0 and sample['q1_1']==q1_1 and int(energy)==0:
        q0_2=sample['q0_2']
        q0_0=sample['q0_0']
        q1_1=sample['outq1_1']
        tgt_before = sample['q1_1']
        break

print('#' * 80)
print("CCNOT operation on q0_2 (control1), q0_0 (control2) and q1_1 (target):")
print("    in:  q0_2={0}, q0_0={1}, q1_1={2}".format(q0_2,q0_0,tgt_before))
print("    out: q0_2={0}, q0_0={1}, q1_1={2}".format(q0_2,q0_0,q1_1))
print('#' * 80)
print()
print("Measurement of q0_0 => {0}".format(q0_0))
print("Measurement of q0_1 => {0}".format(q0_1))
print("Measurement of q0_2 => {0}".format(q0_2))
print("Measurement of q1_0 => {0}".format(q1_0))
print("Measurement of q1_1 => {0}".format(q1_1))
