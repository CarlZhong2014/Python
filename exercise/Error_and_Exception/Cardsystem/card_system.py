def saft_float(obj):
        'safe version of float()'
        try:
            retval = float(obj)
        except (TypeError, ValueError), diag:
            retval = str(diag)
        return retval

def main():
    " handles all the data processing "
    log = open(r'F:\Program\Python\exercise\Error_and_Exception\Cardsystem\cardlog.txt', 'w')
    try:
        cdfile = open(r"F:\Program\Python\exercise\Error_and_Exception\Cardsystem\Carddata.txt", 'r')
    except IOError, Erdetaill:
        log.write("no txns this month --- %s \n" % Erdetaill)
        log.close()
        return

    txns = cdfile.readlines()
    cdfile.close()
    total = 0.00
    log.write('accoutn log:\n')

    for eachTxn in txns:
        result = saft_float(eachTxn)
        if isinstance(result, float):
            total += result
            log.write('data...processed\n')
        else:
            log.write('ignored: %s' % result)
    print '$%.2f (new balance)' % (total)

    log.close()

if __name__ == '__main__':
    main()