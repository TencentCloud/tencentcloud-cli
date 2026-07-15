**Example 1: 查询支持的集群级别**

查询用户支持的集群级别

Input: 

```
tccli cynosdb DescribeClusterLevels --cli-unfold-argument  \
    --Zone ap-guangzhou-3
```

Output: 
```
{
    "Response": {
        "RequestId": "0c646e65-3597-44d7-b68b-d43391eedb33",
        "LevelList": [
            "P0",
            "P1"
        ]
    }
}
```

