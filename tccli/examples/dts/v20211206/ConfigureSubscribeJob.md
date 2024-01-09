**Example 1: 配置订阅**

配置订阅一个cdb整实例的任务，其中db1.table1的数据根据id列值投递到不同的kafka分区，其他的数据根据表名投递

Input: 

```
tccli dts ConfigureSubscribeJob --cli-unfold-argument  \
    --SubscribeMode all \
    --SubscribeId subs-5ft0e2nrc0 \
    --KafkaConfig.DistributeRules.0.DbPattern db1 \
    --KafkaConfig.DistributeRules.0.RuleType cols \
    --KafkaConfig.DistributeRules.0.TablePattern table1 \
    --KafkaConfig.DistributeRules.0.Columns id \
    --KafkaConfig.NumberOfPartitions 8 \
    --KafkaConfig.DefaultRuleType table \
    --AccessType cdb \
    --Protocol json \
    --Endpoints.0.InstanceId cdb-kdxona7h \
    --Endpoints.0.DatabaseRegion ap-guangzhou \
    --Endpoints.0.EncryptConn Encrypted \
    --Endpoints.0.User root \
    --Endpoints.0.Password ****** \
    --ExtraAttr.0.Value true \
    --ExtraAttr.0.Key ProcessXA
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

