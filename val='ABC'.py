val='ABC'
for x in val:
    ord_val=ord(x)
    conv_chr=ord_val+32
    print(chr(conv_chr))


val='abc'
for x in val:
    ord_val=ord(x)
    conv_chr=ord_val-32
    print(chr(conv_chr))
