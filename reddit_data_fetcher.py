import praw
from confluent_kafka import Producer

# Reddit API credentials
reddit_client_id = "PDkp4oGyNlOnp9iJc4NabQ"
reddit_client_secret = ""
reddit_user_agent = "data-analysis:PDkp4oGyNlOnp9iJc4NabQ:v1.0(by /u/DataSmithJeet)"

# Kafka producer configuration
# since reddit-fetcher and kafka are in the same docker network, we can use the service name as the hostname and internal port
kafka_broker = "kafka:19092"
kafka_topic = "reddit_data_topic"

# Debugging statement to print KAFKA_BROKER
print("KAFKA_BROKER:", kafka_broker)

# Authenticate with Reddit API
reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent=reddit_user_agent)

# Initialize Kafka producer
producer = Producer({'bootstrap.servers': kafka_broker})

# Specify the subreddit to fetch data from
subreddit_name = "wallstreetbets"
subreddit = reddit.subreddit(subreddit_name)

# Fetch the top 10 posts from the subreddit
for submission in subreddit.top(limit=10):
    # Create a dictionary to store the post data
    post_data = {
        "title": submission.title,
        "score": submission.score,
        "id": submission.id,
        "url": submission.url,
        "comms_num": submission.num_comments,
        "created": submission.created
    }


    # convert the post data to a srting
    post_data_str = str(post_data)
    print(post_data_str)

    # Send the post data to Kafka
    producer.produce(kafka_topic, key=submission.id, value=post_data_str)

    print("Sent post with id: {}".format(submission.id))

# Flush the producer
producer.flush()