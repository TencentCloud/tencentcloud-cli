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
                "Domain": "tencent.com",
                "RegTime": "2006-01-02 15:04:05",
                "ExpireTime": "2006-01-02 15:04:05",
                "RenewEndTime": "2006-01-02 15:04:05",
                "RestoreEndTime": "2006-01-02 15:04:05",
                "ReservedEndTime": "2006-01-02 15:04:05"
            }
        ],
        "Total": 1,
        "RequestId": "abc"
    }
}
```

