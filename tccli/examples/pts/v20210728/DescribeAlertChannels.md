**Example 1: 查询告警通知接收组列表**



Input: 

```
tccli pts DescribeAlertChannels --cli-unfold-argument  \
    --OrderBy asc \
    --Ascend True \
    --Limit 1 \
    --Offset 1 \
    --ProjectIds project-xx
```

Output: 
```
{
    "Response": {
        "AlertChannelSet": [
            {
                "Status": 1,
                "NoticeId": "notice-xx",
                "ProjectId": "projecct-xx",
                "UpdatedAt": "2022-09-09 13:11:12",
                "AMPConsumerId": "consumer-xx",
                "CreatedAt": "2022-09-09 13:11:12",
                "AppId": 11111,
                "Uin": "11100000",
                "SubAccountUin": "22200000"
            }
        ],
        "Total": 1,
        "RequestId": "abc-123-xyz"
    }
}
```

