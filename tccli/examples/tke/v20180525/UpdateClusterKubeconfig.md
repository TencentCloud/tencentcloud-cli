**Example 1: 更新集群的kubeconfig信息**

更新集群的kubeconfig信息

Input: 

```
tccli tke UpdateClusterKubeconfig --cli-unfold-argument  \
    --ClusterId cls-65r1c5nu \
    --SubAccounts 123456 123457 123458
```

Output: 
```
{
    "Response": {
        "UpdatedSubAccounts": [
            "123456",
            "123457",
            "1234568"
        ],
        "RequestId": "33483fde-efec-4d3c-8ff6-340d9dbc2d01"
    }
}
```

