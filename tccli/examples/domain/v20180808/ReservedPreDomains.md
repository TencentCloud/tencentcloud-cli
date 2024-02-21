**Example 1: 成功示例**



Input: 

```
tccli domain ReservedPreDomains --cli-unfold-argument  \
    --DomainList abc \
    --TemplateId abc
```

Output: 
```
{
    "Response": {
        "SucDomainList": [
            "abc"
        ],
        "FailDomainList": [
            {
                "Domain": "abc",
                "FailReason": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

