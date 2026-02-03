**Example 1: 查询分析集群账号权限**



Input: 

```
tccli cynosdb DescribeLibraDBClusterAccountAllPrivileges --cli-unfold-argument  \
    --ClusterId libradb-i794jfvg \
    --Account.AccountName admin \
    --Account.Host 127.0.0.1
```

Output: 
```
{
    "Response": {
        "DatabasePrivileges": null,
        "GlobalPrivileges": [
            "SELECT"
        ],
        "PrivilegeStatements": null,
        "TablePrivileges": null,
        "RequestId": "83c02582-a157-4bcf-a33d-b190c033c627"
    }
}
```

