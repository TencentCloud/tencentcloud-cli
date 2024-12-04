**Example 1: 添加用户**



Input: 

```
tccli ckafka CreateUser --cli-unfold-argument  \
    --InstanceId ckafka-test \
    --Name yourname \
    --Password Password
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
        "RequestId": "8bdec3bf-585d-4129-9a87-5a7813797c1f"
    }
}
```

