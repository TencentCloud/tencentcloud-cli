**Example 1: 在私有集群安装agent**

注意：只有未安装过agent或者kubeflow相关组件的集群需要安装。

Input: 

```
tccli tia InstallAgent --cli-unfold-argument  \
    --Cluster cls-xxxxxxxx \
    --TiaVersion xxxx-xx-xx
```

Output: 
```
{
    "Response": {
        "TiaVersion": "xxxx",
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

