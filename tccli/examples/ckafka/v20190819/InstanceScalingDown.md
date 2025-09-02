**Example 1: 实例缩容**

实例缩容

Input: 

```
tccli ckafka InstanceScalingDown --cli-unfold-argument  \
    --InstanceId *** \
    --DiskSize 900 \
    --BandWidth 40 \
    --Partition 1000 \
    --UpgradeStrategy 1
```

Output: 
```
{
    "Response": {
        "Result": {
            "DealNames": [
                "20230703002035272950891"
            ]
        },
        "RequestId": "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    }
}
```

