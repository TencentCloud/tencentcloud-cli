**Example 1: 示例1**



Input: 

```
tccli tdai CreateMemoryProInstance --cli-unfold-argument  \
    --VpcId vpc-n4c3s8u4 \
    --SubnetId subnet-8apk7iir \
    --SecurityGroupIds sg-jml79sef \
    --MemoryLimit 20
```

Output: 
```
{
    "Response": {
        "MemoryProId": "mp-bwf6pfu7",
        "VDBInstanceId": "vdb-43xovn43",
        "RequestId": "b424b6f5-920b-4901-8bb4-7ddffafde36a"
    }
}
```

