**Example 1: 查询失败样例**



Input: 

```
tccli ess DescribeBillUsageDetail --cli-unfold-argument  \
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

**Example 2: 查询全部套餐消耗**



Input: 

```
tccli ess DescribeBillUsageDetail --cli-unfold-argument  \
    --StartTime 20230902 \
    --EndTime 20230930 \
    --Offset 0 \
    --Limit 50
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

**Example 3: 查询子企业客户消耗**



Input: 

```
tccli ess DescribeBillUsageDetail --cli-unfold-argument  \
    --StartTime 20230902 \
    --EndTime 20230930 \
    --Offset 0 \
    --Limit 50 \
    --Agent.ProxyOrganizationId xxxxx
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

