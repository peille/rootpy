#!/usr/bin/env python

'''

Examples of using the TreeChain class, a replacement for TChain

'''

from random import gauss
from rootpy.io import open
from rootpy.tree import Tree, TreeChain

# Make two files, each with a Tree called "test"

print "Creating test tree in chaintest1.root"
f = open("chaintest1.root", "recreate")

tree = Tree("test")
tree.create_branches([('x', 'F'),
                      ('y', 'F'),
                      ('z', 'F'),
                      ('i', 'I')])

for i in xrange(10000):
    tree.x = gauss(.5, 1.)
    tree.y = gauss(.3, 2.)
    tree.z = gauss(13., 42.)
    tree.i = i
    tree.fill()

# Make a histogram of x when y > 1
hist1 = tree.Draw('x', 'y > 1', min=-10, max=10, bins=100).Clone()
hist1.SetName('hist1')
hist1.SetDirectory(0) # memory resident
print "The first tree has %f entries where y > 1" % hist1.Integral()

tree.write()
f.close()

print "Creating test tree in chaintest2.root"
f = open("chaintest2.root", "recreate")

tree = Tree("test")
tree.create_branches([('x', 'F'),
                      ('y', 'F'),
                      ('z', 'F'),
                      ('i', 'I')])

for i in xrange(10000):
    tree.x = gauss(.5, 1.)
    tree.y = gauss(.3, 2.)
    tree.z = gauss(13., 42.)
    tree.i = i
    tree.fill()
tree.write()
# Make a histogram of the second tree
hist2 = tree.Draw('x', 'y > 1', min=-10, max=10, bins=100).Clone()
hist2.SetName('hist2')
hist2.SetDirectory(0) # memory resident
print "The second tree has %f entries where y > 1" % hist2.Integral()
f.close()

combined_hist = hist1 + hist2

print "Building TreeChain"
chain = TreeChain('test', ['chaintest2.root', 'chaintest1.root'])
# Make the equivalent of the combined_hist
combined_hist_chain = chain.Draw('x', 'y > 1', min=-10, max=10, bins=100)

residual = combined_hist_chain - combined_hist
print "The combined histogram (separately) minus the combined from the chain "\
        "has %f entries" % residual.Integral()

