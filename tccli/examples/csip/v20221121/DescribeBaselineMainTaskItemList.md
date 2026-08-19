**Example 1: 调用示例**



Input: 

```
tccli csip DescribeBaselineMainTaskItemList --cli-unfold-argument  \
    --MainTaskID 1225 \
    --MemberId mem-tencent-6*************29 \
    --Limit 0 \
    --Offset 10
```

Output: 
```
{
    "Response": {
        "ItemList": [
            {
                "AffectedVersionList": [
                    "All Kubernetes versions"
                ],
                "Category": {
                    "CheckAssetType": "CLUSTER",
                    "Description": "来自互联网安全中心（CIS）的 CIS Benchmarks 是一套全球公认的共识驱动型最佳实践。",
                    "ID": 100000005,
                    "Name": "策略"
                },
                "CheckObject": [
                    "POD"
                ],
                "CustomItemID": 0,
                "DefaultValueList": [],
                "Description": "hostPort 将容器端口直接绑定到宿主机端口，绕过网络策略和隔离，且每个宿主机端口只能被一个 Pod 使用。",
                "FixSuggestion": "删除 hostPort 字段，仅保留 containerPort。对外暴露通过 Service 实现： ports:   - containerPort: 80     # 不设置 hostPort --- apiVersion: v1 kind: Service spec:   ports:   - port: 80     targetPort: 80",
                "ID": 10140,
                "IsCustomConf": false,
                "Name": "最小化使用 HostPorts 的容器准入",
                "ReferenceLink": "https://kubernetes.io/docs/concepts/security/pod-security-standards/",
                "RiskLevel": "MEDIUM",
                "RuleID": 139,
                "SupportCustomValue": false,
                "SupportFix": false,
                "SystemCategory": {
                    "CheckAssetType": "CLUSTER",
                    "Description": "来自互联网安全中心（CIS）的 CIS Benchmarks 是一套全球公认的共识驱动型最佳实践。",
                    "ID": 100000000,
                    "Name": "CIS Kubernetes 基线"
                },
                "WebEditParam": ""
            }
        ],
        "TotalCount": 149,
        "RequestId": "30cfb28c-c73b-4ca3-aa06-7ea57bb79b8a"
    }
}
```

