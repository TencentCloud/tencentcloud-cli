**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeInsPublicEndpoints --cli-unfold-argument  \
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
                "Port": 8888,
                "SubnetId": "subnet-1",
                "Type": "mqtt-ws",
                "Url": "mqtt-gn8qoq3z-cd.mqtt.public.tencenttdmq.com:8888",
                "VpcId": "vpc-1"
            },
            {
                "Host": "mqtt-gn8qoq3z-cd.mqtt.public.tencenttdmq.com",
                "Port": 1883,
                "SubnetId": "subnet-1",
                "Type": "mqtt-tcp",
                "Url": "mqtt-gn8qoq3z-cd.mqtt.public.tencenttdmq.com:1883",
                "VpcId": "vpc-1"
            },
            {
                "Host": "mqtt-gn8qoq3z-cd.mqtt.public.tencenttdmq.com",
                "Port": 8883,
                "SubnetId": "subnet-1",
                "Type": "mqtt-tls",
                "Url": "mqtt-gn8qoq3z-cd.mqtt.public.tencenttdmq.com:8883",
                "VpcId": "vpc-1"
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

