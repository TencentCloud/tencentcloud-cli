**Example 1: 创建访问密钥**



Input: 

```
tccli cam CreateAccessKey --cli-unfold-argument  \
    --TargetUin 123456
```

Output: 
```
{
    "Response": {
        "AccessKey": {
            "AccessKeyId": "AKID8GFED7s****QrFXkmb",
            "SecretAccessKey": "iDVjy****tNzX",
            "Status": "Active",
            "CreateTime": "2020-03-03 18:00:26"
        },
        "RequestId": "f8423e9b-a7da-488d-9539-333f1955ca78"
    }
}
```

