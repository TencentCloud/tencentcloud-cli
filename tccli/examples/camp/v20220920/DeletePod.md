**Example 1: 删除pod固定IP和PVC**



Input: 

```
tccli camp DeletePod --cli-unfold-argument  \
    --DeletePodIP True \
    --DeletePVC True
```

Output: 
```
{
    "Response": {
        "RequestId": "cd0fc7c6-93c4-4f19-9594-c4b157f624c8"
    }
}
```

