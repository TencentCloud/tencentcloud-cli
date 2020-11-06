**Example 1: Rewinding consumption position in queue**

This example shows you how to rewind the consumption position in a queue.

Input: 

```
tccli cmq RewindQueue --cli-unfold-argument  \
    --QueueName test \
    --StartConsumeTime 1582108595
```

Output: 
```
{
    "Response": {
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

