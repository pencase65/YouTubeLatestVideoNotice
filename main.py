import argparse
import acquire


def get_args():
    psr = argparse.ArgumentParser()
    psr.add_argument('-i', '--channel_id', help='Enter your YouTube channel ID')

    return psr.parse_args()


if __name__ == "__main__":
    args = get_args()
    url = acquire.acquire(args.channel_id)
    print(args.channel_id)
    print(url)