#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste


class HierCluster:
    """
    Class used to return results of hierarchical clustering used in
    prestools.clustering.
    """

    def __init__(self):
        self._linkage = None
        self._pair_dist = None
        self._coph_dist = None
        self._coph_matr = None

    @property
    def linkage(self):
        return self._linkage

    @linkage.setter
    def linkage(self, value):
        self._linkage = value

    @property
    def pair_dist(self):
        return self._pair_dist

    @pair_dist.setter
    def pair_dist(self, value):
        self._pair_dist = value

    @property
    def coph_dist(self):
        return self._coph_dist

    @coph_dist.setter
    def coph_dist(self, value):
        self._coph_dist = value

    @property
    def coph_matr(self):
        return self._coph_matr

    @coph_matr.setter
    def coph_matr(self, value):
        self._coph_matr = value

    def __repr__(self):
        return """HierCluster(
        linkage: {}, 
        pair_dist: {}, 
        coph_dist: {}, 
        coph_matr: {}
        )""".format(self.linkage,
                    self.pair_dist,
                    self.coph_dist,
                    self.coph_matr)
