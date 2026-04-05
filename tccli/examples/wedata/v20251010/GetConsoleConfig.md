**Example 1: demo**



Input: 

```
tccli wedata GetConsoleConfig --cli-unfold-argument  \
    --ConfigParams.0.ConfigType 2 \
    --ConfigParams.0.ConfigKeys language
```

Output: 
```
{
    "Response": {
        "Data": {
            "ConfigItems": [
                {
                    "ConfigKey": "language",
                    "ConfigType": 2,
                    "ConfigValue": "zh-CN"
                }
            ]
        },
        "RequestId": "e10f847c-dc89-4703-a622-11d78e8d79ec"
    }
}
```

