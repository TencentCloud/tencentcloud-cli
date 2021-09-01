**Example 1: 创建基础版实例**



Input: 

```
tccli sqlserver CreateBasicDBInstances --cli-unfold-argument  \
    --Zone ap-guangzhou-3 \
    --InstanceChargeType PREPAID \
    --Cpu 1 \
    --Memory 2 \
    --Storage 20 \
    --GoodsNum 1 \
    --DBVersion 2008R2 \
    --SubnetId subnet-pudyecyk \
    --VpcId vpc-huew581t \
    --Period 1 \
    --AutoRenewFlag 0 \
    --StartTime 00:00 \
    --Span 6 \
    --MachineType CLOUD_PREMIUM \
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

