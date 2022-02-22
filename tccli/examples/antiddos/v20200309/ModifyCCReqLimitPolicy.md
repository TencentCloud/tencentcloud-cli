**Example 1: 修改CC频率限制策略**



Input: 

```
tccli antiddos ModifyCCReqLimitPolicy --cli-unfold-argument  \
    --InstanceId xx \
    --Policy.ExecuteDuration 1 \
    --Policy.Uri xx \
    --Policy.Period 1 \
    --Policy.Cookie xx \
    --Policy.Mode xx \
    --Policy.Action xx \
    --Policy.UserAgent xx \
    --Policy.RequestNum 1 \
    --PolicyId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

