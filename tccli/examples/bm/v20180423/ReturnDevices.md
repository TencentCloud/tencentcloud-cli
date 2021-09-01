**Example 1: 退还物理机**



Input: 

```
tccli bm ReturnDevices --cli-unfold-argument  \
    --InstanceIds cpm-xxx0 cpm-xxx1 cpm-xxx2
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

