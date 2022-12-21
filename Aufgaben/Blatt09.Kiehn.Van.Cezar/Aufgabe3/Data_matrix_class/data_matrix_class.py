#!/bin/env python3

import sys, argparse

class DataMatrix:
    def __init__(self,lines,key_col=1,sep='\t'):
        self._matrix=dict()
        self._attribute_list= None
        for line in lines:
            ls = line.rstrip('\n').split(sep)
            if self._attribute_list is None: # in first line
                self._attribute_list = ls
            else:  # not in first line: values
                if len(ls) != len(self._attribute_list):
                    sys.stderr.write('line has {} columns, but {} expected\n'
                                    .format(len(ls),len(self._attribute_list)))
                    exit(1)
                line_dict = dict()
                for attr, value in zip(self._attribute_list,ls):
                    line_dict[attr] = value
                k = ls[key_col]
                if k in self._matrix:
                    sys.stderr.write('key {} in line {} is not unique\n'
                                    .format(k,2+len(self._matrix)))
                    exit(1)
                self._matrix[k] = line_dict
    def show(self,sep,attributes,keys):
        for key in keys:
            for a in attributes:
                if self._matrix[key][a] != '':
                    print(f'{key}{sep}{a}{sep}{self._matrix[key][a]}')
    def show_orig(self,sep,attributes,keys):
        print(sep.join(attributes))
        for key in keys:
            line_elems = list()
            for a in attributes:
                line_elems.append(self._matrix[key][a])
            print(sep.join(line_elems))
    def keys(self):
        return self._matrix.keys()
    def attribute_list(self):
        return self._attribute_list


def parse_command_line(argv):
    p = argparse.ArgumentParser(description=('extract information '
                                            'of data matrix'))
    p.add_argument('-k','--keys',nargs='+',default=None,
                    help='specify keys for which values are output')
    p.add_argument('-a','--attributes',nargs='+',default=None,
                    help='specify attributes output')
    p.add_argument('-o','--orig',action='store_true',default=False,
                    help='output key/value pairs in original format')
    p.add_argument('-s','--sep',type=str,default='\t',
                    help='specify column separator, default is Tab')
    p.add_argument('inputfile',type=str,
                    help='specify inputfile (mandatory argument)')
    return p.parse_args(argv)

def parse_command_line_documentation(argv):
    p = argparse.ArgumentParser(description='extract information ..')
    p.add_argument('inputfile',type=str,
                    help='specify inputfile (mandatory argument)')
    p.add_argument('-k','--keys',nargs='+',default=None,
                    help='specify keys for which values are output')
    p.add_argument('-o','--orig',action='store_true',default=False,
                    help='output key/value pairs in original format')
    p.add_argument('-s','--sep',type=str,default='\t',
                    help='specify column separator, default is Tab')
    return p.parse_args(argv)
if __name__=="__main__":
    args = parse_command_line(sys.argv[1:])

    try:
        stream = open(args.inputfile)
    except IOError as err:
        sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
        exit(1)

    matrix= DataMatrix(stream)
    stream.close()
    if args.attributes:  # option -a was used
        attributes = args.attributes
    else:
        attributes = matrix.attribute_list() # use all attributes
    if args.keys:  # option -k was used
        keys = args.keys
    else:
        keys = matrix.keys()   # use all keys
    if args.orig:
        matrix.show_orig(args.sep,attributes,keys)
    else:
        matrix.show(args.sep,attributes,keys)
