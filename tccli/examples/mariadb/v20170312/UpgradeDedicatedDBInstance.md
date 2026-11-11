**Example 1: 独享集群实例创建示例**



Input: 

```
tccli mariadb UpgradeDedicatedDBInstance --cli-unfold-argument  \
    --InstanceId tdsql-006dngfx4f \
    --Memory 2 \
    --Storage 10 \
    --MasterHostId svr-buhfdoz8 \
    --SlaveHostIds svr-honcouya
```

Output: 
```
{
    "Response": {
        "FlowId": 9,
        "RequestId": "6c0f6fbb-f725-4a9d-abcb-d295ce4a1e7d"
    }
}
```

