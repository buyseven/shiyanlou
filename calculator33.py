import sys

class ArgError(Exception):
    pass


class Args:
    def __init__(self,args):
        self.args = args
    def __parse_arg(self,arg):
        try:
            value = self.args[self.args.index(arg) + 1]
        except (ValueError,IndexError):
            value = None
        return value
    def get_arg(self,arg):
        value = self.__parse_arg(arg)
        if value is None:
            raise ArgError('not found arg %s' % arg)
        return value


class SheBaoConfig:
    def __init__(self,file):
        self.jishu_low,self.jishu_high,self.total_rate = self.__parse_config(file)

    def __prase_config(self,file):
        rate = 0
        jishu_low = 0
        jishu_high = 0

        with open(file) as f:
            for line in f:
                key, value = line.split('=')
                key = key.strip()
                try:
                    value = float(value.strip())
                except ValueError:
                    continue
                if key == 'jishuL':
                    jishu_low = value
                elif key == 'jishuH':
                    jishu_high = value
                else:
                    rate += value
        return jishu_low,jishu_high,rate


class EmployeeData:
    def __init__(self,file):
        self.data = self.__parse_file(file)

    def __parse_file(self,file):
        data = []
        for line in open(file):
            employee_id,gongzi = line.split(',')
            data.append((int(employee_id),int(gongzi)))
        return data
   
    def __iter__(self):
        return iter(self.data)

class Calculator:
    tax_start = 3500
    tax_table = [
        (80000,0.45,13505),
        (55000,0.35,5505),
        (35000,0.3,2755),
        (9000,0.25,1005),
        (4500,0.2,555),
        (1500,0.1,105),
        (0,0.3,0),
    ]  
    
    def __init__(self,config):
        self.config = config

    def calculate(self,data_item):
        employee_id, gongzi = data_item
        if gongzi < self.config.jishu_low:
            shebao = self.config.jishu_low*self.config.total_rate
        elif gongzi > self.config.jishu_high:
            shebao = self.config.jishu_high*self.config.total_rate
        else:
            shebao = gongzi * self.config.total_rate
        left_gongzi = gongzi - shebao
        tax_gongzi = left_gongzi - self.tax_start
        if tax_gongzi < 0:
            tax = 0
        else:
            for item in self.tax_table:
                if tax_gongzi > item[0]:
                    tax = tax_gong * item[1] - item[2]
                    break
        last_gongzi = left_gongzi - tax
        
        return str(employee_id),str(gongzi),'{:.2f}'.format(shebao),'{:.2f}'.format(tax),'{:.2f}'.format(last_gongzi)


class Exporter:
    def __init__(self,file):
        self.file = file

    def export(self,data):
        content = ''
        for item in data:
            line = ','.join(item) + '\n'
            content += line
        with open(self.file,'w') as f:
            f.write(content)


class Executor:
    def __init__(self,args):
        args = Args(args)
        config = SheBaoConfig(args.get_arg('-c'))
        self.employee_data = EmployeeData(args.get_arg('-d'))
        self.exporter = Exporter(args.get_arg('-o'))
        self.calculator = Calculator(config)

    def execute(self):
        results = []
        for item in self.employee_data:
            result = self.calculator.calculate(item)
            result.append(result)
        self.exporter.export(results)


if __name__ == '__main__':
    executor = Executor(sys.argv[1:])
    executor.execute()     
