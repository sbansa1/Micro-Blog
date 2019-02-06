from app import app
import os
import click


@app.cli.group()
def translate():
    """Translation and localization commands."""
    pass

@translate.command()
def update():
    """Update all languages."""
    if os.system("pybabel extract -F babel.cfg -k _l -o messages.pot . "): # returns 0 means command execute successfully
        raise (RuntimeError("Extract Command Failed"))

    if os.system('pybabel update -i messages.pot -d app/translations'):
        raise (RuntimeError("Update Command Failed"))

    os.remove('messages.pot')

@translate.command()
def compile():
    """Compiles All Language Translations"""
    if os.system('pybabel compile -d app/translations'):
        raise (RuntimeError("Compile Command Not Working"))

@translate.command()
@click.argument("lang")
def initLanguage(lang):
    """Function to initialize the language you want yours translation in"""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot . '):
        raise (RuntimeError("Extract Command Failed"))
    if(os.system('pybabel init -i messages.pot -d app/translations -l' + lang)):
        raise (RuntimeError("Init Command Failed"))
    os.remove('messages.pot')