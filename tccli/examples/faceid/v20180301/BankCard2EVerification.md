**Example 1: 认证通过示例**

校验姓名和银行卡号的真实性和一致性。

Input: 

```
tccli faceid BankCard2EVerification --cli-unfold-argument  \
    --Name 韦小宝 \
    --BankCard ' 6225768888888888'
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

**Example 2: 认证不通过示例**

传入错误持卡人信息，校验姓名和银行卡号的真实性和一致性。

Input: 

```
tccli faceid BankCard2EVerification --cli-unfold-argument  \
    --Name 韦小宝 \
    --BankCard ' 6226090210146748'
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

