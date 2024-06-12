#!/usr/local/bin/python

def is_pallendrome(str): # Reverse the string and check that it is same as original string
    return True  if str == str[::-1] else False

def longest_pallendrome(str):
    print(str)
    if not str or len(str) == 1:
        return str
    longest_pallendrome = ""
    str_length = len(str)
    for i in range(str_length):
        if str_length - i <= len(longest_pallendrome): # Longest pallendrome already found.
            break
        for j in range(str_length , i , -1): #Do a reverse lookup.
            if is_pallendrome(str[i:j]):
                if j - i > len(longest_pallendrome):
                    longest_pallendrome = str[i:j]
                    break

    return longest_pallendrome

def main():
    print(longest_pallendrome("babad"))
    str = "jrjnbctoqgzimtoklkxcknwmhiztomaofwwzjnhrijwkgmwwuazcowskjhitejnvtblqyepxispasrgvgzqlvrmvhxusiqqzzibcyhpnruhrgbzsmlsuacwptmzxuewnjzmwxbdzqyvsjzxiecsnkdibudtvthzlizralpaowsbakzconeuwwpsqynaxqmgngzpovauxsqgypinywwtmekzhhlzaeatbzryreuttgwfqmmpeywtvpssznkwhzuqewuqtfuflttjcxrhwexvtxjihunpywerkktbvlsyomkxuwrqqmbmzjbfytdddnkasmdyukawrzrnhdmaefzltddipcrhuchvdcoegamlfifzistnplqabtazunlelslicrkuuhosoyduhootlwsbtxautewkvnvlbtixkmxhngidxecehslqjpcdrtlqswmyghmwlttjecvbueswsixoxmymcepbmuwtzanmvujmalyghzkvtoxynyusbpzpolaplsgrunpfgdbbtvtkahqmmlbxzcfznvhxsiytlsxmmtqiudyjlnbkzvtbqdsknsrknsykqzucevgmmcoanilsyyklpbxqosoquolvytefhvozwtwcrmbnyijbammlzrgalrymyfpysbqpjwzirsfknnyseiujadovngogvptphuyzkrwgjqwdhtvgxnmxuheofplizpxijfytfabx"
    print(longest_pallendrome(str))
if __name__=='__main__':
    main()
            

