# -*- coding: utf-8 -*-
"""
Created on Mon May 15 20:45:53 2023

@author: g361a609
"""

import numpy as np
import math

class Random:
    def __init__(self, seed=4445):
        self.seed, self.m_v, self.m_w, self.m_u = seed, np.uint64(4101842887655102017), np.uint64(1), np.uint64(1)
        self.m_u, self.m_v, self.m_w = np.uint64(self.seed) ^ self.m_v, self.m_u, self.m_v
        self.int64()

    def int64(self):
        with np.errstate(over='ignore'):
            self.m_u = np.uint64(self.m_u * np.uint64(2862933555777941757) + np.uint64(7046029254386353087))
        self.m_v ^= self.m_v >> np.uint64(17)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8)
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21)))
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4)
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w

    def rand(self):
        return 5.42101086242752217E-20 * self.int64()

    def Categorical(self, *args):
        if not all(0 <= p <= 1 for p in args):
            return None
        R = self.rand()
        for i, p in enumerate(args, start=1):
            if R < p:
                return i
            R -= p

    def Exponential(self, beta=1.):
        beta = max(0.0000001, beta)
        R = self.rand()
        while R <= 0.:
            R = self.rand()
        return -math.log(R)/beta

    def Bernoulli(self, p=0.6):
        p = max(0.0000001, min(0.9999999, p))
        return int(self.rand() < p)

    def TruncExp(self, beta, bottom, top):
        a = self.Exponential(beta)
        while not (bottom <= a <= top):
            a = self.Exponential(beta)
        return a
