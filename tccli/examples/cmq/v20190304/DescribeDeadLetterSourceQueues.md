**Example 1: Enumerating the source queues of dead letter queue**

This example shows you how to enumerate the source queues of a dead letter queue.

Input: 

```
tccli cmq DescribeDeadLetterSourceQueues --cli-unfold-argument  \
    --DeadLetterQueueName test123
```

Output: 
```
{
    "Response": {
        "QueueSet": [
            {
                "QueueName": "test",
                "QueueId": "queue-kc7m75to"
            }
        ],
        "TotalCount": 1,
        "RequestId": "83fce81a-7305-49b4-a154-983dd76204da"
    }
}
```

