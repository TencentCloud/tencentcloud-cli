**Example 1: 获取联系组信息**

获取联系组信息。

Input: 

```
tccli dbbrain DescribeAllUserGroup --cli-unfold-argument  \
    --Product mysql \
    --Names group1
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RequestId": "31dd9325-792f-4d76-89ad-ca8902cbe4d9",
        "Groups": [
            {
                "MemberCount": 0,
                "Id": 1,
                "Name": "group1"
            },
            {
                "MemberCount": 2,
                "Id": 2,
                "Name": "group11"
            }
        ]
    }
}
```

