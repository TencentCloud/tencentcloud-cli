**Example 1: 刪除实例账号**

刪除实例账号

Input: 

```
tccli mongodb DeleteAccountUser --cli-unfold-argument  \
    --InstanceId cmgo-9d0p**** \
    --UserName test_user \
    --MongoUserPassword Abc@123
```

Output: 
```
{
    "Response": {
        "FlowId": 0,
        "RequestId": "1df930fb-eb7e-4e3f-bcab-15a1aa5fede0"
    }
}
```

