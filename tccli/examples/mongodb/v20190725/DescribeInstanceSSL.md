**Example 1: 查看实例SSL开启状态**



Input: 

```
tccli mongodb DescribeInstanceSSL --cli-unfold-argument  \
    --InstanceId cmgo-p*******
```

Output: 
```
{
    "Response": {
        "CertUrl": "",
        "ExpiredTime": "2027-06-18 07:17:56",
        "Status": 1,
        "RequestId": "5cfd65ee-caa6-413f-ad84-c70bff4703db"
    }
}
```

