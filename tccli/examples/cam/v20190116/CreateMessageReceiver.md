**Example 1: 创建消息接收人**

创建消息接收人

Input: 

```
tccli cam CreateMessageReceiver --cli-unfold-argument  \
    --Name 用户 \
    --Remark 添加消息接收人 \
    --CountryCode 86 \
    --PhoneNumber 132****4539 \
    --Email 57****@qq.com
```

Output: 
```
{
    "Response": {
        "RequestId": "f709ad6e-991f-49bb-aaaa-c354e434343434"
    }
}
```

