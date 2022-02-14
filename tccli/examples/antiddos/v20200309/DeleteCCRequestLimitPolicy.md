**Example 1: 删除CC频率限制策略**



Input: 

```
tccli antiddos DeleteCCRequestLimitPolicy --cli-unfold-argument  \
    --InstanceId bgpip-0000023c \
    --PolicyId ccRule-00000435
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

