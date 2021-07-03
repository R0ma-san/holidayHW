import psycopg2
import config as c

conn = psycopg2.connect(dbname=c.dbname, user=c.user, password=c.password)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS passengers")
cur.execute("""CREATE TABLE IF NOT EXISTS passengers (
    id integer,
    survived integer,
    class integer,
    name text,
    sex varchar(50),
    age varchar(50),
    sibsp integer,
    parch integer,
    ticket varchar(255),
    fare numeric NULL,
    cabin varchar(255) NULL,
    embarked varchar(50)
)
""")

with open(r'titanic.txt', 'r') as f:
    next(f)
    cur.copy_from(f, 'passengers', sep='|')

conn.commit()

# начало вашего кода

def dead():
    cur.execute("SELECT name FROM passengers WHERE survived = 0")
    print(cur.fetchall())

def amount_of_passengers():
    cur.execute("SELECT MAX(id) FROM passengers")
    for i in cur:
        for j in i:
            return j
            

def firstclass_women():
    cur.execute("SELECT COUNT(*) FROM passengers WHERE sex='female' AND class = 1 AND survived = 1")
    a = cur.fetchone()
    for i in a:
        survived_women = i
        
    persent = survived_women/amount_of_passengers() * 100
    print(f'{persent}%')

def thirdclass_men_less_20():
    cur.execute("SELECT COUNT(*) FROM passengers WHERE (sex='male' AND class = 3 AND age < '20')")
    a = cur.fetchone()
    for i in a:
        survived_men = i
        
    persent = survived_men/amount_of_passengers() * 100
    print(f'{persent}%')

def  secondclass_passenders_more_30():
    cur.execute("SELECT COUNT(*) FROM passengers WHERE (class = 2 AND age > '30')")
    a = cur.fetchone()
    for i in a:
        survived_secondclass_passenders = i
        
    persent = survived_secondclass_passenders/amount_of_passengers() * 100
    print(f'{persent}%')

def secondclass_women_in_Cherbourg():
    cur.execute("SELECT COUNT(*) FROM passengers WHERE (sex='female' AND class = 2 AND embarked = 'C')")
    a = cur.fetchone()
    for i in a:
        survived_secondclass_women = i
        
    persent = survived_secondclass_women/amount_of_passengers() * 100
    print(f'{persent}%')

def passengers_with_siblings():
    cur.execute("SELECT COUNT(*) FROM passengers WHERE sibsp > 1")
    a = cur.fetchone()
    for i in a:
        survived_secondclass_women = i
        
    persent = survived_secondclass_women/amount_of_passengers() * 100
    print(f'{persent}%')

def port():
    cur.execute("SELECT COUNT(*) FROM passengers WHERE (survived = 0 AND embarked = 'C')")
    c = cur.fetchone()
    for i in c:
        Cherbourg = i/amount_of_passengers() * 100

    cur.execute("SELECT COUNT(*) FROM passengers WHERE (survived = 0 AND embarked = 'Q')")
    q = cur.fetchone()
    for i in q:
        Queenstown = i/amount_of_passengers() * 100

    cur.execute("SELECT COUNT(*) FROM passengers WHERE (survived = 0 AND embarked = 'S')")
    s = cur.fetchone()
    for i in s:
        Southampton = i/amount_of_passengers() * 100
        
    if  Cherbourg>Queenstown and Cherbourg>Southampton:
        print('Cherbourg', Cherbourg)
    if  Queenstown>Cherbourg and Queenstown>Southampton:
        print('Queenstown', Queenstown)
    if  Southampton>Cherbourg and Queenstown<Southampton:
        print('Southampton', Southampton)
  
# def find_person():
#     cur.execute("SELECT * FROM passengers WHERE name LIKE '%Brown%' and sex = 'female'")
#     a = cur.fetchall()
#     print(a)

dead()
firstclass_women()
passengers_with_siblings()
secondclass_passenders_more_30()
secondclass_women_in_Cherbourg()
thirdclass_men_less_20()
port()
# find_person()


cur.close()
conn.close()
