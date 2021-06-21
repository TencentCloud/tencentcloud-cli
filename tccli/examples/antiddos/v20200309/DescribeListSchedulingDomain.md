**Example 1: 获取智能调度域名列表**



Input: 

```
tccli antiddos DescribeListSchedulingDomain --cli-unfold-argument  \
    --Offset 0 \
    --Limit 25 \
    --FilterDomain test.com
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "RequestId": "xx",
        "DomainList": [
            {
                "Status": 1,
                "Domain": "xx",
                "ModifyTime": "2020-09-22 00:00:00",
                "TTL": 1,
                "CreatedTime": "2020-09-22 00:00:00",
                "UsrDomainName": "xx",
                "LineIPList": [
                    {
                        "Eip": "xx",
                        "Type": "xx"
                    }
                ],
                "Method": "xx"
            }
        ]
    }
}
```
