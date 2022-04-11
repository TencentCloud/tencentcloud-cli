**Example 1: 设置产品数据模板**

设置产品的数据模板配置

Input: 

```
tccli iotexplorer ModifyModelDefinition --cli-unfold-argument  \
    --ModelSchema {"version":"1.0","profile":{"productID":"9IEQWQY47W"},"properties":[{"id":"power_switch","name":"电灯开关","desc":"控制电灯开灭","required":true,"mode":"rw","define":{"type":"bool","mapping":{"0":"关","1":"开"}}},{"id":"color","name":"颜色1","required":false,"desc":"灯光颜色","mode":"rw","define":{"type":"enum","mapping":{"0":"Red","1":"Green","2":"Blue"}}},{"id":"brightness","name":"颜色","desc":"灯光颜色","mode":"rw","define":{"type":"int","unit":"%","step":"1","min":"0","max":"100"}},{"id":"name","name":"灯位置名称","desc":"灯位置名称：书房、客厅等","mode":"rw","required":true,"define":{"type":"string","min":"0","max":"64"}}],"events":[{"id":"status_report","name":"DeviceStatus","desc":"Report the device status我是中文","type":"info","required":true,"params":[{"id":"status","name":"running_state","desc":"Report current device running state","define":{"type":"bool","mapping":{"0":"normal","1":"fault"}}},{"id":"message","name":"Message","desc":"Some extra message","define":{"type":"string","min":"0","max":"64"}}]},{"id":"low_voltage","name":"LowVoltage","desc":"Alert for device voltage is low","type":"alert","required":false,"params":[{"id":"voltage","name":"Voltage","desc":"Current voltage","define":{"type":"float","unit":"V","step":"1","min":"0.0","max":"24.0"}}]},{"id":"hardware_fault","name":"Hardware_fault","desc":"Report hardware fault","type":"fault","required":false,"params":[{"id":"name","name":"Name","desc":"Name like: memory,tf card, censors ...","define":{"type":"string","min":"0","max":"64"}},{"id":"error_code","name":"Error_Code","desc":"Error code for fault","define":{"type":"int","unit":"","step":"1","min":"0","max":"2000"}}]}]} \
    --ProductId LJ0INDNU7U
```

Output: 
```
{
    "Response": {
        "RequestId": "5c982342-fb08-4fac-8e70-f63834667b52"
    }
}
```

