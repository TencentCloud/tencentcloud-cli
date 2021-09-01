**Example 1: nat规则列表概况**



Input: 

```
tccli cfw DescribeNatRuleOverview --cli-unfold-argument  \
    --Direction 1 \
    --Area ap-chongqing
```

Output: 
```
{
    "Response": {
        "InstanceId": "cfwnat-f3250045",
        "InstanceName": "nat-name",
        "EipList": [
            "192.168.0.1",
            "10.10.10.10"
        ],
        "DnatNum": 10,
        "TotalNum": 100,
        "RemainNum": 4900,
        "BlockNum": 50,
        "EnableNum": 10,
        "RequestId": "cd0e1fdf-157d-438c-9bc8-75925e5d4e20"
    }
}
```

