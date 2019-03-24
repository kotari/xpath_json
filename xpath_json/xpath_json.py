import json
import operator


ops = {
    '<': operator.lt,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
    '>=': operator.ge,
    '>': operator.gt
}


exp_check = ['==', '!=', '<=', '>=', '<', '>']

def __compare__(arg1, operation, arg2):
    op = ops.get(operation)
    return op(arg1, arg2)


def __cast__(to, from_):
    value = None
    if (isinstance(to, int)):
        value = int(from_)
    elif (isinstance(to, float)):
        value = float(from_)
    elif (isinstance(to, bool)):
        value = bool(from_)
    else:
        value = from_
    return value

def __evaluate_expression__(token, value):
    for idx, exp in enumerate(exp_check):
        if (token.find(exp) > -1):
            if ((token.find('[') < token.find(exp)) and (token.find(']') > token.find(exp)) and (token.find(']') == len(token)-1)):
                key = token[token.find('[')+1:token.find(exp)].strip()
                found = extract(key, value, par_elem=True)
                if isinstance(found, type(None)):
                    break
                if (idx > 3):                    
                    value = token[token.find(exp)+1: len(token)-1].strip()
                else:
                    value = token[token.find(exp)+2: len(token)-1].strip()
                if (isinstance(found, list)):
                    filter = []
                    for elem in found:
                        e = elem.get(key, None)
                        if (__compare__(e, exp, __cast__(e, value))):
                            filter.append(elem)
                    return filter
                else:
                    e = found.get(key, None)                       
                    if (__compare__(e, exp, __cast__(e, value))):
                        return found
                return None
    return None


def __expression_found__(token, value):
    for exp in exp_check:
        if (token.find(exp) > -1):
            if ((token.find('[') < token.find(exp)) and (token.find(']') > token.find(exp)) and (token.find(']') == len(token)-1)):
                return True
    return False

def extract(exp, payload, par_elem=False):
    tokens = exp.split('/')
    value = payload
    for idx, token in enumerate(tokens):
        if value == None:
            return value
        elif (token.isdigit()): # This is only for a list
            if (isinstance(value, list) and (int(token) < len(value))):
                value = value[int(token)]
            else:
                return None
        elif (token == '#' and idx+1 == len(tokens)):
            return len(value)
        elif (token == '#'):
            pass
        elif (__expression_found__(token, value)):
            value = __evaluate_expression__(token, value)
        elif (isinstance(value, list)): 
            a = []
            for elem in value:
                if (isinstance(elem, dict)):
                    if (par_elem):
                        a.append(elem)
                    else:
                        a.append(elem.get(token, None))
                else:
                    return None
            value = a
        elif (isinstance(value, dict)):
            if (par_elem == False):
                value = value.get(token, None)
            else:
                if (value.get(token, None) is None):
                    return None
        else:
            return None
    return value

