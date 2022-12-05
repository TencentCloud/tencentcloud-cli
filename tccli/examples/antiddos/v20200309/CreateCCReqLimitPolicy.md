**Example 1: 新增CC频率限制策略**



Input: 

```
tccli antiddos CreateCCReqLimitPolicy --cli-unfold-argument  \
    --Domain www.baidu.com \
    --InstanceId bgpip-000005v7 \
    --Ip 1.1.1.1 \
    --Policy.Action alg \
    --Policy.ExecuteDuration 120 \
    --Policy.Mode equal \
    --Policy.Period 10 \
    --Policy.RequestNum 500 \
    --Policy.Uri / \
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

