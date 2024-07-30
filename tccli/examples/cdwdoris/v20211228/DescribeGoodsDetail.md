**Example 1: 生成GoodsDetail**

生成计费相关接口的GoodsDetail结构

Input: 

```
tccli cdwdoris DescribeGoodsDetail --cli-unfold-argument  \
    --Zone ap-chongqing-1 \
    --HaFlag true \
    --UserVPCId vpc-xxx \
    --UserSubnetId subnet-xxxx \
    --ProductVersion 20.7.2.30 \
    --Case CREATE \
    --ChargeProperties.ChargeType "PREPAID" \
    --ChargeProperties.RenewFlag 1 \
    --ChargeProperties.TimeSpan 1 \
    --ChargeProperties.TimeUnit m
```

Output: 
```
{
    "Response": {
        "Type": "sp_cdwch_standard",
        "GoodsCategoryId": 1,
        "GoodsDetail": "{\"context\":{\"AppID\":1258469122,\"AutoRenewFlag\":0,\"Case\":\"CREATE\",\"Channel\":0,\"ChargeProperties\":{\"ChargeType\":\"PREPAID\",\"RenewFlag\":1,\"TimeSpan\":1,\"TimeUnit\":\"m\"},\"Components\":[\"clickhouse-20.7.2.30\",\"zookeeper-3.4.9\"],\"DealName\":\"\",\"EMRInstanceID\":\"\",\"EMRInstanceNo\":0,\"ExpiredTime\":\"\",\"HAInstance\":true,\"ImageID\":\"\",\"InstanceName\":\"\",\"InstanceType\":\"\",\"ModifyConfigItems\":null,\"OperateUin\":\"\",\"Password\":\"\",\"ProductID\":0,\"Region\":\"ap-guangzhou\",\"RenewPeriod\":0,\"ResourceAppID\":0,\"ResourceOperateUin\":\"\",\"ResourceUin\":\"\",\"Resources\":[{\"Count\":2,\"DiskSpec\":{\"DiskCount\":0,\"DiskSize\":0,\"DiskType\":\"\"},\"SpecName\":\"CVM.S2\",\"Type\":\"DATA\"},{\"Count\":1,\"DiskSpec\":{\"DiskCount\":0,\"DiskSize\":0,\"DiskType\":\"\"},\"SpecName\":\"CVM.S2\",\"Type\":\"COMMON\"}],\"SecurityGroupID\":\"\",\"ServiceName\":\"ClickHouse\",\"StackID\":\"\",\"Tags\":{\"ResourceType\":\"\",\"Tags\":null},\"TimeSpan\":1,\"TimeUnit\":\"m\",\"Topology\":\"\",\"TraceID\":\"trace-vudbhcyqe15awen3\",\"Uin\":\"100010640219\",\"UserSubnetID\":\"subnet-xx111\",\"UserVPCID\":\"vpc-xxx\",\"VIPType\":0,\"Version\":\"20.7.2.30\",\"Zone\":\"ap-guangzhou-4\",\"instanceId\":\"cdwch-bbi1k4he\",\"modifySpec\":null},\"curDeadline\":\"\",\"goodsNum\":1,\"pid\":123,\"productCode\":\"p_cdwch\",\"productInfo\":{\"可用区\":\"ap-guangzhou-4\",\"地域\":\"ap-guangzhou\",\"集群\":\"cdwch-bbi1k4he\"},\"sa2_cpu2_mem4\":\"3\",\"subProductCode\":\"p_sub_iaas\",\"timeSpan\":1,\"timeUnit\":\"m\"}",
        "GoodsNum": 1,
        "PayMode": 1,
        "RegionId": 1,
        "ZoneId": 100004,
        "ResourceId": "cdwch-bbi1k4he",
        "RequestId": "xxx-xxx-xxx-xxx"
    }
}
```

