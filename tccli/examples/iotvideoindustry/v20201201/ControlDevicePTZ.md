**Example 1: PTZ设备远程控制示例**



Input: 

```
tccli iotvideoindustry ControlDevicePTZ --cli-unfold-argument  \
    --DeviceId 34020000001180000036_34020000001320000092 \
    --Command left
```

Output: 
```
{
    "Response": {
        "RequestId": "e1b9e7ac-0989-4af9-a454-26f69d6997d9"
    }
}
```

