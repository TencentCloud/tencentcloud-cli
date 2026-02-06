**Example 1: 获取账号组信息**



Input: 

```
tccli bh DescribeAccountGroups --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AccountGroupSet": [
            {
                "Id": 43,
                "Name": "钉钉",
                "Source": 1001,
                "Status": 0,
                "IdPath": "243.534.2344",
                "NamePath": "全网账号.测试.开发",
                "ParentId": 534,
                "UserTotal": 34
            }
        ],
        "RequestId": "cf85w9eee-b651-4ff3q-9b49-173f9f55733f"
    }
}
```

