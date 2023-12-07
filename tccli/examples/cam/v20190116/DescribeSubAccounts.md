**Example 1: 通过子用户UIN列表查询子用户**

示例

Input: 

```
tccli cam DescribeSubAccounts --cli-unfold-argument  \
    --FilterSubAccountUin 100028732368
```

Output: 
```
{
    "Response": {
        "RequestId": "5b4d1725-5a30-4bd8-b36d-cfa0d1d4706b",
        "SubAccounts": [
            {
                "CreateTime": "2022-11-30 16:05:07",
                "LastLoginIp": "",
                "LastLoginTime": null,
                "Name": "testuser2",
                "Remark": "",
                "Uid": 14866045,
                "Uin": 100028732368,
                "UserType": 2
            }
        ]
    }
}
```

