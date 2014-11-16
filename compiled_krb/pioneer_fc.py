# pioneer_fc.py

from __future__ import with_statement
from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def obstacleFront(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('distObsVal') < 0.25:
          engine.assert_('env', 'detected',
                         (rule.pattern(0).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def obstacleActionLeft(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'detected', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('env', 'dist', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('distObsVal') < 0.25:
              engine.assert_('env', 'action',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(1).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def obstacleActionRight(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        if context.lookup_data('distObsVal') < 0.25:
          engine.assert_('env', 'action',
                         (rule.pattern(0).as_data(context),
                          rule.pattern(1).as_data(context),)),
          rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def noObstacle(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('env', 'dist', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        with knowledge_base.Gen_once if index == 1 \
                 else engine.lookup('env', 'dist', context,
                                    rule.foreach_patterns(1)) \
          as gen_1:
          for dummy in gen_1:
            if context.lookup_data('dist1') >= 0.25 and context.lookup_data('dist2') >= 0.25:
              engine.assert_('env', 'action',
                             (rule.pattern(0).as_data(context),
                              rule.pattern(0).as_data(context),)),
              rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('pioneer')
  
  fc_rule.fc_rule('obstacleFront', This_rule_base, obstacleFront,
    (('env', 'dist',
      (pattern.pattern_literal('Left'),
       contexts.variable('distObsVal'),),
      False),),
    (pattern.pattern_literal('Obstacle_'),))
  
  fc_rule.fc_rule('obstacleActionLeft', This_rule_base, obstacleActionLeft,
    (('env', 'detected',
      (pattern.pattern_literal('Obstacle_'),),
      False),
     ('env', 'dist',
      (pattern.pattern_literal('Left'),
       contexts.variable('distObsVal'),),
      False),),
    (pattern.pattern_literal(1),
     pattern.pattern_literal(-1),))
  
  fc_rule.fc_rule('obstacleActionRight', This_rule_base, obstacleActionRight,
    (('env', 'dist',
      (pattern.pattern_literal('Right'),
       contexts.variable('distObsVal'),),
      False),),
    (pattern.pattern_literal(-1),
     pattern.pattern_literal(1),))
  
  fc_rule.fc_rule('noObstacle', This_rule_base, noObstacle,
    (('env', 'dist',
      (pattern.pattern_literal('Left'),
       contexts.variable('dist1'),),
      False),
     ('env', 'dist',
      (pattern.pattern_literal('Right'),
       contexts.variable('dist2'),),
      False),),
    (pattern.pattern_literal(1),))


Krb_filename = '..\\pioneer.krb'
Krb_lineno_map = (
    ((13, 17), (4, 4)),
    ((18, 18), (5, 5)),
    ((19, 20), (7, 7)),
    ((29, 33), (11, 11)),
    ((34, 38), (12, 12)),
    ((39, 39), (13, 13)),
    ((40, 42), (15, 15)),
    ((51, 55), (20, 20)),
    ((56, 56), (21, 21)),
    ((57, 59), (23, 23)),
    ((68, 72), (28, 28)),
    ((73, 77), (29, 29)),
    ((78, 78), (30, 30)),
    ((79, 81), (32, 32)),
)
