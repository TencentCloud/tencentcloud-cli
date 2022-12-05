**Example 1: 修改CC频率限制策略**



Input: 

```
tccli antiddos ModifyCCReqLimitPolicy --cli-unfold-argument  \
    --InstanceId bgpip-00000001 \
    --Policy.Action alg \
    --Policy.ExecuteDuration 100 \
    --Policy.Mode equal \
    --Policy.Period 10 \
    --Policy.RequestNum 600 \
    --Policy.Uri / \
    --PolicyId ccRule-00009001
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

