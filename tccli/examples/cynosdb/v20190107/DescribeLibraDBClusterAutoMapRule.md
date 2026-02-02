**Example 1: 查询分析集群自动映射规则**



Input: 

```
tccli cynosdb DescribeLibraDBClusterAutoMapRule --cli-unfold-argument  \
    --ClusterId libradb-a405lyzg \
    --InstanceId libradb-ins-80lwcxnx
```

Output: 
```
{
    "Response": {
        "AutoMapRules": [],
        "RequestId": "8417f19e-5b18-4d8f-87fb-440c99191038"
    }
}
```

