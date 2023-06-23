import argparse
import os
import sys

def get_args():
    # 명령 인자 추가
    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip() # 오른쪽 공백 제거

    return args
def main():
    args = get_args()

    # print(args.text)
    # 명령인수가 -o 이면 문자열 쓰고, 아니면 문자열 입력
    # sys 모듈 - stdout (모니터 콘솔에 출력), stdin(모니터 콘솔에 입력)
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write(args.text.upper() + '\n')
    out_fh.close()


if __name__=="__main__":
    main()