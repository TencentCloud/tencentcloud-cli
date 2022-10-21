**Example 1: 查询java内存马事件列表**



Input: 

```
tccli cwp DescribeJavaMemShellList --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "d92d723e-4aac-4f4a-bbf9-e5430e29d289",
        "TotalCount": 1,
        "List": [
            {
                "Id": 12,
                "Quuid": "d92d723e-4aac-4f4a-bbf9-e5430e29d289",
                "Alias": "v_llzlu-PC0",
                "HostIp": "192.168.255.10",
                "Type": 1,
                "Description": "Java (2845)中加载的net...",
                "CreateTime": "2021-01-20 16:17:11",
                "RecentFoundTime": "2021-01-20 16:17:11",
                "Status": 0
            }
        ]
    }
}
```

