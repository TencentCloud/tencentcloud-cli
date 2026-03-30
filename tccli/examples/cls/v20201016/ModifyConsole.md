**Example 1: 修改DataSight控制台实例**

修改DataSight控制台实例

Input: 

```
tccli cls ModifyConsole --cli-unfold-argument  \
    --ConsoleId clsconsole-xxxxxxxx \
    --DomainPrefix datasight \
    --AccessMode public \
    --LoginMode 0 \
    --Accounts.0.UserName username \
    --Accounts.0.Password xxxxxxxx \
    --Accounts.0.SecretId AKIDxxxxxxxxxCIAi4V \
    --Accounts.0.SecretKey xxxxxxxxxxx
```

Output: 
```
{
    "Response": {
        "ConsoleId": "clsconsole-xxxxxxxx",
        "RequestId": "xxxx-xxxx"
    }
}
```

