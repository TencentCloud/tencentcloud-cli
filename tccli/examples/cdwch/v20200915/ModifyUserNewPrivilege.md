**Example 1: 新增、修改集群账号权限（新版）**



Input: 

```
tccli cdwch ModifyUserNewPrivilege --cli-unfold-argument  \
    --InstanceId cdwch-6hxpujog \
    --Cluster default_cluster \
    --UserName admin12345 \
    --AllDatabase True \
    --GlobalPrivileges SELECT ALTER INSERT_ALL CREATE_TABLE TRUNCATE DROP_TABLE DROP_DATABASE CREATE_DATABASE \
    --DatabasePrivilegeList.0.DatabaseName default \
    --DatabasePrivilegeList.0.DatabasePrivileges TRUNCATE SELECT INSERT_ALL \
    --DatabasePrivilegeList.0.TablePrivilegeList.0.TableName trest \
    --DatabasePrivilegeList.0.TablePrivilegeList.0.TablePrivileges TRUNCATE SELECT INSERT_ALL
```

Output: 
```
{
    "Response": {
        "RequestId": "xadasdfxasqs"
    }
}
```

