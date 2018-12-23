#!/usr/bin/python3
import dimod

################################################################################
## CCNOT - control1: q0_0 control2: q0_1 target: q0_2 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q0_1' not in globals():
    q0_1=0
if 'q0_2' not in globals():
    q0_2=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq0_2' : 1, 'q0_2' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq0_2') : 4, ('anc1','q0_2') : -4, ('anc2', 'q0_0') : -2, ('anc2', 'q0_1') : -2, ('anc2', 'outq0_2') : -2, ('anc2', 'q0_2') : 2, ('q0_0', 'q0_1') : 1, ('outq0_2', 'q0_2') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_0']==q0_0 and sample['q0_1']==q0_1 and sample['q0_2']==q0_2 and int(energy)==0:
        q0_0=sample['q0_0']
        q0_1=sample['q0_1']
        q0_2=sample['outq0_2']
        tgt_before = sample['q0_2']
        break

print('#' * 80)
print("CCNOT operation on q0_0 (control1), q0_1 (control2) and q0_2 (target):")
print("    in:  q0_0={0}, q0_1={1}, q0_2={2}".format(q0_0,q0_1,tgt_before))
print("    out: q0_0={0}, q0_1={1}, q0_2={2}".format(q0_0,q0_1,q0_2))
print('#' * 80)
print()
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
## CCNOT - control1: q0_0 control2: q0_1 target: q0_2 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q0_1' not in globals():
    q0_1=0
if 'q0_2' not in globals():
    q0_2=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq0_2' : 1, 'q0_2' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq0_2') : 4, ('anc1','q0_2') : -4, ('anc2', 'q0_0') : -2, ('anc2', 'q0_1') : -2, ('anc2', 'outq0_2') : -2, ('anc2', 'q0_2') : 2, ('q0_0', 'q0_1') : 1, ('outq0_2', 'q0_2') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_0']==q0_0 and sample['q0_1']==q0_1 and sample['q0_2']==q0_2 and int(energy)==0:
        q0_0=sample['q0_0']
        q0_1=sample['q0_1']
        q0_2=sample['outq0_2']
        tgt_before = sample['q0_2']
        break

print('#' * 80)
print("CCNOT operation on q0_0 (control1), q0_1 (control2) and q0_2 (target):")
print("    in:  q0_0={0}, q0_1={1}, q0_2={2}".format(q0_0,q0_1,tgt_before))
print("    out: q0_0={0}, q0_1={1}, q0_2={2}".format(q0_0,q0_1,q0_2))
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
## CCNOT - control1: q0_0 control2: q0_1 target: q0_2 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q0_1' not in globals():
    q0_1=0
if 'q0_2' not in globals():
    q0_2=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq0_2' : 1, 'q0_2' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq0_2') : 4, ('anc1','q0_2') : -4, ('anc2', 'q0_0') : -2, ('anc2', 'q0_1') : -2, ('anc2', 'outq0_2') : -2, ('anc2', 'q0_2') : 2, ('q0_0', 'q0_1') : 1, ('outq0_2', 'q0_2') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_0']==q0_0 and sample['q0_1']==q0_1 and sample['q0_2']==q0_2 and int(energy)==0:
        q0_0=sample['q0_0']
        q0_1=sample['q0_1']
        q0_2=sample['outq0_2']
        tgt_before = sample['q0_2']
        break

print('#' * 80)
print("CCNOT operation on q0_0 (control1), q0_1 (control2) and q0_2 (target):")
print("    in:  q0_0={0}, q0_1={1}, q0_2={2}".format(q0_0,q0_1,tgt_before))
print("    out: q0_0={0}, q0_1={1}, q0_2={2}".format(q0_0,q0_1,q0_2))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_0 control2: q0_1 target: q0_2 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q0_1' not in globals():
    q0_1=0
