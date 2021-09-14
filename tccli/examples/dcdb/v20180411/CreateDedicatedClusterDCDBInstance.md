**Example 1: input demo1**



Input: 

```
tccli dcdb CreateDedicatedClusterDCDBInstance --cli-unfold-argument  \
    --Zone xx \
    --ShardNodeMemory 0 \
    --ShardNodeCpu 0 \
    --ShardNodeNum 0 \
    --ShardMachine xx \
    --ResourceTags.0.TagKey xx \
    --ResourceTags.0.TagValue xx \
    --ClusterId xx \
    --DcnRegion xx \
    --SubnetId xx \
    --DbVersionId xx \
    --DcnInstanceId xx \
    --GoodsNum 0 \
    --ProjectId 1 \
    --ShardNodeStorage 0 \
    --VpcId xx \
    --InstanceName xx \
    --Cpu 0 \
    --ShardNum 0 \
    --SecurityGroupId xx \
    --ShardMemory 0 \
    --ShardStorage 0 \
    --Pid 100
```

Output: 
```
{
    "Response": {
        "RequestId": "14f6980a-7fe1-11ea-b896-525400542aa6"
    }
}
```

