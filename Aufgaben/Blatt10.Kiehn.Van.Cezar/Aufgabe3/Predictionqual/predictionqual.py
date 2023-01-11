#!/bin/env python3
import argparse, sys

def parse_command_line(argv):
  p=argparse.ArgumentParser(description=(
                'Input the gold standard followed by the prediction files'))
  p.add_argument('-g','--gold_standard',type=str,default="goldstandard.tsv")
  p.add_argument('inputfiles',type=str,nargs='+')
  return p.parse_args(argv)
def inputfile2set(inputfile):
    coors=set()
    with open(inputfile) as stream:
        for line in stream.readlines():
            if len(line.split("\t"))!=2:
                continue
            coors.add((int(line.split("\t")[0]),int(line.split("\t")[1])))
    return coors
def evaluate(gs,prediction):
    intersec=gs & prediction
    return (len(intersec),len(intersec)/len(gs),len(intersec)/len(prediction))
def harmonic_mean(a,b):
    return 2/((1/a)+(1/b))
def main():
    try:
        args = parse_command_line(sys.argv[1:])
    except argparse.ArgumentTypeError as err:
        sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
        exit(1)
    set_gs=inputfile2set(args.gold_standard)
    print("#filename\ttp\tsens\tspec\thmean")
    for inputfile in args.inputfiles:
        set=inputfile2set(inputfile)
        eval=evaluate(set_gs,set)
        mean=harmonic_mean(eval[1],eval[2])
        print(f"{inputfile}\t{eval[0]}\t{100*eval[1]:.2f}\t{100*eval[2]:.2f}"+
              f"\t{100*mean:.2f}")
if __name__=="__main__":
    main()