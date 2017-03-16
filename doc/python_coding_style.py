"""
    Following file is a document which describe coding style for  project.
    It doesn't contain any useful code for project.
"""

# ------------------------------- Basics --------------------------------------
"""
    Use PEP8 coding style convention
    All the codes which do not conflict with this document can be ignored in IDE using settings
    @see {http://pep8.readthedocs.org/en/latest/intro.html#error-codes} - coding style convention error codes
    @see {http://flake8.readthedocs.org/en/latest/warnings.html} - warnings codes
"""
"""
    --------------------------- Semicolons -----------------------------------
    - Do not terminate your lines with semi-colons and do not use semi-colons to put two commands on the same line.
"""

"""
    --------------------------- Line length ----------------------------------
    - Maximum line length is 120 characters.
"""

"""
    ---------------------------- Indentation ---------------------------------
    - Indent your code blocks with 4 spaces.
    - Do not use indents on blank lines
"""

"""
    ---------------------------- Blank Lines ---------------------------------
    - Two blank lines between top-level definitions, one blank line between method definitions.
        - Two blank lines before class\mixin\interface definition
        - One blank line after each block of  packages\modules importing
            (blocks separated by block comments of sections)
        - One blank line before method definition
        - No blank lines before/after method description comment
        - No blank lines before/after inline comments
        - One blank line in the end of the file
"""
# Example:
# Methods definition:
def prevMethod():
    """
        Some brief description for prevMethod
        @returns {Integer}
    """
    # make sure you haven't blank line here
    # ...some code
    return 0

def nextMethod( a ):
    """
        Some brief description for prevMethod
        @param a {Integer} - value to increment
        @returns {Integer} - incremented value of param a
    """
    return a+1

"""
    -------------------------- Whitespace ------------------------------------

    - Any block or inline comment must be started with '# ' (# and whitespace)
    - Follow standard typographic rules for the use of spaces around punctuation.
"""
# Example:
#   Good style:
x = 0
y = 0
if x == 4:
     x, y
x, y = y, x

sum(1)
dict['key'] = list[0]

#   Bad style:
x= 0
y=0
if x==4 :
    x , y
x , y=y , x

sum (1)
dict ['key'] = list [ 0 ]

"""
    - Do not use whitespaces for vertical alignment of calls or blocks
"""
# Example:
#   Good style:
foo = 1000  # comment
long_name = 2  # comment that should not be aligned

dictionary = {
    'foo': 1,
    'longName': 2,
    }

#   Bad style:
foo       = 1000  # comment
long_name = 2     # comment that should not be aligned

dictionary = {
      'foo'      : 1,
      'longName': 2,
      }
"""
    -------------------------- Parentheses ------------------------------------

    - Parentheses in method declaration
        - Use one whitespace after opened and before closed bracket in method
            declaration
        - Do not use whitespace before colon
"""
# Example
#   Good style
def someFunction( self, one=None ):
    pass
#   Bad style
def someFunction(self, one = None) :
    pass
"""
    - Parentheses in method call
        - Do not use one whitespace after method name
        - Use one whitespace after opened and before closed bracket
"""
# Example
#   Good style
someFunction( None, 1 )
#   Bad style
someFunction ( None, 1 )

"""
    -------------------------- Classes ---------------------------------------
    - If a class inherits from no other base classes, explicitly inherit from object.
        This also applies to nested classes.
"""
# Example

class SampleClass(object):
    """
        Class description
    """
    # class statement

class OuterClass(object):

        class InnerClass(object):
                pass


class ChildClass(SampleClass):
    """
        Explicitly inherits from another class already.
    """
"""
    ------------------------- Statements -------------------------------------
    - Generally only one statement per line.
        However, you may put the result of a test on the same line as the test
        only if the entire statement fits on one line. In particular, you can
        never do so with try/except since the try and except can't both fit on
        the same line, and you can only do so with an if if there is no else.
"""
# Example:
#   Good style:
if foo: bar(foo)

#   Bad style:
if foo: bar(foo)
    else:   baz(foo)

    try:               bar(foo)
    except ValueError: baz(foo)

    try:
        bar(foo)
    except ValueError: baz(foo)

# ---------------------- Code constructions -----------------------------------
"""
    ----------------------------- Imports ------------------------------------
    - Do not use importing of multiple packages in one line
"""
# Examples:
#   Good style:
import os
import sys

#   Bad style:
import os, sys


