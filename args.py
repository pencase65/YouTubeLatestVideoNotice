import argparse


def get_args():
    psr = argparse.ArgumentParser()
    psr.add_argument('-i', '--channel_id', help='Enter your YouTube channel ID')

    return psr.parse_args()
