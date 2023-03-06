**Example 1: 忽略策略列表**



Input: 

```
tccli cwp DescribeBaselineRuleIgnoreList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "RuleName": "test",
                "CategoryId": -1,
                "RuleDesc": "ignore rule",
                "Items": [],
                "RuleId": 125,
                "RuleType": 1,
                "HostCount": 0,
                "HostIps": [
                    ""
                ]
            }
        ],
        "RequestId": "aaddca9b-8634-47c5-bdf3-add2f36ad7a9",
        "Total": 1
    }
}
```

