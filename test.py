from LZ77 import LZ77_c, LZ77_dec
import time

# Тестирование алгоритма с пустой строкой
def test_empty_string():
    data = ""
    compressed = LZ77_c(data)
    decompressed = LZ77_dec(compressed)
    assert data == decompressed

# Тестирование алгоритма с одним символом
def test_single_character():
    data = "a"
    compressed = LZ77_c(data)
    decompressed = LZ77_dec(compressed)
    assert data == decompressed

# Тестирование алгоритма с повторяющимися символами
def test_repeated_characters():
    data = "aaaabbbbcccc"
    compressed = LZ77_c(data)
    decompressed = LZ77_dec(compressed)
    assert data == decompressed

# Тестирование алгоритма с длинной строкой
def test_long_string():
    data = "abcdefghijklmnopqrstuvwxyz" * 100
    compressed = LZ77_c(data)
    decompressed = LZ77_dec(compressed)
    assert data == decompressed

# Тестирование алгоритма с смешанными символами
def test_mixed_characters():
    data = "abc123!@#"
    compressed = LZ77_c(data)
    decompressed = LZ77_dec(compressed)
    assert data == decompressed

# Тестирование алгоритма с произвольными данными
def test_random_data():
    data = "abracadabra"
    compressed = LZ77_c(data)
    decompressed = LZ77_dec(compressed)
    assert data == decompressed

# Тест на производительность
import time
def test_performance():
    data = "abcdefghijklmnopqrstuvwxyz" * 1000
    start_time = time.time()
    compressed = LZ77_c(data)
    compression_time = time.time() - start_time

    start_time = time.time()
    decompressed = LZ77_dec(compressed)
    decompression_time = time.time() - start_time

    print("Время сжатия: {} секунд".format(compression_time))
    print("Время распаковки: {} секунд".format(decompression_time))


# Запуск всех тестов
if __name__ == '__main__':
    test_empty_string()
    test_single_character()
    test_repeated_characters()
    test_long_string()
    test_mixed_characters()
    test_random_data()
    test_performance()

    print("Проведенные тесты соответствуют ожидаемым результатам.")
    time.sleep(5)

