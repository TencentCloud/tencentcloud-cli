**Example 1: 示例1**



Input: 

```
tccli ioa DescribeUserSecrets --cli-unfold-argument  \
    --UserId  \
    --DomainId 
```

Output: 
```
{
    "Response": {
        "Data": {
            "LimitCount": 1,
            "TotalCount": 1,
            "UserSecrets": {
                "Number": 1,
                "ActivationTime": "",
                "Secret": ""
            }
        },
        "RequestId": "81d13817-209e-4237-978e-71ec82fe2c77"
    }
}
```

