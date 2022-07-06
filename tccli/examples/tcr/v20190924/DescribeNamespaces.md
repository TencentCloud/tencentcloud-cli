**Example 1: 查询命名空间信息**

查询实例内所有的命名空间信息

Input: 

```
tccli tcr DescribeNamespaces --cli-unfold-argument  \
    --Limit 20 \
    --RegistryId tcr-f7g1ir99 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "d92365c7-3484-4d52-8add-93f682e127bd",
        "NamespaceList": [
            {
                "Name": "mytest1",
                "CreationTime": "2020-02-27T00:49:22+08:00",
                "Public": true,
                "NamespaceId": 2
            },
            {
                "Name": "mytest",
                "CreationTime": "2020-02-27T00:44:49+08:00",
                "Public": true,
                "NamespaceId": 1
            }
        ],
        "TotalCount": 2
    }
}
```

