#!/usr/bin/env python
#
# Copyright (C) 2015 ycmd contributors.
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

from hamcrest import assert_that, has_entries
from typescript_handlers_test import Typescript_Handlers_test


class TypeScript_Subcommands_test( Typescript_Handlers_test ):

  def GetType_Basic_test( self ):
    filepath = self._PathToTestFile( 'test.ts' )
    contents = open( filepath ).read()

    event_data = self._BuildRequest( filepath = filepath,
                                     filetype = 'typescript',
                                     contents = contents,
                                     event_name = 'BufferVisit' )

    self._app.post_json( '/event_notification', event_data )

    gettype_data = self._BuildRequest( completer_target = 'filetype_default',
                                       command_arguments = [ 'GetType' ],
                                       line_num = 12,
                                       column_num = 1,
                                       contents = contents,
                                       filetype = 'typescript',
                                       filepath = filepath )

    response = self._app.post_json( '/run_completer_command', gettype_data ).json
    assert_that( response, self._MessageMatcher( 'var foo: Foo' ) )


  def GetType_HasNoType_test( self ):
    filepath = self._PathToTestFile( 'test.ts' )
    contents = open( filepath ).read()

    event_data = self._BuildRequest( filepath = filepath,
                                     filetype = 'typescript',
                                     contents = contents,
                                     event_name = 'BufferVisit' )

    self._app.post_json( '/event_notification', event_data )

    gettype_data = self._BuildRequest( completer_target = 'filetype_default',
                                       command_arguments = [ 'GetType' ],
                                       line_num = 2,
                                       column_num = 1,
                                       contents = contents,
                                       filetype = 'typescript',
                                       filepath = filepath )

    response = self._app.post_json( '/run_completer_command',
                                    gettype_data,
                                    expect_errors = True ).json
    assert_that( response,
                 self._ErrorMatcher( RuntimeError, 'No content available.' ) )


  def GetDoc_Method_test( self ):
    filepath = self._PathToTestFile( 'test.ts' )
    contents = open( filepath ).read()

    event_data = self._BuildRequest( filepath = filepath,
                                     filetype = 'typescript',
                                     contents = contents,
                                     event_name = 'BufferVisit' )

    self._app.post_json( '/event_notification', event_data )

    gettype_data = self._BuildRequest( completer_target = 'filetype_default',
                                       command_arguments = [ 'GetDoc' ],
                                       line_num = 29,
                                       column_num = 9,
                                       contents = contents,
                                       filetype = 'typescript',
                                       filepath = filepath )

    response = self._app.post_json( '/run_completer_command',
                                    gettype_data ).json
    assert_that( response,
                 has_entries( {
                   'detailed_info': '(method) Bar.testMethod(): void\n\n'
                                    'Method documentation',
                 } ) )


  def GetDoc_Class_test( self ):
    filepath = self._PathToTestFile( 'test.ts' )
    contents = open( filepath ).read()

    event_data = self._BuildRequest( filepath = filepath,
                                     filetype = 'typescript',
                                     contents = contents,
                                     event_name = 'BufferVisit' )

    self._app.post_json( '/event_notification', event_data )

    gettype_data = self._BuildRequest( completer_target = 'filetype_default',
                                       command_arguments = [ 'GetDoc' ],
                                       line_num = 31,
                                       column_num = 2,
                                       contents = contents,
                                       filetype = 'typescript',
                                       filepath = filepath )

    response = self._app.post_json( '/run_completer_command',
                                    gettype_data ).json
    assert_that( response,
                 has_entries( {
                   'detailed_info': 'class Bar\n\n'
                                    'Class documentation\n\n'
                                    'Multi-line',
                 } ) )
