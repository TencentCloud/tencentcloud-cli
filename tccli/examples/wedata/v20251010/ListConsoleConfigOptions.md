**Example 1: demo**



Input: 

```
tccli wedata ListConsoleConfigOptions --cli-unfold-argument  \
    --ConfigParams.0.ConfigType 2 \
    --ConfigParams.0.ConfigKeys language
```

Output: 
```
{
    "Response": {
        "Data": {
            "ConfigOptionItems": [
                {
                    "ConfigKey": "language",
                    "ConfigOptions": [
                        "zh-CN",
                        "en-US"
                    ],
                    "ConfigType": 2
                }
            ]
        },
        "RequestId": "76ecd2ae-573b-4578-9097-b4fed4ad6602"
    }
}
```

