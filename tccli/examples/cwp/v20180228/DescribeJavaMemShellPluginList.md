**Example 1: 查询java内存马插件列表**



Input: 

```
tccli cwp DescribeJavaMemShellPluginList --cli-unfold-argument  \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Quuid": "e1f081aa-7777-4fdf-a2f7-88f3faa3d302",
                "Alias": "armtest7.4安装卸载",
                "HostIp": "172.16.48.133",
                "JavaShellStatus": 0,
                "Exception": 0,
                "CreateTime": "2022-04-13 17:01:37",
                "ModifyTime": "2022-04-13 21:04:23"
            }
        ],
        "RequestId": "da2d723e-4aac-4f4a-bbf9-e5430e29d289",
        "TotalCount": 21
    }
}
```

