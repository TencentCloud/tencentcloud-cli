**Example 1: 获取kube-apiserver状态**



Input: 

```
tccli tke DescribeMasterComponent --cli-unfold-argument  \
    --ClusterId cls-pd41w15e \
    --Component kube-apiserver
```

Output: 
```
{
    "Response": {
        "RequestId": "1ac0d3ae-063e-4789-93fe-3c73e93191b9",
        "Component": "kube-apiserver",
        "Status": "Shutdown"
    }
}
```

