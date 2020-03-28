import shutil

x_path = 'X:/fwtest/Traces/XJ/p6s/Integrity_CIV-S09/JSA002BG_07-18-19_18-29-42/errors/Error_000_ERR_DEVICE_TIMEOUT'
l_path = 'D:/work/FA/CCB8-30230/p6s/Integrity_CIV-S09/JSA002BG_07-18-19_18-29-42/errors/Error_000_ERR_DEVICE_TIMEOUT'

shutil.copytree(x_path, l_path)

