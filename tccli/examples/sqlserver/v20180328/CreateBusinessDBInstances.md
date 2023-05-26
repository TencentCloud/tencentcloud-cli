**Example 1: 创建商业智能服务实例**

创建商业智能服务实例

Input: 

```
tccli sqlserver CreateBusinessDBInstances --cli-unfold-argument  \
    --Storage 50 \
    --Cpu 1 \
    --Zone ap-guangzhou-1 \
    --Memory 2 \
    --ProjectId 1 \
    --GoodsNum 1 \
    --SubnetId subnet-xxxx \
    --VpcId vpc-xxxxxx \
    --DBVersion 201703 \
    --StartTime 01:34 \
    --Span 4 \
    --MachineType CLOUD_PREMIUM \
    --Weekly 1 5
```

Output: 
```
{
    "Response": {
        "DealName": "20200318114212",
        "RequestId": "2b6f7e2a-e909-4753-84b7-0db3e6099877",
        "FlowId": 100439,
        "InstanceIdSet": [
            "mssqlbi-sdjiej23"
        ]
    }
}
```

