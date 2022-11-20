# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            print("X=",bool(x==1), " Y=", bool(y==1)," Z=", bool(z==1), "Then answer is", bool((not((x==1)or(y==1)or(z==1)))==(not(x==1) and not(y==1) and not(z==1) )) )