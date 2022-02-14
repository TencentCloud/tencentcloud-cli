**Example 1: 修改CC清洗阈值**



Input: 

```
tccli antiddos ModifyCCThresholdPolicy --cli-unfold-argument  \
    --InstanceId bgpip-0000023c \
    --Ip 1.3.2.6 \
    --Domain 1.sdc.com \
    --Protocol HTTP \
    --Threshold 1000
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

