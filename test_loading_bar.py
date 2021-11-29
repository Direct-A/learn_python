#coding: utf-8
#Author: sYc
# Date: 2021-01-17 16:13:08
#Version: 0.1
# Description: test loading bar

from tqdm import tqdm
num = 0
with tqdm(total=num) as pbar:
    pbar.set_description('Processing')
    num += num
    pbar.update(num)
