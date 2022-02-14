**Example 1: 新增CC频率限制策略**



Input: 

```
tccli antiddos CreateCCReqLimitPolicy --cli-unfold-argument  \
    --InstanceId xx \
    --Ip xx \
    --Domain xx \
    --Policy.ExecuteDuration 1 \
    --Policy.Uri xx \
    --Policy.Period 1 \
    --Policy.Cookie xx \
    --Policy.Mode xx \
    --Policy.Action xx \
    --Policy.UserAgent xx \
    --Policy.RequestNum 1 \
    --Protocol xx
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

