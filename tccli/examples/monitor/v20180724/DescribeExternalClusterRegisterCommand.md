**Example 1: 查看外部集群注册命令**



Input: 

```
tccli monitor DescribeExternalClusterRegisterCommand --cli-unfold-argument  \
    --InstanceId prom-abcd \
    --ClusterId ecls-abcd
```

Output: 
```
{
    "Response": {
        "Command": "\n---\napiVersion: v1\nkind: Namespace\nmetadata:\n  name: prom-abcd\n---\napiVersion: v1\nkind: ServiceAccount\nmetadata:\n  name: proxy-agent-installer\n  namespace:  prom-abcd\n---\napiVersion: rbac.authorization.k8s.io/v1\nkind: ClusterRoleBinding\nmetadata:\n  name: install-proxy-agent\nroleRef:\n  apiGroup: rbac.authorization.k8s.io\n  kind: ClusterRole\n  name: cluster-admin\nsubjects:\n- kind: ServiceAccount\n  name: proxy-agent-installer\n  namespace:  prom-abcd\n---\napiVersion: batch/v1\nkind: Job\nmetadata:\n  name: proxy-agent-installer\n  namespace: prom-abcd\nspec:\n  backoffLimit: 5\n  ttlSecondsAfterFinished: 60\n  template:\n    spec:\n      tolerations:\n      - operator: Exists\n      serviceAccountName: proxy-agent-installer\n      containers:\n      - name: installer\n        image: ccr.ccs.tencentyun.com/cloudmonitor/agent-installer:v0.0.3\n        args:\n        - upgrade \n        - tmp\n        - ./\n        - --install\n        - -n\n        - prom-abcd\n        - --set\n        - proxyAgent.enabled=true\n        - --set \n        - proxyAgent.instanceId=prom-abcd\n        - --set\n        - proxyAgent.instanceToken=token\n        - --set\n        - proxyAgent.clusterId=ecls-abcd\n        - --set\n        - proxyAgent.clusterType=external\n        - --set\n        - proxyAgent.serverAddress=1.1.1.1:8008\n        - --set\n        - proxyAgent.image=ccr.ccs.tencentyun.com/cloudmonitor/multi-proxy:v1.0.12\n        - --set\n        - kubeStateMetrics.enabled=true\n        - --set\n        - kubeStateMetrics.image=ccr.ccs.tencentyun.com/cloudmonitor/tmp-kube-state-metrics:v2.6.0-shard\n        - --set\n        - nodeExporter.enabled=true\n        - --set\n        - nodeExporter.image=ccr.ccs.tencentyun.com/tkeimages/node-exporter:v1.3.1\n      restartPolicy: Never\n",
        "RequestId": "r3mh2ud5r9568u-e4n3tdamu8uqkwvfu"
    }
}
```

