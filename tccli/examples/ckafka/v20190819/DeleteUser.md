**Example 1: 删除用户**



Input: 

```
tccli ckafka DeleteUser --cli-unfold-argument  \
    --InstanceId ckafka-test \
    --Name name
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
        "RequestId": "c0f25f9c-4a80-48bb-ad2a-a5107041d486"
    }
}
```

