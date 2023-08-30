**Example 1: 查询ck集群信息**



Input: 

```
tccli cdwch DescribeCkSqlApis --cli-unfold-argument  \
    --InstanceId cdwdoris-czj3e8qw \
    --Cluster default \
    --UserName admin \
    --ApiType GetSystemUsers
```

Output: 
```
{
    "Response": {
        "ReturnData": "abc",
        "RequestId": "abc"
    }
}
```

