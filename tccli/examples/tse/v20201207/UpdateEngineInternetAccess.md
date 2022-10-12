**Example 1: 修改引擎公网访问配置**

修改引擎公网访问配置

Input: 

```
tccli tse UpdateEngineInternetAccess --cli-unfold-argument  \
    --InstanceId ins-xxxxx \
    --EnableClientInternetAccess true \
    --EngineType eureka
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

