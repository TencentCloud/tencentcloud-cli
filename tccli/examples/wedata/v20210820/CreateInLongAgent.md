**Example 1: 注册采集器**



Input: 

```
tccli wedata CreateInLongAgent --cli-unfold-argument  \
    --ExecutorGroupId abc \
    --AgentType 1 \
    --ClusterId abc \
    --ProjectId abc \
    --AgentName abc \
    --TkeRegion ap-beijing
```

Output: 
```
{
    "Response": {
        "AgentId": "abc",
        "RequestId": "abc"
    }
}
```

