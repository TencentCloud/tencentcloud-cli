**Example 1: 修改集群只读开关**



Input: 

```
tccli cynosdb ModifyClusterReadOnly --cli-unfold-argument  \
    --ClusterIds cynosdbmysql-jl17y89v cynosdbmysql-2d9pq38h \
    --ReadOnlyOperation ON \
    --IsInMaintainPeriod no
```

Output: 
```
{
    "Response": {
        "ClusterTaskIds": [
            {
                "ClusterId": "cynosdbmysql-jl17y89v",
                "TaskId": "176551"
            },
            {
                "ClusterId": "cynosdbmysql-2d9pq38h",
                "TaskId": "176552"
            }
        ],
        "RequestId": "48b7cd8a-f6dd-4e47-a78a-ssfff"
    }
}
```

