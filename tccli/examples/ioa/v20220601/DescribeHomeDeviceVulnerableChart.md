**Example 1: 示例1**

示例1

Input: 

```
tccli ioa DescribeHomeDeviceVulnerableChart --cli-unfold-argument  \
    --OsType abc \
    --DayRange 0 \
    --Key abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "VulnerablePie": {
                "Ignore": 0,
                "Fail": 0,
                "Fix": 0,
                "Detect": 0
            },
            "VulnerableData": [
                {
                    "Date": "abc",
                    "Data": {
                        "Ignore": 0,
                        "Fail": 0,
                        "Fix": 0,
                        "Detect": 0
                    }
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

**Example 2: DescribeHomeDeviceVulnerableChart**

DescribeHomeDeviceVulnerableChart

Input: 

```
tccli ioa DescribeHomeDeviceVulnerableChart --cli-unfold-argument  \
    --OsType 0 \
    --DayRange 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "请求签名验证失败，请检查您的签名计算是否正确。"
        },
        "RequestId": "7fa42e59-701b-44de-8137-702b144c8480"
    }
}
```

