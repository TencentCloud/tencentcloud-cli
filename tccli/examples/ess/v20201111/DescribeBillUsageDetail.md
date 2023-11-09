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
                "CreateOrganizationName": "典子谦示例企业",
                "FlowId": "yDwFdUUckps******uzcbXwoXbRF6ja3",
                "FlowName": "典子谦示例合同",
                "OperatorName": "典子谦;张三",
                "QuotaName": "企业版运营礼包",
                "QuotaType": "CloudEnterprise",
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
    --Agent.ProxyOrganizationId yDxbNUyKQDx3oAUuO4zjEBQGidlGe4hP
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "CostTime": 1695037514,
                "CostType": 1,
                "CreateOrganizationName": "张三示例企业",
                "FlowId": "yDwFdUUckps******xAhL7zuaIwkMth4",
                "FlowName": "张三示业合同",
                "OperatorName": "典子谦;张三",
                "QuotaName": "企业版运营礼包",
                "QuotaType": "CloudEnterprise",
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

