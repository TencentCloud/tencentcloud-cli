**Example 1: 查询**



Input: 

```
tccli cdwdoris DescribeUserPolicy --cli-unfold-argument  \
    --InstanceId abc \
    --UserName abc \
    --PassWord abc \
    --WhiteHost abc
```

Output: 
```
{
    "Response": {
        "AccountInfo": {
            "UserName": "abc",
            "Host": "abc",
            "UserDescription": "abc"
        },
        "Permissions": [
            {
                "GlobalPermissions": [
                    "abc"
                ],
                "DatabasePermissions": [
                    {
                        "DatabaseName": "abc",
                        "Permissions": [
                            "abc"
                        ]
                    }
                ],
                "TablePermissions": [
                    {
                        "TableName": "abc",
                        "Permissions": [
                            "abc"
                        ]
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

