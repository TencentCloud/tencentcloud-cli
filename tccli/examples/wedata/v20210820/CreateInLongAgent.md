**Example 1: 注册采集器**



Input: 

```
tccli wedata CreateInLongAgent --cli-unfold-argument  \
    --ExecutorGroupId xx \
    --AgentType 1 \
    --ClusterId xx \
    --ProjectId xx \
    --AgentName xx \
    --TkeRegion ap-beijing
```

Output: 
```
{
    "Response": {
        "AgentId": "xx",
        "RequestId": "xx"
    }
}
```

