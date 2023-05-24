**Example 1: 查询SCDN域名列表**

查询SCDN域名列表

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
                "WafLevel": 200,
                "CC": "close",
                "Area": "global",
                "AclRuleNumbers": 3,
                "Ddos": "close",
                "ProjectId": "0",
                "Bot": "close"
            }
        ],
        "TotalCount": 11
    }
}
```

