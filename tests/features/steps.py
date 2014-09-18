# -*- coding: utf-8 -*-
from lettuce import *
import app.match as m


@step(u'"([^"]*)" and "([^"]*)" start a match to "([^"]*)" sets')
def group1_and_group2_start_a_match_to_group3_sets(step, g1, g2, g3):
    world.match = m.Match(g1, g2, g3)


@step(u'When: "([^"]*)" and "([^"]*)" start a match to "([^"]*)" sets')
def when_group1_and_group2_start_a_match_to_group3_sets(step, g1, g2, g3):
    assert False, 'This step must be implemented'


@step(u'I see score: "([^"]*)"')
def then_i_see_score_group1(step, group1):
    assert world.match.score() == group1, 'Error got: ' + world.match.score()


@step(u'When: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def when_group1_won_the_group2_set_group3_group4(step, g1, g2, g3, g4):
    assert False, 'This step must be implemented'


@step(u'And: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def and_group1_won_the_group2_set_group3_group4(step, g1, g2, g3, g4):
    assert False, 'This step must be implemented'


@step(u'Then: The match score is: "([^"]*)"')
def then_the_match_score_is_group1(step, group1):
    assert False, 'This step must be implemented'
