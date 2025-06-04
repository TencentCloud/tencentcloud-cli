**Example 1: 查看外部集群 Agent 卸载命令**



Input: 

```
tccli monitor DescribeExternalClusterUninstallCommand --cli-unfold-argument  \
    --InstanceId prom-abcd \
    --ClusterId ecls-abcd
```

Output: 
```
{
    "Response": {
        "Command": "\n---\napiVersion: v1\nkind: ServiceAccount\nmetadata:\n  name: tmp-uninstaller\n  namespace: default\n---\napiVersion: rbac.authorization.k8s.io/v1\nkind: ClusterRoleBinding\nmetadata:\n  name: tmp-uninstaller\nroleRef:\n  apiGroup: rbac.authorization.k8s.io\n  kind: ClusterRole\n  name: cluster-admin\nsubjects:\n- kind: ServiceAccount\n  name: tmp-uninstaller\n  namespace: default\n---\napiVersion: batch/v1\nkind: Job\nmetadata:\n  name: tmp-uninstaller\n  namespace: default\nspec:\n  backoffLimit: 2\n  ttlSecondsAfterFinished: 10\n  template:\n    spec:\n      tolerations:\n      - operator: Exists\n      serviceAccountName: tmp-uninstaller\n      containers:\n      - name: uninstaller\n        image: ccr.ccs.tencentyun.com/cloudmonitor/agent-installer:v0.0.9\n        command:\n        - uninstall\n        args:\n        - all \n        - prom-abcd\n      restartPolicy: Never\n",
        "RequestId": "bfa18d10-fe18-4f0e-b7e8-18857f951655"
    }
}
```

