**Example 1: 切换用户身份**



Input: 

```
tccli cam ChangeTokenUser --cli-unfold-argument  \
    --TokenUin 100000009472 \
    --TokenOwnerUin 100000009472 \
    --TokenChangeUin 100000009473 \
    --TokenChangeOwnerUin 100000009473 \
    --Platform coding \
    --Type wx \
    --SaaSToken abcef \
    --ClientIP 1.1.1.1 \
    --ClientUA chrome
```

Output: 
```
{
    "Response": {
        "Key": "abcedf",
        "Uin": 100000009473,
        "OwnerUin": 100000009473,
        "ExpireTimestamp": 123456789,
        "RequestId": 0
    }
}
```

