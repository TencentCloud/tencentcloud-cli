**Example 1: 查询快照策略关联实例列表**



Input: 

```
tccli vpc DescribeSnapshotAttachedInstances --cli-unfold-argument  \
    --SnapshotPolicyId sspolicy-g6jwvm35 \
    --Offset 0 \
    --Limit 2 \
    --Filters.0.Name uniqInstanceId \
    --Filters.0.Values sg-ntrgm89v
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "InstanceId": "sg-ntrgm89v",
                "InstanceRegion": "ap-shanghai",
                "InstanceType": "securitygroup",
                "SnapshotPolicyId": "sspolicy-g6jwvm35",
                "InstanceName": "test11111"
            }
        ],
        "TotalCount": 1,
        "RequestId": "2099cfcf-fe15-4825-93a1-642c9ad2630f"
    }
}
```

