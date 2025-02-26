**Example 1: 申请创建客户账户**

申请创建客户账户

Input: 

```
tccli intlpartnersmgt CreateAccount --cli-unfold-argument  \
    --Extended for personal \
    --CountryCode 852 \
    --Area HK \
    --PhoneNum 18888888888 \
    --AccountType business \
    --Mail account@qq.com \
    --Password ABCabc123! \
    --ConfirmPassword ABCabc123 \
    --VerifyCode 364928
```

Output: 
```
{
    "Response": {
        "Uin": "200000123456",
        "RequestId": "a9e390a7-a1af-42cd-8178-13bd046337a7"
    }
}
```

