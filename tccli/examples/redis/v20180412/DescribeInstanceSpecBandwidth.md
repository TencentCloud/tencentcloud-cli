**Example 1: 查询带宽规格**

查询带宽规格

Input: 

```
tccli redis DescribeInstanceSpecBandwidth --cli-unfold-argument  \
    --InstanceId crs-xjhsdj**** \
    --ShardSize 0 \
    --ShardNum 0 \
    --ReplicateNum 0 \
    --ReadOnlyWeight 0 \
    --Type 0
```

Output: 
```
{
    "Response": {
        "Bandwidth": 0,
        "ClientLimit": 0,
        "RequestId": "4297c734-2f56-49d9-9c14-9d092fXXXXXX"
    }
}
```