"""
    - Use import x for importing packages and modules.
    - Use from x import y where x is the package prefix and y is the module
        name with no prefix.
    - Use from x import y as z if two modules named y are to be imported or
        if y is an inconveniently long name.
"""
# Example:
# The module sound.effects.echo may be imported as follows:
from os.path import split
split('\some\where\here')


"""
    - All new code should import each module by its full package name.
"""
# Example:
# Reference in code with complete name.
import os.path.split

# Reference in code with just module name (preferred).
from os.path import split

# -------------------------------- Global entities-----------------------------
"""
    ----------------------------- Variables ----------------------------------
    - Avoid global variables in favor of class variables. Some exceptions are:
        - Default options for scripts.
        - Module-level constants. For example: PI = 3.14159. Constants should be
            named using all caps with underscores; see Naming below.
        - It is sometimes useful for globals to cache values needed
            or returned by functions.
        - If needed, globals should be made internal to the module
            and accessed through public module level functions; see Naming below.
    - If you have global variable declared in code - it obviously must have full
        doc comment (see DocComments section below to find out full comment criteria)
"""
"""
    ----------------------------- Functions ----------------------------------
    - Avoid global functions in favor of class methods. Some exceptions are:
        - function are needed for third party module\package\class etc...
    - If you have global function declared in code - it obviously must have full
        doc comment (see DocComments section below to find out full comment criteria)
    - Exception: main() function in executable file
"""

# -------------------------------- Naming -------------------------------------
"""
    Basically use camel case as the naming rule
    Additionally use PEP8 naming convention rules
    Exceptions in error codes of PEP8:
        - N802 - function name should be lowercase
        - N803 - argument name should be lowercase
        - N806 - variable in function should be lowercase
    @see {https://github.com/flintwork/pep8-naming} - naming convention error codes

    [Note] - not applicable for third party packages
"""
"""
    ----------------------------- Packages -----------------------------------
    - According to camel case, but lowerCase of first character
    Example: somePackageName
"""
"""
    ----------------------------- Modules ------------------------------------
    - According to camel case, but lowerCase of first character
    Example: someModuleName
"""
# Example
#   To be more informative in packages and modules naming - try to get names for packages and modules to make "from" or
#   import calls as in example below:
import packageName.moduleName.ClassName
from packageName.moduleName import ClassName

# In other case if you have more than one class in the file it is can be informative to get file name in lower case to make
# pretty "import" or "from" call

import fileName.ClassName
from fileName import ClassName
"""
    ----------------------------- Classes ------------------------------------
    - According to camel case, but UpperCase of first character
    Example: SomeClassName
"""
"""
    ----------------------------- Interfaces ---------------------------------
    - Use PEP8 naming convention for interfaces. Always start name with "I" (upper
        case) character
    Example: ISomeInterfaceName
"""
"""
    ----------------------------- Exceptions ---------------------------------
    - Use PEP8 naming convention for exceptions. Always start name with "E" (upper
        case) character
    Example: ESomeExceptionName
"""
"""
    ----------------------------- Mixins ---------------------------------
    - Use PEP8 naming convention for mixins. Always start name with "M" (upper
        case) character
    Example: MSomeMixinName

"""
#example
class MSomeMixin(object):
    """
        [MIXIN] some description for mixin
        @class MSomeMixin
        @package Core
    """
    def test( self ):
        """
            Some method description
            @return {void}
        """
        print "Mixin1"
        pass


class MElseMixin(object):
    """
        [MIXIN] some description for mixin
        @class MElseMixin
        @package Core
    """
    def test( self ):
        """
            Some method description
            @return {void}
        """
        print "Mixin2"
        pass


class SomeMixedClass(object, MSomeMixin, MElseMixin):
    """
        Some class description
        @class SomeMixedClass
        @package Core
    """
"""
    ----------------------------- Abstract classes ---------------------------
    - Always start name with "A" character (Upper Case)
    Example: AClassName
"""
"""
    ----------------------------- Variables ----------------------------------
    - Use default camel case rules for any kind of variables.
        Camel case with first character in lower case.
    Example: myVeryGoodVar, variable, foo, bar
"""
"""
    ----------------------------- Properties ---------------------------------
    - Use default camel case rules for any kind of properties.
        Camel case with first character in lower case.
    - Also use single or double "_" character to show access modification
    Example:
        somePublicProperty
        _someProtectedProperty
        __somePrivateProperty
"""
"""
    ----------------------------- Methods ------------------------------------
    - Use default camel case rules for any kind of methods.
        Camel case with first character in lower case.
    - Also use single or double "_" character to show access modification
    Example:
        somePublicMethods
        _someProtectedMethods
        __somePrivateMethods
"""
"""
    ----------------------------- Folder -------------------------------------
    - Folder name always is the name of package/module. Be attentive
"""
"""
    ----------------------------- File ---------------------------------------
    - Recommendation. File can have same name as the class in this file plus '.py'
    - no prefixes and no postfixes
    Exceptions:
        - If file contains full set of entities to be a module or a package - file MUST be named in lower case,
            accordingly to package naming rule (See above)
        - If file contains more than one class it is recommended to get it's name in lower case to make pretty "import"
            and "from" calls (See example below)
    Example:
        filename: FooBar.py
        for class: FooBar
"""
# Example:
import fileName.ClassName
from fileName import ClassName

