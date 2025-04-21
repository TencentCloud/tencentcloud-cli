**Example 1: 查询账户分组下的用户个数**

查询账户分组下的用户个数

Input: 

```
tccli ioa DescribeAccountGroupsUserTotal --cli-unfold-argument  \
    --AccountGroupIds 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Item": [
                {
                    "UserTotal": 0,
                    "AccountGroupId": 0
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

