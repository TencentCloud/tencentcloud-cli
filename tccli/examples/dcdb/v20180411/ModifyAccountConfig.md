**Example 1: 修改账号最大连接数**

修改实例tdsqlshard-lfkz0geb下，账号user_test的最大连接数为 123

Input: 

```
tccli dcdb ModifyAccountConfig --cli-unfold-argument  \
    --InstanceId tdsqlshard-lfkz0geb \
    --UserName user_test \
    --Host % \
    --Configs.0.Config max_user_connections \
    --Configs.0.Value 123
```

Output: 
```
{
    "Response": {
        "RequestId": "3c200ca1-4cac-480e-9f58-574a35a7b895"
    }
}
```

