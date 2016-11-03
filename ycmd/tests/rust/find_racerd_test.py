# Copyright (C) 2016 ycmd contributors
#
# This file is part of ycmd.
#
# ycmd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ycmd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ycmd.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from future import standard_library
standard_library.install_aliases()
from builtins import *  # noqa

from hamcrest import assert_that, equal_to
from mock import patch

from ycmd import user_options_store
from ycmd.tests.test_utils import UserOption, TemporaryExecutable
from ycmd.completers.rust.rust_completer import ( FindRacerdBinary,
                                                  RACERD_BINARY_RELEASE,
                                                  RACERD_BINARY_DEBUG )


def FindRacerdBinary_UseRacerdSpecifiedByTheUser_test():
  with TemporaryExecutable() as fake_racerd_binary:
    with UserOption( 'racerd_binary_path', fake_racerd_binary ) as user_options:
      assert_that( FindRacerdBinary( user_options ),
                   equal_to( fake_racerd_binary ) )


@patch( 'ycmd.completers.rust.rust_completer._ExistsReleaseRacerd',
        return_value = True )
def FindRacerdBinary_UseVendoredReleaseVersionIfAvailabe_test( *args ):
  assert_that( FindRacerdBinary( user_options_store.DefaultOptions() ),
               equal_to( RACERD_BINARY_RELEASE ) )


@patch( 'ycmd.completers.rust.rust_completer._ExistsReleaseRacerd',
        return_value = False )
@patch( 'ycmd.completers.rust.rust_completer._ExistsDebugRacerd',
        return_value = True )
def FindRacerdBinary_UseVendoredDebugVersionIfAvailabe_test( *args ):
  assert_that( FindRacerdBinary( user_options_store.DefaultOptions() ),
               equal_to( RACERD_BINARY_DEBUG ) )


@patch( 'ycmd.completers.rust.rust_completer._ExistsReleaseRacerd',
        return_value = False )
@patch( 'ycmd.completers.rust.rust_completer._ExistsDebugRacerd',
        return_value = False )
@patch( 'ycmd.utils.PathToFirstExistingExecutable', return_value = '/a/racerd' )
def FindRacerdBinary_UseFirstAvailableRacerdAsLastResort_test( *args ):
  assert_that( FindRacerdBinary( user_options_store.DefaultOptions() ),
               equal_to( '/a/racerd' ) )
