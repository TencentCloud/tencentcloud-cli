**Example 1: 获取爆破破解规则**



Input: 

```
tccli cwp DescribeBruteAttackRules --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Rules": [
            {
                "LoginFailTimes": 1,
                "LoginFailTimesDefault": 1,
                "TimeRange": 1,
                "Enable": true,
                "TimeRangeDefault": 1
            }
        ],
        "RequestId": "5336f9fe-55bc-d1de-b5d2-ead1f6be2ea7"
    }
}
```

