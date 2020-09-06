#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random


# In[4]:


puntos_atributos=[3,5,7]
puntos_habilidades=[7,9,13]


# In[5]:


Nat_and_conducta=["Ansioso de emociones", "Arquitecto", "Autócrata", "Bellaco", "Bravucón", "Camaleón", "Capitalista", "Celebrante", "Científico", "Competidor", 'Confabulador', 'Conformista', 'Depravado', 'Diletante', 'Director', 'Enigma', 'Fanático', 'Gallardo', 'Gurú', 'Hedonista', 'Hosco', 'Idealista', 'Juez', 'Mártir', 'Masoquista', 'Monstruo', 'Niño', 'Ojo de la tormenta', 'Pedagogo', 'Penitente', 'Perfeccionista', 'Protector', 'Rebelde', 'Repulsivo', 'Sádico', 'Sociópata', 'Soldado', 'Solitario', 'Superviviente', 'Tradicionalista', 'Truhán', 'Visionario']
Clanes=['Brujah', 'Gangrel', 'Malkavian', 'Nosferatu', 'Toreador', 'Tremere', 'Ventrue']


# In[6]:


Fisicos=['Fuerza', 'Destreza', 'Resistencia']
Sociales=['Carisma', 'Manipulación', 'Apariencia']
Mentales=['Percepción','Inteligencia', 'Astucia']
Atributos=['Fisicos', 'Sociales', 'Mentales']
Virtudes=['Conciencia', 'Autocontrol', 'Coraje']


# In[7]:


Talentos=['Alerta', 'Atletismo', 'Callejeo', 'Consciencia', 'Empatía', 'Expresión', 'Intimidación', 'Liderazgo', 'Pelea', 'Subterfugio']
Tecnicas=['Armas de fuego', "Artesanía", 'Conducir', 'Etiqueta', 'Interpretación', 'Latrocinio', 'Pelea con Armas', 'Sigilo', 'Supervivencia', 'Trato con Animales']
Conocimientos=['Academicismo', 'Ciencias', 'Finanzas', 'Informática', 'Investigación', 'Leyes', 'Medicina', 'Ocultismo', 'Política', 'Tecnología']
Habilidades=['Talentos', 'Tecnicas', 'Conocimientos']


# In[8]:


Trasfondos=['Aliados', 'Contactos', 'Criados', 'Dominio', 'Estatus', 'Fama', 'Generación', 'Identidad alternativa', 'Influencia', 'Mentor', 'Rebaño', 'Recursos']


# In[9]:


Disciplinas=[['Animalismo', ['Gangrel','Nosferatu']], ['Auspex', ['Malkavian','Toreador', 'Tremere']], ['Celeridad', ['Brujah','Toreador']], ['Dementación', ['Malkavian']], ['Dominación', ['Tremere','Ventrue']], ['Fortaleza', ['Gangrel','Ventrue']], ['Ofuscación', ['Malkavian','Nosferatu']], ['Potencia', ['Brujah','Nosferatu']], ['Presencia', ['Toreador','Ventrue', 'Brujah']],['Protean', ['Gangrel']], ['Taumaturgia', ['Tremere']]]


# In[25]:


def pj():
    try:
        crear_pj()
    except: 
        pj()
        
def depurar_disc(Clan):
    disciplinas_del_clan=[]
    for i in Disciplinas:
        if Clan in i[1]:
            disciplinas_del_clan=disciplinas_del_clan + [i]
    return disciplinas_del_clan

def armar_duplas(a,b):
    lst=[]
    for i in a:
        lst = lst + [[i, b[a.index(i)]]]
    return lst

def duplas_to_dic(a):
    dict={}
    for l2 in a:
        dict[l2[0]] = l2[1:][0]
    return dict

def generacion(lst):
        for i in lst:
            if "Generación" in i:
                return i[1]
   
