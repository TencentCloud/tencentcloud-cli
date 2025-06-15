**Example 1: 停机kube-apiserver**



Input: 

```
tccli tke ModifyMasterComponent --cli-unfold-argument  \
    --ClusterId cls-pd41w15e \
    --Component kube-apiserver \
    --Operation shutdown \
    --DryRun False
```

Output: 
```
{
    "Response": {
        "RequestId": "1ac0d3ae-063e-4789-93fe-3c73e93191b9"
    }
}
```

