**Example 1: 主机信息与标签信息查询**

根据主机Quuid数组查询主机信息

Input: 

```
tccli cwp DescribeHostInfo --cli-unfold-argument  \
    --QuuidList "1"
```

Output: 
```
{
    "Response": {
        "RequestId": "3ca51296-46f5-4ad9-80b2-58f02783bb18 ",
        "HostInfoList": [
            {
                "HostIp": "xx",
                "AliasName": "xx",
                "Quuid": "xx",
                "TagList": [
                    "xx"
                ]
            },
            {
                "TagList": [
                    "xx"
                ],
                "AliasName": "xx",
                "Quuid": "xx",
                "HostIp": "xx"
            }
        ]
    }
}
```