def crear_pj():
    global Virtudes          
    Naturaleza=random.choice(Nat_and_conducta)
    Conducta=random.choice(Nat_and_conducta)
    Clan=random.choice(Clanes)
    disciplinas_orden=random.sample(depurar_disc(Clan), len(depurar_disc(Clan)))
    Virtudes_orden=random.sample(Virtudes, 3)
    Atributos_orden=random.sample(Atributos,3)
    Habilidades_orden=random.sample(Habilidades, 3)
    Fisicos_orden=random.sample(Fisicos,3)
    Sociales_orden=random.sample(Sociales,3)
    Mentales_orden=random.sample(Mentales,3)
    Tecnicas_orden=random.sample(Tecnicas, 10)
    Conocimientos_orden=random.sample(Conocimientos, 10)
    Talentos_orden=random.sample(Talentos, 10)
    Trasfondos_orden=random.sample(Trasfondos,12)
    data_atributos=duplas_to_dic(armar_duplas(Atributos_orden, puntos_atributos ))
    data_habilidades=duplas_to_dic(armar_duplas(Habilidades_orden, puntos_habilidades ))
    
    counter=data_atributos.get('Fisicos')
    Fisicos_order_points=[]
    i=0   
    while counter>0:
        rnd=random.randint(0, 4)
        if counter-rnd>0:
            Fisicos_order_points=Fisicos_order_points + [[Fisicos_orden[i], rnd+1]]
            counter = counter - rnd
            i=i+1
            if i==2 and counter+1<5 :
                Fisicos_order_points=Fisicos_order_points+[[Fisicos_orden[i], counter+1]]
                counter=0
            elif i==2 and counter+1>=5:
                print ('Re-attempting:')
               
                   
    counter=data_atributos.get('Mentales')
    Mentales_order_points=[]
    i=0   
    while counter>0:
        rnd=random.randint(0, 4)
        if counter-rnd>0:
            Mentales_order_points=Mentales_order_points + [[Mentales_orden[i], rnd+1]]
            counter = counter - rnd
            i=i+1
            if i==2 and counter+1<5:
                Mentales_order_points=Mentales_order_points+[[Mentales_orden[i], counter+1]]
                counter=0
            elif i==2 and counter+1>=5:
                print ('Re-attempting:')
                    
    counter=data_atributos.get('Sociales')
    Sociales_order_points=[]
    i=0   
    while counter>0:
        rnd=random.randint(0, 4)
        if counter-rnd>0:
            Sociales_order_points=Sociales_order_points + [[Sociales_orden[i], rnd+1]]
            counter = counter - rnd
            i=i+1
            if i==2 and counter+1<5:
                Sociales_order_points=Sociales_order_points+[[Sociales_orden[i], counter+1]]
                counter=0
            elif i==2 and counter+1>=5:
                print ('Re-attempting:')
                                
    counter=data_habilidades.get('Talentos')
    Talentos_order_points=[]
    i=0   
    while counter>0:
        rnd=random.randint(0, 3)
        if counter-rnd>0:
            Talentos_order_points=Talentos_order_points + [[Talentos_orden[i], rnd]]
            counter = counter - rnd
            i=i+1
            if i==9 and counter<6:
                Talentos_order_points=Talentos_order_points+[[Talentos_orden[i], counter]]
                counter=0
            elif i==9 and counter>=6:
                print ('Re-attempting:')
                               
    counter=data_habilidades.get('Tecnicas')
    Tecnicas_order_points=[]
    i=0   
    while counter>0:
        rnd=random.randint(0, 3)
        if counter-rnd>0:
            Tecnicas_order_points=Tecnicas_order_points + [[Tecnicas_orden[i], rnd]]
            counter = counter - rnd
            i=i+1
            if i==9 and counter<6:
                Tecnicas_order_points=Tecnicas_order_points+[[Tecnicas_orden[i], counter]]
                counter=0
            elif i==9 and counter>=6:
                print ('Re-attempting:')
                   
    counter=data_habilidades.get('Conocimientos')
    Conocimientos_order_points=[]
    i=0   
    while counter>0:
        rnd=random.randint(0, 3)
        if counter-rnd>0:
            Conocimientos_order_points=Conocimientos_order_points + [[Conocimientos_orden[i], rnd]]
            counter = counter - rnd
            i=i+1
            if i==9 and counter<6:
                Conocimientos_order_points=Conocimientos_order_points+[[Conocimientos_orden[i], counter]]
                counter=0
            elif i==9 and counter>=6:
                print ('Re-attempting:')
                               
    counter=3
    disciplinas_order_points=[]
    i=0   
    while counter>0:
        rnd=random.randint(0, 3)
        if counter-rnd>0:
            disciplinas_order_points=disciplinas_order_points + [[disciplinas_orden[i][0], rnd]]
            counter = counter - rnd
            i=i+1
            if i==len(disciplinas_orden)-1:
                disciplinas_order_points=disciplinas_order_points+[[disciplinas_orden[i][0], counter]]
                counter=0
                  
     
    counter=5
    Trasfondos_order_points=[]
    i=0   
    while counter>0:
        rnd=random.randint(0, 5)
        if counter-rnd>0:
            Trasfondos_order_points=Trasfondos_order_points + [[Trasfondos_orden[i], rnd]]
            counter = counter - rnd
            i=i+1
            if i==len(Trasfondos_orden)-1:
                Trasfondos_order_points=Trasfondos_order_points+[[Trasfondos_orden[i], counter]]
                counter=0
            elif i==2 and counter+1>=5:
                print ('Re-attempting:')
                    
    counter=7
    Virtudes_order_points=[]
    i=0   
    while counter>0:
        rnd=random.randint(0, 4)
        if counter-rnd>0:
            Virtudes_order_points=Virtudes_order_points + [[Virtudes_orden[i], rnd+1]]
            counter = counter - rnd
            i=i+1
            if i==len(Virtudes_orden)-1 and counter+1<5:
                Virtudes_order_points=Virtudes_order_points+[[Virtudes_orden[i], counter+1]]
                counter=0    
            elif i==len(Virtudes_orden)-1 and counter+1>=5:
                print ('Re-attempting:')
                    
    Virtudes_values={}
    for i in Virtudes_order_points:
        Virtudes_values[i[0]]= i[1]
    
    Humanidad=Virtudes_values['Conciencia'] + Virtudes_values['Autocontrol']
    Fuerza_de_voluntad= Virtudes_values['Coraje']
        
   
    
    print('\n'+'Clan: ' + Clan)
    print('Naturaleza: ' + Naturaleza)
    print('Conducta: ' + Conducta)
    print("Generación:"+ str(13-generacion(Trasfondos_order_points)))
    print("\n")
    print('Atributos: ')
    print(Fisicos_order_points)
    print(Sociales_order_points) 
    print(Mentales_order_points)
    print('\n'+'Habilidades: ')
    print(Talentos_order_points)
    print()
    print(Tecnicas_order_points) 
    print()
    print(Conocimientos_order_points)
    print()
    print()
    print('Disciplinas: ')
    print(disciplinas_order_points)
    print()
    print('Trasfondos: ')
    print(Trasfondos_order_points)
    print()
    print('Virtudes: ')
    print(Virtudes_order_points)
    print()
    print('Humanidad:'+str(Humanidad))
    print('Fuerza de voluntad:'+str(Fuerza_de_voluntad))
    
      
    
    
    print()
    print('Recuerda debes agregar un concepto al personaje.')
    print('Y que debes agregar los 15 puntos gratis de acuerdo a la siguiente tabla:'+'\n')
    print('Atributo 5 por círculo')
    print('Habilidad 2 por círculo')
    print('Disciplina 7 por círculo')
    print('Trasfondo 1 por círculo')
    print('Virtud 2 por círculo')
    print('Humanidad/Senda 2 por círculo')
    print('Fuerza de Voluntad 1 por círculo')
    
  
    


    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
       
      


# In[26]:


pj()


# In[ ]:




