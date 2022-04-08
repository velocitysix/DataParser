

import pandas as pd
#from xlsxwriter import Workbook
Answer=input("Are you working with an existing spreadhseet or do you need one to be created? (Answer 'old' for existing and 'new' if you need one created: ")

if Answer.lower()=='old':
    netpins = []
    filename = input("enter file path of html file: ")
    excelfile = input("enter filepath of excel file: ")
    tables = pd.read_html(filename)
    sp500_table = tables[0]
    df = pd.DataFrame(sp500_table)
    datalist = df.values.tolist()
    res1 = [i[0] for i in datalist]
    res1.pop(0)
    # print(res1)
    df2 = pd.read_excel(excelfile, sheet_name='Net_Groups')

    netE = df2.values.tolist()
    flat_list = [item for sublist in netE for item in sublist]
    flat_list = [flat_list for flat_list in flat_list if str(flat_list) != 'nan']
    del flat_list[0:18]
    # print(flat_list)
    notfound = []
    new = []
    for string in flat_list:
        if string not in res1:
            notfound.append(string)

    xx = list(set(flat_list).symmetric_difference(res1))
    print(xx)

    for string in res1:
        if string not in flat_list:
            new.append(string)
    # print(matches)
    # print(notfound)

    df3 = pd.DataFrame(list(zip(notfound, new)), columns=["No Longer In Logic", "New Nets"])
    print(df3)
    writer = pd.ExcelWriter('analysisoutputMARCH30.xlsx')
    df3.to_excel(writer)
    writer.save()
else:
        unpopulated = input("Enter filepath of unpopulated SI Workbook: ")
        filename = input("enter file path of html file: ")
        tables = pd.read_html(filename)
        sp500_table = tables[0]
        df = pd.DataFrame(sp500_table)
        datalist = df.values.tolist()
        res1 = [i[0] for i in datalist]
        res1.pop(0)
        GIN = []
        CLK_DIFF = []
        I2C = []
        JTAG = []
        SPI = []
        UART = []
        CFAM_GPIO = []
        PUPD = []
        PCIe_CDFP = []
        PCIe_North = []
        PCIe_South = []
        PCIe_AP = []
        PWR = []
        PLL = []
        DC = []
        NOTCRIT = []
        IMP = []
        for string in res1:
            fullstring= string
            substring = "GIN"
            substring2= "CLK"
            substring3= "I2C"
            substring4= "JTAG"
            substring5= "SPI"
            substring6= "UART"
            substring7= "TO_SW"
            substring8 = "PD"
            substring9 = "PU"
            substring10 = "PC_HUB_RTMR"
            substring11 = "PC_RTMR_HUB"
            substring12 = "PC_IO"
            substring13 = "PC_RTMR_SW_JI"
            substring14 = "PC_RTMR_SW_JO"
            substring15 = "PC_SW"
            substring16 = "PC_SW1"
            substring17 = "PC_XCO"
            substring18 = "PWR"
            substring19 = "GND"
            substring20 = "+"
            substring21 = "PCIE_PLL"
            substring22 = "EFUSE"
            substring23 = "SSB"
            substring24 = "NC"
            substring25 = "DIFF_PAIR"



            if fullstring.find(substring) != -1:
                GIN.append(string)
            if fullstring.find(substring2) != -1:
                CLK_DIFF.append(string)
            if fullstring.find(substring3) != -1:
                I2C.append(string)
            if fullstring.find(substring4) != -1:
                JTAG.append(string)
            if fullstring.find(substring5) != -1:
                SPI.append(string)
            if fullstring.find(substring6) != -1:
                UART.append(string)
            if fullstring.find(substring7) != -1:
                CFAM_GPIO.append(string)
            if fullstring.find(substring8) != -1:
                PUPD.append(string)
            if fullstring.find(substring9) != -1:
                PUPD.append(string)
            if fullstring.find(substring10) != -1:
                PCIe_CDFP.append(string)
            if fullstring.find(substring11) != -1:
                PCIe_CDFP.append(string)
            if fullstring.find(substring12) != -1:
                PCIe_North.append(string)
            if fullstring.find(substring13) != -1:
                PCIe_South.append(string)
            if fullstring.find(substring14) != -1:
                PCIe_South.append(string)
            if fullstring.find(substring15) != -1:
                PCIe_AP.append(string)
            if fullstring.find(substring16) != -1:
                PCIe_AP.append(string)
            if fullstring.find(substring17) != -1:
                PCIe_AP.append(string)
            if fullstring.find(substring18) != -1:
                PWR.append(string)
            if fullstring.find(substring19) != -1:
                PWR.append(string)
            if fullstring.find(substring20) != -1:
                PWR.append(string)
            if fullstring.find(substring21) != -1:
                PLL.append(string)
            if fullstring.find(substring22) != -1:
                DC.append(string)
            if fullstring.find(substring23) != -1:
                DC.append(string)
            if fullstring.find(substring24) != -1:
                NOTCRIT.append(string)
            if fullstring.find(substring25) != -1:
                IMP.append(string)

        df2 = pd.read_excel(unpopulated, sheet_name='Net_Groups')
        df2.insert()




        print(res1)
        print(GIN)
        print(CLK_DIFF)
        print(I2C)
        print(JTAG)
        print(SPI)
        print(UART)
        print(CFAM_GPIO)
        print(PUPD)
        print(PCIe_CDFP)
        print(PCIe_North)
        print(PCIe_South)
        print(PCIe_AP)
        print(PWR)
        print(PLL)
        print(DC)
        print(NOTCRIT)
        print(IMP)


    # print(flat_list)







