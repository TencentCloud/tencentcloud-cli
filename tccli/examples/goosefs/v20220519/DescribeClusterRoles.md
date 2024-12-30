**Example 1: 查询集群角色列表**

查询集群角色列表

Input: 

```
tccli goosefs DescribeClusterRoles --cli-unfold-argument  \
    --ClusterId g_cvm_x419f8qc \
    --RoleName GooseFS_QCSLinkedRoleInManageCloudService
```

Output: 
```
{
    "Response": {
        "ClusterRoles": [
            {
                "ClusterId": "g_cvm_x419f8qc",
                "RoleName": "GooseFS_QCSLinkedRoleInManageCloudService",
                "Description": "列举集群角色列表",
                "DirectoryList": [
                    "root"
                ]
            }
        ],
        "RequestId": "a10aeff3-cc7c-4535-8af5-db3b9bc108cb"
    }
}
```

