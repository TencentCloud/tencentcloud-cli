**Example 1: 示例**

示例

Input: 

```
tccli trocket DescribeMQTTInsPublicEndpoints --cli-unfold-argument  \
    --InstanceId mqtt-gn8qoq3z
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Bandwidth": 2,
        "Endpoints": [
            {
                "Host": "mqtt-gn8qoq3z-cd.mqtt.public.tencenttdmq.com",
                "Port": 22,
                "SubnetId": null,
                "Type": "mqtt-ws",
                "Url": null,
                "VpcId": null
            },
            {
                "Host": "mqtt-gn8qoq3z-cd.mqtt.public.tencenttdmq.com",
                "Port": 11,
                "SubnetId": null,
                "Type": "mqtt-tcp",
                "Url": null,
                "VpcId": null
            },
            {
                "Host": "mqtt-gn8qoq3z-cd.mqtt.public.tencenttdmq.com",
                "Port": 33,
                "SubnetId": null,
                "Type": "mqtt-tls",
                "Url": null,
                "VpcId": null
            }
        ],
        "InstanceId": "mqtt-gn8qoq3z",
        "RequestId": "3891d712-94f7-4d03-9420-fae4fa3a61ea",
        "Rules": [
            {
                "Allow": true,
                "IpRule": "0.0.0.0/0",
                "Remark": ""
            }
        ],
        "Status": "NORMAL"
    }
}
```

