from mypackages.modfuncoes import *

professores = []
alunos = []
disciplinas = []
turma = []

# FUNÇÕES ALUNOS


def list_alunos():  # l ista de alunos
    a = "-" * 70
    print("\nAlunos\n\n%s" % a)
    for p in alunos:
        show_data_student(p[0], p[1])
    print(a)


def show_data_student(student, cpf):  # exibe os dados dos alunos
    print("Alunx: %s CPF: %s" % (student, cpf))


def search_student(student):  # busca os dados dos alunos
    name = student.lower()
    for d, c in enumerate(alunos):
        if (c[0].lower()) == name:
            return d
    return None


def new_student():  # adiciona novo aluno
    global alunos
    name = ask_name()
    cpf = ask_cpf()
    alunos.append([name, cpf])


def delete_student():  # exclui um determinado aluno
    global alunos
    name = ask_name()
    m = search_student(name)
    if m is not None:
        del alunos[m]
    else:
        print("Alunx não encontradx")


def modify_student():  # modifica um determinado aluno
    s = search_student(ask_name())
    if s is not None:
        name = alunos[s][0]
        cpf = alunos[s][1]
        print("Encontrado.")
        show_data_student(name, cpf)
        name = ask_name()
        cpf = ask_cpf()
        alunos[s] = [name, cpf]
    else:
        print("Não encontrado!")


def read_student():  # Lê um arquivo que contém dados dos alunos
    try:
        global alunos
        archive_name = ask_archive_name()
        archive = open(archive_name, "r", encoding="utf-8")
        alunos = []
        for l in archive.readlines():
            student, cpf = l.strip().split("#")
            alunos.append([student, cpf])
        archive.close()
    except FileNotFoundError:
        print("\nArquivo não encontrado!")
    except ValueError:
        print("Erro: Talvez o arquivo que vocẽ está tentando abrir não "
              "esteja no formato ideal para ser lido neste programa.")


def save_alunos():  # Salva um arquivo com os dados dos alunos
    name_archive = ask_archive_name()
    archive = open(name_archive, "w", encoding="utf-8")
    for e in alunos:
        archive.write("%s#%s\n" % (e[0], e[1]))
    archive.close()


def menu_alunos():  # Menu dos alunos
    while True:
        try:
            print('''
1 - Criar
2 - Ler
3 - Editar
4 - Apagar
5 - Salvar arquivo
6 - Abrir arquivo
7 - Voltar ao menu principal
''')
            choice = int(input("Escolha uma opção: "))
            if choice == 1:
                new_student()
            elif choice == 2:
                list_alunos()
            elif choice == 3:
                modify_student()
            elif choice == 4:
                delete_student()
            elif choice == 5:
                save_alunos()
            elif choice == 6:
                read_student()
            elif choice == 7:
                menuprincipal()
            elif choice != range(1, 8):
                opcaoinvalida()
        except ValueError:
            opcaoinvalida()


# FUNÇÕES DISCIPLINAS ##########################

def ask_matter():  # Solicita/Retorna o nome da disciplina
    return input("Nome da disciplina: ")


def show_matter_data(matter, cod):  # Exibe os dados da disciplina
    print("Disciplina: %s Código: %s" % (matter, cod))


def list_disciplinas():  # Lista as disciplinas cadastradas
    a = "-" * 70
    print("\nDisciplinas\n\n%s" % a)
    for e in disciplinas:
        show_matter_data(e[0], e[1])
    print(a)


def search_matter(matter):  # Busca uma determinada disciplina
    mname = matter.lower()
    for d, c in enumerate(disciplinas):
        if (c[0].lower()) == mname:
            return d
    return None


def new_matter():  # Adiciona uma nova disciplina
    global disciplinas
    name = ask_matter()
    cod = ask_matter_cod()
    disciplinas.append([name, cod])


def delete_matter():  # Exclui uma determinada disciplina
    global disciplinas
    name = ask_matter()
    m = search_matter(name)
    if m is not None:
        del disciplinas[m]
    else:
        print("Disciplina não encontrada.")


def modify_matter():  # Modifica uma determinada disciplina
    s = search_matter(ask_matter())
    if s is not None:
        matter = disciplinas[s][0]
        cod = disciplinas[s][1]
        print("Encontrado.")
        show_matter_data(matter, cod)
        matter = ask_matter()
        cod = ask_matter_cod()
        disciplinas[s] = [matter, cod]
    else:
        print("Não encontrado")


