**Example 1: 修改账号配置**

修改账号配置

Input: 

```
tccli cynosdb ModifyAccountParams --cli-unfold-argument  \
    --ClusterId cynosdbmysql-xxxxxxxx \
    --Account.AccountName andy \
    --Account.Host % \
    --AccountParams.0.ParamName max_user_connections \
    --AccountParams.0.ParamValue 400
```

Output: 
```
{
    "Response": {
        "RequestId": "51169b54-61d4-4604-a07e-e519a5527923"
    }
}
```

