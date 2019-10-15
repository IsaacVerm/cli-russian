import click


@click.command()
@click.argument('russian')
@click.argument('root')
@click.argument('english')
@click.argument('case')
@click.argument('gender')
@click.argument('number')
def annotate_noun(russian, root, english, case, gender, number):
    click.echo('Russian noun is %s' % russian)
    click.echo('Based on root noun %s' % root)
    click.echo('English translation of this noun is %s' % english)
    click.echo('Case is %s' % case)
    click.echo('Gender is %s' % gender)
    click.echo('Number is %s' % number)


if __name__ == '__main__':
    annotate_noun()
