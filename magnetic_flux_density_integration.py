import magnetic_flux_data


"""inputs
"""
AD_B = magnetic_flux_data.AD_magnetic_flux_list
AD_distance = magnetic_flux_data.AD_distance_list
BF_B = magnetic_flux_data.BF_magnetic_flux_list
BF_distance = magnetic_flux_data.BF_distance_list
"""variable
"""
len_AD_data = len(AD_distance)
len_AD_data2 = len(AD_B)
len_BF_data = len(BF_distance)
len_BF_data2 = len(BF_B)
if not (len_AD_data == len_AD_data2 and len_BF_data == len_BF_data2):
    print("データの長さが違うため計算できません")


def calculate_magnetic_flux_density_integration():
    Total_B_of_AD = 0
    Total_B_of_BF = 0
    for i in range(len_AD_data-1):
        Total_B_of_AD \
            += (AD_B[i+1]+AD_B[i])\
                *(AD_distance[i+1]-AD_distance[i])/2
    for i in range(len_BF_data-1):
        Total_B_of_BF += (BF_B[i+1]+BF_B[i])*(BF_distance[i+1]-BF_distance[i])/2
    print(Total_B_of_AD)
    print(Total_B_of_BF)
    print((115.18-17.79)/1.257)

calculate_magnetic_flux_density_integration()