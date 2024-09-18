**Example 1: 查询策略列表**



Input: 

```
tccli tke DescribeOpenPolicyList --cli-unfold-argument  \
    --ClusterId cls-gzzr1v5t \
    --Category baseline
```

Output: 
```
{
    "Response": {
        "OpenPolicyInfoList": [
            {
                "EnforcementAction": "deny",
                "EventNums": 0,
                "Kind": "blockclusterdeletion",
                "Name": "block-cluster-deletion-rule",
                "PolicyCategory": "cluster",
                "PolicyDesc": "集群中存在任意节点（普通节点、原生节点、注册节点），需先下线节点后方可删除",
                "PolicyName": "存在节点的集群不允许删除"
            },
            {
                "EnforcementAction": "dryrun",
                "EventNums": 0,
                "Kind": "blocknamespacedeletion",
                "Name": "block-namespace-deletion-rule",
                "PolicyCategory": "namespace",
                "PolicyDesc": "命名空间内如果存在pod、service、ingress、pvc，需清空上述资源后方可删除",
                "PolicyName": "存在workload、服务与路由、存储对象的命名空间不允许删除"
            },
            {
                "EnforcementAction": "dryrun",
                "EventNums": 0,
                "Kind": "blockcrddeletion",
                "Name": "block-crd-deletion-rule",
                "PolicyCategory": "configuration",
                "PolicyDesc": "crd定义的apiversion下如果有创建cr资源，则清空cr后方可删除crd",
                "PolicyName": "存在cr的crd不允许删除"
            },
            {
                "EnforcementAction": "dryrun",
                "EventNums": 0,
                "Kind": "blockpvdeletion",
                "Name": "block-pv-deletion-rule",
                "PolicyCategory": "storage",
                "PolicyDesc": "pv如果处于bound状态，则不允许被删除",
                "PolicyName": "绑定状态的pv不允许删除"
            },
            {
                "EnforcementAction": "dryrun",
                "EventNums": 0,
                "Kind": "blockservicewithingressdeletion",
                "Name": "block-service-with-ingress-deletion-rule",
                "PolicyCategory": "network",
                "PolicyDesc": "ingress-controller前端svc，如果存在ingress配置，则svc不允许删除",
                "PolicyName": "应用了ingress规则的svc不允许删除"
            }
        ],
        "RequestId": "224782f1-c990-4383-8f21-bb369c9ca396"
    }
}
```

