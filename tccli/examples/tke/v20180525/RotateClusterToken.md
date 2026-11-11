**Example 1: 轮转集群的token**



Input: 

```
tccli tke RotateClusterToken --cli-unfold-argument  \
    --ClusterId cls-h92i9b7e \
    --Force True \
    --ClusterType TKE \
    --Operation CreateNewToken
```

Output: 
```
{
    "Response": {
        "RequestId": "8859cd95-1c52-48fd-a100-600d9bfea6b1"
    }
}
```

