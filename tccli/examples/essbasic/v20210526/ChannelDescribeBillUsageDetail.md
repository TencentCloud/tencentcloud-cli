**Example 1: 查询失败样例**



Input: 

```
tccli essbasic ChannelDescribeBillUsageDetail --cli-unfold-argument  \
    --StartTime 20230902 \
    --EndTime 20230930 \
    --Offset 0 \
    --Limit 500 \
    --Agent.AppId yDwFdUUckpsw******yQ0af8bHosXQtb \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId 
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

**Example 2: 查询某个应用下某个子客的消耗情况**



Input: 

```
tccli essbasic ChannelDescribeBillUsageDetail --cli-unfold-argument  \
    --StartTime 20230902 \
    --EndTime 20230930 \
    --Offset 0 \
    --Limit 20 \
    --Agent.AppId yDwFdUUckpsw******yQ0af8bHosXQtb \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId 
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "CostTime": 1695037514,
                "CostType": 1,
                "CreateOrganizationName": "典子谦示例企业",
                "FlowId": "yDwFdUUckps******uzcbXwoXbRF6ja3",
                "FlowName": "典子谦示例合同",
                "OperatorName": "张三;典子谦",
                "QuotaName": "企业版运营礼包",
                "QuotaType": "CloudEnterprise",
                "Remark": "",
                "FlowStatus": "ALL",
                "UseCount": 1
            }
        ],
        "RequestId": "s16992572741898xxxx",
        "Total": 1
    }
}
```

**Example 3: 查询某应用下渠道企业的消耗情况**



Input: 

```
tccli essbasic ChannelDescribeBillUsageDetail --cli-unfold-argument  \
    --StartTime 20230902 \
    --EndTime 20230930 \
    --Offset 0 \
    --Limit 20 \
    --Agent.AppId yDwFdUUckpsw******yQ0af8bHosXQtb
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "CostTime": 1695037514,
                "CostType": 1,
                "CreateOrganizationName": "典子谦示例企业",
                "FlowId": "yDwFdUUckps******uzcbXwoXbRF6ja3",
                "FlowName": "典子谦示例合同",
                "OperatorName": "张三;典子谦",
                "QuotaName": "企业版运营礼包",
                "QuotaType": "CloudEnterprise",
                "Remark": "",
                "FlowStatus": "ALL",
                "UseCount": 1
            }
        ],
        "RequestId": "s16992572741898xxxx",
        "Total": 1
    }
}
```

