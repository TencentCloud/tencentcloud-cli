**Example 1: 创建APM实例**

创建APM实例

Input: 

```
tccli apm CreateApmInstance --cli-unfold-argument  \
    --Name 云监控-测试 \
    --Description 测试环境 \
    --Tags.0.Key appid \
    --Tags.0.Value 123123422
```

Output: 
```
{
    "Response": {
        "InstanceId": "sSBebnOhf",
        "RequestId": "49fktc24elkfi4a1mkyir-9t2pt2stlx"
    }
}
```

