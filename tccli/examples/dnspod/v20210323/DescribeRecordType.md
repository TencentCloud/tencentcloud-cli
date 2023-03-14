**Example 1: 获取等级允许的记录类型**

 获取等级允许的记录类型

Input: 

```
tccli dnspod DescribeRecordType --cli-unfold-argument  \
    --DomainGrade DP_Expert
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "TypeList": [
            "A",
            "CNAME",
            "MX",
            "TXT",
            "NS",
            "SPF",
            "SRV",
            "CAA",
            "显性URL",
            "隐性URL"
        ]
    }
}
```

