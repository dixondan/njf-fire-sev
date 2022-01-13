
variables = ['BAI_post_off', 'CSI_post_off',
             'MIRBI_post_off', 'MSAVI_pre', 'NBR_pre', 'NDVI_pre', 'NDWI_pre',
             'VARI_pre', 'dMSAVI_off', 'dNBR_off', 'dNDVI_off', 'dNDWI_off',
             'dVARI_off']

date_range = 64 #search window days post fire

shift = 'Shift'#modis shift yes

bands = ['dNBR_off', 'dNDVI_off', 'dNDWI_off', 'dVARI_off',
         'dMSAVI_off', 'BAI_post_off', 'CSI_post_off', 'MIRBI_post_off',
         'NBR_pre', 'NDVI_pre', 'NDWI_pre', 'VARI_pre', 'MSAVI_pre']

# randomly selected train and test fires

train_fires = ['f_066', 'f_063', 'f_060', 'f_005', 'f_019', 'f_008', 'f_034', 'f_065', 'f_031', 'f_033',
       'f_050', 'f_027', 'f_016', 'f_007', 'f_061', 'f_002', 'f_056', 'f_030', 'f_001', 'f_059',
       'f_020', 'f_017', 'f_054', 'f_023', 'f_048', 'f_044', 'f_058', 'f_035', 'f_040', 'f_032',
      'f_012','f_041', 'f_013', 'f_070']

test_fires =  ['f_003', 'f_004', 'f_006', 'f_009', 'f_010',  'f_014', 'f_015', 'f_018', 'f_021',
          'f_022', 'f_024', 'f_025', 'f_026', 'f_028', 'f_029', 'f_036', 'f_039', 'f_046',
          'f_047', 'f_055', 'f_057', 'f_062', 'f_064', 'f_068','f_011', 'f_038', 'f_043',
         'f_069', 'f_067', 'f_071']
