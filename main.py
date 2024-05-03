from argentina import Argentina
from brasil import Brasil


obj_arg = Argentina();
obj_bra = Brasil();

for pais in (obj_arg, obj_bra):
    pais.capital();
    pais.lingua_oficial();