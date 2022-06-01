**Example 1: 查询用户组列表**

查询用户组列表

Input: 

```
tccli dasb DescribeUserGroups --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "GroupSet": [
            {
                "Id": 1,
                "Name": "研发一部"
            }
        ],
        "RequestId": "xx"
    }
}
```

