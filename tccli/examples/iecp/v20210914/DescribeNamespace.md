**Example 1: DescribeNamespace**



Input: 

```
tccli iecp DescribeNamespace --cli-unfold-argument  \
    --EdgeUnitID 1 \
    --Namespace default
```

Output: 
```
{
    "Response": {
        "RequestId": "72d540a0-ed11-4370-b977-96c6c224a1d8",
        "Status": "Active",
        "Description": "",
        "Namespace": "test",
        "CreateTime": "2021-01-01 00:00:00",
        "Protected": false,
        "Yaml": ""
    }
}
```

