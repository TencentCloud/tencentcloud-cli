**Example 1: 漏洞影响主机列表**

漏洞影响主机列表

Input: 

```
tccli cwp DescribeVulEffectModules --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --VulId 100435
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "VulEffectModuleInfo": [
            {
                "Name": "xx",
                "FixCmd": "xx",
                "Rule": "xx",
                "Version": "xx",
                "Uuids": [
                    "xx"
                ],
                "Path": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

