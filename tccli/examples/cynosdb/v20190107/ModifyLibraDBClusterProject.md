**Example 1: 修改分析集群项目 ID**



Input: 

```
tccli cynosdb ModifyLibraDBClusterProject --cli-unfold-argument  \
    --ClusterIdSet libradb-i8okw971 \
    --ProjectId 0
```

Output: 
```
{
    "Response": {
        "AffectedClusterIdSet": [
            "libradb-i8okw971"
        ],
        "RequestId": "6efb3d4f-fcb4-4f4b-8e43-459520443ae7"
    }
}
```

