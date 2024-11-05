**Example 1: 查询上次任务的检测项的汇总信息列表**



Input: 

```
tccli tcss DescribeComplianceTaskPolicyItemSummaryList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name RiskLevel \
    --Filters.0.Values 3 2 1 0 \
    --Filters.0.ExactMatch True \
    --Filters.1.Name ItemType \
    --Filters.1.Values CATEGORY_DOCKER_RUNTIME \
    --Filters.1.ExactMatch True \
    --AssetType ASSET_CONTAINER
```

Output: 
```
{
    "Response": {
        "PolicyItemSummaryList": [
            {
                "ApplicableVersion": "docker 1.11-1.13, 17.12-20.10.2",
                "AssetType": "ASSET_CONTAINER",
                "AuditProcedure": "运行以下命令执行检查\ndocker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Privileged={{ .HostConfig.Privileged }}'",
                "BasePolicyItemId": 1,
                "BenchmarkStandardId": 1,
                "BenchmarkStandardName": "CIS Docker",
                "Category": "CATEGORY_DOCKER_RUNTIME",
                "CheckResult": "RESULT_FAILED",
                "CheckStatus": "CHECK_FINISHED",
                "CustomerPolicyItemId": 6190,
                "Description": "开启了privileged权限之后，会让容器拥有底层主机的大部分权限，不应该在创建容器时使用该参数",
                "FailedAssetCount": 29,
                "FixSuggestion": "不要运行带有--privileged标志的容器。 例如，不要启动如下容器：docker run --interactive --tty --privileged centos/bin/bash。",
                "IsEnable": 1,
                "LastCheckTime": "2024-10-30 02:02:27",
                "Name": "确保不使用特权容器",
                "PassedAssetCount": 210,
                "RiskLevel": "3",
                "WhitelistId": 0
            }
        ],
        "RequestId": "a9aae028-b4f8-4ec3-8f77-5c102c4b5fcf",
        "TaskId": 0,
        "TotalCount": 33
    }
}
```

