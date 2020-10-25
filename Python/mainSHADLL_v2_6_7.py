#!/usr/bin/python3
#-*- coding: utf-8 -*-

#https://docs.python.org/3/library/ctypes.html

import sys
import time
#import timeit
import ctypes 
import struct

#def  digest(hs0, hs1, hs2, hs3,            hs4,hs5, hs6, hs7):
#        return struct.pack(">8Q", hs0, hs1, hs2, hs3,    hs4,hs5, hs6, hs7)
    
# Загрузка библиотеки
libc = ctypes.CDLL('C:\my_python\c_from_python-master\my\myDLL2_7.dll')
 
###
## C
###

print("ctypes\n")
print("C\n")

#start_time = time.time()

##
# Работа с функциями
##
# Указываем, что функция принимает аргумент char *
#test.func_ret_str.argtypes = [ctypes.POINTER(ctypes.c_char), ]

#void  DLL_EXPORT sha512_process(uint64_t state[8], const uint8_t data[], uint64_t length)
#uint64_t * DLL_EXPORT sha512_process( const uint8_t data[], uint64_t length)
#libc.sha512_process.argtypes = [ ctypes.POINTER(ctypes.c_char),ctypes.c_ulonglong]

# Указываем, что функция принимает аргумент char *
libc.sha512_process.argtypes = [ ctypes.POINTER(ctypes.c_char)]

# Указываем, что функция возвращает uint64_t *
#libc.sha512_process.restype = ctypes.POINTER(ctypes.c_int) #ctypes.c_void

# Указываем, что функция возвращает void
#libc.sha512_process.restype = ctypes.c_void


print('\nРабота с переменными:')
# Указываем, что переменная типа int
Lng = ctypes.c_ulonglong.in_dll(libc, "length")
hs0 = ctypes.c_ulonglong.in_dll(libc, "h0")
hs1 = ctypes.c_ulonglong.in_dll(libc, "h1")
hs2 = ctypes.c_ulonglong.in_dll(libc, "h2")
hs3 = ctypes.c_ulonglong.in_dll(libc, "h3")
hs4 = ctypes.c_ulonglong.in_dll(libc, "h4")
hs5 = ctypes.c_ulonglong.in_dll(libc, "h5")
hs6 = ctypes.c_ulonglong.in_dll(libc, "h6")
hs7 = ctypes.c_ulonglong.in_dll(libc, "h7")

#ch_s=ctypes.c_char_p.in_dll(libc, "data")  
print('ret Lg==length: ', Lng.value)

# Изменяем значение переменной.
#ch_s="starting string"
#print('ch_s=',ch_s)
original_string = "starting string"
Lng.value = len(original_string)
print('new Lg==length: ', Lng.value)

#hash=libc.sha512_process(mutable_string.raw,Lng)  # Works???
#hash=libc.sha512_process(original_string.encode('utf-8'))

#start_time = time.perf_counter()
# Необходимо строку привести к массиву байтов, 
#libc.sha512_process(original_string.encode('utf-8'))

# Буфер строки ctypes является изменяемым, однако...
print("Calling C function with mutable buffer this time")
# ... нужно закодировать оригинал, чтобы получить биты для 
mutable_string = ctypes.create_string_buffer(str.encode(original_string))
print("Before:", mutable_string.value)

libc.sha512_process(mutable_string)  # 
#libc.sha512_process()
# Время работы
#print("--- {} seconds ---".format( (time.perf_counter() - start_time)) )

hash=[hs0.value,hs1.value,hs2.value,hs3.value,hs4.value,hs5.value,hs6.value,hs7.value]
print(' HASH=',hash)
#print( digest(hs0.value, hs1.value, hs2.value, hs3.value, hs4.value,hs5.value, hs6.value, hs7.value))

#original_string ='The quick brown fox jumped over the lazy dog' # <- RFC 
#print('original_string =',original_string )
# Изменяем значение переменной.
ch_s='The quick brown fox jumped over the lazy dog' # <- RFC
Lng.value = len(ch_s)
print('new Lg==length: ', Lng.value)

mutable_string = ctypes.create_string_buffer(str.encode(ch_s))
print("Before:", mutable_string.value)

libc.sha512_process(mutable_string)  # 



#hash=libc.sha512_process(mutable_string.raw,Lng)  # Works???
#hash=libc.sha512_process(original_string.encode('utf-8'))

#start_time = time.perf_counter()
# Необходимо строку привести к массиву байтов,

#libc.sha512_process()
# Время работы
#print("--- {} seconds ---".format( (time.perf_counter() - start_time)) )
hs0 = ctypes.c_ulonglong.in_dll(libc, "h0")
hs1 = ctypes.c_ulonglong.in_dll(libc, "h1")
hs2 = ctypes.c_ulonglong.in_dll(libc, "h2")
hs3 = ctypes.c_ulonglong.in_dll(libc, "h3")
hs4 = ctypes.c_ulonglong.in_dll(libc, "h4")
hs5 = ctypes.c_ulonglong.in_dll(libc, "h5")
hs6 = ctypes.c_ulonglong.in_dll(libc, "h6")
hs7 = ctypes.c_ulonglong.in_dll(libc, "h7")
hash=[hs0.value,hs1.value,hs2.value,hs3.value,hs4.value,hs5.value,hs6.value,hs7.value]
print(' HASH=',hash)
# Необходимо строку привести к массиву байтов, и массив байтов к строке.
#print('ret func_ret_str: ', test.func_ret_str('Hello!'.encode('utf-8')).decode("utf-8") )
#print('ret func_many_args: ', test.func_many_args(15, 18.1617, 'X'.encode('utf-8'), 32000).decode("utf-8"))

# Время работы
#print("--- {} seconds ---".format((time.time() - start_time)))

