**Example 1: 设置smtp密码**

设置smtp密码：包含新增和修改密码

Input: 

```
tccli ses UpdateEmailSmtpPassWord --cli-unfold-argument  \
    --Password 123 \
    --EmailAddress abc@ef.com
```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

