**Example 1: 查询告警通知接收组列表**



Input: 

```
tccli pts DescribeAlertChannels --cli-unfold-argument  \
    --OrderBy xx \
    --Ascend True \
    --Limit 1 \
    --Offset 1 \
    --ProjectIds xx
```

Output: 
```
{
    "Response": {
        "AlertChannelSet": [
            {
                "Status": {
                    "SendNotice": 1,
                    "AbortJob": 1
                },
                "NoticeId": "xx",
                "ProjectId": "xx",
                "UpdatedAt": "xx",
                "AMPConsumerId": "xx",
                "CreatedAt": "xx"
            }
        ],
        "Total": 1,
        "RequestId": "xx"
    }
}
```

