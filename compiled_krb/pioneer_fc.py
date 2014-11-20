# pioneer_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def obstacle1(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('distance')<0.5:
          engine.assert_('env', 'action',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def obstacle2(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('distance')<0.40:
          engine.assert_('env', 'action',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def obstacle3(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('distance')<0.5:
          engine.assert_('env', 'action',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def obstacle4(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('distance')<0.5:
          engine.assert_('env', 'action',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def obstacle5(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('distance')<0.5:
          engine.assert_('env', 'action',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def obstacle6(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('distance')<0.5:
          engine.assert_('env', 'action',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def obstacle7(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('distance')<0.4:
          engine.assert_('env', 'action',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def obstacle8(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('distance')<0.5:
          engine.assert_('env', 'action',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def obstacle9(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('distance')<0.25:
          engine.assert_('env', 'action',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def obstacle10(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('distance')<0.25:
          engine.assert_('env', 'action',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def obstacle11(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('distance')<0.25:
          engine.assert_('env', 'action',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def obstacle12(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('distance')<0.25:
          engine.assert_('env', 'action',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def obstacle13(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('distance')<0.25:
          engine.assert_('env', 'action',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def obstacle14(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('distance')<0.25:
          engine.assert_('env', 'action',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def obstacle15(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('distance')<0.25:
          engine.assert_('env', 'action',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def obstacle16(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('distance')<0.25:
          engine.assert_('env', 'action',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),
                          rule.pattern(2).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('pioneer')
  
  fc_rule.fc_rule('obstacle1', This_rule_base, obstacle1,
    (('env', 'dist',
      (pattern.pattern_literal(1),
       contexts.variable('distance'),),
      False),),
    (pattern.pattern_literal(0.2),
     pattern.pattern_literal(0),
     pattern.pattern_literal(1),))
  
  fc_rule.fc_rule('obstacle2', This_rule_base, obstacle2,
    (('env', 'dist',
      (pattern.pattern_literal(2),
       contexts.variable('distance'),),
      False),),
    (pattern.pattern_literal(1.25),
     pattern.pattern_literal(1),
     pattern.pattern_literal(2),))
  
  fc_rule.fc_rule('obstacle3', This_rule_base, obstacle3,
    (('env', 'dist',
      (pattern.pattern_literal(3),
       contexts.variable('distance'),),
      False),),
    (pattern.pattern_literal(0),
     pattern.pattern_literal(-0.5),
     pattern.pattern_literal(3),))
  
  fc_rule.fc_rule('obstacle4', This_rule_base, obstacle4,
    (('env', 'dist',
      (pattern.pattern_literal(4),
       contexts.variable('distance'),),
      False),),
    (pattern.pattern_literal(-2),
     pattern.pattern_literal(-2.5),
     pattern.pattern_literal(4),))
  
  fc_rule.fc_rule('obstacle5', This_rule_base, obstacle5,
    (('env', 'dist',
      (pattern.pattern_literal(5),
       contexts.variable('distance'),),
      False),),
    (pattern.pattern_literal(-2.5),
     pattern.pattern_literal(-2),
     pattern.pattern_literal(5),))
  
  fc_rule.fc_rule('obstacle6', This_rule_base, obstacle6,
    (('env', 'dist',
      (pattern.pattern_literal(6),
       contexts.variable('distance'),),
      False),),
    (pattern.pattern_literal(-0.5),
     pattern.pattern_literal(0),
     pattern.pattern_literal(6),))
  
  fc_rule.fc_rule('obstacle7', This_rule_base, obstacle7,
    (('env', 'dist',
      (pattern.pattern_literal(7),
       contexts.variable('distance'),),
      False),),
    (pattern.pattern_literal(1),
     pattern.pattern_literal(1.25),
     pattern.pattern_literal(7),))
  
  fc_rule.fc_rule('obstacle8', This_rule_base, obstacle8,
    (('env', 'dist',
      (pattern.pattern_literal(8),
       contexts.variable('distance'),),
      False),),
    (pattern.pattern_literal(0.2),
     pattern.pattern_literal(0.5),
     pattern.pattern_literal(8),))
  
  fc_rule.fc_rule('obstacle9', This_rule_base, obstacle9,
    (('env', 'dist',
      (pattern.pattern_literal(9),
       contexts.variable('distance'),),
      False),),
    (pattern.pattern_literal(0),
     pattern.pattern_literal(0.2),
     pattern.pattern_literal(9),))
  
  fc_rule.fc_rule('obstacle10', This_rule_base, obstacle10,
    (('env', 'dist',
      (pattern.pattern_literal(10),
       contexts.variable('distance'),),
      False),),
    (pattern.pattern_literal(0.5),
     pattern.pattern_literal(1),
     pattern.pattern_literal(10),))
  
  fc_rule.fc_rule('obstacle11', This_rule_base, obstacle11,
    (('env', 'dist',
      (pattern.pattern_literal(11),
       contexts.variable('distance'),),
      False),),
    (pattern.pattern_literal(1),
     pattern.pattern_literal(1.25),
     pattern.pattern_literal(11),))
  
  fc_rule.fc_rule('obstacle12', This_rule_base, obstacle12,
    (('env', 'dist',
      (pattern.pattern_literal(12),
       contexts.variable('distance'),),
      False),),
    (pattern.pattern_literal(1),
     pattern.pattern_literal(1.5),
     pattern.pattern_literal(12),))
  
  fc_rule.fc_rule('obstacle13', This_rule_base, obstacle13,
    (('env', 'dist',
      (pattern.pattern_literal(13),
       contexts.variable('distance'),),
      False),),
    (pattern.pattern_literal(1.5),
     pattern.pattern_literal(1),
     pattern.pattern_literal(13),))
  
  fc_rule.fc_rule('obstacle14', This_rule_base, obstacle14,
    (('env', 'dist',
      (pattern.pattern_literal(14),
       contexts.variable('distance'),),
      False),),
    (pattern.pattern_literal(1.25),
     pattern.pattern_literal(1),
     pattern.pattern_literal(14),))
  
  fc_rule.fc_rule('obstacle15', This_rule_base, obstacle15,
    (('env', 'dist',
      (pattern.pattern_literal(15),
       contexts.variable('distance'),),
      False),),
    (pattern.pattern_literal(1),
     pattern.pattern_literal(0.5),
     pattern.pattern_literal(15),))
  
  fc_rule.fc_rule('obstacle16', This_rule_base, obstacle16,
    (('env', 'dist',
      (pattern.pattern_literal(16),
       contexts.variable('distance'),),
      False),),
    (pattern.pattern_literal(0.2),
     pattern.pattern_literal(0),
     pattern.pattern_literal(16),))


Krb_filename = '../pioneer.krb'
Krb_lineno_map = (
    ((13, 17), (3, 3)),
    ((18, 18), (4, 4)),
    ((19, 22), (6, 6)),
    ((31, 35), (10, 10)),
    ((36, 36), (11, 11)),
    ((37, 40), (13, 13)),
    ((49, 53), (17, 17)),
    ((54, 54), (18, 18)),
    ((55, 58), (20, 20)),
    ((67, 71), (24, 24)),
    ((72, 72), (25, 25)),
    ((73, 76), (27, 27)),
    ((85, 89), (31, 31)),
    ((90, 90), (32, 32)),
    ((91, 94), (34, 34)),
    ((103, 107), (38, 38)),
    ((108, 108), (39, 39)),
    ((109, 112), (41, 41)),
    ((121, 125), (45, 45)),
    ((126, 126), (46, 46)),
    ((127, 130), (48, 48)),
    ((139, 143), (52, 52)),
    ((144, 144), (53, 53)),
    ((145, 148), (55, 55)),
    ((157, 161), (59, 59)),
    ((162, 162), (60, 60)),
    ((163, 166), (62, 62)),
    ((175, 179), (66, 66)),
    ((180, 180), (67, 67)),
    ((181, 184), (69, 69)),
    ((193, 197), (73, 73)),
    ((198, 198), (74, 74)),
    ((199, 202), (76, 76)),
    ((211, 215), (80, 80)),
    ((216, 216), (81, 81)),
    ((217, 220), (83, 83)),
    ((229, 233), (88, 88)),
    ((234, 234), (89, 89)),
    ((235, 238), (91, 91)),
    ((247, 251), (96, 96)),
    ((252, 252), (97, 97)),
    ((253, 256), (99, 99)),
    ((265, 269), (103, 103)),
    ((270, 270), (104, 104)),
    ((271, 274), (106, 106)),
    ((283, 287), (110, 110)),
    ((288, 288), (111, 111)),
    ((289, 292), (113, 113)),
)
