**Example 1: 创建访问密钥**



Input: 

```
tccli cam CreateAccessKey --cli-unfold-argument  \
    --TargetUin 100013065917
```

Output: 
```
{
    "Response": {
        "AccessKey": {
            "AccessKeyId": "AKID***",
            "SecretAccessKey": "iDVd***",
            "Status": "Active",
            "CreateTime": "2020-03-03 18:00:26"
        },
        "RequestId": "f8423e9b-a7da-488d-9539-333f1955ca78"
    }
}
```

