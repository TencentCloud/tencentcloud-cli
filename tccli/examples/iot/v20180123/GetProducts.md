**Example 1: 获取产品列表**

获取产品列表

Input: 

```
tccli iot GetProducts --cli-unfold-argument  \
    --Offset 0 \
    --Length 2
```

Output: 
```
{
    "Response": {
        "RequestId": "e0cc5d58-3664-4aa7-9523-629e114a17a4",
        "Products": [
            {
                "ProductId": "iot-5aawn3i8",
                "ProductKey": "mqtt-5por2uztc",
                "AppId": 1251006373,
                "Name": "字符串3",
                "Description": "字符串",
                "Domain": "mqtt-5por2uztc.ap-guangzhou.mqtt.tencentcloudmq.com",
                "AuthType": 1,
                "DataProtocol": "native",
                "Deleted": 0,
                "Message": "",
                "CreateTime": "2018-06-20 15:34:07"
            },
            {
                "ProductId": "iot-gk2hv9pq",
                "ProductKey": "mqtt-1e86or9j0",
                "AppId": 1251006373,
                "Name": "字符串2",
                "Description": "字符串",
                "Domain": "mqtt-1e86or9j0.ap-guangzhou.mqtt.tencentcloudmq.com",
                "AuthType": 1,
                "DataProtocol": "native",
                "Deleted": 0,
                "Message": "",
                "CreateTime": "2018-06-20 15:11:19"
            }
        ],
        "Total": 8
    }
}
```

