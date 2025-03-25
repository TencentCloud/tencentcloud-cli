**Example 1: 重置密码**

修改用户密码

Input: 

```
tccli cdwpg ResetAccountPassword --cli-unfold-argument  \
    --InstanceId cdwpg-dfsgdxxxxx \
    --UserName admin \
    --NewPassword cdwpg123456
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "RequestId": "2dd36228-8290-43b7-b83c-ff71cf6f5fd4"
    }
}
```

