**Example 1: Unbinding dead letter queue**

This example shows you how to unbind a dead letter queue.

Input: 

```
tccli cmq UnbindDeadLetter --cli-unfold-argument  \
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

