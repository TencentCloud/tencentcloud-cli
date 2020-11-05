**Example 1: Modifying account remarks**



Input: 

```
tccli sqlserver ModifyAccountRemark --cli-unfold-argument  \
    --InstanceId mssql-j8kv137v\
    --Accounts.0.UserName test\
    --Accounts.0.Remark testRemark
```

Output: 
```
{
    "Response": {
        "RequestId": "4be5990d-a4b5-49dc-b2b4-e713b6aa7ba3"
    }
}
```

