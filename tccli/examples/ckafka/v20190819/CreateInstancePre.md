**Example 1: 创建预付费实例**

创建硬盘大小 200GB，峰值带宽 20MB/s 的专业版预付费实例

Input: 

```
tccli ckafka CreateInstancePre --cli-unfold-argument  \
    --InstanceName test55 \
    --VpcId vpc-rmcgxxxx \
    --SubnetId subnet-mnzcxxxx \
    --ZoneId 450001 \
    --Period 1m \
    --RenewFlag 0 \
    --InstanceType 1 \
    --KafkaVersion 1.1.1 \
    --SpecificationsType profession \
    --DiskSize 200 \
    --BandWidth 20 \
    --Partition 400 \
    --DiskType CLOUD_BASIC \
    --PublicNetworkMonthly 0
```

Output: 
```
{
    "Response": {
        "RequestId": "323c3bbe-db79-48c3-9b76-63aacd65b169",
        "Result": {
            "Data": {
                "DealNameInstanceIdMapping": [
                    {
                        "DealName": "20230608002033899990000",
                        "InstanceIdList": [
                            "ckafka-mom5xxxx"
                        ]
                    }
                ],
                "DealNames": [
                    "2023060800203389990000"
                ],
                "FlowId": 0,
                "InstanceId": "ckafka-mom5xxxx"
            },
            "ReturnCode": "0",
            "ReturnMessage": "ok[apply ok]"
        }
    }
}
```

**Example 2: 创建预付费标准版实例**

创建预付费标准版实例，规格为入门型(general) ，周期为一个月

Input: 

```
tccli ckafka CreateInstancePre --cli-unfold-argument  \
    --InstanceName test57 \
    --VpcId vpc-rmcgxxxx \
    --SubnetId subnet-mnzcxxxx \
    --ZoneId 450001 \
    --Period 1m \
    --RenewFlag 2 \
    --InstanceType 1 \
    --KafkaVersion 1.1.1 \
    --SpecificationsType standard \
    --DiskSize 200 \
    --BandWidth 20 \
    --Partition 400
```

Output: 
```
{
    "Response": {
        "RequestId": "2050ebf8-e255-4b90-ba0c-2fe8465e821a",
        "Result": {
            "Data": {
                "DealNameInstanceIdMapping": [
                    {
                        "DealName": "20230608002033922780000",
                        "InstanceIdList": [
                            "ckafka-bz4dxxxx"
                        ]
                    }
                ],
                "DealNames": [
                    "20230608002033922780000"
                ],
                "FlowId": 0,
                "InstanceId": "ckafka-bz4dxxxx"
            },
            "ReturnCode": "0",
            "ReturnMessage": "ok[apply ok]"
        }
    }
}
```

