**Example 1: 查询 IP 分组的配置信息**

查询指定站点的 IP 分组配置信息，并按每页 10 条返回第 1 页内容。

Input: 

```
tccli teo DescribeSecurityIPGroupInfo --cli-unfold-argument  \
    --ZoneId zone-20hyebgyfsko \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "IPGroups": [
            {
                "GroupId": 123,
                "Name": "ExampleIpGroup",
                "Content": [
                    "123.123.123.0",
                    "23.23.23.0/24"
                ]
            }
        ],
        "RequestId": "5e5a0d0f-52f3-4bad-9bd3-dcf1d5c954e7"
    }
}
```

