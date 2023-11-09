**Example 1: 查询明细消耗**

NeedAggregate设置为false为查询明细消耗

Input: 

```
tccli essbasic DescribeUsage --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --StartDate 2023-11-06 \
    --EndDate 2023-11-08 \
    --NeedAggregate False \
    --Limit 1000 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 4,
        "Details": [
            {
                "ProxyOrganizationOpenId": "org_zhansan",
                "ProxyOrganizationName": "张三示例企业",
                "Date": "2023-11-06",
                "Usage": 12,
                "Cancel": 0,
                "FlowChannel": "企业版"
            },
            {
                "ProxyOrganizationOpenId": "org_dianziqian",
                "ProxyOrganizationName": "典子谦示例企业",
                "Date": "2023-11-07",
                "Usage": 30,
                "Cancel": 0,
                "FlowChannel": "企业版"
            },
            {
                "ProxyOrganizationOpenId": "org_lisi",
                "ProxyOrganizationName": "李四示例企业",
                "Date": "2023-11-07",
                "Usage": 0,
                "Cancel": 5,
                "FlowChannel": "企业版"
            },
            {
                "ProxyOrganizationOpenId": "org_dianziqian",
                "ProxyOrganizationName": "典子谦示例企业",
                "Date": "2023-11-08",
                "Usage": 6,
                "Cancel": 0,
                "FlowChannel": "企业版"
            }
        ],
        "RequestId": "5f01d19e-d4dc-4e8b-b709-024132d16da9"
    }
}
```

**Example 2: 查询汇总消耗**

NeedAggregate设置为true为查询汇总消耗

Input: 

```
tccli essbasic DescribeUsage --cli-unfold-argument  \
    --Agent.AppId yDwhxUUckp3gl8j5UuFX33LSNozpRsbi \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.ProxyAppId  \
    --StartDate 2023-11-06 \
    --EndDate 2023-11-08 \
    --NeedAggregate True \
    --Limit 1000 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 2,
        "Details": [
            {
                "ProxyOrganizationOpenId": "org_zhangsan",
                "ProxyOrganizationName": "张三实例企业",
                "Date": "1970-01-01",
                "Usage": 0,
                "Cancel": 5,
                "FlowChannel": "企业版"
            },
            {
                "ProxyOrganizationOpenId": "org_dianziqian",
                "ProxyOrganizationName": "典子谦示例企业",
                "Date": "1970-01-01",
                "Usage": 48,
                "Cancel": 0,
                "FlowChannel": "企业版"
            }
        ],
        "RequestId": "f6ad02ec-0399-46c8-a9d9-4dde2aedc036"
    }
}
```

