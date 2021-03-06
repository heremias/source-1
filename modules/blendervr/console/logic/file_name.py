# -*- coding: utf-8 -*-
# file: blendervr/console/logic/file_name.py

## Copyright (C) LIMSI-CNRS (2014)
##
## contributor(s) : Jorge Gascon, Damien Touraine, David Poirier-Quinot,
## Laurent Pointal, Julian Adenauer,
##
## This software is a computer program whose purpose is to distribute
## blender to render on Virtual Reality device systems.
##
## This software is governed by the CeCILL  license under French law and
## abiding by the rules of distribution of free software.  You can  use,
## modify and/ or redistribute the software under the terms of the CeCILL
## license as circulated by CEA, CNRS and INRIA at the following URL
## "http://www.cecill.info".
##
## As a counterpart to the access to the source code and  rights to copy,
## modify and redistribute granted by the license, users are provided only
## with a limited warranty  and the software's author,  the holder of the
## economic rights,  and the successive licensors  have only  limited
## liability.
##
## In this respect, the user's attention is drawn to the risks associated
## with loading,  using,  modifying and/or developing or reproducing the
## software by the user in light of its specific status of free software,
## that may mean  that it is complicated to manipulate,  and  that  also
## therefore means  that it is reserved for developers  and  experienced
## professionals having in-depth computer knowledge. Users are therefore
## encouraged to load and test the software's suitability as regards their
## requirements in conditions enabling the security of their systems and/or
## data to be ensured and,  more generally, to use and operate it in the
## same conditions as regards security.
##
## The fact that you are presently reading this means that you have had
## knowledge of the CeCILL license and that you accept its terms.
##

import os


class FileName:

    def __init__(self, file_name, anchor=None):
        self._file_name = file_name
        self.strip(anchor)

    def strip(self, anchor):
        if self._file_name and anchor and \
                            (not hasattr(self, '_origin_file_name')):
            relpath = os.path.relpath(self._file_name, anchor)
            if not relpath.startswith('..'):
                self._origin_file_name = self._file_name.replace('\\', '/')
                self._file_name = relpath.replace('\\', '/')

    def unstrip(self, anchor):
        if not self._file_name:
            return None

        if hasattr(self, '_origin_file_name'):
            if anchor:
                return os.path.join(anchor, self._file_name).replace('\\', '/')
            return self._origin_file_name

        if anchor:
            raise Exception('Invalid apply of anchor')
        return self._file_name
