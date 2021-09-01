**Example 1: 查询个人版命名空间信息**



Input: 

```
tccli tcr DescribeNamespacePersonal --cli-unfold-argument  \
    --Namespace mynamespace \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "Data": {
            "NamespaceCount": 1,
            "NamespaceInfo": [
                {
                    "Namespace": "test",
                    "CreationTime": "2018-07-25 15:07:12",
                    "RepoCount": 2
                }
            ]
        }
    }
}
```

