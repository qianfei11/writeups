#!/usr/bin/env python
from pwn import *
import gmpy2
import libnum

context.log_level = 'debug'

#r = remote('138.68.67.161', 60005)

def getKeys():
    r.recvuntil('> ')
    r.sendline('k')
    r.recvline()
    r.recvline()
    r.recvline()
    data = r.recvline().split(', ')
    e = int(data[0][2:])
    n = int(data[1][:-1])
    d = int(data[2][1:])
    keys = (e, n, d)
    info(keys)
    return keys

#keys = []
#for i in range(3):
#    keys.append(getKeys())
#print keys
#r.interactive()

keys = [
    (65537, 69708697251779917631675520185136074492292403162222284420001529450041612742786988755354405899677313388243531818979419755273380311281265661544386895006956548641840229719108303702727370393386697903559884830553453875454007619469593142422173980284832699446666480212048921915140476170476129315048209052907031867357L, 21933610724155113622576268394001724096396869640175560782837962353926912986084356853749228741890014486152400470561280113119190310800478801390158264216220617682210533790235387669897447265772640728610106572535091425677910204099793031270190982924653023135264570394751074259772567046553123170998660604230490571821L),
    (65537, 111492316189772978769435074695527007629601414132274650485577122002114962750113611176981179835433961958221262103826726924905611079266634314310076665219908262625747128966221434071575141301710466347637564970772278718302154391574059326896801724433852872326315168125231177155004877887187610177288922077862111925857L, 41302019507382217351486103170087197937523278946295435623980978195024902965458569238060165769636476012354788918575846869445632631680353813613989674202495266528185291434527700831037064715517768737745171558646613784821257634996082893634332329909434752357966328350439550309668246807206445537841208911078407163393L),
    (65537, 69380641198253738543788276822761354312243496718485455639731885565104340377399827224343687176959977740661647668885797368555621626191040382421764361061813179137555998812352790934435994074139234074925475324706453096114463615359291003847277272722603451036503142566248183741196223940955743643034122922717272662941L, 11527622594988860628397859931383010926743968075554085882189305307206939017188866116024206321160828198087563993873650724723471686033755568979211622863452454542219927090942483655888523302929906460789278761064213361742531808963902022155164315053430898104856665840601188702919576270895601518142007261291649555197L)
]

def find_prime_factors(n, e, d):
    k = e * d - 1
    s = 0
    t = k
    while t % 2 == 0:
        t = t / 2
        s += 1
    i = s
    a = 2
    while True:
        b = gmpy2.powmod(a, t, n)
        if b == 1:
            a = nextprime(a)
            continue
        while i != 1:
            c = gmpy2.powmod(b, 2, n)
            if c == 1:
                break
            else:
                b = c
                i -= 1
        if b == n - 1:
            a = nextprime(a)
            continue
        p = gmpy2.gcd(b - 1, n)
        q = n / p
        return p, q

for k in keys:
    e = k[0]
    n = k[1]
    d = k[2]
    if d > 0:
        p, q = find_prime_factors(n, e, d)
        if p == 1 or q == 1:
            print '[!] Broken'
        else:
            print '[*] Prime pair found'
            print 'p =', p
            print 'q =', q

e = 65537
n = 2318553827267041599931064141028026591078453523755133761420994537426231546233197332557815088229590256567177621743082082713100922775483908922217521567861530205737139513575691852244362271068595653732088709994411183164926098663772268120044065766077197167667585331637038825079142327613226776540743407081106744519
c = 2255296633936604604490193777189642999170921517383872458719910324954614900683697288325565056935796303372973284169167013060432104141786712034296127844869460366430567132977266285093487512605926172985342614713659881511775812329365735530831957367531121557358020217773884517112603921006673150910870383826703797655

p = 12117717634661447128647943483912040772241097914126380240028878917605920543320951000813217299678214801720664141663955381289172887935222185768875580129870000
while True:
    p -= 1
    if n % p == 0:
        print p
        break

q = n / p
assert p * q == n
phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)
m = gmpy2.powmod(c, d, n)
flag = libnum.n2s(m)
print flag

