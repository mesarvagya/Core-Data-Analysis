import numpy as np
def histogram_using_numpy(filename, bins=10):
    datas =  np.loadtxt(filename, delimiter="\t", usecols=(0,))
    hist, bin_edges = np.histogram(datas, bins)
    return hist, bin_edges


def histogram_using_list(filename, bins=10, take_col=0):
    f = open(filename,"r")
    data = []
    for item in f.readlines():
        data.append(float(item.split()[take_col]))
    f.close()
    mi,ma = min(data), max(data)

    def get_count(binmin,binmax,inclusive_endpoint=False):
        count = 0
        for item in data:
            if item >= binmin and item < binmax:
                count += 1
            elif inclusive_endpoint and item == binmax:
                count += 1
        return count

    bin_edges = np.linspace(mi, ma, bins+1)

    tot = []
    binlims = zip(bin_edges[0:-1], bin_edges[1:])
    for i,(binmin,binmax) in enumerate(binlims):
        inclusive = (i == (len(binlims) - 1))
        tot.append(get_count(binmin, binmax, inclusive))

    return tot, bin_edges

nump_hist, nump_bin_edges = histogram_using_numpy("data.txt", bins=7)
func_hist, func_bin_edges = histogram_using_list("data.txt", bins=7)

print "Histogram:"
print "  From numpy:      %s" % list(nump_hist)
print "  From my function %s" % list(func_hist)
