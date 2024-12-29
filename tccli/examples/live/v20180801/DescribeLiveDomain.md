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
        "RequestId": "6dad49b1-6a37-4288-9068-0be2ab6ce19b",
        "DomainInfo": {
            "Name": "push.livhub.net",
            "Type": 0,
            "Status": 1,
            "PlayType": 1,
            "IsDelayLive": 0,
            "IsMiniProgramLive": 0,
            "CreateTime": "2023-10-30 14:01:48",
            "BCName": 1,
            "CurrentCName": "push.livhub.net.tlivepush.com.",
            "TargetDomain": "push.livhub.net.tlivepush.com",
            "RentTag": 0,
            "RentExpireTime": "78894"
        }
    }
}
```

