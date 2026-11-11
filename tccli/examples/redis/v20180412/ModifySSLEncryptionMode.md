**Example 1: 更改实例传输加密模式为强制加密**

更改实例为强制传输加密模式，非加密连接会断开

Input: 

```
tccli redis ModifySSLEncryptionMode --cli-unfold-argument  \
    --InstanceId crs-kb5f4wul \
    --EncryptionMode required
```

Output: 
```
{
    "Response": {
        "TaskId": 2031422420,
        "RequestId": "ca5a6781-6dd2-459b-9989-978477be7e28"
    }
}
```

