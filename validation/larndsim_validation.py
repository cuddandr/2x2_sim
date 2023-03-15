import matplotlib
import matplotlib.pyplot as plt
import h5py
import argparse
from matplotlib.backends.backend_pdf import PdfPages

def main(sim_file):

    sim_h5 = h5py.File(sim_file,'r')
    print('\n----------------- File content -----------------')
    print('File:',sim_file)
    print('Keys in file:',list(sim_h5.keys()))
    for key in sim_h5.keys():
        print('Number of',key,'entries in file:', len(sim_h5[key]))
    print('------------------------------------------------\n')

    output_pdf_name = sim_file.split('.h5')[0]+'_validations.pdf'
    # temperarily, put output in this directory, not the same as the
    # simulation file itself
    output_pdf_name = output_pdf_name.split('/')[-1] # !!
    with PdfPages(output_pdf_name) as output:

        ### Plot time structure of packets: 
        packets = sim_h5['packets']
        #plt.figure(figsize=(6,8))
        plt.plot(packets['timestamp'])
        plt.xlabel('packet index')
        plt.ylabel('timestamp')
        output.savefig()
        plt.close()

        plt.hist(packets['timestamp'],bins=100)
        plt.xlabel('timestamp')
        output.savefig()
        plt.close()

        plt.plot(packets['receipt_timestamp'])
        plt.xlabel('packet index')
        plt.xlabel('receipt_timestamp')
        output.savefig()
        plt.close()

        plt.hist(packets['receipt_timestamp'],bins=100)
        plt.xlabel('receipt_timestamp')
        output.savefig()
        plt.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sim_file', default=None, type=str,help='''string corresponding to the path of the larnd-sim output simulation file to be considered''')
    args = parser.parse_args()
    main(**vars(args))

