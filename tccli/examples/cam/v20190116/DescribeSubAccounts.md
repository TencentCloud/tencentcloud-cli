**Example 1: 通过子用户UIN列表查询子用户**



Input: 

```
tccli cam DescribeSubAccounts --cli-unfold-argument  \
    --FilterSubAccountUin 200000548558
```

Output: 
```
{
    "Response": {
        "SubAccounts": [
            {
                "Remark": "xx",
                "Uid": 1,
                "Uin": 1,
                "UserType": 1,
                "CreateTime": "2020-09-22 00:00:00",
                "Name": "xx",
                "LastLoginIp": "",
                "LastLoginTime": null
            }
        ],
        "RequestId": "xx"
    }
}
```

