**Example 1: 创建引擎实例**



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
    --TradeType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "5d996e05507e42d5970cd2e25ed5267a",
        "InstanceId": "ers-12345678"
    }
}
```

