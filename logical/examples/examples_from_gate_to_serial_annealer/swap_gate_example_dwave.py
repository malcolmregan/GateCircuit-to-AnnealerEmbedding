#!/usr/bin/python3
import dimod

################################################################################
## SWAP - control: q0_0 target: q0_1 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q0_1' not in globals():
    q0_1=0

qubit_weights = {'q0_0' : 1, 'q0_1' : 1, 'outq0_0' : 1, 'outq0_1' : 1, 'a' : 6, 'b' : 6}
binding_weights = {('c', 'outq0_0') : 2,('c','outq0_1') : 2, ('c', 'a') : -4, ('c', 'b') : -4, ('q0_0', 'outq0_0') : -2, ('q0_0', 'a') : 2, ('q0_0', 'b') : -2, ('q0_1', 'outq0_1') : -2, ('q0_1', 'a') : -2, ('q0_1', 'b') : 2, ('outq0_0', 'a') : -4, ('outq0_1', 'b') : -4}
bqm = dimod.BinaryQuadraticModel(qubit_weights, binding_weights, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['c']==1 and sample['q0_0']==q0_0 and sample['q0_1']==q0_1 and int(energy)==0:
        q0_0=sample['outq0_0']
        q0_1=sample['outq0_1']
        tgt1_before = sample['q0_0']
        tgt2_before = sample['q0_1']
        break

print('#' * 80)
print("SWAP operation on q0_0 (control), q0_1 (target):")
print("    in:  q0_0={0}, q0_1={1}".format(tgt1_before, tgt2_before))
print("    out: q0_0={0}, q0_1={1}".format(q0_0, q0_1))
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
## SWAP - control: q0_0 target: q0_1 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q0_1' not in globals():
    q0_1=0

qubit_weights = {'q0_0' : 1, 'q0_1' : 1, 'outq0_0' : 1, 'outq0_1' : 1, 'a' : 6, 'b' : 6}
binding_weights = {('c', 'outq0_0') : 2,('c','outq0_1') : 2, ('c', 'a') : -4, ('c', 'b') : -4, ('q0_0', 'outq0_0') : -2, ('q0_0', 'a') : 2, ('q0_0', 'b') : -2, ('q0_1', 'outq0_1') : -2, ('q0_1', 'a') : -2, ('q0_1', 'b') : 2, ('outq0_0', 'a') : -4, ('outq0_1', 'b') : -4}
bqm = dimod.BinaryQuadraticModel(qubit_weights, binding_weights, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['c']==1 and sample['q0_0']==q0_0 and sample['q0_1']==q0_1 and int(energy)==0:
        q0_0=sample['outq0_0']
        q0_1=sample['outq0_1']
        tgt1_before = sample['q0_0']
        tgt2_before = sample['q0_1']
        break

print('#' * 80)
print("SWAP operation on q0_0 (control), q0_1 (target):")
print("    in:  q0_0={0}, q0_1={1}".format(tgt1_before, tgt2_before))
print("    out: q0_0={0}, q0_1={1}".format(q0_0, q0_1))
print('#' * 80)
print()
################################################################################
## SWAP - control: q0_0 target: q0_1 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q0_1' not in globals():
    q0_1=0

qubit_weights = {'q0_0' : 1, 'q0_1' : 1, 'outq0_0' : 1, 'outq0_1' : 1, 'a' : 6, 'b' : 6}
binding_weights = {('c', 'outq0_0') : 2,('c','outq0_1') : 2, ('c', 'a') : -4, ('c', 'b') : -4, ('q0_0', 'outq0_0') : -2, ('q0_0', 'a') : 2, ('q0_0', 'b') : -2, ('q0_1', 'outq0_1') : -2, ('q0_1', 'a') : -2, ('q0_1', 'b') : 2, ('outq0_0', 'a') : -4, ('outq0_1', 'b') : -4}
bqm = dimod.BinaryQuadraticModel(qubit_weights, binding_weights, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['c']==1 and sample['q0_0']==q0_0 and sample['q0_1']==q0_1 and int(energy)==0:
        q0_0=sample['outq0_0']
        q0_1=sample['outq0_1']
        tgt1_before = sample['q0_0']
        tgt2_before = sample['q0_1']
        break

print('#' * 80)
print("SWAP operation on q0_0 (control), q0_1 (target):")
print("    in:  q0_0={0}, q0_1={1}".format(tgt1_before, tgt2_before))
print("    out: q0_0={0}, q0_1={1}".format(q0_0, q0_1))
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
## SWAP - control: q0_0 target: q0_1 ##
################################################################################
if 'q0_0' not in globals():
    q0_0=0
if 'q0_1' not in globals():
    q0_1=0

qubit_weights = {'q0_0' : 1, 'q0_1' : 1, 'outq0_0' : 1, 'outq0_1' : 1, 'a' : 6, 'b' : 6}
binding_weights = {('c', 'outq0_0') : 2,('c','outq0_1') : 2, ('c', 'a') : -4, ('c', 'b') : -4, ('q0_0', 'outq0_0') : -2, ('q0_0', 'a') : 2, ('q0_0', 'b') : -2, ('q0_1', 'outq0_1') : -2, ('q0_1', 'a') : -2, ('q0_1', 'b') : 2, ('outq0_0', 'a') : -4, ('outq0_1', 'b') : -4}
bqm = dimod.BinaryQuadraticModel(qubit_weights, binding_weights, 0, dimod.BINARY)
sampler = dimod.ExactSolver()
response = sampler.sample(bqm)

for sample, energy in response.data(['sample', 'energy']):
    if sample['c']==1 and sample['q0_0']==q0_0 and sample['q0_1']==q0_1 and int(energy)==0:
        q0_0=sample['outq0_0']
        q0_1=sample['outq0_1']
        tgt1_before = sample['q0_0']
        tgt2_before = sample['q0_1']
        break

print('#' * 80)
print("SWAP operation on q0_0 (control), q0_1 (target):")
print("    in:  q0_0={0}, q0_1={1}".format(tgt1_before, tgt2_before))
print("    out: q0_0={0}, q0_1={1}".format(q0_0, q0_1))
print('#' * 80)
print()
print("Measurement of q0_0 => {0}".format(q0_0))
print("Measurement of q0_1 => {0}".format(q0_1))
