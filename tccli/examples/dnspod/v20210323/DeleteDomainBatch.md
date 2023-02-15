**Example 1: 批量删除域名**

 

Input: 

```
tccli dnspod DeleteDomainBatch --cli-unfold-argument  \
    --DomainList sdfsdfsdf.com
```

Output: 
```
{
    "Response": {
        "RequestId": "0f8cc178-1a8d-4923-a24d-2b47883386f7",
        "JobId": "1701611",
        "DetailList": [
            {
                "DomainId": "12620428",
                "Domain": "sdfsdfsdf.com",
                "Error": null,
                "Status": "waiting",
                "Operation": "remove"
            }
        ]
    }
}
```

