**Example 1: 银行卡三要素核验一致示例**



Input: 

```
tccli faceid BankCardVerification --cli-unfold-argument  \
    --IdCard 11204416541220243X \
    --Name 韦小宝 \
    --BankCard ' 6226090210146748'
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "认证通过",
        "RequestId": "a5fdb909-5ee6-43ff-a152-bb1b9744ee8b"
    }
}
```

**Example 2: 银行卡三要素核验不一致示例**



Input: 

```
tccli faceid BankCardVerification --cli-unfold-argument  \
    --IdCard ' 11204416541220243X' \
    --Name 韦小宝 \
    --BankCard ' 6225768888888888'
```

Output: 
```
{
    "Response": {
        "Result": "-1",
        "Description": "认证未通过",
        "RequestId": "89f695b2-18fd-44b6-bffc-96972052666f"
    }
}
```

