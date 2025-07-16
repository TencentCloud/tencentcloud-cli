**Example 1: 删除多通道安全加速网关的线路**

删除多通道安全加速网关的指定自定义线路。

Input: 

```
tccli teo DeleteMultiPathGatewayLine --cli-unfold-argument  \
    --ZoneId zone-27q0p0bal192 \
    --GatewayId mpgw-lbxuhk1oh \
    --LineId line-2
```

Output: 
```
{
    "Response": {
        "RequestId": "a622678d-ea5b-41e8-9cd2-d335816141a0"
    }
}
```

