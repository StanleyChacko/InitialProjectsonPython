def funcomp():
    a=raw_input("Server_Name:")
    b=raw_input("DB_Name:")
    c=raw_input("Username:")
    d=raw_input("Password:")
    #print 'Server_Name=\t%s;DB_Name=\t%s;Username=\t%s;' %(a)%(b)
    kk="server=%s;dbname=%s;user=%s;passwd=%s" %(a,b,c,d)
    print "kk:",kk
    print '\"Server_Name=',a,';DB_Name=',b,';Username=',c,';Password=',d,'\"\n'
    return kk

def funstringDict(xx):
    rry=dict(x.split('=') for x in kk.split(';'))
    print "Dictionary inside", rry
    return rry

kk=funcomp()
print "String:",kk

rry1=funstringDict(kk)
print "Dictionary outside:",rry1