def read_matter():  # Lê um arquivo que contém dados de disciplina(s)
    try:
        global disciplinas
        archive_name = ask_archive_name()
        archive = open(archive_name, "r", encoding="utf-8")
        disciplinas = []
        for l in archive.readlines():
            matter, cod = l.strip().split("#")
            disciplinas.append([matter, cod])
        archive.close()
    except FileNotFoundError:
        print("\nArquivo não encontrado!")


def save_matter():  # Salva um arquivo com informações de disciplinas
    name_archive = ask_archive_name()
    archive = open(name_archive, "w", encoding="utf-8")
    for e in disciplinas:
        archive.write("%s#%s\n" % (e[0], e[1]))
    archive.close()


def menu_disciplinas():  # Menu das disciplinas
    while True:
        try:
            print('''
1 - Criar   
2 - Ler
3 - Editar
4 - Apagar
5 - Salvar arquivo
6 - Abrir arquivo

7 - Retornar ao menu principal

    ''')
            choice = int(input("Escolha uma opção: "))

            if choice == 1:
                new_matter()
            elif choice == 2:
                list_disciplinas()
            elif choice == 3:
                modify_matter()
            elif choice == 4:
                delete_matter()
            elif choice == 5:
                save_matter()
            elif choice == 6:
                read_matter()
            elif choice == 7:
                menuprincipal()
            elif choice != range(1, 8):
                opcaoinvalida()
        except ValueError:
            opcaoinvalida()


# fUNÇÕES PROFESSORES ####################################################

def ask_department():  # Solicita/Retorna o departamento
    return input("Department: ")


def show_data_prof(name, cpf, dep):  # Exibe as informações do(s) professor(es)
    print("Nome: %s CPF: %s Departamento: %s" % (name, cpf, dep))


def list_prof():  # Lista as informações dos professores
    a = "-" * 70
    print("\nProfessores\n\n%s" % a)
    for e in professores:
        show_data_prof(e[0], e[1], e[2])
    print(a)


def search_prof(name):  # Procura um determinado professor
    mname = name.lower()
    for p, e in enumerate(professores):
        if e[0].lower() == mname:
            return p
    return None


def new_prof():  # Adiciona um novo professor
    global professores
    name = ask_name()
    cpf = ask_cpf()
    dep = ask_department()
    professores.append([name, cpf, dep])


def delete_prof():  # Exclui um determinado professor
    global professores
    name = ask_name()
    s = search_prof(name)
    if s is not None:
        del professores[s]
    else:
        print("Nome não encontrado.")


def altera_prof():  # Modifica as informações de um determinado professor
    s = search_prof(ask_name())
    if s is not None:
        name = professores[s][0]
        cpf = professores[s][1]
        dep = professores[s][2]
        print("Encontrado.")
        show_data_prof(name, cpf, dep)
        name = ask_name()
        cpf = ask_cpf()
        dep = ask_department()
        professores[s] = [name, cpf, dep]
    else:
        print("Nome não encontrado.")


def read_prof():  # Lê um arquivo com informações de professores
    global professores
    archive_name = ask_archive_name()
    archive = open(archive_name, "r", encoding="utf-8")
    professores = []
    for l in archive.readlines():
        name, cpf, department = l.strip().split("#")
        professores.append([name, cpf, department])
    archive.close()


def save_prof():  # Salva um arquivo com as informações de(os) professor(es)
    name_archive = ask_archive_name()
    archive = open(name_archive, "w", encoding="utf-8")
    for e in professores:
        archive.write("%s#%s#%s\n" % (e[0], e[1], e[2]))
    archive.close()


def menu_prof():  # Menu dos professores
    while True:
        try:
            print('''
1 - Criar
2 - Ler
3 - Editar
4 - Apagar
5 - Salvar arquivo
6 - Abrir arquivo

7 - Retornar ao menu principal
''')
            choice = int(input("Escolha uma opção: "))
            if choice == 1:
                new_prof()
            elif choice == 2:
                list_prof()
            elif choice == 3:
                altera_prof()
            elif choice == 4:
                delete_prof()
            elif choice == 5:
                save_prof()
            elif choice == 6:
                read_prof()
            elif choice == 7:
                menuprincipal()
            elif choice != range(1, 8):
                opcaoinvalida()
        except ValueError:
            opcaoinvalida()


# FUNÇÕES TURMAS ##################################

def ask_turma_cod():  # Solicita/Retorna o código da turma
    return input("Informe o código da turma: ")


def ask_period():  # Solicita/Retorna e retorna o período
    return input("Informe o período: ")


def ask_cpf_prof():  # Solicita/Retorna o CPF do professor
    return input("Informe o CPF do(a) professor(a): ")


def ask_cpf_alunos():  # Solicita/Retorna o CPF do aluno (assumindo que uma turma deve ter pelo menos um aluno)
    return input("Informe o CPF do(a) aluno(a): ")


