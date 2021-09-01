**Example 1: 更新产品信息**

更新产品信息

Input: 

```
tccli iot UpdateProduct --cli-unfold-argument  \
    --ProductId iot-4e0wsxpi \
    --Name 名称 \
    --Description 描述 \
    --DataTemplate.0.Number.Name Temperature \
    --DataTemplate.0.Number.Desc 温度 \
    --DataTemplate.0.Number.Mode rw \
    --DataTemplate.0.Number.Range 0 50.1 \
    --DataTemplate.1.String.Name Message \
    --DataTemplate.1.String.Desc 留言 \
    --DataTemplate.1.String.Mode rw \
    --DataTemplate.1.String.Range 0 1024 \
    --DataTemplate.2.Enum.Name Weather \
    --DataTemplate.2.Enum.Desc 天气 \
    --DataTemplate.2.Enum.Mode r \
    --DataTemplate.2.Enum.Range Sunny Rainy \
    --DataTemplate.3.Bool.Name Lock \
    --DataTemplate.3.Bool.Desc 锁 \
    --DataTemplate.3.Bool.Mode rw \
    --DataTemplate.3.Bool.Range true false
```

Output: 
```
{
    "Response": {
        "RequestId": "b78d722c-c32c-4108-b9d8-a75be705e227",
        "Product": {
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
            "ProductId": "iot-4e0wsxpi",
            "ProductKey": "mqtt-1ec1b84pe",
            "AppId": 1251006373,
            "Name": "名称",
            "Description": "描述",
            "Domain": "mqtt-1ec1b84pe.ap-guangzhou.mqtt.tencentcloudmq.com",
            "Standard": 3,
            "AuthType": 1,
            "DataProtocol": "template",
            "Deleted": 0,
            "Message": "",
            "CreateTime": "2018-03-12 15:59:51",
            "UpdateTime": "2018-07-05 21:02:06",
            "Username": "AKIDhFcnnbEo8HoGqGeWNSM5d0BC0b2O4aKs",
            "Password": "E4udpi9C7GrfuMGDCVa5qQ20k6eVlyCSbroIG0eF7Gs="
        }
    }
}
```

