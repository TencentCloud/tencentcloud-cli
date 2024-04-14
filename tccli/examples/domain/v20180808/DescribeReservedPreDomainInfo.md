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

**Example 2: 请求成功示例**

请求成功获取参数示例

Input: 

```
tccli domain DescribeReservedPreDomainInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "a6bd9e77-517f-4fd8-9ee9-f7042b7ae847",
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

