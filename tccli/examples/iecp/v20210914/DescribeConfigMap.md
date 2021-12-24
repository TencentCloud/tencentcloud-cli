**Example 1: DescribeConfigMap**



Input: 

```
tccli iecp DescribeConfigMap --cli-unfold-argument  \
    --EdgeUnitID 1 \
    --ConfigMapName iecp
```

Output: 
```
{
    "Response": {
        "RequestId": "72d540a0-ed11-4370-b977-96c6c224a1d8",
        "Name": "test",
        "Namespace": "default",
        "Yaml": "",
        "Json": "",
        "CreateTime": "2021-01-01 00:00:00"
    }
}
```

