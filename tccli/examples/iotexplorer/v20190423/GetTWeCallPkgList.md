**Example 1: 成功查询示例**



Input: 

```
tccli iotexplorer GetTWeCallPkgList --cli-unfold-argument  \
    --MiniProgramAppId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc",
        "Total": 1,
        "TWeCallPkgList": [
            {
                "PkgId": "1qaz",
                "PkgType": 1,
                "CreateTime": 45674345567,
                "ExpireTime": 45674345567,
                "LicenseTotalNum": 1,
                "LicenseUsedNum": 1
            }
        ]
    }
}
```

