import click
import klaws.s3

@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def main(ctx, debug):    
    """ Having fun with AWS and Kaggle """
    #ctx.obj['DEBUG'] = debug
    #greet = 'Howdy' if as_cowboy else 'Hello'
    #click.echo('{0}, {1}.'.format(greet, name))

    
@main.command()
@click.pass_context
def check_s3(ctx):
    click.echo('checking S3')
    print(klaws.s3.buckets())
    #click.echo('Debug is %s' % (ctx.obj['DEBUG'] and 'on' or 'off'))
    
if __name__ == '__main__':
    main(obj={})    