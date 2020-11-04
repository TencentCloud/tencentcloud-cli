**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveDomain --cli-unfold-argument  \
    --DomainName yourdomain.test.com
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "DomainInfo": {
            "Name": "abc.com",
            "Type": 1,
            "Status": 1,
            "CreateTime": "2018-08-29 10:00:00",
            "BCName": 1,
            "TargetDomain": "yourdomain.test2.com",
            "CurrentCName": "yourdomain.test.com",
            "IsDelayLive": 0,
            "RentTag": 0,
            "RentExpireTime": "0000-00-00 00:00:00"
        }
    }
}
```

