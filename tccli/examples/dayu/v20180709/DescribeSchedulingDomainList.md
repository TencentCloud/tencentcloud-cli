**Example 1: 获取调度域名列表**



Input: 

```
tccli dayu DescribeSchedulingDomainList --cli-unfold-argument  \
    --Limit 30 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "8466d9e1-70a9-4575-8e02-df15bd50bc49",
        "Total": 1,
        "DomainList": [
            {
                "Domain": "1.test.com",
                "BGPIpList": [],
                "CTCCIpList": [],
                "CUCCIpList": [],
                "CMCCIpList": [],
                "OverseaIpList": [],
                "Method": "priority",
                "CreateTime": "2019-08-21 12:32:12",
                "Status": 1,
                "ModifyTime": "2019-08-21 12:32:45"
            }
        ]
    }
}
```

