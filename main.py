import acquire
import args
import WebhookExecution
import WebhookSetting

if __name__ == "__main__":
    args = args.get_args()
    # コマンドライン引数で-wもしくは--webhooksettingがある場合はWebhookURLの設定をして終了
    if 'None' not in args.webhook_setting:
        WebhookSetting.webhooksetting(args.webhook_setting)
        quit(0)
    url = acquire.acquire(args.channel_id)
    print(args.channel_id)
    print(url)
    WebhookExecution.webhookrun(str(args.channel_id))


