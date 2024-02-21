**Example 1: 成功示例**



Input: 

```
tccli domain DescribePreDomainList --cli-unfold-argument  \
    --Page 0 \
    --Size 0
```

Output: 
```
{
    "Response": {
        "ReservedDomainList": [
            {
                "Domain": "abc",
                "RegTime": "abc",
                "ExpireTime": "abc",
                "RenewEndTime": "abc",
                "RestoreEndTime": "abc",
                "ReservedEndTime": "abc"
            }
        ],
        "Total": 0,
        "RequestId": "abc"
    }
}
```