if 'q0_2' not in globals():
    q0_2=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq0_2' : 1, 'q0_2' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq0_2') : 4, ('anc1','q0_2') : -4, ('anc2', 'q0_0') : -2, ('anc2', 'q0_1') : -2, ('anc2', 'outq0_2') : -2, ('anc2', 'q0_2') : 2, ('q0_0', 'q0_1') : 1, ('outq0_2', 'q0_2') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_0']==q0_0 and sample['q0_1']==q0_1 and sample['q0_2']==q0_2 and int(energy)==0:
        q0_0=sample['q0_0']
        q0_1=sample['q0_1']
        q0_2=sample['outq0_2']
        tgt_before = sample['q0_2']
        break

print('#' * 80)
print("CCNOT operation on q0_0 (control1), q0_1 (control2) and q0_2 (target):")
print("    in:  q0_0={0}, q0_1={1}, q0_2={2}".format(q0_0,q0_1,tgt_before))
print("    out: q0_0={0}, q0_1={1}, q0_2={2}".format(q0_0,q0_1,q0_2))
print('#' * 80)
print()
################################################################################
## CCNOT - control1: q0_0 control2: q0_1 target: q0_2 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q0_1' not in globals():
    q0_1=0
if 'q0_2' not in globals():
    q0_2=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq0_2' : 1, 'q0_2' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq0_2') : 4, ('anc1','q0_2') : -4, ('anc2', 'q0_0') : -2, ('anc2', 'q0_1') : -2, ('anc2', 'outq0_2') : -2, ('anc2', 'q0_2') : 2, ('q0_0', 'q0_1') : 1, ('outq0_2', 'q0_2') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_0']==q0_0 and sample['q0_1']==q0_1 and sample['q0_2']==q0_2 and int(energy)==0:
        q0_0=sample['q0_0']
        q0_1=sample['q0_1']
        q0_2=sample['outq0_2']
        tgt_before = sample['q0_2']
        break

print('#' * 80)
print("CCNOT operation on q0_0 (control1), q0_1 (control2) and q0_2 (target):")
print("    in:  q0_0={0}, q0_1={1}, q0_2={2}".format(q0_0,q0_1,tgt_before))
print("    out: q0_0={0}, q0_1={1}, q0_2={2}".format(q0_0,q0_1,q0_2))
print('#' * 80)
print()
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
## CCNOT - control1: q0_0 control2: q0_1 target: q0_2 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q0_1' not in globals():
    q0_1=0
if 'q0_2' not in globals():
    q0_2=0

bqm = dimod.BinaryQuadraticModel({'anc1' : 4, 'anc2' : 4, 'outq0_2' : 1, 'q0_2' : 1}, {('anc1', 'anc2') : -4, ('anc1', 'outq0_2') : 4, ('anc1','q0_2') : -4, ('anc2', 'q0_0') : -2, ('anc2', 'q0_1') : -2, ('anc2', 'outq0_2') : -2, ('anc2', 'q0_2') : 2, ('q0_0', 'q0_1') : 1, ('outq0_2', 'q0_2') : -2}, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['q0_0']==q0_0 and sample['q0_1']==q0_1 and sample['q0_2']==q0_2 and int(energy)==0:
        q0_0=sample['q0_0']
        q0_1=sample['q0_1']
        q0_2=sample['outq0_2']
        tgt_before = sample['q0_2']
        break

print('#' * 80)
print("CCNOT operation on q0_0 (control1), q0_1 (control2) and q0_2 (target):")
print("    in:  q0_0={0}, q0_1={1}, q0_2={2}".format(q0_0,q0_1,tgt_before))
print("    out: q0_0={0}, q0_1={1}, q0_2={2}".format(q0_0,q0_1,q0_2))
print('#' * 80)
print()
print("Measurement of q0_0 => {0}".format(q0_0))
print("Measurement of q0_1 => {0}".format(q0_1))
print("Measurement of q0_2 => {0}".format(q0_2))
