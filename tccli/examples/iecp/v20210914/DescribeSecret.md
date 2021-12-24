**Example 1: DescribeSecret**



Input: 

```
tccli iecp DescribeSecret --cli-unfold-argument  \
    --EdgeUnitID 1 \
    --SecretName iecp \
    --SecretNamespace default
```

Output: 
```
{
    "Response": {
        "RequestId": "137ac961-6173-4250-995f-4769cd41c945",
        "Name": "iecp",
        "Namespace": "default",
        "CreateTime": "2021-01-01 00:00:00",
        "Yaml": "",
        "Json": ""
    }
}
```

