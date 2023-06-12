**Example 1: 添加邮件发送联系人信息**

添加邮件发送联系人信息。

Input: 

```
tccli dbbrain AddUserContact --cli-unfold-argument  \
    --Name 张三 \
    --ContactInfo test@qq.com \
    --Product mysql
```

Output: 
```
{
    "Response": {
        "Id": 1,
        "RequestId": "77db16d7-bbe8-48a7-868b-ed776a96f1ab"
    }
}
```

