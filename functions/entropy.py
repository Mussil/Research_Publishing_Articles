import json

import numpy as np
import scipy.stats
from matplotlib import pyplot as plt
from helpers import checkedYear, prettyCat


def dataForEntropy(source_dict):
    with open(source_dict, "r") as read_file:
        dict = json.load(read_file)
        categories=prettyCat.keys()
        for category in categories:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.yaxis.grid(True)  # Hide the horizontal gridlines
            ax.xaxis.grid(True)  # Show the vertical gridlines
            for namePop, categories in dict.items():
                categoryData=categories[category]
                xAxis = []
                yAxis = []
                for year, x in categoryData.items():
                    xAxis.append(year)
                    value, counts = np.unique(x, return_counts=True)
                    yAxis.append(scipy.stats.entropy(counts))
                plt.plot(xAxis, yAxis, label=f'{namePop} {checkedYear}')
            plt.xlabel('Years')
            plt.legend()
            box = ax.get_position()
            ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
            ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
            plt.title(f'{prettyCat[category]}')
            plt.savefig(f'{path}{category}_{namePop}_{checkedYear}.pdf', bbox_inches='tight')
            plt.close()


if __name__=='__main__':
    path= '../plotsArxiv/entropy/'
    source_dict='../ArXivDataOfAllPop2010BycategoryByYear.json'
    dataForEntropy(source_dict)
