**Example 1: 查询当前实例的全部账户信息**

查询当前实例的全部账户信息

Input: 

```
tccli mongodb DescribeAccountUsers --cli-unfold-argument  \
    --InstanceId cmgo-9d0p****
```

Output: 
```
{
    "Response": {
        "Users": [
            {
                "UserName": "test_user",
                "AuthRole": [
                    {
                        "Mask": 0,
                        "NameSpace": "collection"
                    }
                ],
                "CreateTime": "2022-03-04 19:00:00",
                "UpdateTime": "2022-03-04 19:00:00",
                "UserDesc": "测试账号"
            }
        ],
        "RequestId": "1df930fb-eb7e-4e3f-bcab-15a1aa5fede0"
    }
}
```

