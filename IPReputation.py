register_module_line('IPReputation', 'start', __line__())




def ip_reputation():
    results = demisto.executeCommand('ip', {'ip': demisto.get(demisto.args(), 'ip')})

    for item in results:
        if isError(item):
            item['Contents'] = item['Brand'] + ' returned an error.\n' + str(item['Contents'])

    demisto.results(results)


def main():
    ip_reputation()


if __name__ in ('__main__', '__builtin__', 'builtins'):  # pragma: no cover
    main()

register_module_line('IPReputation', 'end', __line__())
