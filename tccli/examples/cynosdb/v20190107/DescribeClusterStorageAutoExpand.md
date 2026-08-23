**Example 1: 自动扩容配置详情**

Describe Cluster Storage Auto Expand

Input: 

```
tccli cynosdb DescribeClusterStorageAutoExpand --cli-unfold-argument  \
    --ClusterId cynosdbmysql-kdyalkr6
```

Output: 
```
{
    "Response": {
        "ExpandStep": 0,
        "MaxStorageLimit": 0,
        "StorageAutoExpand": "",
        "StorageUsageThreshold": 0,
        "RequestId": "208d25c1-09d2-4279-9ab1-e4f9edb7dc3e"
    }
}
```

