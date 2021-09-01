**Example 1: 重置密码**



Input: 

```
tccli bm ResetDevicePassword --cli-unfold-argument  \
    --InstanceIds cpm-xxx0 cpm-xxx1 cpm-xxx2 \
    --Password newpasswd
```

Output: 
```
{
    "Response": {
        "TaskId": 123,
        "RequestId": "3f02fb0c-f782-4cef-9007-d63c68146e39"
    }
}
```

