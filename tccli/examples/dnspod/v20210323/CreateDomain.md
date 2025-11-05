**Example 1: 添加域名**

 

Input: 

```
tccli dnspod CreateDomain --cli-unfold-argument  \
    --Domain dnspod.com \
    --IsMark no \
    --GroupId 2
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "DomainInfo": {
            "Id": 62,
            "Punycode": "dnspod.com",
            "Domain": "dnspod.com",
            "GradeNsList": [
                "source.dnspod.net",
                "low.dnspod.net"
            ]
        }
    }
}
```

