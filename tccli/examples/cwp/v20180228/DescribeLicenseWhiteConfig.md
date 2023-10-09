**Example 1: 示例**

查询是否有试用配置

Input: 

```
tccli cwp DescribeLicenseWhiteConfig --cli-unfold-argument  \
    --RuleName cwp
```

Output: 
```
{
    "Response": {
        "FlagShip": {
            "Deadline": 7,
            "IsApplyFor": true,
            "LicenseNum": 10,
            "SourceType": 1
        },
        "PrattWhitney": {
            "Deadline": 0,
            "IsApplyFor": false,
            "LicenseNum": 0,
            "SourceType": 0
        },
        "Professional": {
            "Deadline": 7,
            "IsApplyFor": false,
            "LicenseNum": 10,
            "SourceType": 1
        },
        "RequestId": "5ebd92e8-9873-4b4c-a26a-7f43048d42d2"
    }
}
```

