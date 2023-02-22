**Example 1: 获取集群kubeconfig文件**

获取集群的kubeconfig文件，不同子账户获取自己的kubeconfig文件，该文件中有每个子账户自己的kube-apiserver的客户端证书，默认首次调此接口时候创建客户端证书，时效20年，未授予任何权限，如果是集群所有者或者主账户，则默认是cluster-admin权限。

Input: 

```
tccli tke DescribeClusterKubeconfig --cli-unfold-argument  \
    --ClusterId cls-65r1c5nu
```

Output: 
```
{
    "Response": {
        "Kubeconfig": "[REDACTED]",
        "RequestId": "33483fde-efec-4d3c-8ff6-340d9dbc2d01"
    }
}
```

