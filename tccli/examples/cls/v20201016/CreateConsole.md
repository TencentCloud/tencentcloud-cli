**Example 1: 创建DataSight控制台实例**

创建DataSight控制台实例

Input: 

```
tccli cls CreateConsole --cli-unfold-argument  \
    --AccessMode public \
    --LoginMode 0 \
    --DomainPrefix datasight \
    --Accounts.0.UserName username \
    --Accounts.0.Password xxxxxxxx \
    --Accounts.0.SecretId secretid \
    --Accounts.0.SecretKey secretkey
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxx-xxxxx",
        "ConsoleId": "clsconsole-xxxxxxxx"
    }
}
```

