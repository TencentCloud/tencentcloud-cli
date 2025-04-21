**Example 1: 示例1**

示例1

Input: 

```
tccli ioa DescribeHomeDeviceVirusChart --cli-unfold-argument  \
    --OsType abc \
    --DayRange 0 \
    --Key abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "VirusPie": {
                "Ignore": 0,
                "KillFail": 0,
                "KillSucceed": 0,
                "Trust": 0
            },
            "VirusData": [
                {
                    "Date": "abc",
                    "Data": {
                        "Ignore": 0,
                        "KillFail": 0,
                        "KillSucceed": 0,
                        "Trust": 0
                    }
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

**Example 2: DescribeHomeDeviceVirusChart**

DescribeHomeDeviceVirusChart

Input: 

```
tccli ioa DescribeHomeDeviceVirusChart --cli-unfold-argument  \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "515acb55-ac50-49bc-a417-1f676ca91675"
    }
}
```

