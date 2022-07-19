**Example 1: 删除转发规则**



Input: 

```
tccli iotvideo DeleteForwardRule --cli-unfold-argument  \
    --ProductID TDCZ2WD29Z \
    --Skey d \
    --QueueType 1 \
    --QueueName hub_test_topic
```

Output: 
```
{
    "Response": {
        "Result": 0,
        "ErrMsg": "",
        "Endpoint": "100004557990",
        "QueueName": "",
        "ProductID": "TDCZ2WD29Z",
        "RequestId": "0eefd3f4-cb3a-4793-8127-0905c69be0cd"
    }
}
```

