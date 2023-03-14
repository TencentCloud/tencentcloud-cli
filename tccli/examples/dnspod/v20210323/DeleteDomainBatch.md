**Example 1: 批量删除域名**

 批量删除域名

Input: 

```
tccli dnspod DeleteDomainBatch --cli-unfold-argument  \
    --DomainList sdfsdfsdf.com
```

Output: 
```
{
    "Response": {
        "DetailList": [
            {
                "Domain": "yyds999.com",
                "DomainId": 12620607,
                "Error": null,
                "Operation": "remove",
                "Status": "waiting"
            }
        ],
        "JobId": 1703509,
        "RequestId": "5090a972-50ca-4be9-abf3-a1f90e8db36c"
    }
}
```

