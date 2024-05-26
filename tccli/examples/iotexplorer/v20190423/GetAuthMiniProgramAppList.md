**Example 1: 成功查询小程序列表**



Input: 

```
tccli iotexplorer GetAuthMiniProgramAppList --cli-unfold-argument  \
    --MiniProgramAppId 123wdc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc",
        "Total": 1,
        "MiniProgramList": [
            {
                "MiniProgramAppId": "1qaz",
                "MiniProgramName": "appBane",
                "LicenseNum": 100,
                "CreateTime": 45674345567
            }
        ]
    }
}
```

