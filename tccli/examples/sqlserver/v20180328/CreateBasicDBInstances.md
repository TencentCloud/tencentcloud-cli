**Example 1: 创建基础版实例**

创建基础版实例

Input: 

```
tccli sqlserver CreateBasicDBInstances --cli-unfold-argument  \
    --VpcId vpc-huew581t \
    --AutoRenewFlag 0 \
    --Zone ap-guangzhou-3 \
    --GoodsNum 1 \
    --TimeZone China Standard Time \
    --DBVersion 2008R2 \
    --Storage 20 \
    --Period 1 \
    --MachineType CLOUD_PREMIUM \
    --Collation Chinese_PRC_CI_AS \
    --InstanceChargeType PREPAID \
    --StartTime 00:00 \
    --Memory 2 \
    --SubnetId subnet-pudyecyk \
    --Span 6 \
    --Cpu 1 \
    --Weekly 1
```

Output: 
```
{
    "Response": {
        "DealName": "20200713383000001111250",
        "RequestId": "d84adfca-3ff0-46d2-b400-b5527446df72"
    }
}
```

