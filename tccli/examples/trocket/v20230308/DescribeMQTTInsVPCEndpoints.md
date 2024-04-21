**Example 1: 样例**

样例

Input: 

```
tccli trocket DescribeMQTTInsVPCEndpoints --cli-unfold-argument  \
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

