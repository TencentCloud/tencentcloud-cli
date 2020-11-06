**Example 1: 重置密码**

重置密码

Input: 

```
tccli iot AppResetPassword --cli-unfold-argument  \
    --AccessToken xxx \
    --OldPassword oldpassword \
    --NewPassword newpassword
```

Output: 
```
{
    "Response": {
        "RequestId": "6b07242c-dd95-420f-9ab2-032eba5a49f0"
    }
}
```

