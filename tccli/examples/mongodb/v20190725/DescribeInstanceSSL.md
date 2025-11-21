**Example 1: 查看实例SSL开启状态**



Input: 

```
tccli mongodb DescribeInstanceSSL --cli-unfold-argument  \
    --InstanceId cmgo-eqmoaxxx
```

Output: 
```
{
    "Response": {
        "Status": 1,
        "ExpiredTime": "2023-05-04 12:13:00",
        "CertUrl": "http://sample/cert",
        "RequestId": "12345-abcdef"
    }
}
```

