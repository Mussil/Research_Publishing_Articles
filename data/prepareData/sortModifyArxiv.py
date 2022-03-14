'''
sort original data of arXiv by date
save it to new file
'''
import json

months={'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Sept':'09','Oct':'10','Nov':'11','Dec':'12'}

def get_time(dict):
    '''
    :param dict: dict from the file of arXiv
    :return: integer that represent the date
    '''

    versions=dict.get("versions")
    v1=versions[0].get('created')

    _,date=v1.split(', ')
    day, month,year,time,gmt=date.split(' ')
    month=months[month]

    return year*365+month*31+day #single value that represnt the date

def createNewFile(source_dict,dest_dict):
    '''
    :param source_dict: the file that will be modified
    :param dest_dict: the new file , list of dicts
    :return:
    '''

    with open(source_dict) as f:
        data = [json.loads(line) for line in f]  # from lots of dict to one list

        data.sort(key=get_time)  # sort the list by update_date"

        with open(dest_dict, 'w') as file:
            file.write(json.dumps(data))  # use `json.loads` to do the reverse


if __name__=='__main__':
    path='../'
    source_dict = path+'originalData/'+'arxiv-metadata-oai-snapshot.json'
    dest_dict = path+'modifiedData/'+'arxiv.json'
    createNewFile(source_dict,dest_dict)

