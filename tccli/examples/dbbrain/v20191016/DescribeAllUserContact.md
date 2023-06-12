**Example 1: 获取联系人信息**

获取联系人信息。

Input: 

```
tccli dbbrain DescribeAllUserContact --cli-unfold-argument  \
    --Product mysql \
    --Names zhangsan
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "Contacts": [
            {
                "Mail": "zhangsan@qq.com",
                "Id": 1,
                "Name": "zhangsan"
            },
            {
                "Mail": "zhangsan2@qq.com",
                "Id": 2,
                "Name": "zhangsan2"
            }
        ],
        "RequestId": "b2d08895-1cfe-48bc-b7f7-87fd7cb5d6f1"
    }
}
```

