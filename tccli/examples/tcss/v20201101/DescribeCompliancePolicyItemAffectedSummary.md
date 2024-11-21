**Example 1: 查询某检测项影响的信息**



Input: 

```
tccli tcss DescribeCompliancePolicyItemAffectedSummary --cli-unfold-argument  \
    --CustomerPolicyItemId 474567
```

Output: 
```
{
    "Response": {
        "PolicyItemSummary": {
            "ApplicableVersion": "docker 1.11-1.13, 17.12-20.10.2",
            "AssetType": "ASSET_IMAGE",
            "AuditProcedure": "执行以下命令审计\ndocker ps --quiet | xargs --max-args=1 -I{} docker exec {} cat /proc/1/status | grep '^Uid:' | awk '{print $3}'",
            "BasePolicyItemId": 178,
            "BenchmarkStandardId": 2,
            "BenchmarkStandardName": "CIS Docker",
            "Category": "CATEGORY_DOCKER_IMAGES_BUILD_FILE",
            "CheckResult": "RESULT_FAILED",
            "CheckStatus": "CHECK_FINISHED",
            "CustomerPolicyItemId": 5914,
            "Description": "在可能的情况下，最好以非root用户的身份运行容器。",
            "FailedAssetCount": 208,
            "FixSuggestion": "确保容器镜像的Dockerfile包含以下指令：USER <用户名或ID> 其中用户名或ID是指可以在容器基础镜像中找到的用户。 如果在容器基础镜像中没有创建特定用户，则在USER指令之前添加useradd命令以添加特定用户。例如，在Dockerfile中创建用户：RUN useradd -d /home/username -m -s /bin/bash username USER username注意：如果镜像中有容器不需要的用户，请考虑删除它们。 删除这些用户后，提交镜像，然后生成新的容器实例以供使用。",
            "IsEnable": 0,
            "LastCheckTime": "2024-10-30 02:02:09",
            "Name": "确保创建使用容器的用户",
            "PassedAssetCount": 0,
            "RiskLevel": "1",
            "WhitelistId": 0
        },
        "RequestId": "3e8b4c60-58ba-4acc-97fc-33f086c7a3bb"
    }
}
```

