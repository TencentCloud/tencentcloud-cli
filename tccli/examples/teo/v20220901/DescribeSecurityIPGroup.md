**Example 1: 查询安全 IP 分组的配置信息**

查询指定站点中，安全 IP 分组的配置信息。

Input: 

```
tccli teo DescribeSecurityIPGroup --cli-unfold-argument  \
    --ZoneId zone-nqicqhasui
```

Output: 
```
{
    "Response": {
        "IPGroups": [
            {
                "GroupId": 123,
                "Name": "ExampleIpGroup",
                "Content": [
                    "2.2.2.2",
                    "23.23.23.0/24"
                ]
            }
        ],
        "RequestId": "ddf831fc-cf45-40fe-81b0-2d9cdd4c1bd6"
    }
}
```

