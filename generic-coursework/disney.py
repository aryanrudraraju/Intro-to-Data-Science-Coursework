# Last 20 locations accessed from each device
device1 = "lon_fra_dub_lon_fra_ber_lon_fra_dub_lon_fra_mad_mil_vie_lon_fra_dub_lon_fra_ber"
device2 = "mil_rom_lon_fra_dub_lon_fra_dub_lon_fra_dub_lon_fra_dub_lon_fra_mad_mil_ath_mil"

def get_shared_pattern(str1, str2):
    """Find shared access patterns"""
    longest_str = ""
    for start in range(len(str1)):
        for end in range(start + 1, len(str1) + 1):
            
            curr_str = str1[start:end]
            
            if curr_str in str2:
                if len(curr_str) > len(longest_str):
                    longest_str = curr_str
    return longest_str

print(get_shared_pattern(device1, device2))                