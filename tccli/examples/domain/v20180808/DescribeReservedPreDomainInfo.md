**Example 1: 成功示例**



Input: 

```
tccli domain DescribeReservedPreDomainInfo --cli-unfold-argument  \
    --DomainList abc \
    --ReservedStatus 0 \
    --ReservedTimeSort abc \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ReservedPreDomainInfoList": [
            {
                "Domain": "abc",
                "ReservedStatus": 0,
                "FailReason": "abc",
                "ChangeOwnerTime": "abc",
                "RegTime": "abc",
                "ExpireTime": "abc",
                "ResourceId": "abc"
            }
        ],
        "Total": 0,
        "RequestId": "abc"
    }
}
```

