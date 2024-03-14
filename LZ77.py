import time

def LZ77_c(data):
    compr = []
    ind = 0
    data_length = len(data)
    
    while ind < data_length:
        longest_match = ''
        longest_length = 0
        longest_offset = 0
        
        # Поиск самой длинной совпадающей подстроки
        for offset in range(1, min(ind,4096)+1):
            if data[ind-offset] == data[ind]:
                length = 1
                while length < min(data_length-ind, 4096-offset) and data[ind-offset+length] == data[ind+length]:
                    length += 1
                
                if length > longest_length:
                    longest_length = length
                    longest_offset = offset
        
        # Добавление информации о совпадении в сжатые данные
        if longest_length > 0:
            # Ограничиваем длину совпадения, чтобы не выйти за границы строки
            longest_length = min(longest_length, data_length-ind)
            compr.append((-longest_offset, longest_length, data[ind+longest_length] if ind+longest_length<data_length else ''))
            ind += longest_length + 1
        else:
            compr.append((0, 0, data[ind]))
            ind += 1
    
    return compr

def LZ77_dec(compr):
    decompr = ''
    
    for item in compr:
        offset, length, char = item
        
        if length == 0:
            decompr += char
        else:
            start = len(decompr)+offset
            substring = decompr[start:start+length]
            decompr += substring + char
    
    return decompr

if __name__ == "__main__":
    data = input("Введите текст для сжатия: ")
    c_data = LZ77_c(data)
    dec_data = LZ77_dec(c_data)

    print("Входные данные:", data)
    print("Сжатые данные:", c_data)
    print("Данные после распаковки:", dec_data)
    time.sleep(5)
