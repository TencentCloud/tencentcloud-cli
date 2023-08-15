**Example 1: 同步调用设备行为**

云端调用后，设备端上报`$thing/up/action/TOIDHQ3AOQ/light1`
```
{
	"method": "action_reply",
	"clientToken": "0fe1260b7a724b67ba873ca7df703e0d",
	"code": 0,
	"response": { "brightness": 1, "color": 1, "light_switch": 1 },
	"status": "succ"
}
```

Input: 

```
tccli iotexplorer CallDeviceActionSync --cli-unfold-argument  \
    --DeviceName light1 \
    --InputParams {"vol":3} \
    --ActionId actid \
    --ProductId TOIDHQ3AOQ
```

Output: 
```
{
    "Response": {
        "ClientToken": "0fe1260b7a724b67ba873ca7df703e0d",
        "OutputParams": "{\"brightness\":1,\"color\":1,\"light_switch\":1}",
        "RequestId": "235fe48b-0c31-4a7c-aaf6-83ba3e9s4bcf",
        "Status": "succ"
    }
}
```

**Example 2: 同步调用设备行为，设备不在线。**

当设备不在线或未订阅相关 topic 时，设备返回情况如样例所示。

Input: 

```
tccli iotexplorer CallDeviceActionSync --cli-unfold-argument  \
    --DeviceName light1 \
    --InputParams {"brightness":3} \
    --ActionId actid \
    --ProductId TOIDHQ3AOQ
```

Output: 
```
{
    "Response": {
        "ClientToken": "",
        "OutputParams": "",
        "RequestId": "b2621fc1-d6d9-4929-af0b-3fb0e919658a",
        "Status": "FailedOperation.ActionUnreachable|动作消息不可达"
    }
}
```

**Example 3: 同步调用设备行为，设备超时**

当设备响应时间过长时，设备返回情况如样例所示。

Input: 

```
tccli iotexplorer CallDeviceActionSync --cli-unfold-argument  \
    --DeviceName light1 \
    --InputParams {"brightness":3} \
    --ActionId actid \
    --ProductId TOIDHQ3AOQ
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.Timeout",
            "Message": "调用超时"
        },
        "RequestId": "b1de7dcf-5029-4d70-b6b5-d1ad0f785552"
    }
}
```

