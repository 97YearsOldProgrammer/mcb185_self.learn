import toolbox

print(toolbox.transcribe('ACGT'))
print(toolbox.revcomp('CCCCAGT'))
print(toolbox.translate('ATGTAA'))

s = 'ACGTGGGGGGCATATG'
print(toolbox.gc_comp(s))
print(toolbox.gc_skew(s), toolbox.gc_skew(toolbox.revcomp(s)))