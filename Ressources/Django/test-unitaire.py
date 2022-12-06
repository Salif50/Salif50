#unit test
assertTrue(a) # a is True
assertFalse(a) # a is False

assertEqual(a, b) # a == b
assertNotEqual(a, b) # a != b

assertGreater(a, b) # a > b
assertGreaterEqual(a, b) # a >= b
assertLess(a, b) # a < b
assertLessEqual(a, b) # a <= b

assertIs(a, b) # a is b
assertIsNot(a, b) # a is not b

assertIsNone(a) # a is None
assertIsNotNone(a) # a is not None

assertIn(a, b) # a in b
assertNotIn(a, b) # a not in b

assertIsInstance(a, ClassName) # isinstance(a, ClassName)
assertNotIsInstance(a, ClassName) # not isinstance(a, ClassName)
assertMultiLineEqual(s1, s2) # compare deux chaînes
assertSequenceEqual(s1, s2) # compare deux séquences
assertListEqual(l1, l2) # compare deux listes
assertTupleEqual(t1, t2) # compare deux tuples
assertSetEqual(s1, s2) # compare deux ensembles
assertDictEqual(d1, d2) # compare deux dictionnaires
assertAlmostEqual(a, b) # round(a-b, 7) == 0
assertNotAlmostEqual(a, b) # round(a-b, 7) != 0

assertCountEqual(a, b) # mêmes éléments dans le même nombre + même ordre

assertRegex(s, r) # l'expression rationnelle correspond à la chaîne
assertNotRegex(s, r) # l'expression rationnelle ne correspond pas à la chaîne
assertRaises(exception, function, *args, **kwds) # fonction génère exception
assertRaisesRegex(exception, regex, function, *args, **kwds) # fonction génère exception + valide regex

assertWarns(warning, function, *args, **kwds) # fonction génère avertissement
assertWarnsRegex(exception, regex, function, *args, **kwds) # fonction génère avertissement + valide regex

assertLogs(logger, level) 
