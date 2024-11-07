**Example 1: 认证通过示例**

输入银行卡号、姓名、开户证件号、开户手机号，校验信息的真实性和一致性。

Input: 

```
tccli faceid BankCard4EVerification --cli-unfold-argument  \
    --Name 韦小宝 \
    --BankCard 6225768888888888 \
    --Phone 16137688175 \
    --IdCard 11204416541220243X
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "认证通过",
        "RequestId": "74e742e8-f91d-49c3-9744-c20f3baca117"
    }
}
```

**Example 2: 认证不通过示例**

传入的有误的姓名信息，校验信息的真实性和一致性

Input: 

```
tccli faceid BankCard4EVerification --cli-unfold-argument  \
    --Name 韦小宝 \
    --BankCard 6226090210146748 \
    --Phone 16137688175 \
    --IdCard ' 11204416541220243X'
```

Output: 
```
{
    "Response": {
        "Result": "-6",
        "Description": "持卡人信息有误",
        "RequestId": "24fe7851-49e9-4a4a-ac1e-3bd5c09323fd"
    }
}
```

