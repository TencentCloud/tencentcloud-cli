**Example 1: 示例1**



Input: 

```
tccli csip DescribeIaCFileReport --cli-unfold-argument  \
    --AssetId 8130 \
    --MemberId mem-a6df317cb6a8c424
```

Output: 
```
{
    "Response": {
        "File": "apiVersion: v1\nkind: Service\nmetadata:\n  name: ai-inference-svc\n  namespace: ai-platform\n  labels:\n    app: ai-inference\nspec:\n  type: NodePort\n  selector:\n    app: ai-inference\n  ports:\n    - name: http\n      port: 8080\n      targetPort: 8080\n      nodePort: 30080\n    - name: metrics\n      port: 9090\n      targetPort: 9090\n      nodePort: 30090\n",
        "Risks": [
            {
                "Description": "Service 不应使用 NodePort 类型。NodePort 会在每个节点的 IP 上暴露服务的静态端口，这可能带来安全风险，因为它绕过了负载均衡器的安全控制，直接将服务暴露在节点网络上。",
                "Level": 0,
                "Line": 9,
                "RuleName": "K8s Service 应避免使用 NodePort 类型",
                "Suggestion": "将 Service 类型改为 ClusterIP 或 LoadBalancer，避免直接暴露节点端口。"
            }
        ],
        "ScanTime": "2026-04-01T07:23:22Z",
        "Status": 2,
        "RequestId": "6f25933a-914d-46d6-af68-37763a102b26"
    }
}
```

