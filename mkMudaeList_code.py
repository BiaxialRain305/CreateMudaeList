# Activate the virtual environment
import pyperclip


def main():
    inp = pyperclip.paste().splitlines()
    temp2 = ''
    for i in inp:
        if not i or 'Page ' and ' / ' in i or 'Total value: ' in i or ':kakera:\r' in i or '\u200b' in i \
                or 'Top 15 value: ' in i or 'AVG: ' in i or '🏆 TOP ' in i and ' TOP 1000' in i \
                or ' $wa, ' in i and ' $ha, ' in i and ' $wg, ' in i and ' $hg' in i and '(' not in i and ')' not in i \
                or ' wishlist (' in i and ')' in i:
            inp = inp[+1:]
            continue

        elif i[0] == '$':
            inp = pyperclip.paste()
            return inp

        temp = i

        if temp[0] == '#':
            temp = i.split(' - ')[1]

        temp = \
            temp.split(' · ')[0].replace('💞', '').replace('✅', '').replace('⭐', '').replace('🔐', '').replace(
                '❌', '').replace('🚫', '').replace(':kakera:', '').strip().split('  ')[0].split(' 🚫 ')[0].split(
                '(Soulkeys: ')[0].split(
                ' - Touhou')[0].split(' | ')[0].split(' => ')[0].split(' ⚠')[0]

        if temp[len(temp) - 3:] == ' ka' or ' (' in i and ')' in i or ' - Touhou' in i:
            if temp.count(' - ') > 1:
                temp = temp.split(' - ')[0] + ' - ' + temp.split(' - ')[1]
            else:
                temp = temp.split(' - ')[0]

        if temp[len(temp) - 3:] == ' ka':
            remove_num = temp[:len(temp) - 3]
            while remove_num[len(remove_num) - 1].isnumeric():
                remove_num = remove_num[:-1]

            temp = remove_num

        # DL Making Below and t flag without rank
        remove_dl = temp
        if remove_dl[len(remove_dl) - 1] == ')':
            remove_dl = remove_dl[:-1]
            while remove_dl[len(remove_dl) - 1].isnumeric() or remove_dl[len(remove_dl) - 1] == '(':
                remove_dl = remove_dl[:-1]

                if not remove_dl[len(remove_dl) - 1].isnumeric() or remove_dl[len(remove_dl) - 1] != '(':
                    break

            if remove_dl[len(remove_dl) - 3:] == '$hg':
                remove_dl = remove_dl.split(' ~ ')[0]

            while remove_dl[len(remove_dl) - 1].isnumeric() or remove_dl[len(remove_dl) - 1] == '(' and remove_dl[
                len(remove_dl) - 2] == ' ':
                remove_dl = remove_dl[:-1]
                temp = remove_dl

        # DL Making Above ^

        if inp[0] == i:
            temp2 = temp2 + temp  # + "\n"
        else:
            temp2 = temp2 + "$" + temp  # + "\n"
    # temp2.replace('\n', '')
    out = temp2
    print(out)
    return pyperclip.copy(out)


if __name__ == '__main__':
    main()
