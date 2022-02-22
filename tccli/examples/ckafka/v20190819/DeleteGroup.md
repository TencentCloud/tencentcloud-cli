**Example 1: 删除消费组实例**



Input: 

```
tccli ckafka DeleteGroup --cli-unfold-argument  \
    --InstanceId ckafka-6er88krk \
    --Group test
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "group delete success",
            "Data": null
        },
        "RequestId": "7118b7f95-43de-4d27-8sdadsa-dsadsadsa"
    }
}
```

