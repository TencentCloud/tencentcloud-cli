**Example 1: 获取命名空间列表**



Input: 

```
tccli iecp DescribeNamespaces --cli-unfold-argument  \
    --EdgeUnitID 1 \
    --NamePattern default
```

Output: 
```
{
    "Response": {
        "RequestId": "72d540a0-ed11-4370-b977-96c6c224a1d8",
        "Items": [
            {
                "Status": "Active",
                "Description": "",
                "Namespace": "test",
                "CreateTime": "2021-01-01 00:00:00",
                "Protected": false,
                "Yaml": ""
            }
        ]
    }
}
```

