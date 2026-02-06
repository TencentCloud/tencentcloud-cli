**Example 1: 查看分析集群库表映射关系**

查看分析集群库表映射关系

Input: 

```
tccli cynosdb DescribeLibraDBClusterTableMapping --cli-unfold-argument  \
    --ClusterId libradb-ln26puh1 \
    --InstanceId libradb-ins-4v4hcwgs
```

Output: 
```
{
    "Response": {
        "RequestId": "253f5807-47f3-478a-b2d0-5de7bf3774f7",
        "TableMappings": [],
        "TotalCnt": 0
    }
}
```

