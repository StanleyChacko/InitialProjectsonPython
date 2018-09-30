def funcomp():
    a=raw_input("Server_Name:")
    b=raw_input("DB_Name:")
    c=raw_input("Username:")
    d=raw_input("Password:")
    #print 'Server_Name=\t%s;DB_Name=\t%s;Username=\t%s;' %(a)%(b)
    print '\"Server_Name=',a,';DB_Name=',b,';Username=',c,';Password=',d,'\"\n'
    return a,b,c,d



#to give personal computer details

compdetails=funcomp()
print '\"Server_Name=',compdetails[0],';DB_Name=',compdetails[1],';Username=',compdetails[2],';Password=',compdetails[3],'\"\n'
