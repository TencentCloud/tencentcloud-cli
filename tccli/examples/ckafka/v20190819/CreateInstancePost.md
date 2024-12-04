**Example 1: 创建专业版实例**

创建峰值带宽为 20MB/s，硬盘大小 200GB 的专业版实例

Input: 

```
tccli ckafka CreateInstancePost --cli-unfold-argument  \
    --InstanceName yourtest45 \
    --VpcId vpc-test \
    --SubnetId subnet-test \
    --KafkaVersion 2.4.2 \
    --SpecificationsType profession \
    --DiskType CLOUD_BASIC \
    --BandWidth 20 \
    --DiskSize 200 \
    --Partition 400 \
    --TopicNum 200 \
    --ZoneId 450001
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok[apply success]",
            "Data": {
                "FlowId": 0,
                "RouteDTO": {
                    "RouteId": 0
                }
            }
        },
        "RequestId": "84770b4b-df34-4ccf-8e22-41d3b1d0fe0d"
    }
}
```

