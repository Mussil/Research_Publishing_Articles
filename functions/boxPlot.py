import json
from matplotlib import pyplot as plt
from helpers import checkedYear, prettyCat


def dataForBoxPlot(source_dict):
    with open(source_dict, "r") as read_file:
        dict = json.load(read_file)
        for namePop, categories in dict.items():
            print(namePop)
            for category,years in categories.items():
                xAxis = []
                yAxis = []
                print(f'\t{category}')
                for year,values in years.items():
                    xAxis.append(year)
                    yAxis.append(values)
                amount=len(values)
                fig = plt.figure()
                ax = fig.add_subplot(111)
                ax.yaxis.grid(True) # Hide the horizontal gridlines
                ax.xaxis.grid(True) # Show the vertical gridlines
                plt.boxplot(yAxis, meanline=True, whis=[1, 99], showfliers=False, showmeans=True)
                xx = list(range(1, len(xAxis) + 1))
                plt.xticks(xx, xAxis)
                plt.xlabel('Years')
                plt.title(f'{prettyCat[category]}\n{namePop} {checkedYear}\n Amount of authors: {amount}')
                plt.savefig(f'{path}{category}_{namePop}_{checkedYear}.pdf', bbox_inches='tight')
                plt.close()

if __name__=='__main__':
    path= '../plotsArxiv/boxPlot/'
    source_dict='../ArXivDataOfAllPop2010BycategoryByYear.json'
    dataForBoxPlot(source_dict)
