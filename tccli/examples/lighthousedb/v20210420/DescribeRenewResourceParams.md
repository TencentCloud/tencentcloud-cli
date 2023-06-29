**Example 1: 获取续费集群入参**



Input: 

```
tccli lighthousedb DescribeRenewResourceParams --cli-unfold-argument  \
    --ClusterId lhdbmysql-0mc0efsx \
    --TimeSpan 1 \
    --TimeUnit m
```

Output: 
```
{
    "Response": {
        "Param": "{\"raw_goodsData\":[{\"regionId\":1,\"zoneId\":100003,\"payMode\":1,\"GoodsCategoryId\":0,\"goodsDetail\":{\"pid\":1007359,\"productCode\":\"p_lighthousedb\",\"subProductCode\":\"sp_lighthousedb_mysql\",\"curDeadline\":\"2021-05-07 17:35:05\",\"timeSpan\":1,\"timeUnit\":\"m\",\"sv_lighthousedb_cpu_mysql\":1,\"sv_lighthousedb_memory_mysql\":1,\"sv_lighthousedb_storage_mysql\":1000,\"productInfo\":[{\"name\":\"集群名称\",\"value\":\"cynosdbmysql-3ou4g46j\"},{\"name\":\"配置\",\"value\":\"1核1GB内存1000G存储，MYSQL5.7\"},{\"name\":\"地域\",\"value\":\"广州\"},{\"name\":\"可用区\",\"value\":\"广州三区\"}],\"resourceId\":\"lhdbmysql-ins-0mc0efsx\"}}]}",
        "RequestId": ""
    }
}
```

