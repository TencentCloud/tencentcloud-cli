**Example 1: 查询Serverless部署组列表**

查询Serverless部署组列表

Input: 

```
tccli tsf DescribeServerlessGroups --cli-unfold-argument  \
    --ApplicationId application-6ym9kjba \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "63871c25-31d0-40dd-b65e-5a95a57ed461",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "GroupId": "group-nalmm3wy",
                    "GroupName": "group12345",
                    "ApplicationId": "application-6ym9kjba",
                    "ApplicationName": "wzz-node-8",
                    "ClusterId": "cluster-6ymj295y",
                    "ClusterName": "serverless_cluster",
                    "NamespaceId": "namespace-evj92lly",
                    "NamespaceName": "serverless_cluster_default",
                    "PkgId": "pkg-a7d4f954"
                }
            ]
        }
    }
}
```

