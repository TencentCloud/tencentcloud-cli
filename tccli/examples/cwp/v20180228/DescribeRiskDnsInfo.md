**Example 1: 示例**

查询恶意请求详情

Input: 

```
tccli cwp DescribeRiskDnsInfo --cli-unfold-argument  \
    --Id 1
```

Output: 
```
{
    "Response": {
        "RiskDnsInfo": {
            "Url": "xx",
            "AccessCount": 1,
            "ProcessName": "xx",
            "ProcessMd5": "xx",
            "GlobalRuleId": 1,
            "UserRuleId": 1,
            "Status": 1,
            "CreateTime": "xx",
            "MergeTime": "xx",
            "Quuid": "xx",
            "HostIp": "xx",
            "Alias": "xx",
            "Description": "xx",
            "Id": 1,
            "Reference": "xx",
            "CmdLine": "xx",
            "Pid": 1,
            "Uuid": "xx",
            "SuggestScheme": "xx",
            "Tags": [
                "xx"
            ],
            "MachineWanIp": "xx",
            "MachineStatus": "xx"
        },
        "RequestId": "xx"
    }
}
```

