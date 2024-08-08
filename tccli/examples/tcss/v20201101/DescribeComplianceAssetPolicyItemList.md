**Example 1: 请求资产检测项列表**

请求资产检测项列表

Input: 

```
tccli tcss DescribeComplianceAssetPolicyItemList --cli-unfold-argument  \
    --CustomerAssetId 2202462 \
    --Offset 0 \
    --Limit 3 \
    --AssetType ASSET_CONTAINER
```

Output: 
```
{
    "Response": {
        "AssetPolicyItemList": [
            {
                "BasePolicyItemId": 142,
                "BenchmarkStandardId": 1,
                "BenchmarkStandardName": "CIS Docker",
                "Category": "CATEGORY_DOCKER_RUNTIME",
                "CheckResult": "RESULT_PASSED",
                "CheckStatus": "CHECK_FINISHED",
                "CustomerPolicyItemId": 2809,
                "FixSuggestion": "使用--health-cmd和其他参数运行容器。 例如，docker run -d --health-cmd ='stat /etc/passwd || exit1'nginx。",
                "LastCheckTime": "2024-07-24 11:12:16",
                "Name": "检查容器运行时的健康状态",
                "RiskLevel": "1",
                "VerifyInfo": "e822238a07e0d193a12c0608f2d821812664d3d9cf5871cc9bedc9eab562e602:Healthcheck=null\n",
                "WhitelistId": 0
            },
            {
                "BasePolicyItemId": 141,
                "BenchmarkStandardId": 1,
                "BenchmarkStandardName": "CIS Docker",
                "Category": "CATEGORY_DOCKER_RUNTIME",
                "CheckResult": "RESULT_PASSED",
                "CheckStatus": "CHECK_FINISHED",
                "CustomerPolicyItemId": 2808,
                "FixSuggestion": "如无必须，不要使用 --cgroup-parent 选项在docker运行。",
                "LastCheckTime": "2024-07-24 11:12:16",
                "Name": "确保cgroup安全使用",
                "RiskLevel": "1",
                "VerifyInfo": "e822238a07e0d193a12c0608f2d821812664d3d9cf5871cc9bedc9eab562e602:CgroupParent=\n",
                "WhitelistId": 0
            },
            {
                "BasePolicyItemId": 140,
                "BenchmarkStandardId": 1,
                "BenchmarkStandardName": "CIS Docker",
                "Category": "CATEGORY_DOCKER_RUNTIME",
                "CheckResult": "RESULT_PASSED",
                "CheckStatus": "CHECK_FINISHED",
                "CustomerPolicyItemId": 2807,
                "FixSuggestion": "在docker exec命令中不要使用--privileged选项。",
                "LastCheckTime": "2024-07-24 11:12:16",
                "Name": "确保docker exec命令不能使用特权选项",
                "RiskLevel": "2",
                "VerifyInfo": "e822238a07e0d193a12c0608f2d821812664d3d9cf5871cc9bedc9eab562e602:ExecIDs=null\n",
                "WhitelistId": 0
            }
        ],
        "RequestId": "dc08e10e-5ac8-4e94-9321-6c2f89d8ed5c",
        "TotalCount": 24
    }
}
```

