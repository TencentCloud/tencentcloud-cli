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
        "ReturnData": "[{\"InstanceId\":\"cdwch-xxxxxxxx\",\"UserName\":\"test_user\",\"Describe\":\"\",\"Type\":\"RBAC\",\"Cluster\":\"default_cluster\"}]",
        "RequestId": "23808b41-a7ac-48fa-9b6b-6686a1814d0a"
    }
}
```

