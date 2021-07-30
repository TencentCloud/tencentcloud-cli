**Example 1: 拉取云存用户列表**



Input: 

```
tccli iotvideo DescribeCloudStorageUsers --cli-unfold-argument  \
    --DeviceName xx \
    --Offset 0 \
    --Limit 10 \
    --ProductId xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Users": [
            {
                "UserId": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

