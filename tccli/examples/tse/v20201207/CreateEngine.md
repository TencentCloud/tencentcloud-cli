**Example 1: 创建引擎实例**

创建引擎实例

Input: 

```
tccli tse CreateEngine --cli-unfold-argument  \
    --EngineType zookeeper \
    --EngineVersion 3.4.14 \
    --EngineProductVersion STANDARD \
    --EngineRegion ap-beijing \
    --EngineResourceSpec spec-xxxxxx \
    --EngineNodeNum 3 \
    --VpcId vpc-xxxxxx \
    --SubnetId subnet-xxxxxx \
    --EngineName qzone-photo-prod \
    --TradeType 0 \
    --ReportPolarisLogToCLS false
```

Output: 
```
{
    "Response": {
        "InstanceId": "xx",
        "RequestId": "xx"
    }
}
```

