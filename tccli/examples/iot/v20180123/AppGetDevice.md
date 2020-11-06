**Example 1: 获取绑定设备信息**

获取绑定设备的基本信息与数据模板定义

Input: 

```
tccli iot AppGetDevice --cli-unfold-argument  \
    --AccessToken xxx \
    --ProductId iot-4e0wsxpi \
    --DeviceName abc
```

Output: 
```
{
    "Response": {
        "RequestId": "c01da37e-7419-44bc-a7fc-93c59ec1cc7a",
        "AppDevice": {
            "DeviceInfo": "{\"product\":\"iot-4e0wsxpi\",\"device\":\"abc\",\"sdk-ver\":\"2.3\",\"firm-ver\":\"LINUX_V1.0\",\"topic\":\"ota\\/update\\/iot-4e0wsxpi\\/abc\"}",
            "DataTemplate": [
                {
                    "Number": {
                        "Desc": "温度",
                        "Mode": "rw",
                        "Name": "Temperature",
                        "Range": [
                            0,
                            50.1
                        ]
                    },
                    "String": null,
                    "Enum": null,
                    "Bool": null
                },
                {
                    "String": {
                        "Desc": "留言",
                        "Mode": "rw",
                        "Name": "Message",
                        "Range": [
                            0,
                            1024
                        ]
                    },
                    "Number": null,
                    "Enum": null,
                    "Bool": null
                },
                {
                    "Enum": {
                        "Desc": "天气",
                        "Mode": "r",
                        "Name": "Weather",
                        "Range": [
                            "Sunny",
                            "Rainy"
                        ]
                    },
                    "Number": null,
                    "String": null,
                    "Bool": null
                },
                {
                    "Bool": {
                        "Desc": "锁",
                        "Mode": "rw",
                        "Name": "Lock",
                        "Range": [
                            true,
                            false
                        ]
                    },
                    "Number": null,
                    "String": null,
                    "Enum": null
                }
            ],
            "Region": "ap-guangzhou",
            "ProductId": "iot-4e0wsxpi",
            "DeviceName": "abc",
            "CreateTime": "2018-07-06 02:14:14",
            "UpdateTime": "2018-07-06 02:14:14",
            "DeviceId": "ap-guangzhou/iot-4e0wsxpi/abc",
            "AliasName": ""
        }
    }
}
```