# ----------------------- File structure rules --------------------------------
"""
    - Recommended to have one file for just one class
        In other case if you have some helper classes for your general class - fell free to implement it in same file
        But if helper classes used (means class instantiation) in some other file\module\package - it is recommended
        to move this helper class in separate file...

    - No plain calls in file, which contain class\interface\mixin definition

    - Use less of plain code calls.
        Excellent code have just one plain code call per file:
        if __name__ == '__main__':
            main()

    - Use classes in static context as containers for global functions or variables

    - All core files must have header doc comment with license information
        and information of author, project, module
        Exception is:
            - customTest.py
            - customIntegration.py
            - .yaml files
            - all .json or else config files

    - All files must have trailing blank line
"""
# -------------------- Doc Comments Recommendations --------------------------
"""
    ------------------ Base doc comment statements ---------------------------
    - Use Doxygen doc comment format
    - Use @ character as doxygen tag start symbol, instead of \
    - For list of all doxygen doc comment tags see:
        http://www.stack.nl/~dimitri/doxygen/manual/commands.html
    - Use one whitespace as separator of doxygen tag and tag content
        (Exception: Header doc comment)
    - Use enums of value types for variables, properties and arguments in
        @var and @prop tags.
        Example:
            @prop somePropName {Integer|Boolean|None}
    - Or use code type "Mixed" if entity requires any value type, existed in Python
        Example
            @prop somePropName {Mixed}
    - Use @see tag if your entity use external entity
        (especially if you are using global variable or function)
"""
"""
    ----------------------- File header comment ------------------------------
    - File header comment must be a default doc comment section
        (started and ended with triple quotes)
    - No indent between line start and quotes of header doc comment
    - List of tags, must be present in header doc comment:
        @file - name of current one file
        @author - name and e-mail of file author
        @date - date create of the file
        @brief - short description for content of this file

        [@package] - optional - name of the package for file
        [@class|@interface] - optional - name of the class\interface\mixin of this file
    - Header doc comment, is single one comment type which have 2 indents between tag name and tag content
        Example:
        @tag        tag text
"""
# Example: Header doc comment:
"""
     * ********************************************************************
     *  Project      myAwesome
     *  (c) copyright 2015
     *  Company      ACDC Awesome
     *  All rights reserved
     *  Secrecy Level STRICTLY CONFIDENTIAL
     * ********************************************************************

    @file       codingStyle.py
    @author     Dmitri Batulin <dbatulin@luxoft.com>
    @date       08.07.2015
    @brief      Coding style description file
    @package    myAwesome
"""

"""
    ----------------------- Comments for entities ----------------------------
    [Be attentive]
    - For all entities - only doc comments will describe API.
    - Inline or block comments must describe function logic.
        It won't be included into API.
"""
"""
    ----------------------- Comments for interfaces  --------------------------
    - All interfaces and it's methods or properties must have full comment coverage
        It contains one comment for interface itself
            (Interface description, @package Tag, etc...)
        one comment for each property
            (Property description, list of types for property(for multi type)
            or one type(for single type))
        and one comment for each interface method
            (Method description, @param tags for each method argument and @return tag)
"""
# Example
"""
    header comment here
"""


from abc import ABCMeta, abstractmethod, abstractproperty



class iSomeInterface(metaclass=ABCMeta):
    """
        Here is the interface description
    """
    @abstractmethod
    def someMethod( self, one, two=None ):
        """
            Here is the method description
            @param one {String|Array} - can be string or array type value
            @param two {Integer|None} - [optional]:None - this is description for arg
            @return {Integer}
        """
        pass

