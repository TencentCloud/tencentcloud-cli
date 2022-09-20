**Example 1: 查询当前实例的全部账户信息；**



Input: 

```
tccli mongodb DescribeAccountUsers --cli-unfold-argument  \
    --InstanceId xx
```

Output: 
```
{
    "Response": {
        "Users": [
            {
                "UserName": "xx",
                "AuthRole": [
                    {
                        "Mask": 0,
                        "NameSpace": "xx"
                    }
                ],
                "UserDesc": "xx",
                "UpdateTime": "xx",
                "CreateTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

