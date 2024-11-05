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
                "AssetType": "1",
                "HostIds": [
                    "d99a1b46-cc2d-4633-a11f-4a7663d2523e"
                ],
                "RuleName": "high level",
                "CategoryId": -1,
                "RuleDesc": "ignore rule",
                "Items": [
                    {
                        "ItemId": 1002,
                        "ItemName": "itemname",
                        "CustomItemValues": [
                            100
                        ],
                        "CategoryId": 50
                    }
                ],
                "RuleId": 125,
                "RuleType": 1,
                "HostCount": 0,
                "HostIps": [
                    "127.0.0.1"
                ]
            }
        ],
        "RequestId": "aaddca9b-8634-47c5-bdf3-add2f36ad7a9",
        "Total": 1
    }
}
```

