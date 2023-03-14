**Example 1: 获取域名概览信息**

获取域名概览信息

Input: 

```
tccli dnspod DescribeDomainPreview --cli-unfold-argument  \
    --Domain dnspod.cn
```

Output: 
```
{
    "Response": {
        "Domain": {
            "AliasCount": 0,
            "DomainParkingStatus": 0,
            "Grade": "DP_Free",
            "GradeTitle": "免费版",
            "LineCount": 0,
            "LineGroupCount": 0,
            "MaxAliasCount": 0,
            "Name": "dnspod.cn",
            "Records": 27,
            "ResolveCount": 8918,
            "VASCount": 0
        },
        "RequestId": "cf7d3e8f-662a-4c20-86e4-b927458e9ffe"
    }
}
```

