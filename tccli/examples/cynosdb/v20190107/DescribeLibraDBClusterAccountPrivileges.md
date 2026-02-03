**Example 1: 查询分析集群账号权限**



Input: 

```
tccli cynosdb DescribeLibraDBClusterAccountPrivileges --cli-unfold-argument  \
    --ClusterId libradb-i794jfvg \
    --AccountName admin \
    --Host 127.0.0.1 \
    --Db Database1 \
    --Type *
```

Output: 
```
{
    "Response": {
        "Privileges": [
            "SELECT"
        ],
        "RequestId": "83c02582-a157-4bcf-a33d-b190c033c627"
    }
}
```

