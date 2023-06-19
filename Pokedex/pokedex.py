from tkinter import *
from PIL import Image, ImageTk
from random import sample
from data import *

# Cores
backgroundFont = '#FFFFFF'
font = '#444466'

# Criando janela
app = Tk()
app.title('Pokedex')
app.geometry('550x510')
app.resizable(False, False)
app.config(bg=backgroundFont)

# Preparando imagens
gengarHead = Image.open('Pokedex/images/gengarhead.png')
gengarHead = gengarHead.resize((40, 40))
gengarHead = ImageTk.PhotoImage(gengarHead)

pikachuHead = Image.open('Pokedex/images/pikachuhead.png')
pikachuHead = pikachuHead.resize((40, 40))
pikachuHead = ImageTk.PhotoImage(pikachuHead)

charmanderHead = Image.open('Pokedex/images/charmanderhead.png')
charmanderHead = charmanderHead.resize((40, 40))
charmanderHead = ImageTk.PhotoImage(charmanderHead)

articunoHead = Image.open('Pokedex/images/articunohead.png')
articunoHead = articunoHead.resize((40, 40))
articunoHead = ImageTk.PhotoImage(articunoHead)

alakazamHead = Image.open('Pokedex/images/alakazamhead.png')
alakazamHead = alakazamHead.resize((40, 40))
alakazamHead = ImageTk.PhotoImage(alakazamHead)

# Função para trocar o pokemon


def changePokemon(i):
    global pokeImage, imagePokemon

    # Mudando cor do Frame Pokemon
    pokeFrame['bg'] = pokemon[i]['Type'][3]

    # Mudando nome, tipo e id
    pokeName['text'] = i
    pokeName['bg'] = pokemon[i]['Type'][3]
    pokeType['text'] = pokemon[i]['Type'][1]
    pokeType['bg'] = pokemon[i]['Type'][3]
    pokeId['text'] = pokemon[i]['Type'][0]
    pokeId['bg'] = pokemon[i]['Type'][3]

    # Mudando imagem e cor de fundo
    imagePokemon = Image.open(pokemon[i]['Type'][2])
    imagePokemon = imagePokemon.resize((238, 238))
    imagePokemon = ImageTk.PhotoImage(imagePokemon)
    pokeImage = Label(pokeFrame, image=imagePokemon, relief='flat',
                      bg=pokemon[i]['Type'][3], fg=backgroundFont)
    pokeImage.place(x=160, y=50)

    # Mudando Status
    hp['text'] = pokemon[i]['Status'][0]
    attack['text'] = pokemon[i]['Status'][1]
    defense['text'] = pokemon[i]['Status'][2]
    speed['text'] = pokemon[i]['Status'][3]
    total['text'] = pokemon[i]['Status'][4]
    skillOne['text'] = pokemon[i]['Skills'][0]
    skillTwo['text'] = pokemon[i]['Skills'][1]


pokeFrame = Frame(app, width=550, height=295, bg='#a292bc')
pokeFrame.pack()

# Configurando pokeFrame
pokeName = Label(pokeFrame, text='Gengar', width=9, height=1, font=(
    'fixedysys 20'), anchor='w', bg='#a292bc', fg=backgroundFont)
pokeName.place(x=15, y=16)

pokeType = Label(pokeFrame, text='Shadow', width=11, height=1, font=(
    'Ivy 10 bold'), anchor='w', bg='#a292bc', fg=backgroundFont)
pokeType.place(x=15, y=55)

pokeId = Label(pokeFrame, text='#0094', width=6, height=1, font=(
    'Ivy 10 bold'), anchor='w', bg='#a292bc', fg=backgroundFont)
pokeId.place(x=15, y=83)


# Configurando infos
status = Label(app, text='Status', width=6, height=1,
               font=('Verdana 17'), bg=backgroundFont, fg=font)
status.place(x=15, y=300)

hp = Label(app, text='HP: 60', width=10, height=1, anchor='w',
           font=('Verdana 10'), bg=backgroundFont, fg=font)
hp.place(x=8, y=340)

attack = Label(app, text='Attack: 65', width=10, height=1,
               anchor='w', font=('Verdana 10'), bg=backgroundFont, fg=font)
attack.place(x=8, y=365)

defense = Label(app, text='Defense: 60', width=11, height=1,
                anchor='w', font=('Verdana 10'), bg=backgroundFont, fg=font)
defense.place(x=8, y=390)

speed = Label(app, text='Speed: 110', width=10, height=1,
              anchor='w', font=('Verdana 10'), bg=backgroundFont, fg=font)
speed.place(x=8, y=415)

total = Label(app, text='Total: 295', width=10, height=1,
              anchor='w', font=('Verdana 10'), bg=backgroundFont, fg=font)
total.place(x=8, y=440)

skills = Label(app, text='Skills', width=6, height=1,
               font=('Verdana 17'), bg=backgroundFont, fg=font)
skills.place(x=230, y=300)

skillOne = Label(app, text='Shadow Punch', width=14, height=1,
                 anchor='w', font=('Verdana 10'), bg=backgroundFont, fg=font)
skillOne.place(x=250, y=340)

skillTwo = Label(app, text='Dream Eater', width=14, height=1,
                 anchor='w', font=('Verdana 10'), bg=backgroundFont, fg=font)
skillTwo.place(x=250, y=365)


# Criando botões
poke1_button = Button(app, command=lambda: changePokemon('Gengar'), image=gengarHead, text='Gengar', width=140, font=(
    'Verdana 12'), bg=backgroundFont, fg=font, compound=LEFT, anchor='w', relief='ridge', overrelief='sunken')
poke1_button.place(x=400, y=10)

poke2_button = Button(app, command=lambda: changePokemon('Pikachu'), image=pikachuHead, text='Pikachu', width=140, font=(
    'Verdana 12'), bg=backgroundFont, fg=font, compound=LEFT, anchor='w', relief='ridge', overrelief='sunken')
poke2_button.place(x=400, y=65)

poke3_button = Button(app, command=lambda: changePokemon('Charmander'), image=charmanderHead, text='Charmander', width=140, font=(
    'Verdana 12'), bg=backgroundFont, fg=font, compound=LEFT, anchor='w', relief='ridge', overrelief='sunken')
poke3_button.place(x=400, y=120)

poke4_button = Button(app, command=lambda: changePokemon('Articuno'), image=articunoHead, text='Articuno', width=140, font=(
    'Verdana 12'), bg=backgroundFont, fg=font, compound=LEFT, anchor='w', relief='ridge', overrelief='sunken')
poke4_button.place(x=400, y=175)

poke5_button = Button(app, command=lambda: changePokemon('Alakazam'), image=alakazamHead, text='Alakazam', width=140, font=(
    'Verdana 12'), bg=backgroundFont, fg=font, compound=LEFT, anchor='w', relief='ridge', overrelief='sunken')
poke5_button.place(x=400, y=230)


# Configurando qual pokemon aparece quando executar
listPokemon = ['Gengar', 'Pikachu', 'Charmander', 'Articuno', 'Alakazam']
choicedPokemon = sample(listPokemon, 1)
changePokemon(choicedPokemon[0])

app.mainloop()
