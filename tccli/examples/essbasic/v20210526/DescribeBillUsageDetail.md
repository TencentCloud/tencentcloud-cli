**Example 1: 查询失败样例**



Input: 

```
tccli essbasic DescribeBillUsageDetail --cli-unfold-argument  \
    --Agent.AppId ydxxxxxx \
    --Agent.ProxyOrganizationOpenId orgxxxx \
    --StartTime 20230902 \
    --EndTime 20230930 \
    --Offset 0 \
    --Limit 1000
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.Limit",
            "Message": "分页参数不合法"
        },
        "RequestId": "s169935778xxxxxxx"
    }
}
```

**Example 2: 查询渠道客户消耗**



Input: 

```
tccli essbasic DescribeBillUsageDetail --cli-unfold-argument  \
    --StartTime 20230902 \
    --EndTime 20230930 \
    --Offset 0 \
    --Limit 1000 \
    --Agent.AppId ydxxxxxx \
    --Agent.ProxyOrganizationOpenId orgxxxx
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "CostTime": 1695037514,
                "CostType": 1,
                "FlowId": "yDwJOU5e7ikveIUxMW0p2uJxxxxxxxxxx",
                "FlowName": "腾讯电子签xxxxx合同",
                "OperatorName": "张三;李斯",
                "QuotaName": "签署报告（出证服务）",
                "QuotaType": "CloudProve",
                "Remark": "",
                "Status": 4,
                "UseCount": 1
            }
        ],
        "RequestId": "s16992572741898xxxx",
        "Total": 1
    }
}
```

