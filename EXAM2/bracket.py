
user_input="{[]}"

symbol_table={
    "<":">",
    "[":"]",
    "(":")",
    "{":"}"
}
symbol_stack=[]
top=-1
is_Valid=True

for symbol in user_input:
    if symbol in symbol_table:
        top+=1
        symbol_stack.append(symbol)
    
    else:
        current_symbol=symbol_stack[top]
        current_symbol_closing=symbol_table[current_symbol]

        if symbol == current_symbol_closing:
            symbol_stack.pop()
            top-=1
        
        else:
            is_Valid=False
            break
if len(symbol_stack)!=0:
    print("not valid")

else:
    print("Valid")
    

