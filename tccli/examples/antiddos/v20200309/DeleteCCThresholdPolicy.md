**Example 1: 删除CC清洗阈值策略**



Input: 

```
tccli antiddos DeleteCCThresholdPolicy --cli-unfold-argument  \
    --InstanceId bgpip-0000011x \
    --Ip 1.1.1.3 \
    --Domain test.com \
    --Protocol http
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