def show_turma_data(turmacod, period, mattercod, cpfprof, cpfstudent):  # Exibe as informações da turma
    print('''
Código da turma: %s 
Período: %s 
Código da disciplina: %s 
Cpf professor: %s 
Quantidade de alunos: %s'''
          % (turmacod, period, mattercod, cpfprof, len(cpfstudent)))


def listar_turmas():  # Lista todas as turmas cadastradas
    a = "-" * 70
    print(a)
    for e in turma:
        show_turma_data(e[0], e[1], e[2], e[3], e[4])
    print(a)


def search_turma(turmacod):  # Busca uma determinada turma
    mname = turmacod.lower()
    for d, c in enumerate(turma):
        if (c[0].lower()) == mname:
            return d
    return None


def new_turma():  # Adiciona uma nova turma
    global turma
    turmacod = ask_turma_cod()
    period = ask_period()
    mattercod = ask_matter_cod()
    cpfp = ask_cpf_prof()
    cpfst = list()
    cpfst.append(ask_cpf_alunos())
    turma.append([turmacod, period, mattercod, cpfp, cpfst])


def delete_turma():  # Exclui uma determinada turma
    global turma
    name = ask_turma_cod()
    m = search_turma(name)
    if m is not None:
        del turma[m]
    else:
        print("Turma não encontrada.")


def modify_turma():  # Possibilita modificar as informações de uma determinada turma
    s = search_turma(ask_turma_cod())
    if s is not None:
        turmacod = turma[s][0]
        period = turma[s][1]
        mattercod = turma[s][2]
        cpfp = turma[s][3]
        cpfst = turma[s][4]
        print("Encontrado.")
        show_turma_data(turmacod, period, mattercod, cpfp, cpfst)
        turmacod = ask_turma_cod()
        period = ask_period()
        mattercod = ask_matter_cod()
        cpfp = ask_cpf_prof()
        cpfst = ask_cpf_alunos()
        turma[s] = [turmacod, period, mattercod, cpfp, cpfst]
    else:
        print("Não encontrado.")


def read_turma():  # Lẽ um arquivo com informações de turmas
    try:
        global turma
        archive_name = ask_archive_name()
        archive = open(archive_name, "r", encoding="utf-8")
        turma = []
        for l in archive.readlines():
            turmacod, period, mattercod, cpfp, cpfst = l.strip().split("#")
            turma.append([turmacod, period, mattercod, cpfp, cpfst])
        archive.close()
        for e in turma:
            if e[4] != "":
                n = e[4].replace("[", "")
                n = n.replace("]", "")
                n = n.replace(" ", "")
                n = n.replace("'", "")
                n = n.split(",")
                e[4] = n

    except FileNotFoundError:
        print("\nArquivo não encontrado!")
    except ValueError:
        print("Erro: Talvez o arquivo que vocẽ está tentando abrir não "
              "esteja no formato ideal para ser lido neste programa.")


def save_turma():  # Salva um arquivo com informações de turmas
    name_archive = ask_archive_name()
    archive = open(name_archive, "w", encoding="utf-8")
    for e in turma:
        archive.write("%s#%s#%s#%s#%s\n" % (e[0], e[1], e[2], e[3], e[4]))
    archive.close()


def listar_alunos():  # Lista todos os alunos de uma determinada turma
    cod = ask_turma_cod()
    for l in turma:
        if cod == l[0]:
            for x in l[4]:
                print(x)

        else:
            print("Turma não encontrada.")


def apagar_alunos():
    cod = ask_turma_cod()
    cpf = ask_cpf_alunos()
    for l in turma:
        if l[0] == cod:
            if cpf in l[4]:
                l[4].remove(cpf)


def menu_turma():  # Menu das turmas
    while True:
        try:
            print('''
    1 - Criar turma   
    2 - listar turmas
    3 - Editar 
    4 - Apagar 
    5 - Salvar arquivo
    6 - Abrir arquivo
    7 - Adicionar aluno(a)    
    8 - Apagar aluno(a)
    9 - Listar alunos por turma
    0 - Retornar ao menu principal


        ''')
            choice = int(input("Escolha uma opção: "))

            if choice == 0:
                menuprincipal()
            elif choice == 1:
                new_turma()
            elif choice == 2:
                listar_turmas()
            elif choice == 3:
                modify_turma()
            elif choice == 4:
                delete_turma()
            elif choice == 5:
                save_turma()
            elif choice == 6:
                read_turma()
            elif choice == 7:
                add_alunos()
            elif choice == 8:
                apagar_alunos()
            elif choice == 9:
                listar_alunos()
            elif choice != range(0, 7):
                opcaoinvalida()

        except ValueError:
            opcaoinvalida()


