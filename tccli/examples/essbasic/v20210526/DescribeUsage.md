**Example 1: 第三方平台用量查询-需要汇总**

第三方平台用量查询-需要汇总

Input: 

```
tccli essbasic DescribeUsage --cli-unfold-argument  \
    --StartDate 2020-07-11 \
    --EndDate 2020-07-12 \
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
                "Date": "2020-09-22",
                "ProxyOrganizationOpenId": "org1",
                "Usage": 100,
                "ProxyOrganizationName": "合作企业",
                "FlowChannel": "test",
                "Cancel": 0
            },
            {
                "Date": "2020-09-22",
                "ProxyOrganizationOpenId": "org2",
                "Usage": 166,
                "ProxyOrganizationName": "合作企业",
                "FlowChannel": "test",
                "Cancel": 0
            }
        ],
        "RequestId": "id"
    }
}
```

**Example 2: 第三方平台用量查询查询-无需汇总**

第三方平台用量查询查询-无需汇总

Input: 

```
tccli essbasic DescribeUsage --cli-unfold-argument  \
    --StartDate 2020-07-11 \
    --EndDate 2020-07-12 \
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
                "ProxyOrganizationName": "合作企业",
                "FlowChannel": "test",
                "Cancel": 0
            },
            {
                "Date": "2020-07-12",
                "ProxyOrganizationOpenId": "org1",
                "Usage": 50,
                "ProxyOrganizationName": "合作企业",
                "FlowChannel": "test",
                "Cancel": 0
            },
            {
                "Date": "2020-07-11",
                "ProxyOrganizationOpenId": "org2",
                "Usage": 80,
                "ProxyOrganizationName": "合作企业",
                "FlowChannel": "test",
                "Cancel": 0
            },
            {
                "Date": "2020-07-12",
                "ProxyOrganizationOpenId": "org2",
                "Usage": 86,
                "ProxyOrganizationName": "合作企业",
                "FlowChannel": "test",
                "Cancel": 0
            }
        ],
        "RequestId": "id"
    }
}
```

