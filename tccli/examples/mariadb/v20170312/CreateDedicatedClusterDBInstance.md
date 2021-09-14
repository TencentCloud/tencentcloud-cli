**Example 1: input demo1**



Input: 

```
tccli mariadb CreateDedicatedClusterDBInstance --cli-unfold-argument  \
    --DbVersionId xx \
    --VpcId  \
    --DcnInstanceId xx \
    --Zone xx \
    --GoodsNum 0 \
    --ProjectId 1 \
    --SecurityGroupIds xx \
    --Pid 0 \
    --DcnRegion xx \
    --Machine xx \
    --Storage 0 \
    --ResourceTags.0.TagKey xx \
    --ResourceTags.0.TagValue xx \
    --Manual 0 \
    --Memory 0 \
    --SubnetId  \
    --DeviceNo xx \
    --ClusterId xx \
    --InstanceName xx
```

Output: 
```
{
    "Response": {
        "RequestId": "14f6980a-7fe1-11ea-b896-525400542aa6",
        "InstanceIds": [
            "tdsql-xxxxxx"
        ],
        "FlowId": 1122
    }
}
```

