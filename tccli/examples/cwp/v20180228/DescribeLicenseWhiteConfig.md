**Example 1: 示例**

查询是否有试用配置

Input: 

```
tccli cwp DescribeLicenseWhiteConfig --cli-unfold-argument  \
    --RuleName cwp_yunying
```

Output: 
```
{
    "Response": {
        "FlagShip": {
            "Deadline": 7,
            "IsApplyFor": false,
            "LicenseNum": 10,
            "SourceType": 6
        },
        "LOG": {
            "Deadline": 0,
            "IsApplyFor": false,
            "LicenseNum": 0,
            "SourceType": 0
        },
        "PrattWhitney": {
            "Deadline": 0,
            "IsApplyFor": false,
            "LicenseNum": 0,
            "SourceType": 0
        },
        "Professional": {
            "Deadline": 0,
            "IsApplyFor": false,
            "LicenseNum": 0,
            "SourceType": 0
        },
        "RASP": {
            "Deadline": 0,
            "IsApplyFor": false,
            "LicenseNum": 0,
            "SourceType": 0
        },
        "RequestId": "09c2d4b3-ffdf-495d-9817-a89fdad0de89"
    }
}
```

