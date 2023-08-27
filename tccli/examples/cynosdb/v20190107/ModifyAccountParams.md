**Example 1: 修改账号配置**

修改账号配置

Input: 

```
tccli cynosdb ModifyAccountParams --cli-unfold-argument  \
    --ClusterId cynosdbmysql-xxxxxxxx \
    --Account.AccountName test \
    --Account.Host % \
    --AccountParams.0.ParamName max_user_connections \
    --AccountParams.0.ParamValue 400
```

Output: 
```
{
    "Response": {
        "RequestId": "147706"
    }
}
```

