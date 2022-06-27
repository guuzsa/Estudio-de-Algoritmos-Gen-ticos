
def sort(array,index):

    less = []
    equal = []
    greater = []
    
    index_less = []
    index_equal = []
    index_greater = []

    if len(array) > 1:
        pivot = array[0]
        for i in range(len(array)):
            if array[i] < pivot:
                less.append(array[i])
                index_less.append(index[i])
            elif array[i] == pivot:
                equal.append(array[i])
                index_equal.append(index[i])
            elif array[i] > pivot:
                greater.append(array[i])
                index_greater.append(index[i])
        [less,index_less] = sort(less,index_less)
        [greater,index_greater] = sort(greater,index_greater)
        return [less+equal+greater, index_less+index_equal+index_greater]
    else:  
        return [array,index]
    


def reordenar(v,i):
    v_aux = [];
    l = len(v);
    for j in range(l):
        v_aux.append(v[i[j]]);
    return v_aux;


def empaquetar_array(v,n):
    l = len(v);
    v_aux = [];
    for i in range(0,l,n):
        pack = [];
        j = 0;
        while j < n and i+j < l:
            pack.append(v[i+j]);
            j += 1;
        if len(pack) == n:
            v_aux.append(pack);
    return v_aux;





