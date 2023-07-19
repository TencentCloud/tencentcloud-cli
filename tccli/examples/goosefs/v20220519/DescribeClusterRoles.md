**Example 1: 查询集群角色列表**

查询集群角色列表

Input: 

```
tccli goosefs DescribeClusterRoles --cli-unfold-argument  \
    --ClusterId abc \
    --RoleName abc
```

Output: 
```
{
    "Response": {
        "ClusterRoles": [
            {
                "ClusterId": "abc",
                "RoleName": "abc",
                "Description": "abc",
                "DirectoryList": [
                    "abc"
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

