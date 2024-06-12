**Example 1: 成功示例**



Input: 

```
tccli domain DescribeReservedPreDomainInfo --cli-unfold-argument  \
    --DomainList abdwww.cn \
    --ReservedStatus 0 \
    --ReservedTimeSort asc \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ReservedPreDomainInfoList": [
            {
                "Domain": "abdwww.cn",
                "ReservedStatus": 0,
                "FailReason": "",
                "ChangeOwnerTime": "2024-03-01 20:13:23",
                "RegTime": "2022-03-01 20:13:23",
                "ExpireTime": "2024-03-01 20:13:23",
                "ResourceId": "domain-dfo23req"
            }
        ],
        "Total": 1,
        "RequestId": "xxxx-xxx-xxx-xxxx"
    }
}
```

**Example 2: 请求成功示例**

请求成功获取参数示例

Input: 

```
tccli domain DescribeReservedPreDomainInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "xxxx-xxx-xxx-xxxx",
        "ReservedPreDomainInfoList": [
            {
                "BusinessId": "P0011712734968570466",
                "ChangeOwnerTime": "2024-03-15 08:40:34",
                "Domain": "fdasfasfdsaf.com",
                "ExpireTime": "2024-01-14 08:40:34",
                "FailReason": "",
                "RegTime": "2020-01-14 08:40:34",
                "ReservedStatus": 6,
                "ResourceId": "R0011712734968672830"
            }
        ],
        "Total": 1
    }
}
```

