**Example 1: 创建一个预付费专业版实例**

创建一个预付费专业版实例

Input: 

```
tccli ckafka CreateInstancePre --cli-unfold-argument  \
    --InstanceName ckafka测试 \
    --VpcId vpc-rmcgxxxx \
    --SubnetId subnet-mnzcxxxx \
    --ZoneId 450001 \
    --Period 1m \
    --RenewFlag 0 \
    --InstanceType 1 \
    --KafkaVersion 2.4.1 \
    --SpecificationsType profession \
    --DiskSize 200 \
    --BandWidth 20 \
    --Partition 400 \
    --DiskType CLOUD_BASIC \
    --PublicNetworkMonthly 0 \
    --CustomSSLCertId TPNd2oBB
```

Output: 
```
{
    "Response": {
        "Result": {
            "Data": {
                "DealNameInstanceIdMapping": [
                    {
                        "DealName": "20251204581021815942281",
                        "InstanceIdList": [
                            "ckafka-ma4ab5n5"
                        ]
                    }
                ],
                "DealNames": [
                    "20251204581021815942281"
                ],
                "FlowId": 0,
                "InstanceId": "ckafka-ma4ab5n5"
            },
            "ReturnCode": "0",
            "ReturnMessage": "ok"
        },
        "RequestId": "8c8050a7-ea8d-44f1-a00e-c09cd673afa3"
    }
}
```

