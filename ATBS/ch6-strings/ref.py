#!/usr/bin/env python3

def main():
    """This is a multiline comment that
    describes what main() does"""

    print("""Dear Rodrigo,

I'm a multiline string.
    I'm tabbed. It's not ignored

Sincerely,
This Program""")

    name = "Rodrigo"
    age = 99

    # Two ways to do the same thing
    str_interpolation = "I'm %s. I'm %s" % (name, age)
    print(str_interpolation)
    f_str = f"I'm also {name}, {age} years old."
    print(f_str)

    print("")
    print("'hello'.islower():", 'hello'.islower())
    print("'hello123'.islower():", 'hello123'.islower())
    print("'Hello'.islower():", 'Hello'.islower())
    print("'1234'.islower():", '1234'.islower())

    print("")
    print("'HELLO'.isupper():", 'HELLO'.isupper())
    print("'Hello'.isupper():", 'Hello'.isupper())
    print("'1234'.isupper():", '1234'.isupper())    

    print("")
    print("'hello'.isalpha():", 'hello'.isalpha())
    print("'hello123'.isalpha():", 'hello123'.isalpha())    
    print("'hello123'.isalnum():", 'hello123'.isalnum()) 
    print("'123'.isdecimal():", '123'.isdecimal())    
    print("'123.35'.isdecimal():", '123.35'.isdecimal())
    print("'     '.isspace():", '     '.isspace())    

    print("")
    print("'This Is Title Case'.istitle():",'This Is Title Case'.istitle())      
    print("'This Is Title Case 123'.istitle():",'This Is Title Case 123'.istitle())     
    print("'This Is not Title Case'.istitle():",'This Is not Title Case'.istitle())        
    print("'This is Not Title Case'.istitle():",'This is Not Title Case'.istitle())      
    print("'This Is NOT Title Case'.istitle():",'This Is NOT Title Case'.istitle())

    print("")
    print("'Hello, world!'.startswith('Hello'):", 'Hello, world!'.startswith('Hello'))
    print("'Hello, world!'.endswith('Hello'):", 'Hello, world!'.endswith('world!'))
    print("'abc123'.startswith('abcdef'):", 'abc123'.startswith('abcdef'))
    print("'abc123'.endswith('12'):", 'abc123'.endswith('12'))
    print("'Hello, world!'.startswith('Hello, world!'):", 'Hello, world!'.startswith('Hello, world!'))
    print("'Hello, world!'.endswith('Hello, world!'):", 'Hello, world!'.endswith('Hello, world!'))

    print("")
    print("' '.join(['My', 'name', 'is', 'Rodrigo',]):", ' '.join(['My', 'name', 'is', 'Rodrigo',]))
    print("'--'.join(['My', 'name', 'is', 'Rodrigo',]):", '--'.join(['My', 'name', 'is', 'Rodrigo',])) 


    print("")
    print("'Hello, world!'.partition('w'):", 'Hello, world!'.partition('w'))
    print("'Hello, world!'.partition('o'):", 'Hello, world!'.partition('o'))    
    print("'Hello, world!'.partition('world'):", 'Hello, world!'.partition('world'))      
    print("'Hello, world!'.partition('XYZ'):", 'Hello, world!'.partition('XYZ'))
    before, sep, after = "Hello, world!".partition("orl")
    print(f"before: {before}\nsep: {sep}\nafter: {after}")

    print("")
    print("'Hello'.rjust(15)\n", 'Hello'.rjust(15))
    
    print("")    
    print("'Hello'.rjust(20)\n", 'Hello'.rjust(20))

    print("")    
    print("'Hello'.ljust(15)\n", 'Hello'.ljust(15), "hm")

    print("")    
    print("'Hello'.ljust(20, '.')\n", 'Hello'.ljust(20, '.'), "hm")

    print("")    
    print("'Hello'.center(20, '_')\n", 'Hello'.center(20, '_'))

    print("")
    spam = '   \t    Hello, world      '
    print(r"spam = ' \t    Hello, world      '")
    print("spam.strip():", spam.strip())
    print("spam.lstrip():", spam.lstrip())
    print("spam.rstrip():", spam.rstrip())
    spam = 'SpamSpamBaconSpamEggsSpamSpam'
    print("spam = 'SpamSpamBaconSpamEggsSpamSpam'")
    print("spam.strip('pamS'):", spam.strip("pamS"))

    print("")
    print("ord() - Returns Unicode code point".center(50, '-'))
    print("ord('A'):", ord('A'))
    print("ord('B'):", ord('B'))
    print("ord('4'):", ord('4'))
    print("ord('!'):", ord('!'))
    print("ord('A') < ord('B'):", ord('A') < ord('B'))

    print("")    
    print("chr() - Returns character from code point".center(50, '-'))  
    print("chr('A'):", chr(65))
    print("chr(ord('A')):", chr(ord('A')))
    print("chr(ord('A') + 1):", chr(ord('A') + 1))



if __name__ == "__main__":
    main()