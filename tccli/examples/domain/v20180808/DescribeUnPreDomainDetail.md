**Example 1: 查询预释放未预约域名详情接口**



Input: 

```
tccli domain DescribeUnPreDomainDetail --cli-unfold-argument  \
    --Domain abc
```

Output: 
```
{
    "Response": {
        "Domain": "abc",
        "PreCount": 0,
        "RegTime": "abc",
        "DeleteTime": "abc",
        "ExpireTime": "abc",
        "Status": "abc",
        "CurrentPrice": 0,
        "AppointBondPrice": 0,
        "IsAppoint": true,
        "BusinessId": "abc",
        "IsDomainUser": true,
        "RequestId": "abc"
    }
}
```

