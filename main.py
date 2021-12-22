import machine as m
import pickle

e = m.Enigma()
r = 'ABC'
org = 'this is a first test for the enigma simulator'

print('Original text "{}"'.format(org))
print('Rotor position {}\n'.format(r))
e.set_rotor_position(r)

cypher = e.encipher(org)
print('encripted text "{}"'.format(cypher))

e.set_rotor_position(r)
plain = e.decipher(cypher)
print('decripted text "{}"'.format(plain))
