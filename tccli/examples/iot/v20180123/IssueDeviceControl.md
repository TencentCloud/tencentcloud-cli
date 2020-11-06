**Example 1: 下发设备控制指令**

下发设备控制指令

Input: 

```
tccli iot IssueDeviceControl --cli-unfold-argument  \
    --ProductId iot-4e0wsxpi \
    --DeviceName device1 \
    --ControlData {"light":"on"}
```

Output: 
```
{
    "Response": {
        "RequestId": "ed6fdebb-7cd3-45a1-b0b5-47fef22d6f5d"
    }
}
```

