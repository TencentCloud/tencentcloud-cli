**Example 1: 实例详情**



Input: 

```
tccli iotexplorer DescribeActivateDevice --cli-unfold-argument  \
    --InstanceId ins-BoSq3gRJ27
```

Output: 
```
{
    "Response": {
        "Data": {
            "InstanceId": "ins-DGAFvpuVF7",
            "InstanceType": 0,
            "DeviceActivationDetails": {
                "TotalDeviceNum": 650,
                "UsedDeviceNum": 18,
                "TotalNormalLicense": 600,
                "UsedNormalLicense": 19,
                "TotalBluetoothLicense": 0,
                "UsedBluetoothLicense": 0
            },
            "RegisteredDeviceType": {
                "NormalDeviceNum": 0,
                "GatewayDeviceNum": 0,
                "SubDeviceNum": 0
            },
            "RegisteredDeviceNetType": {
                "NormalDeviceNum": 0,
                "BluetoothDeviceNum": 0
            }
        },
        "RequestId": "ef9ec631-7337-5059arty-tl3o5wefr5"
    }
}
```

