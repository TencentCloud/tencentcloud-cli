**Example 1: 示例**



Input: 

```
tccli es DescribeServerlessSpaceUser --cli-unfold-argument  \
    --SpaceId abc \
    --Offset 0 \
    --Limit 0 \
    --UserNames abc \
    --UserTypes 0 \
    --PrivilegeTypes 0
```

Output: 
```
{
    "Response": {
        "ServerlessSpaceUsers": [
            {
                "Username": "abc",
                "Password": "abc",
                "CreateTime": "abc",
                "Status": 0,
                "IndicesScope": [
                    "abc"
                ],
                "PrivilegeType": 0
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

