
lib2to3_fix_names = set([
    'lib2to3.fixes.fix_apply',
    'lib2to3.fixes.fix_except',
    'lib2to3.fixes.fix_exec',
    'lib2to3.fixes.fix_execfile',
    'lib2to3.fixes.fix_exitfunc',
    'lib2to3.fixes.fix_funcattrs',
    'lib2to3.fixes.fix_has_key',
    'lib2to3.fixes.fix_idioms',
    'lib2to3.fixes.fix_long',
    'lib2to3.fixes.fix_methodattrs',
    'lib2to3.fixes.fix_ne',
    'lib2to3.fixes.fix_numliterals',
    'lib2to3.fixes.fix_operator',
    'lib2to3.fixes.fix_paren',
    'lib2to3.fixes.fix_reduce',
    'lib2to3.fixes.fix_repr',
    'lib2to3.fixes.fix_set_literal',
    'lib2to3.fixes.fix_standarderror',
    'lib2to3.fixes.fix_sys_exc',
    'lib2to3.fixes.fix_throw',
    'lib2to3.fixes.fix_tuple_params',
    'lib2to3.fixes.fix_types',
    'lib2to3.fixes.fix_ws_comma',
    'lib2to3.fixes.fix_xreadlines'
])

# fixes that involve using six
six_fix_names = set([
    'libmodernize.fixes.fix_basestring',
    'libmodernize.fixes.fix_dict_six',
    'libmodernize.fixes.fix_filter',
    'libmodernize.fixes.fix_imports_six',
    'libmodernize.fixes.fix_input_six',
    'libmodernize.fixes.fix_int_long_tuple',
    'libmodernize.fixes.fix_map',
    'libmodernize.fixes.fix_metaclass',
    'libmodernize.fixes.fix_raise_six',
    'libmodernize.fixes.fix_unicode',
    'libmodernize.fixes.fix_unicode_type',
    'libmodernize.fixes.fix_xrange_six',
    'libmodernize.fixes.fix_zip',
])

# Fixes that are opt-in only.
opt_in_fix_names = set([
    'libmodernize.fixes.fix_open',
])
