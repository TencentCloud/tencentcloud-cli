**Example 1: Modifying queue attributes**

This example shows you how to modify queue attributes.

Input: 

```
tccli cmq ModifyQueueAttribute --cli-unfold-argument  \
    --QueueName test \
    --MaxMsgSize 1024
```

Output: 
```
{
    "Response": {
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

