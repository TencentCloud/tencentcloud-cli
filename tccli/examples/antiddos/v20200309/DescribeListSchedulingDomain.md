**Example 1: 获取智能调度域名列表**

查询智能调度列表

Input: 

```
tccli antiddos DescribeListSchedulingDomain --cli-unfold-argument  \
    --Limit 1 \
    --FilterDomain www.test.com \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "RequestId": "0506d138-ef0f-4ff4-83b0-f1d85e740afd",
        "DomainList": [
            {
                "Status": 1,
                "Domain": "www.test.com",
                "ModifyTime": "2020-09-22 00:00:00",
                "TTL": 1,
                "CreatedTime": "2020-09-22 00:00:00",
                "UsrDomainName": "www.test.com",
                "LineIPList": [
                    {
                        "Eip": "1.1.1.1",
                        "Type": "bgp"
                    }
                ],
                "Method": "priority"
            }
        ]
    }
}
```

