**Example 1: 创建投递SCF任务**



Input: 

```
tccli cls CreateDeliverCloudFunction --cli-unfold-argument  \
    --TopicId xx \
    --FunctionName xx \
    --MaxMsgNum 1 \
    --Namespace xx \
    --Timeout 1 \
    --Qualifier xx
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60xxx-0xxx-4xxx-bxxx-270359fb5xxx"
    }
}
```