"""
    ----------------------- Comments for classes ------------------------------
    - Only public entities of classes must be obviously covered by comments
    - Comments for public entities must contain all of necessary tags:
        Methods:
            Description
            @param
            @return
            [@see] - if this method uses some external entity
            [@throws] - if it rises an exception
        Property
            Description
            @var - type of property value
            @see - multiple tag which refers to usage of this property
    - It is recommend to comment protected methods of class to generate
        developers API for plugins
    - For protected and private methods of properties, it is recommend
        (but not necessary) to use @protected and @private tags
"""
"""
    ----------------------- Comments for mixins ------------------------------
    - same as for classes
    Additional info: Using mixins, try to additionally identify this class as mixin
    For example use [MIXIN] tag as first word in class description
    - Still use @class tag for mixin name definition in doc comment
    @see example of mixin in Naming section
"""
"""
    ----------------------- Comments for methods -----------------------------
    - Public methods must be covered by full doc comments
        - Full Doc Comment statement is:
            - Brief description
            - Full description - in case if it necessary
            - @param tags for all method arguments
                (including all data types for each argument)
                See example below...
            - @return tag for returned value (even if method is void)
            - @throws tag, if method rises an exception
            - @see tag if method uses some functionality from
                mixin\parent class\global function\global variable
                or static call of external class) with reference to used functionality
    - Protected methods can be covered by regular doc comment
        - Regular Doc Comment statement is:
            - Brief description
            - @protected tag - is not necessary, but recommend
            - @param tags with minimal description (data types is not necessary)
            - @return tag - is not necessary, but recommend
            - @throws tag - if method rises an exception
            - @see tag - is not necessary
    - Private methods is not necessary to have doc comment, but still recommend to use brief description
        and @private tag
"""
# Example of allowable doc comment coverage for class:

"""
    file header here
"""


# imports here


class ExampleClass(object):
    """
        Example class of code coverage for methods
        @class ExampleClass
        @package Core
    """

    def __init__ ( self ):
        """
            Class constructor
        """
        self._propertyName= 1
        pass

    # ***************************************************************
    # Properties
    @property
    def propertyName ( self ):
        """
            Description of class property
            @var {Integer}
            @see {ExampleClass#publicMethod()} - usage
        """
        return self._propertyName

    # ***************************************************************
    # Methods
    def publicMethod ( self, one, two=None, three=1 ):
        """
            Some brief description for method (single line)
            Some long description, which describes method logic (multi line)
            @param one {Mixed} - first operand to sum it with "three" argument
            @param two {Boolean|None} - [optional]:None - some description for argument
            @param three {Integer} - [optional]:1 - some description for argument
            @throws {MyAwesomeException} - raised if argument two is not True or None
            @return {Integer} - returns the summ of "one" and "three" arguments or value of @link{ExampleClass#propertyName}
            @see {ExampleClass#propertyName}
        """
        if two == True:
            return int(one) + three
        elif two is None:
            return self.propertyName
        else:
            raise MyAwesomeException('Something goes wrong!')


    def _protectedMethod ( self, one, two=None, three=1):
        """
            Protected method with regular coverage
            @protected
            @param one - first argument
            @param two - second argument
            @param three - third argument
            @throws {MyAwesomeException} - raised if argument two is not True or None
            @return {Integer} - returns the summ of "one" and "three" arguments or value of @link{ExampleClass#propertyName}
        """
        if two == True:
            return int(one) + three
        elif two is None:
            return self.propertyName
        else:
            raise MyAwesomeException('Something goes wrong!')

    def _otherProtectedMethod ( self, one, two=None, three=1):
        """
            Protected method with minimal regular coverage
            @param one - first argument
            @param two - second argument
            @param three - third argument
            @throws {MyAwesomeException} - raised if argument two is not True or None
        """
        if two == True:
            return int(one) + three
        elif two is None:
            return self.propertyName
        else:
            raise MyAwesomeException('Something goes wrong!')

    def __privateMethod ( self, one, two=None, three=1):
        """
            Method to summ arguments "one" and "tree" with additional logic
            @private
        """
        if two == True:
            return int(one) + three
        elif two is None:
            return self.propertyName
        else:
            raise MyAwesomeException('Something goes wrong!')

    def __oterPrivateMethod ( self, one, two=None, three=1):
        """
            Method to summ arguments "one" and "tree" with additional logic
        """
        if two == True:
            return int(one) + three
        elif two is None:
            return self.propertyName
        else:
            raise MyAwesomeException('Something goes wrong!')

    def __anoterPrivateMethod ( self, one, two=None, three=1):
        if two == True:
            return int(one) + three
        elif two is None:
            return self.propertyName
        else:
            raise MyAwesomeException('Something goes wrong!')
