**Example 1: 创建按量计费实例**

创建按量计费实例

Input: 

```
tccli ckafka CreateInstancePost --cli-unfold-argument  \
    --InstanceName test \
    --VpcId vpc-12341234 \
    --SubnetId subnetId-12341233 \
    --MsgRetentionTime 1440 \
    --BandWidth 8 \
    --ZoneId 100003 \
    --ClusterId 55
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok[apply ok]",
            "Data": {
                "FlowId": 492917
            }
        },
        "RequestId": "4effa7c3-edb2-4310-9202-ea8259ca122f"
    }
}
```

