**Example 1: 重置密码**

修改用户密码

Input: 

```
tccli cdwpg ResetAccountPassword --cli-unfold-argument  \
    --InstanceId cdwch-12345678 \
    --UserName test \
    --NewPassword cdwpg123456
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "RequestId": "abcdd"
    }
}
```

