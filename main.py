import acquire
import args
import WebhookExecution

if __name__ == "__main__":
    args = args.get_args()
    url = acquire.acquire(args.channel_id)
    print(args.channel_id)
    print(url)
    WebhookExecution.webhookrun(str(args.channel_id))


