**Example 1: 查询 IP 组中的 IP 或网段内容**

通过指定 GroupId 查询 IP 组中的 IP 或网段列表。如果 IP 或网段列表数量超过 100000，可以通过分页查询的方式逐步获取所有数据。

Input: 

```
tccli teo DescribeSecurityIPGroupContent --cli-unfold-argument  \
    --ZoneId zone-nqicqhasui \
    --GroupId 100121 \
    --Limit 1000 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "IPTotalCount": 5,
        "IPList": [
            "1.1.1.1",
            "1.2.3.1",
            "1.2.4.1",
            "1.5.3.1",
            "6.2.3.1"
        ],
        "RequestId": "ddf831fc-cf45-40fe-81b0-2d9cdd4c1bd6"
    }
}
```

