**Example 1: 查询公共配置发布信息**



Input: 

```
tccli tsf DescribePublicConfigReleases --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --ConfigName ebs-demo
```

Output: 
```
{
    "Response": {
        "RequestId": "69d073be-25d1-4ba8-b1eb-92cdc21ad4ea",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "ConfigReleaseId": "dcfgr-gyqpwbpa",
                    "ConfigId": "dcfg-p-gvkwzpjv",
                    "ConfigName": "ebs-demo",
                    "ConfigVersion": "3.0",
                    "ReleaseTime": "2019-05-16 14:24:32",
                    "GroupId": null,
                    "GroupName": null,
                    "NamespaceId": "namespace-6yooxgdy",
                    "NamespaceName": "ebs-demo",
                    "ClusterId": null,
                    "ClusterName": null,
                    "ReleaseDesc": null
                }
            ]
        }
    }
}
```

