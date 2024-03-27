**Example 1: 拉取云存用户列表**



Input: 

```
tccli iotexplorer DescribeCloudStorageUsers --cli-unfold-argument  \
    --DeviceName sdfsdf \
    --Offset 0 \
    --Limit 10 \
    --ProductId lsdjfjf
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Users": [
            {
                "UserId": "dfsdf"
            }
        ],
        "RequestId": "sdfdsfesdsf"
    }
}
```

