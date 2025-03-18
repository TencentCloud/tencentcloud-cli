**Example 1: 样例**

样例

Input: 

```
tccli mqtt DescribeInsVPCEndpoints --cli-unfold-argument  \
    --InstanceId mqtt-25zqb75a
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Endpoints": [
            {
                "Host": "mqtt-25zqb75a-qy.mqtt.qcloud.tencenttdmq.com",
                "Ip": "10.0.0.25",
                "Port": 1883,
                "SubnetId": "subnet-fr9ez60m",
                "Type": "mqtt-tcp",
                "Url": "mqtt-25zqb75a-qy.mqtt.qcloud.tencenttdmq.com:1883",
                "VpcId": "vpc-35wk4c6h"
            },
            {
                "Host": "mqtt-25zqb75a-qy.mqtt.qcloud.tencenttdmq.com",
                "Ip": "10.0.0.25",
                "Port": 8888,
                "SubnetId": "subnet-fr9ez60m",
                "Type": "mqtt-ws",
                "Url": "mqtt-25zqb75a-qy.mqtt.qcloud.tencenttdmq.com:8888",
                "VpcId": "vpc-35wk4c6h"
            }
        ],
        "RequestId": "4313484d-47c1-4fc8-b402-f997d2ba7256"
    }
}
```

**Example 2: 示例**

示例

Input: 

```
tccli mqtt DescribeInsVPCEndpoints --cli-unfold-argument  \
    --InstanceId mqtt-g4r4x85z
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Endpoints": [
            {
                "Host": "mqtt-g4r4x85z-cd-vpc.mqtt.tencenttdmq.com",
                "Ip": "127.0.0.1",
                "Port": 1883,
                "SubnetId": null,
                "Type": "mqtt-tcp",
                "Url": "mqtt-g4r4x85z-cd-vpc.mqtt.tencenttdmq.com:1883",
                "VpcId": null
            },
            {
                "Host": "mqtt-g4r4x85z-cd-vpc.mqtt.tencenttdmq.com",
                "Ip": "127.0.0.1",
                "Port": 8888,
                "SubnetId": null,
                "Type": "mqtt-ws",
                "Url": "mqtt-g4r4x85z-cd-vpc.mqtt.tencenttdmq.com:8888",
                "VpcId": null
            },
            {
                "Host": "mqtt-g4r4x85z-cd-vpc.mqtt.tencenttdmq.com",
                "Ip": "127.0.0.1",
                "Port": 8883,
                "SubnetId": null,
                "Type": "mqtt-tls",
                "Url": "mqtt-g4r4x85z-cd-vpc.mqtt.tencenttdmq.com:8883",
                "VpcId": null
            }
        ],
        "RequestId": "ec17e61f-7749-4192-bbc7-804b031a7da8"
    }
}
```

