import argparse
import os

import numpy as np
import pandas as pd


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', help='Ponto inicial')
    parser.add_argument('--end', help='Ponto final')
    parser.add_argument('--data', help='Banco de dados')
    args = parser.parse_args()
    data_directory = os.path.join(
        os.getcwd(), 'banco_de_dados', f'matriz_{args.data}.txt'
    )
    data = np.loadtxt(data_directory)
    try:
        args.start=int(args.start)
        args.start=int(args.end)
    except:
        # convert to numerical values
        coord_diretorio = os.path.join(
            os.getcwd(), 'banco_de_dados', f'coord_{args.data}.csv'
        )
        coords = pd.read_csv(coord_diretorio)
        names_to_numbers = {coords['Cidade'][j]: j for j in range(len(coords))}
        args.start = names_to_numbers[args.start]
        args.end = names_to_numbers[args.end]
    return data, args.start, args.end
