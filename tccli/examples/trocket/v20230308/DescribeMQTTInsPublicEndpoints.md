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
                "Host": "mqttproxy-gn8qoq3z-gz-public.mqtt.tencenttdmq.com",
                "Port": 8888,
                "SubnetId": null,
                "Type": "mqtt-ws",
                "Url": "mqttproxy-gn8qoq3z-gz-public.mqtt.tencenttdmq.com:8888",
                "VpcId": null
            },
            {
                "Host": "mqttproxy-gn8qoq3z-gz-public.mqtt.tencenttdmq.com",
                "Port": 1883,
                "SubnetId": null,
                "Type": "mqtt-tcp",
                "Url": "mqttproxy-gn8qoq3z-gz-public.mqtt.tencenttdmq.com:1883",
                "VpcId": null
            },
            {
                "Host": "mqttproxy-gn8qoq3z-gz-public.mqtt.tencenttdmq.com",
                "Port": 8883,
                "SubnetId": null,
                "Type": "mqtt-tls",
                "Url": "mqttproxy-gn8qoq3z-gz-public.mqtt.tencenttdmq.com:8883",
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

