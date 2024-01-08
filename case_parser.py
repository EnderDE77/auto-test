def letter_to_bool(letter):
    if letter == 'T':
        return True
    if letter == 'F':
        return False
    return None

def parse_text_dict():
    link = 'case_gen.txt'
    file = open(link,'r')
    text = file.read()
    text = text.split('\n\n')
    clc = {}
    for group in text:
        if group[:2] == '&&': #indicate jerry mashup
            mashup = group.split('\n')
            clc['mashup'] = []
            if len(mashup) > 1:
                for jerry_combo in mashup[1:]:
                    clc['mashup'].append([])
                    jerry_combo = jerry_combo.split('.')
                    jerry_combo_val = jerry_combo[-1]
                    for jerry in jerry_combo[:-1]:
                        jerry = jerry.split('_')
                        clc['mashup'][-1].append(clc[jerry[0]]['jerry'][jerry[1]]) #add jerrys that were added in case_gen
                    clc['mashup'][-1].append([letter_to_bool(jerry_combo_val)])
        else: # indicate regular argument
            arg = group.split('\n')
            header = arg[0].split('_')
            name = header[0]
            clc[name] = {}
            clc[name]['type'] = header[1] #saves type
            clc[name]['jerry'] = {}
            if len(arg) > 1: #indicate if there are jerrys for an argument
                for jerry in arg[1:]:
                    jerry = jerry[1:].split('_')
                    vals = jerry[1].split('.')
                    if len(vals) > 1:
                        for i in range(1,len(vals)): #this works for numbers, and has the side effect of not working on strings (which is used for regex)
                            if vals[i].isdecimal():
                                vals[i] = float(vals[i])
                        clc[name]['jerry'][jerry[0]] = vals
    return clc


if __name__ == '__main__':
    args = parse_text_dict()
    print(args)