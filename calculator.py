def valid(number, base):
    sist = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    valid_sist = sist[:base]
    for n in number:
        if n.upper() not in valid_sist:
            return False
    return True

def table(base):
    sist = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = {}

    for i in range(base):
        for k in range(base):
            product = i * k
            res = ""
            while product > 0:
                res = sist[product % base] + res
                product //= base
            res = res if res else "0"
            table[(sist[i], sist[k])] = res
    return table

def summ(a, b, base, add_table):
    sist = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    perenos = 0
    maxlen = max(len(a), len(b))
    a = a.zfill(maxlen)
    b = b.zfill(maxlen)
    
    for i in range(maxlen - 1, -1, -1):
        numa = a[i]
        numb = b[i]
        val_a = sist.index(numa)
        val_b = sist.index(numb)
        total = val_a + val_b + perenos
        perenos = total // base
        resnum = sist[total % base]
        res = resnum + res
    
    if perenos:
        res = sist[perenos] + res
    return res

def diff(a, b, base):
    sist = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    take = 0
    maxlen = max(len(a), len(b))
    a = a.zfill(maxlen)
    b = b.zfill(maxlen)
    
    if a < b:
        return None

    for i in range(maxlen - 1, -1, -1):
        numa = a[i]
        numb = b[i]
        val_a = sist.index(numa) - take
        val_b = sist.index(numb)

        if val_a < val_b:
            val_a += base
            take = 1
        else:
            take = 0
        
        resnum = sist[val_a - val_b]
        res = resnum + res
    res = res.lstrip('0') or '0'
    return res

def multiply(a, b, base, multitable):
    sist = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = "0"
    
    for i, numb in enumerate(reversed(b)):
        partial = "0"
        for k, numa in enumerate(reversed(a)):
            product = multitable[(numa, numb)]
            if product != "0":
                product += "0" * k
            partial = summ(partial, product, base, {})
        if partial != "0":
            partial += "0" * i
        res = summ(res, partial, base, {})
    return res

def main():
    print("Калькулятор для различных систем счисления")
    print("Доступные операции: +, -, *")
    
    try:
        base = int(input("Введите основание системы счисления (2-36): "))
        if base < 2 or base > 36:
            print("Ошибка: основание должно быть от 2 до 36")
            return
        
        num1 = input("Введите первое число: ").upper().strip()
        if not valid(num1, base):
            print(f"Ошибка: число {num1} не соответствует системе с основанием {base}")
            return
        
        operation = input("Введите операцию (+, -, *): ").strip()
        if operation not in ['+', '-', '*']:
            print("Ошибка: неверная операция")
            return

        num2 = input("Введите второе число: ").upper().strip()
        if not valid(num2, base):
            print(f"Ошибка: число {num2} не соответствует системе с основанием {base}")
            return
        
        multitable = table(base)
        if operation == '+':
            res = summ(num1, num2, base, {})
            print(f"Результат: {num1} + {num2} = {res}")
        
        elif operation == '-':
            res = diff(num1, num2, base)
            if res is None:
                print("Ошибка: результат вычитания отрицательный")
            else:
                print(f"Результат: {num1} - {num2} = {res}")
        
        elif operation == '*':
            res = multiply(num1, num2, base, multitable)
            print(f"Результат: {num1} * {num2} = {res}")
    
    except ValueError:
        print("Ошибка: введены некорректные данные")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        
if __name__ == "__main__":
    main()
