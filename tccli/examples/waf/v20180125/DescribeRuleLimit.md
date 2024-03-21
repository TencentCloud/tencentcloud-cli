**Example 1: DescribeRuleLimit**



Input: 

```
tccli waf DescribeRuleLimit --cli-unfold-argument  \
    --Domain test.qcloudwaf.com
```

Output: 
```
{
    "Response": {
        "Res": {
            "CC": 0,
            "CustomRule": 0,
            "IPControl": 0,
            "AntiLeak": 0,
            "AntiTamper": 0,
            "AutoCC": 0,
            "AreaBan": 0,
            "CCSession": 0,
            "AI": 0,
            "CustomWhite": 0
        },
        "RequestId": "123"
    }
}
```

