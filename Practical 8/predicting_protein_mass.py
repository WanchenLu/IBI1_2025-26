def mass(protein):
    table = {"G":57.02,"A":71.04,"S":87.03,"P":97.05,"V":99.07,"T":101.05,"C":103.01,"I":113.08,"L":113.08,"N":114.04,"D":115.03,"Q":128.06,"K":128.09,"E":129.04,"M":131.04,"H":137.06,"F":147.07,"R":156.10,"Y":163.06,"W":186.08}
    total = 0
    for aa in protein:   
        if aa not in table:
            raise ValueError("supplied amino acid has no recorded mass")
        total += table[aa]
    return total
protein = "GASPV"
print (mass(protein))