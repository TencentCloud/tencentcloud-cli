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
        "ReturnData": [
            {
                "InstanceId": "cdwch-1vud9x9x",
                "UserName": "cdwch",
                "Describe": "",
                "Type": "RBAC",
                "Cluster": "default_cluster"
            },
            {
                "InstanceId": "cdwch-1vud9x9x",
                "UserName": "willltgu",
                "Describe": "",
                "Type": "RBAC",
                "Cluster": ""
            },
            {
                "InstanceId": "cdwch-1vud9x9x",
                "UserName": "willltguo",
                "Describe": "",
                "Type": "RBAC",
                "Cluster": ""
            },
            {
                "InstanceId": "cdwch-1vud9x9x",
                "UserName": "default",
                "Describe": "xml 用户，只能查询不能做任何修改",
                "Type": "XML",
                "Cluster": ""
            }
        ],
        "RequestId": "xx",
        "ErrMsg": "xx"
    }
}
```

