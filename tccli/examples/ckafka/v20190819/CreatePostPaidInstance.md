**Example 1: 创建后付费专业版实例**

创建硬盘大小 200GB，峰值带宽 20MB/s 的专业版后付费实例

Input: 

```
tccli ckafka CreatePostPaidInstance --cli-unfold-argument  \
    --InstanceName test55 \
    --VpcId vpc-rmcgxxxx \
    --SubnetId subnet-mnzcxxxx \
    --ZoneId 450001 \
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

**Example 2: 批量创建后付费专业版实例**

同时创建三个后付费专业版实例

Input: 

```
tccli ckafka CreatePostPaidInstance --cli-unfold-argument  \
    --InstanceName test58 \
    --VpcId vpc-rmcg5cpf \
    --SubnetId subnet-mnzcs7gk \
    --KafkaVersion 2.4.2 \
    --SpecificationsType profession \
    --BandWidth 20 \
    --DiskSize 200 \
    --Partition 400 \
    --TopicNum 200 \
    --ZoneId 450001 \
    --InstanceNum 3 \
    --PublicNetworkMonthly 12
```

Output: 
```
{
    "Response": {
        "RequestId": "cda79237-6424-482a-b2d2-97d4853b33b4",
        "Result": {
            "Data": {
                "DealNameInstanceIdMapping": [
                    {
                        "DealName": "20230608002033915320000",
                        "InstanceIdList": [
                            "ckafka-bz4dxxxx",
                            "ckafka-o9gdxxxx",
                            "ckafka-aj5gxxxx"
                        ]
                    }
                ],
                "DealNames": [
                    "20230608002033915320000"
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

**Example 3: 创建后付费多可用区专业版实例**

创建一个三可用区的专业版实例

Input: 

```
tccli ckafka CreatePostPaidInstance --cli-unfold-argument  \
    --InstanceName test55 \
    --VpcId vpc-rmcgxxxx \
    --SubnetId subnet-mnzcxxxx \
    --ZoneId 450001 \
    --InstanceType 1 \
    --KafkaVersion 1.1.1 \
    --SpecificationsType profession \
    --DiskSize 200 \
    --BandWidth 20 \
    --Partition 400 \
    --DiskType CLOUD_BASIC \
    --PublicNetworkMonthly 0 \
    --MultiZoneFlag True \
    --ZoneIds 450001 450002 450003
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

