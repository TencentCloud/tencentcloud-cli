**Example 1: 认证通过示例 [前往调试工具]（https://console.cloud.tencent.com/api/explorer?Product=faceid&Version=2018-03-01&Action=BankCardVerification&Sig**

认证通过场景

Input: 

```
tccli faceid BankCardVerification --cli-unfold-argument  \
    --IdCard 440111201903211111 \
    --Name 张三 \
    --BankCard 6222222222222222222
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

**Example 2: 认证失败示例 [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=faceid&Version=2018-03-01&Action=BankCardVerification&Sig**

认证失败场景

Input: 

```
tccli faceid BankCardVerification --cli-unfold-argument  \
    --IdCard 440111201903211111 \
    --Name 张三 \
    --BankCard 6222222222222222222
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

