**Example 1: 修改密码**



Input: 

```
tccli ckafka ModifyPassword --cli-unfold-argument  \
    --InstanceId ckafka-test \
    --Name name \
    --Password 1 \
    --PasswordNew 2
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok",
            "Data": null
        },
        "RequestId": "21c3d702-ae87-4a2a-a51b-b3d4516f121a"
    }
}
```

