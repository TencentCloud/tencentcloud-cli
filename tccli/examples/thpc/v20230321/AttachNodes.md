**Example 1: 绑定计算节点到集群**

本接口 (AttachNodes) 用于绑定一个或者多个计算节点指定资源到指定集群中。

Input: 

```
tccli thpc AttachNodes --cli-unfold-argument  \
    --ClusterId hpc-2j8ntf9l \
    --QueueName compute \
    --ImageId img-39ywauzd \
    --ResourceType CVM \
    --ResourceSet ins-7i4yut4b \
    --UserData IyEvYmluL2Jhc2gKZWNobyAiSGFwcHnvvIEgVGhlIHRpbWUgaXMgbm93ICQoZGF0ZSAtUikhIiA+ICAvdG1wL3Vzcl9kYXRhLnR4dA== \
    --SkipResetInstance False
```

Output: 
```
{
    "Response": {
        "RequestId": "e81d404b-4fa2-49de-bce7-6499a3529f04"
    }
}
```

