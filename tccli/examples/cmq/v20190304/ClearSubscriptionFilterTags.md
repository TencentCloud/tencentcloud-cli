**Example 1: Clearing the message tags of subscriber**



Input: 

```
tccli cmq ClearSubscriptionFilterTags --cli-unfold-argument  \
    --TopicName ConnTopic \
    --SubscriptionName Queue
```

Output: 
```
{
    "Response": {
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

