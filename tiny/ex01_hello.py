import argparse

def get_args():
    # description : 설명cd
    parser = argparse.ArgumentParser(description='Say hello')

    # 명령행 인수 : -n, --name
    parser.add_argument('-n',
                        '--name',
                        metavar='name',
                        default='World',
                        help='Name to great')
    return parser.parse_args()


def main():
    args = get_args()
    print('Hello, ' + args.name + "!")

if __name__=="__main__":
    main()