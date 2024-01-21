**Example 1: 示例**

示例

Input: 

```
tccli trocket DescribeMQTTInsVPCEndpoints --cli-unfold-argument  \
    --InstanceId mqtt-47ka4rdr
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Endpoints": [
            {
                "Host": "mqtt-47ka4rdr-cd-qcloud.mqtt.tencenttdmq.com",
                "Port": 1883,
                "SubnetId": null,
                "Type": "mqtt-tcp",
                "Url": "mqtt-47ka4rdr-cd-qcloud.mqtt.tencenttdmq.com:1883",
                "VpcId": null
            },
            {
                "Host": "mqtt-47ka4rdr-cd-qcloud.mqtt.tencenttdmq.com",
                "Port": 8888,
                "SubnetId": null,
                "Type": "mqtt-ws",
                "Url": "mqtt-47ka4rdr-cd-qcloud.mqtt.tencenttdmq.com:8888",
                "VpcId": null
            }
        ],
        "RequestId": "31911506-4e35-45b6-8261-a51bf3d85bd5"
    }
}
```

