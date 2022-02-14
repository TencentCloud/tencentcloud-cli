**Example 1: 修改CC防护等级**



Input: 

```
tccli antiddos ModifyCCLevelPolicy --cli-unfold-argument  \
    --InstanceId bgpip-0000023c \
    --Ip 1.3.2.6 \
    --Domain 1.sdc.com \
    --Protocol HTTP \
    --Level loose
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

