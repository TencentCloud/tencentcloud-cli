**Example 1: 获取所有类型的子账号列表**

获取所有类型的子账号列表

Input: 

```
tccli cam ListAccounts --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "IsTruncated": false,
        "Marker": "",
        "Users": [
            {
                "ConsoleLogin": 1,
                "CountryCode": "86",
                "CreateTime": "2022-11-23 17:07:28",
                "Email": "gavi*******@tencent.com",
                "Name": "gavi*******@tencent.com",
                "PhoneNum": "132****0828",
                "Remark": "",
                "Uid": 906949110,
                "Uin": 0,
                "UserType": "Owner"
            }
        ],
        "RequestId": "e89738b3-7eb3-46fe-be37-7d3210625d78"
    }
}
```

