**Example 1: 重置mssql-njj2mtpl的账户密码**



Input: 

```
tccli sqlserver ResetAccountPassword --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl \
    --Accounts.0.UserName test_user_4 \
    --Accounts.0.Password 1234qwer()
```

Output: 
```
{
    "Response": {
        "RequestId": "aa77bb20-7522-4b1e-bc0f-ad5d82790b17",
        "FlowId": 30457
    }
}
```

