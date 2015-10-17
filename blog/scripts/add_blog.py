import argparse
from pyramid.paster import bootstrap


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config")
    args = parser.parse_args()

    env = bootstrap(args.config)
    print(env)
    name = input('name: ')
    title = input('title: ')
    description = input('description: ')
    env["root"].add_blog(name=name, title=title, description=description)
    import transaction
    transaction.commit()

if __name__ == '__main__':
    main()
