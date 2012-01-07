#     Copyright 2012, Kay Hayen, mailto:kayhayen@gmx.de
#
#     Python tests originally created or extracted from other peoples work. The
#     parts were too small to be protected.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
"Some doc"

def tryScope1(x):
    try:
        try:
            x += 1
        finally:
            print "Finally is executed"

            try:
                z = 1
            finally:
                print "Deep Nested finally is executed"
    except:
        print "Exception occured"
    else:
        print "No exception occured"

tryScope1( 1 )
print "*" * 20
tryScope1( [ 1 ] )

def tryScope2( x, someExceptionClass ):
    try:
        x += 1
    except someExceptionClass, e:
        print "Exception class from argument occured:", someExceptionClass, e
    else:
        print "No exception occured"

def tryScope3( x ):
    if x:
        try:
            x += 1
        except TypeError:
            print "TypeError occured"
    else:
        print "Not taken"


print "*" * 20

tryScope2( 1, TypeError )
tryScope2( [ 1 ], TypeError )

print "*" * 20

tryScope3( 1 )
tryScope3( [ 1 ] )
tryScope3( [] )

print "*" * 20

def tryScope4( x ):
    try:
        x += 1
    except:
        print "exception occured"
    else:
        print "no exception occured"
    finally:
        print "finally obeyed"

tryScope4( 1 )
tryScope4( [ 1 ] )
