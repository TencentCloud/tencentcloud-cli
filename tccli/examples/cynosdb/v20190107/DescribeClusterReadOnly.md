**Example 1: 查询集群只读开关**



Input: 

```
tccli cynosdb DescribeClusterReadOnly --cli-unfold-argument  \
    --ClusterIds cynosdbmysql-jl17y89v cynosdbmysql-2d9pq38h
```

Output: 
```
{
    "Response": {
        "ClusterReadOnlyValues": [
            {
                "ClusterId": "cynosdbmysql-jl17y89v",
                "ReadOnlyValue": "ON"
            },
            {
                "ClusterId": "cynosdbmysql-2d9pq38h",
                "ReadOnlyValue": "ON"
            }
        ],
        "RequestId": "48b7cd8a-f6dd-4e47-a78a-ssfff"
    }
}
```

