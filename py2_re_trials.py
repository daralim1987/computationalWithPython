#!/usr/bin/python

################################
## CS 3430: S18
## Py2 regexp examples
## author: vladimir kulyukin
################################

import re

txt_01 = '12345'
txt_02 = 'abcde'
txt_03 = ' .;!?\~'
txt_04 = ' .;!?\_'
txt_05 = ' .;!?\~_\n'
txt_06 = ' \t\n'

txt_lst = (txt_01, txt_02, txt_03, txt_04, txt_05, txt_06)

def find_digit_char(txt):
    if re.search(r'\d', txt):
        print 'There is at least one digit char in ' + repr(txt)
    else:
        print 'There are no digit chars in ' + repr(txt)

def digit_char_tests(txts):
    print r'***** \d Tests *****'
    for  txt in txts: find_digit_char(txt)

def find_nondigit_char(txt):
    if re.search(r'\D', txt):
        print 'There is at least one nondigit char in ' + repr(txt)
    else:
        print 'There are no nondigit chars in ' + repr(txt)

def nondigit_char_tests(txts):
    print r'***** \d Tests *****'
    for  txt in txts: find_nondigit_char(txt)

txt_01 = '12345'
txt_02 = '1+1=2'
txt_03 = ' a + b =     c   '

def test_1(txt):
    match_01 = re.search(r'(\d)', txt)
    if not match_01 is None:
        print "group = '%s'" % match_01.group()
        print "span  = %s" % str(match_01.span())
        print '---------------'
    else:
        print 'no match found'
        print '---------------'

def test_2(txt):
    match_02 = re.search(r'(\d+)', txt)
    if not match_02 is None:
        print "group = '%s'" % match_02.group()
        print "span  = %s" % str(match_02.span())
        print '---------------'
    else:
        print 'no match found'
        print '---------------'

def test_3(txt):
    match_03 = re.search(r'(\d)(\w*)(\d)', txt)
    if not match_03 is None:
        print 'groups  = %s' % str(match_03.groups())
        print 'span    = %s' % str(match_03.span())
        print 'group 1 = %s' % str(match_03.group(1))
        print 'group 2 = %s' % str(match_03.group(2))
        print 'group 3 = %s' % str(match_03.group(3))
        print '---------------'
    else:
        print 'no match found'
        print '---------------'

def test_4(txt):
    match_04 = re.search(r'(\d+)\+(\d+)=(\d+)', txt)
    if not match_04 is None:
        print 'group 1 = %s' % str(match_04.group(1))
        print 'group 2 = %s' % str(match_04.group(2))
        print 'group 3 = %s' % str(match_04.group(3))
        print 'span    = %s' % str(match_04.span())
        print '---------------'
    else:
        print 'no match found'
        print '---------------'

def test_5(txt):
    match_05 = re.search(r'\s*(\w+)\s*(\+|\-|\*)\s*(\w+)\s*=\s*(\w+)\s*', txt)
    if not match_05 is None:
        print 'group 1 = %s' % str(match_05.group(1))
        print 'group 2 = %s' % str(match_05.group(2))
        print 'group 3 = %s' % str(match_05.group(3))
        print 'span    = %s' % str(match_05.span())
        print '---------------'
    else:
        print 'no match found'
        print '---------------'

## this is an example of a closure - a function
## returning another function
def make_re_match_fun(regex, pos_msg, neg_msg):
    def search_fun(txt):
        if re.search(regex, txt):
            print pos_msg + repr(txt)
        else:
            print neg_msg + repr(txt)
    return search_fun

def run_re_tests(re_match_fun, txts):
    for txt in txts: re_match_fun(txt)

def display_groups_by_backrefs(pat, txt):
    print '-------------------------'
    print 'pat = ' + str(pat) + '; ' + 'text = ' + txt
    match = re.search(pat, txt)
    if not match is None:
        num_of_groups = len(match.groups())
        print 'num of groups = ', num_of_groups
        for i in xrange(num_of_groups+1):
            print str(i) + ' --> ' + match.group(i)
    print '-------------------------'

## Uncomment to run the tests
if __name__ == '__main__':
    '''
    print '******Test 1: NON-DIGIT CHARS\n',
    run_re_tests(make_re_match_fun(r'\D',
                                   'There is a non-digit character in ',
                                   'There are no non-digit characters in '),
                 txt_lst)
    print

    print '******Test 2: WORD CHARS\n',
    run_re_tests(make_re_match_fun(r'\w',
                                   'There is a word character in ',
                                   'There are no word characters in '),
                 txt_lst)
    print

    print '******Test 3: NON-WORD CHARS\n',
    run_re_tests(make_re_match_fun(r'\W',
                                   'There is a non-word character in ',
                                   'There are no non-word characters in '),
                 txt_lst)
    print
    
    print '*****Test 4: SPACE CHARS\n',
    run_re_tests(make_re_match_fun(r'\s',
                                   'There is a space character in ',
                                   'There are no space characters in '),
                 txt_lst)
    print
    
    print '*****Test 5: NON-SPACE CHARS\n',
    run_re_tests(make_re_match_fun(r'\S',
                                   'There is a non-space character in ',
                                   'There are no non-space characters in '),
                 txt_lst)

    display_groups_by_backrefs(r'(\w)(\w)(\w)', 'abc')
    display_groups_by_backrefs(r'(\w{3})', 'abc')
    display_groups_by_backrefs(r'(\w*)(\w)', 'abc')
    display_groups_by_backrefs(r'(\w*)(\w)(\w)(\w)', 'abc')
    '''
    pass


