**Example 1: 描述WAF威胁情报封禁模块详情**

描述WAF威胁情报封禁模块详情

Input: 

```
tccli waf DescribeWafThreatenIntelligence --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "WafThreatenIntelligenceDetails": {
            "DefenseStatus": 0,
            "LastUpdateTime": "2020-09-22T00:00:00+00:00",
            "Tags": [
                "global"
            ]
        },
        "RequestId": "1234"
    }
}
```