def add_alunos():  # Adiciona aluno(s) em uma determinada turma
    global turma
    codturma = ask_turma_cod()
    for l in turma:
        if l[0] == codturma:
            l[4].append(ask_cpf_alunos())
        else:
            print("Turma não encontrada.")


# RELATÓRIOS
# Relatórios Professores

def ata_exercicios():  # Gera uma ata de exercício
    global turma
    coddisciplina = ask_matter_cod()
    codturma = ask_turma_cod()

    for l in turma:
        if codturma == l[0] and coddisciplina == l[2]:

            print("\nPeríodo: %s " % l[1])
            print("Código da disciplina: %s" % l[2])
            print("Código da turma: %s" % l[0])
            print("CPF do(s) professore(s): %s" % l[3])
            print("CPF do(s) aluno(s): \n")
            for x in l[4]:
                print(x)


def turmas_prof():  # Menu para escolha da exibição de turmas por professor
    while True:
        try:
            print('''
1 - Listar todas as turmas 
2 - Turmas por semestre
0 - Voltar ao menu anterior

''')
            choice = int(input("Escolha uma opção: "))
            if choice == 1:
                todas_turmas_prof()
            elif choice == 2:
                turmas_semestre_prof()
            elif choice == 0:
                menu_prof()
            elif choice != range(0, 2):
                opcaoinvalida()
        except ValueError:
            opcaoinvalida()


def todas_turmas_prof():  # Exibe todas as turmas de um determinado professor
    cpf = ask_cpf_prof()

    for t in turma:
        if int(t[3]) == int(cpf):
            print("Código da turma: %s" % t[0])
            print("\nPeríodo: %s " % t[1])
            print("Código da disciplina: %s" % t[2])
            print("CPF dx(s) Professorx(s): %s" % t[3])


def turmas_semestre_prof():  # Exibe as turmas de um determinado professor em um determinado semestre
    cpf = ask_cpf_prof()
    sem = ask_period()

    for t in turma:
        if int(t[3]) == int(cpf) and t[1] == sem:
            print("\nPeríodo: %s " % t[1])
            print("Código da disciplina: %s" % t[2])
            print("Código da turma: %s" % t[0])
            print("CPF dx(s) Professorx(s): %s" % t[3])


# Relatórios Alunos

def disc_alunos():
    while True:
        try:
            print('''
1 - Listar todas as turmas 
2 - Turmas por semestre
0 - Voltar ao menu anterior

    ''')
            choice = int(input("Escolha uma opção: "))
            if choice == 1:
                todas_turmas_alu()
            elif choice == 2:
                turmas_semestre_alu()
            elif choice == 0:
                menu_alunos()
            elif choice != range(0, 2):
                opcaoinvalida()
        except ValueError:
            opcaoinvalida()


def todas_turmas_alu():  # Lista todas as turmas de um determinado aluno
    cpf = ask_cpf_alunos()

    for t in turma:
        for x in t[4]:
            if x == cpf:
                print("Código da turma: %s" % t[0])
                print("\nPeríodo: %s " % t[1])
                print("Código da disciplina: %s" % t[2])
                print("CPF dx(s) Professorx(s): %s" % t[3])
                print("CPF Aluno: %s" % x)


def turmas_semestre_alu():  # Lista todas as turmas de um aluno em um determinado semestre
    cpf = ask_cpf_alunos()
    sem = ask_period()

    for t in turma:
        for x in t[4]:
            if x == cpf and t[1] == sem:
                print("\nCódigo da turma: %s" % t[0])
                print("Período: %s " % t[1])
                print("Código da disciplina: %s" % t[2])
                print("CPF dx(s) Professorx(s): %s" % t[3])
                print("CPF Aluno: %s" % x)


def menuprincipal():  # menu principal do programa
    print('''
1 - Professores
2 - disciplinas
3 - Alunos
4 - Turmas
5 - Gerar ata de exercício
6 - Listar turmas por professor(a)
7 - Listar disciplinas por aluno(a)

0 - Sair
        ''')
    while True:
        try:
            choice = int(input("Escolha uma opção: "))
            if choice == 0:
                break
            elif choice == 1:
                menu_prof()
            elif choice == 2:
                menu_disciplinas()
            elif choice == 3:
                menu_alunos()
            elif choice == 4:
                menu_turma()
            elif choice == 5:
                ata_exercicios()
            elif choice == 6:
                list_prof()
            elif choice == 7:
                disc_alunos()

            elif choice != range(0, 7):
                opcaoinvalida()
        except ValueError:
            opcaoinvalida()


menuprincipal()
