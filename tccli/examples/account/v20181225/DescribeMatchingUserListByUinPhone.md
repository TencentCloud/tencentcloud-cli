**Example 1: 通过当前账号的UIN获取和这个账号安全手机相同的主账号用户列表**

通过当前账号的UIN获取和这个账号安全手机相同的主账号用户列表

Input: 

```
tccli account DescribeMatchingUserListByUinPhone --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "UserInfoList": [
            {
                "Uin": 100002034,
                "UserName": "test"
            }
        ],
        "RequestId": "e297543a-80de-4039-83c8-9d35d4545"
    }
}
```

