import click
import csv


@click.command()
@click.option('--russian', prompt='Give the original Russian noun', help='the declined form of the noun')
@click.option('--root', prompt='Give the root', help='nominative singular form of the noun')
@click.option('--english', prompt='Give the English translation of the noun', help='English translation of the noun')
@click.option('--case', type=click.Choice(['nom', 'gen', 'dat', 'acc', 'ins', 'pre']), prompt='Specify the case of the noun', help="case can be either nom(iniative), gen(initive), dat(ive), acc(usative), ins(trumental) or pre(positional) ")
@click.option('--gender', type=click.Choice(['m', 'f', 'n']), prompt='Specify the gender of the noun', help="gender can be either m(asculine), f(eminine) or n(euter)")
@click.option('--number', type=click.Choice(['sg', 'pl']), prompt="Specify the number of the noun", help="number can be either sg (singular) or pl (plural)")
def annotate_noun(russian, root, english, case, gender, number):
    """Adds annotation for the Russian noun."""
    click.echo('Russian noun is %s' % russian)
    click.echo('Based on root noun %s' % root)
    click.echo('English translation of this noun is %s' % english)
    click.echo('Case is %s' % case)
    click.echo('Gender is %s' % gender)
    click.echo('Number is %s' % number)

    with open('nouns.tsv', 'a') as out:
        # tsvs use tabs as separators
        tsv_writer = csv.writer(out, delimiter='\t')

        # write noun as row
        tsv_writer.writerow([russian, root, english, case, gender, number])
