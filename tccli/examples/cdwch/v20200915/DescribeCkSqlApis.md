**Example 1: 查询ck集群信息**



Input: 

```
tccli cdwch DescribeCkSqlApis --cli-unfold-argument  \
    --InstanceId xx \
    --Cluster xx \
    --UserName xx \
    --ApiType xx
```

Output: 
```
{
    "Response": {
        "ReturnData": {
            "NodeIp": "xx",
            "TableName": "xx",
            "Exists": true,
            "TotalBytes": 0
        },
        "RequestId": "xx",
        "ErrMsg": "xx"
    }
}
```

