**Example 1: DescribeConfigMaps**



Input: 

```
tccli iecp DescribeConfigMaps --cli-unfold-argument  \
    --EdgeUnitID 1 \
    --NamePattern test \
    --ConfigMapNamespace default \
    --Offset 0 \
    --Limit 10 \
    --Sort.Field CreateTime \
    --Sort.Order ASC
```

Output: 
```
{
    "Response": {
        "RequestId": "72d540a0-ed11-4370-b977-96c6c224a1d8",
        "Items": [
            {
                "Name": "test",
                "Namespace": "default",
                "CreateTime": "2021-01-01 00:00:00"
            }
        ]
    }
}
```

