**Example 1: 创建 APM 业务系统**

创建 APM 业务系统

Input: 

```
tccli apm CreateApmInstance --cli-unfold-argument  \
    --Name 可观测-测试 \
    --Description 测试环境 \
    --Tags.0.Key appid \
    --Tags.0.Value 123123422
```

Output: 
```
{
    "Response": {
        "InstanceId": "apm-CVfliqa8U",
        "RequestId": "49fktc24elkfi4a1mkyir-9t2pt2stlx"
    }
}
```

