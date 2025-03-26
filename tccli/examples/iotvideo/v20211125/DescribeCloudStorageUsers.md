**Example 1: 拉取云存用户列表**



Input: 

```
tccli iotvideo DescribeCloudStorageUsers --cli-unfold-argument  \
    --DeviceName dev \
    --Offset 0 \
    --Limit 10 \
    --ProductId product
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Users": [
            {
                "UserId": "user"
            }
        ],
        "RequestId": "id"
    }
}
```

