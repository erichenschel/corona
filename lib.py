import random

tt = """Ala / A GCU, GCC, GCA, GCG
Ile / I AUU, AUC, AUA
Arg / R CGU, CGC, CGA, CGG; AGA, AGG
Leu / L CUU, CUC, CUA, CUG; UUA, UUG
Asn / N AAU, AAC
Lys / K AAA, AAG
Asp / D GAU, GAC
Met / M AUG
Phe / F UUU, UUC
Cys / C UGU, UGC
Pro / P CCU, CCC, CCA, CCG
Gln / Q CAA, CAG
Ser / S UCU, UCC, UCA, UCG; AGU, AGC
Glu / E GAA, GAG
Thr / T ACU, ACC, ACA, ACG
Trp / W UGG
Gly / G GGU, GGC, GGA, GGG
Tyr / Y UAU, UAC
His / H CAU, CAC
Val / V GUU, GUC, GUA, GUG
STOP    UAA, UGA, UAG
""".strip()
dec = {}
for t in tt.split("\n"):
  k = t[:len("Val / V")].strip()
  v = t[len("Val / V "):]
  if '/' in k:
    k = k.split("/")[-1].strip()
  k = k.replace("STOP", "*")
  v = v.replace(",", "").replace(";", "").lower().replace("u", "t").split(" ")
  for vv in v:
    if vv in dec:
      print("dup", vv)
    dec[vv.strip()] = k

def translate(x, protein=False):
    pass
