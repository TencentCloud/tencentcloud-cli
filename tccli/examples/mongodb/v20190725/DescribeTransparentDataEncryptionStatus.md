**Example 1: 获取当前实例是否已开启数据加密**



Input: 

```
tccli mongodb DescribeTransparentDataEncryptionStatus --cli-unfold-argument  \
    --InstanceId cmgo-igjysqkr
```

Output: 
```
{
    "Response": {
        "TransparentDataEncryptionStatus": "open",
        "KeyInfoList": [
            {
                "KeyId": "abc",
                "KeyName": "abc",
                "CreateTime": "abc",
                "Status": "abc",
                "KeyUsage": "abc",
                "KeyOrigin": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

