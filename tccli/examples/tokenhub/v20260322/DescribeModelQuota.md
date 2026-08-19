**Example 1: 正常响应**



Input: 

```
tccli tokenhub DescribeModelQuota --cli-unfold-argument  \
    --ModelId deepseek-v3.2
```

Output: 
```
{
    "Response": {
        "ModelId": "deepseek-v3.2",
        "RequestId": "8f6c89c0-b82c-4e4d-9f39-11d27eb449ca",
        "TPMLimit": 300000
    }
}
```

