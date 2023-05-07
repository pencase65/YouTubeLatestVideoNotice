import argparse


def get_args():
    psr = argparse.ArgumentParser()
    psr.add_argument('-i', '--channel_id', help='Enter your YouTube channel ID')
    psr.add_argument('-w', '--webhook_setting', help='Enter your Webhook URL', default='None')

    return psr.parse_args()
