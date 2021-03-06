# coding: utf-8
# 2019/11/27 @ tongshiwei

import pytest
import gym


@pytest.fixture(scope="module")
def env():
    return gym.make('KSS-v0', learner_num=50)


@pytest.fixture(scope="module")
def learner(env):
    yield env.begin_episode()
    env.end_episode()


@pytest.fixture(scope="module")
def q_bank(env):
    return env.q_bank


@pytest.fixture(scope="module")
def tester(env):
    return env.tester
