**Example 1: 认证通过示例 [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=faceid&Version=2018-03-01&Action=BankCard2EVerification&S**



Input: 

```
tccli faceid BankCard2EVerification --cli-unfold-argument  \
    --Name 张三\
    --BankCard 6222222222222222222
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "认证通过",
        "RequestId": "c6daaf7f-dbdc-4a9d-a20b-9a14ffdd8328"
    }
}
```

**Example 2: 认证不通过示例  [前往调试工具] (https://console.cloud.tencent.com/api/explorer?Product=faceid&Version=2018-03-01&Action=BankCard2EVerificatio**



Input: 

```
tccli faceid BankCard2EVerification --cli-unfold-argument  \
    --Name 张三\
    --BankCard 6222222222222222222
```

Output: 
```
{
    "Response": {
        "Result": "-4",
        "Description": "持卡人信息有误",
        "RequestId": "d668328c-7847-42d7-bdce-215ebadffd9b"
    }
}
```

