**Example 1: Clearing heaped messages in queue**

This example shows you how to clear heaped messages in a queue.

Input: 

```
tccli cmq ClearQueue --cli-unfold-argument  \
    --QueueName test
```

Output: 
```
{
    "Response": {
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

