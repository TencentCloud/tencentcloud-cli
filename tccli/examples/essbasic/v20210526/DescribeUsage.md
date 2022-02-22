**Example 1: 渠道用量查询查询-无需汇总**



Input: 

```
tccli essbasic DescribeUsage --cli-unfold-argument  \
    --StartDate 2020-07-11 \
    --EndDate 2020-07-12 \
    --Agent.ProxyAppId  \
    --Agent.ProxyOperator.OpenId  \
    --Agent.ProxyOperator.ClientIp  \
    --Agent.ProxyOperator.CustomUserId  \
    --Agent.ProxyOperator.ProxyIp  \
    --Agent.ProxyOperator.Channel  \
    --Agent.ProxyOrganizationId  \
    --Agent.AppId testappid1 \
    --NeedAggregate False
```

Output: 
```
{
    "Response": {
        "Total": 4,
        "Details": [
            {
                "Date": "2020-07-11",
                "ProxyOrganizationOpenId": "org1",
                "Usage": 50,
                "ProxyOrganizationName": "合作企业"
            },
            {
                "Date": "2020-07-12",
                "ProxyOrganizationOpenId": "org1",
                "Usage": 50,
                "ProxyOrganizationName": "合作企业"
            },
            {
                "Date": "2020-07-11",
                "ProxyOrganizationOpenId": "org2",
                "Usage": 80,
                "ProxyOrganizationName": "合作企业"
            },
            {
                "Date": "2020-07-12",
                "ProxyOrganizationOpenId": "org2",
                "Usage": 86,
                "ProxyOrganizationName": "合作企业"
            }
        ],
        "RequestId": "xx"
    }
}
```

**Example 2: 渠道用量查询-需要汇总**



Input: 

```
tccli essbasic DescribeUsage --cli-unfold-argument  \
    --StartDate 2020-07-11 \
    --EndDate 2020-07-12 \
    --Agent.ProxyAppId  \
    --Agent.ProxyOperator.OpenId  \
    --Agent.ProxyOperator.ClientIp  \
    --Agent.ProxyOperator.CustomUserId  \
    --Agent.ProxyOperator.ProxyIp  \
    --Agent.ProxyOperator.Channel  \
    --Agent.ProxyOrganizationId  \
    --Agent.AppId testappid1 \
    --NeedAggregate True
```

Output: 
```
{
    "Response": {
        "Total": 2,
        "Details": [
            {
                "Date": "",
                "ProxyOrganizationOpenId": "org1",
                "Usage": 100,
                "ProxyOrganizationName": "合作企业"
            },
            {
                "Date": "",
                "ProxyOrganizationOpenId": "org2",
                "Usage": 166,
                "ProxyOrganizationName": "合作企业"
            }
        ],
        "RequestId": "xx"
    }
}
```

