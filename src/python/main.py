import pickle
import sys
import markov
import argparse
import interactive

parser = argparse.ArgumentParser(description='Markov Chain Text Generator script')


# read/gen/build -if ../butalci.txt -of ./sample.out -df ./butalci.dump -rf ./butalci.dump -l 80

def parse_args():
    parser.add_argument('action', metavar='ACT', type=str, help='Actions: read, gen, build')
    parser.add_argument('-if', '--in-file', help='Filename to read')
    parser.add_argument('-of', '--out-file', help='Filename to write to (generated text)')
    parser.add_argument('-df', '--write-dump', help='Pickle file to write')
    parser.add_argument('-rf', '--read-dump', help='Pickle file to read')
    parser.add_argument('-l', '--length', type=int, help='Length of text to generate')

    args = parser.parse_args()

    return args


def build_generate(args):
    if args.in_file is None or args.out_file is None or args.length is None:
        parser.print_help()
        sys.exit(0)

    text = markov.load_text(args.in_file)
    markov_data = markov.generate_matrix(text)

    states = markov.generate_text(markov_data, args.length)

    markov.to_file(states, markov_data['words'], args.out_file)


def generate_from(args):
    if args.read_dump is None or args.out_file is None or args.length is None:
        parser.print_help()
        sys.exit(0)

    print('Loading processing data from Pickle dump: {0}'.format(args.read_dump))
    markov_data = pickle.load(open(args.read_dump, 'rb'))
    states = markov.generate_text(markov_data, args.length)

    markov.to_file(states, markov_data['words'], args.out_file)


def dump_data(args):
    if args.in_file is None or args.write_dump is None:
        parser.print_help()
        sys.exit(0)

    text = markov.load_text(args.in_file)
    markov_data = markov.generate_matrix(text)
    print('Dumping processing data to Pickle dump: {0}'.format(args.write_dump))
    pickle.dump(markov_data, open(args.write_dump, 'wb'), protocol=4)


def main(args):
    if args.action == 'interactive':
        interactive.interactive_session(args)
    if args.action == 'gen':
        build_generate(args)
    elif args.action == 'read':
        generate_from(args)
    elif args.action == 'build':
        dump_data(args)
    else:
        parser.print_help()
        sys.exit(0)


if __name__ == '__main__':
    args = parse_args()
    main(args)
