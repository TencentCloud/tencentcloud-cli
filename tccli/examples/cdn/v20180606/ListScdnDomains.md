**Example 1: 查询SCDN域名列表**



Input: 

```
tccli cdn ListScdnDomains --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "DomainList": [
            {
                "Domain": "www.test.com",
                "Status": "online",
                "Waf": "/",
                "Acl": "yes",
                "Cc": "no",
                "Dddos": "close"
            }
        ],
        "TotalCount": 11
    }
}
```

