import os
import time
import argparse
import random
from datetime import datetime
from pathlib import Path

parser = argparse.ArgumentParser(description="Generate random XML file name in specific time")
parser.add_argument("-t", "--time", default=3)
option = parser.parse_args()

time_between_creation = int(option.time)


def generatexml(filename):
    folder = Path('xmls')
    if not os.path.exists(folder):
        Path("xmls").mkdir(parents=True, exist_ok=True)

    now = datetime.now()

    sample_names_values = ("Auditorio", 'Marcenaria', 'Saguao', 'Salao', 'Sala-de-estar')
    sample_material = random.randrange(1, 9999)
    sample_name = random.choice(sample_names_values)
    sample_date = now.strftime('%Y-%m-%d_%Hh-%Mm-%Ss')

    txt_filename = str(sample_name) + '_' + str(sample_material) + '_' + str(sample_date) + ".xml"
    new_txt = Path(folder, str(txt_filename))

    f = open(new_txt, "a")
    f.writelines(str(sample_name) + filename)
    f.close()

    print(f"Writing log file: {new_txt}\n")
    return


while 1:
    generatexml(f'{random.randrange(50, 350)}')
    time.sleep(time_between_creation)
