**Example 1: 绑定成功示例**



Input: 

```
tccli account BindGoogleAndPreLoginForSaaS --cli-unfold-argument  \
    --ClientUA 127.0.0.1 \
    --Platform intlSaaSAvatar \
    --Password Mdsadgfoa= \
    --Mail test@gmail.com \
    --IdToken eyJhbGciOiJSx7Pgwyu7IzoA
```

Output: 
```
{
    "Response": {
        "ExpiredTime": "1735307671",
        "Key": "4e1b668233042905fbb5420ffa972948",
        "RequestId": "80d188d7-9194-4291-9676-249455da2bde",
        "Sid": "SaaSSidb1182796-03b9-3e39-0682-07aa4f362979",
        "Uin": 450600000015
    }
}
```

