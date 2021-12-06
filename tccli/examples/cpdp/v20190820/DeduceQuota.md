**Example 1: DeduceQuota**



Input: 

```
tccli cpdp DeduceQuota --cli-unfold-argument  \
    --AnchorId 100180419 \
    --Amount 2323 \
    --OrderId o1232518
```

Output: 
```
{
    "Response": {
        "ErrCode": "SUCCESS",
        "Result": {
            "AnchorName": "主播名称",
            "AgentId": "AgentId",
            "AnchorId": "100180419",
            "AgentName": "代理商名称"
        },
        "ErrMsg": "成功",
        "RequestId": "123123"
    }
}
```

