**Example 1: PushMmsContent**



Input: 

```
tccli zj PushMmsContent --cli-unfold-argument  \
    --License KA3431QZPU \
    --InstanceId 1138 \
    --Session bbb \
    --Tel 123456
```

Output: 
```
{
    "Response": {
        "Data": {
            "ReturnCode": 0,
            "ReturnMsg": "submitted",
            "MessageId": 15923841632
        },
        "RequestId": "111111"
    }
}
```

