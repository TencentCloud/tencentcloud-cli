**Example 1: 透传Payload批量下发至设备**



Input: 

```
tccli iotexplorer BatchPublishMessage --cli-unfold-argument  \
    --ProductId XXV7WNTR4F \
    --DeviceNames dev_1 \
    --Topic XXV7WNTR4F/${deviceName}/data \
    --Payload hello
```

Output: 
```
{
    "Response": {
        "Failures": [
            {
                "DeviceName": "dev_4",
                "ErrCode": 23102,
                "ErrMsg": "push: device offline (qos0): push: device unreachable",
                "Status": "OFFLINE"
            }
        ],
        "SuccessCount": 3,
        "Total": 4,
        "RequestId": "d6120860-b5a0-4cb7-a0a7-8de054461ef3"
    }
}
```

**Example 2: 将接收到的经过业务系统base64编码后的Payload进行二进制编码后批量下发至设备**



Input: 

```
tccli iotexplorer BatchPublishMessage --cli-unfold-argument  \
    --ProductId XXV7WNTR4F \
    --DeviceNames dev_1 \
    --Topic XXV7WNTR4F/${deviceName}/data \
    --Payload MQ== \
    --Qos 1 \
    --PayloadEncoding base64
```

Output: 
```
{
    "Response": {
        "Failures": [],
        "SuccessCount": 2,
        "Total": 2,
        "RequestId": "5522bd8b-d860-45c3-86cb-0c829fabaace"
    }
}
```

