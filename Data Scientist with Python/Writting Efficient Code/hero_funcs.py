


def convert_units(heroes, heights, weights):
    new_hts = [ht * 0.39370 for ht in heights]
    # c
    new_wts = [wt * 2.20462 for wt in weights]
    
    hero_data = {}
    
    for i, hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])
        
    return hero_data



def calc_bmi_arrays(sample_indices, hts, wts):

    # Gather sample heights and weights as arrays
    s_hts = hts[sample_indices]
    s_wts = wts[sample_indices]

    # Convert heights from cm to m and square with broadcasting
    s_hts_m_sqr = (s_hts / 100) ** 2

    # Calculate BMIs as an array using broadcasting
    bmis = s_wts / s_hts_m_sqr

    return bmis