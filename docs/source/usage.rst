Usage
=====

Filefisher is a handy tool to find and parse file and folder names. Here, we show
its basic usage and some example. For more detailed information on the functionalities
presented here, please refer to the `API reference`_.

Setup
-----

Define regular folder and file patterns with the intuitive python syntax:

.. code-block:: python
    
    from filefisher import FileFinder

    path_pattern = "/root/{category}"
    file_pattern = "{category}_file_{number}"

    ff = FileFinder(path_pattern, file_pattern)


Create file and path names
--------------------------

Everything enclosed in curly brackets is a placeholder. Thus, you can create file and
path names like so:

.. code-block:: python

    ff.create_path_name(category="a")
    >>> /root/a/

    ff.create_file_name(category="a", number=1)
    >>> a_file_1

    ff.create_full_name(category="a", number=1)
    >>> /root/a/a_file_1

Find files on disk
------------------

However, the strength of filefisher is parsing file names on disk. Assuming you have the
following folder structure:

.. code-block::

    /root/a/a_file_1
    /root/a/a_file_2
    /root/b/b_file_1
    /root/b/b_file_2
    /root/c/c_file_1
    /root/c/c_file_2

You can then look for paths:

.. code-block:: python

    ff.find_paths()
    >>> <FileContainer: 3 paths>
    >>>            category
    >>>  path                 
    >>>  /root/a/*        a
    >>>  /root/b/*        b
    >>>  /root/c/*        c

The placeholders (here `{category}`) is parsed and returned. You can also look for
files:

.. code-block:: python

    ff.find_files()
    >>> <FileContainer: 6 paths>
    >>>                         category number
    >>>  path                                   
    >>>  /root/a/a_file_1.rtf        a  1
    >>>  /root/a/a_file_2.rtf        a  2
    >>>  /root/b/b_file_1.rtf        b  1
    >>>  /root/b/b_file_2.rtf        b  2
    >>>  /root/c/c_file_1.rtf        c  1
    >>>  /root/c/c_file_2.rtf        c  2

It's also possible to filter for certain files:

.. code-block:: python

    ff.find_files(category=["a", "b"], number=1)
    >>> <FileContainer: 2 paths>
    >>>                     category number
    >>>  path                              
    >>>  /root/a/a_file_1        a      1
    >>>  /root/b/b_file_1        b      1

Often we need to be sure to find **exactly one** file or path. This can be achieved using

.. code-block:: python

    ff.find_single_file(category="a", number=1)
    >>> <FileContainer: 1 paths>
    >>>                     category number
    >>>  path
    >>>  /root/a/a_file_1       a      1


If none or more than one file is found a `ValueError` is raised.

Format syntax
-------------

You can pass format specifiers to allow more complex formats, see
[format-specification](https://github.com/r1chardj0n3s/parse#format-specification) for details.
Using format specifiers, you can parse names that are not possible otherwise.

Example
*******

.. code-block:: python

    from filefisher import FileFinder

    paths = ["a1_abc", "ab200_abcdef",]

    ff = FileFinder("", "{letters:l}{num:d}_{beg:2}{end}", test_paths=paths)

    fc = ff.find_files()

    fc

which results in the following:

.. code-block:: python

    <FileContainer: 2 paths>
                letters  num beg   end
    path                               
    a1_abc             a    1  ab     c
    ab200_abcdef      ab  200  ab  cdef


Note that `fc.df.num` has now a data type of `int` while without the `:d` it would be an
string (or more precisely an object as pandas uses this dtype to represent strings).


Filters
-------

Filters can postprocess the found paths in `<FileContainer>`. Currently only a `priority_filter`
is implemented.

Example
*******

Assuming you have data for several models with different time resolution, e.g., 1 hourly
(`"1h"`), 6 hourly (`"6h"`), and daily (`"1d"`), but not all models have all time resolutions:

.. code-block::

    /root/a/a_1h
    /root/a/a_6h
    /root/a/a_1d

    /root/b/b_1h
    /root/b/b_6h

    /root/c/c_1h

You now want to get the `"1d"` data if available, and then the `"6h"` etc.. This can be achieved with the `priority filter`. Let's first parse the file names:

.. code-block:: python

    ff = FileFinder("/root/{model}", "{model}_{time_res}")

    files = ff.find_files()
    files

which yields:

.. code-block::

    <FileContainer: 6 paths>
                model time_res
    path                         
    /root/a/a_1d     a       1d
    /root/a/a_1h     a       1h
    /root/a/a_6h     a       6h
    /root/b/b_1h     b       1h
    /root/b/b_6h     b       6h
    /root/c/c_1h     c       1h

We can now apply a `priority_filter` as follows:

.. code-block:: python

    from filefisher.filters import priority_filter

    files = priority_filter(files, "time_res", ["1d", "6h", "1h"])
    files

Resulting in the desired selection:

.. code-block::
    
    <FileContainer: 3 paths>
                model time_res
    path                         
    /root/a/a_1d     a       1d
    /root/b/b_6h     b       6h
    /root/c/c_1h     c       1h


.. _API reference: api.html