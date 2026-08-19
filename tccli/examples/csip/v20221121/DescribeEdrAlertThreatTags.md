**Example 1: 查看告警对应腾讯云、安全中心、情报标签**



Input: 

```
tccli csip DescribeEdrAlertThreatTags --cli-unfold-argument  \
    --Targets.0.Id 1000000000000580 \
    --Targets.0.AlertId ed7ba2b9a95370778b2a589412f655aa \
    --Targets.0.AppId 260108008 \
    --Targets.0.Quuid 11c73bc2-6918-4457-88d3-1c22ef2de87b \
    --Targets.0.InstanceId ins-h0zrmp36 \
    --Targets.0.AlertSubType BRUTE_FORCE
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AlertId": "ed7ba2b9a95370778b2a589412f655aa",
                "CSIPTags": [],
                "CloudTags": [],
                "ThreatTags": []
            }
        ],
        "RequestId": "bcd1a021-e2b3-4352-9d79-37499e8f2f56"
    }
}
```

