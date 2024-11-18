# Code de Hugo && Thomas
suits_symbols = {
    'coeur': '♥',  # Coeur
    'pic': '♠',  # Pique
    'carreaux': '♦',  # Carreau
    'trèfle': '♣'   # Trèfle
}

def print_card(rank, suit):
    card_templateA = [
        "###########",
        f"# {'A'}       #", 
        f"#         #",
        f"#         #",
        f"#    {suits_symbols[suit]}    #",
        f"#         #",
        f"#         #",
        f"#    {'A'}    #",
        "###########"
    ]
    card_template2 = [
        "###########",
        f"# {rank:<2}      #",
        f"#         #",
        "#         #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        "#         #",
        "#         #",
        f"#      {rank:>2} #",
        "###########"
    ]
    card_template3 = [
        "###########",
        f"# {rank:<2}      #",
        f"#    {suits_symbols[suit]}    #",
        "#         #",
        f"#    {suits_symbols[suit]}    #",
        "#         #",
        f"#    {suits_symbols[suit]}    #",
        f"#      {rank:>2} #",
        "###########"
    ]
    
    card_template4 = [
        "###########",
        f"# {rank:<2}      #",
        f"#         #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        f"#         #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        f"#         #",
        f"#      {rank:>2} #",
        "###########"
    ]
    
    card_template5 = [    
        "###########",
        f"# {rank:<2}      #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        "#         #",
        f"#    {suits_symbols[suit]}    #",
        "#         #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        f"#      {rank:>2} #",
        "###########"
    ]
    
    card_template6 = [    
        "###########",
        f"# {rank:<2}      #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        "#         #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        "#         #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        f"#      {rank:>2} #",
        "###########"
    ]
    
    card_template7 = [
        "###########",
        f"# {rank:<2}      #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        f"#    {suits_symbols[suit]}    #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        "#         #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        f"#      {rank:>2} #",
        "###########"
        
    ]
    
    card_template8 = [
        "###########",
        f"# {rank:<2}      #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        f"#    {suits_symbols[suit]}    #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        f"#    {suits_symbols[suit]}    #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        f"#      {rank:>2} #",
        "###########"
    ]

    card_template9 = [
        "###########",
        f"# {rank:<2}      #", 
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        f"#   {suits_symbols[suit]} {suits_symbols[suit]}   #",
        f"#    {suits_symbols[suit]}    #",
        f"#   {suits_symbols[suit]} {suits_symbols[suit]}   #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        f"#      {rank:>2} #",
        "###########"
    ]

    card_template10 = [
        "###########",
        f"# {rank:<2}      #", 
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        f"#  {suits_symbols[suit]}   {suits_symbols[suit]}  #",
        f"#      {rank:>2} #",
        "###########"
    ]

    card_templateJ = [
        "###########",
        f"# {'J'}       #", 
        f"#  {suits_symbols[suit]}    {suits_symbols[suit]} #",
        f"#  {suits_symbols[suit]}    {suits_symbols[suit]} #",
        f"#  {suits_symbols[suit]}    {suits_symbols[suit]} #",
        f"#  {suits_symbols[suit]}    {suits_symbols[suit]} #",
        f"#  {suits_symbols[suit]}    {suits_symbols[suit]} #",
        f"#  {suits_symbols[suit]}  {'J'}   #",
        "###########"
    ]

    card_templateQ = [
        "###########",
        f"# {'Q'}     {suits_symbols[suit]} #", 
        f"#  {suits_symbols[suit]}    {suits_symbols[suit]} #",
        f"#  {suits_symbols[suit]}    {suits_symbols[suit]} #",
        f"#  {suits_symbols[suit]}    {suits_symbols[suit]} #",
        f"#  {suits_symbols[suit]}    {suits_symbols[suit]} #",
        f"#  {suits_symbols[suit]}    {suits_symbols[suit]} #",
        f"#  {suits_symbols[suit]}  {'Q'}   #",
        "###########"
    ]
    
    card_templateK = [
        "###########",
        f"# {'K'}     {suits_symbols[suit]} #", 
        f"#  {suits_symbols[suit]}    {suits_symbols[suit]} #",
        f"#  {suits_symbols[suit]}    {suits_symbols[suit]} #",
        f"#  {suits_symbols[suit]} {suits_symbols[suit]} {suits_symbols[suit]}  #",
        f"#  {suits_symbols[suit]}    {suits_symbols[suit]} #",
        f"#  {suits_symbols[suit]}    {suits_symbols[suit]} #",
        f"#  {suits_symbols[suit]}  {'K'}   #",
        "###########"
    ]

    
    if rank == 14:
        for line in card_templateA:
            print(line)

    if rank == 2:
        for line in card_template2:
            print(line)
    
    if rank == 3:
        for line in card_template3:
            print(line)
    
    if rank == 4:
        for line in card_template4:
            print(line)
    
    if rank == 5:
        for line in card_template5:
            print(line)
    
    if rank == 6:
        for line in card_template6:
            print(line)
    
    if rank == 7:
        for line in card_template7:
            print(line)
    
    if rank == 8:
        for line in card_template8:
            print(line)
            
    if rank == 9:
        for line in card_template9:
            print(line)

    if rank == 10:
        for line in card_template10:
            print(line)
    if rank == 11:
        for line in card_templateJ:
            print(line)

    if rank == 12:
        for line in card_templateQ:
            print(line)

    if rank == 13:
        for line in card_templateK:
            print(line)
    
    if rank >= 10:
        return 0
    if rank <= 1:
        return 0
    return 1

