**Example 1: DescribeSecrets**



Input: 

```
tccli iecp DescribeSecrets --cli-unfold-argument  \
    --EdgeUnitID 1 \
    --Offset 0 \
    --Limit 1 \
    --Sort.Field CreateTime \
    --Sort.Order ASC
```

Output: 
```
{
    "Response": {
        "RequestId": "137ac961-6173-4250-995f-4769cd41c945",
        "TotalCount": 1,
        "Items": [
            {
                "Name": "iecp",
                "Namespace": "default",
                "CreateTime": "2021-01-01 00:00:00"
            }
        ]
    }
}
```

