**Example 1: 删除 TDSQL-C 分析集群**

彻底下线 TDSQL-C 分析集群

Input: 

```
tccli cynosdb DeleteLibraDBCluster --cli-unfold-argument  \
    --ClusterId libradb-i8okw971
```

Output: 
```
{
    "Response": {
        "FlowId": 2105108,
        "RequestId": "fe34045a-0fa2-4507-b8a6-6dd5a527faf0"
    }
}
```

