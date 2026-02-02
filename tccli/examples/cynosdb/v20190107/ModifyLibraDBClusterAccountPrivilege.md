**Example 1: 修改分析集群账号权限**



Input: 

```
tccli cynosdb ModifyLibraDBClusterAccountPrivilege --cli-unfold-argument  \
    --ClusterId libradb-i794jfvg \
    --Account.AccountName admin \
    --Account.Host 127.0.0.1 \
    --GlobalPrivileges SELECT
```

Output: 
```
{
    "Response": {
        "RequestId": "4ea944a8-fd25-438a-a892-55bb073c60b7"
    }
}
```

