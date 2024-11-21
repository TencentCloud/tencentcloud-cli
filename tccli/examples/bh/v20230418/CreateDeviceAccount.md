**Example 1: 新建主机账号**

新建主机账号

Input: 

```
tccli bh CreateDeviceAccount --cli-unfold-argument  \
    --Account ubuntu \
    --DeviceId 1
```

Output: 
```
{
    "Response": {
        "Id": 1,
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082"
    }
}
```

