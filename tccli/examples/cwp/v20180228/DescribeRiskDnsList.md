**Example 1: 获取恶意请求列表**

入侵检测-获取恶意请求列表

Input: 

```
tccli cwp DescribeRiskDnsList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "4234234",
        "RiskDnsList": [
            {
                "Url": "odysseusweb.ru",
                "AccessCount": 6,
                "ProcessName": "C:\\Program Files (x86)\\Internet Explorer\\iexplore.exe",
                "ProcessMd5": "97cdf8b51cea8d0f296e6871e388979d",
                "GlobalRuleId": 0,
                "UserRuleId": 0,
                "Status": 0,
                "CreateTime": "2019-12-25 22:31:54",
                "MergeTime": "2019-12-25 22:31:54",
                "Quuid": "e761c2dc-bc72-40cd-b9ed-d233c86b1a8b",
                "HostIp": "2402:4e00:1010:5401:0:8f51:5190:3bfa",
                "Alias": "ipv6_windows_test",
                "Description": "",
                "Uuid": "e761c2dc-bc72-40cd-b9ed-d233c86b1a8",
                "Pid": 1,
                "Id": 1,
                "CmdLine": "xx",
                "Reference": "xx"
            }
        ],
        "TotalCount": 20
    }
}
```

