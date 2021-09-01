**Example 1: 查询部署组明细**



Input: 

```
tccli tsf DescribeServerlessGroup --cli-unfold-argument  \
    --GroupId group-jy9jxpkv
```

Output: 
```
{
    "Response": {
        "RequestId": "e8201d29-c559-4906-96d9-546c4b5fbcf4",
        "Result": {
            "GroupName": "wzz-node-8",
            "Status": "Running",
            "ApplicationName": "wzz-node-8",
            "ClusterId": "cluster-5yrw3koa",
            "Memory": "1Gi",
            "CreateTime": "2020-01-31 21:16:17.0",
            "PkgName": "code2.zip",
            "GroupId": "group-jy9jxpkv",
            "NamespaceName": "wzz_default",
            "InstanceCount": 1,
            "PkgVersion": "20200131212742",
            "ClusterName": "wzz",
            "NamespaceId": "namespace-qv35e69y",
            "ApplicationId": "application-6ym9kjba",
            "PkgId": "pkg-76578126",
            "InstanceRequest": 1,
            "StartupParameters": ""
        }
    }
}
```

