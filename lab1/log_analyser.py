"""Log analyser. Prints out ERROR, WARNING and FATAL logs to the output file.

Usage:
  log_analyser <logfile> [<output_file>]
  log_analyser -h | --help

Options:
  -h --help     Show this screen.
"""

from docopt import docopt

default_output_file = 'filename_err.log'

args = docopt(__doc__)

input_file = args['<logfile>']
output_file = args['<output_file>']

if not output_file:
    output_file = default_output_file

output_logs_levels = ('ERROR', 'WARNING', 'FATAL')

with open(input_file) as fp:
    with open(output_file, 'w') as out:
        for line in fp:
            # This actually makes naive `grep` and so finds lines as:
            # TrigL2SiTrackFinder_MuonA.TrigL2SiTrackFinder...  DEBUG setting label X TRT_ERROR  for bin 4
            #
            # I've tried to split the line and look at the first/second column, but this does not help for lines such as:
            # T2VertexBeamSpot_activeAllTE_L2StarB.T2Vertex...WARNING Variable: [VertexProbPass] not exported by parent algorithm: T2VertexBeamSpot_activeAllTE_L2StarB this are available:
            #
            # when there's no white character between the level and the name (possible bug in the logger/logfile?)
            if any(word in line for word in output_logs_levels):
                out.write(line)

