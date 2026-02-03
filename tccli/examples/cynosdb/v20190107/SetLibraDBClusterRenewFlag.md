**Example 1: 修改分析集群续费模式**



Input: 

```
tccli cynosdb SetLibraDBClusterRenewFlag --cli-unfold-argument  \
    --ResourceIds libradb-ln26puh1 \
    --AutoRenewFlag 2
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "RequestId": "bf3ec59e-1973-4ee8-9c05-715af4fd3fac"
    }
}
```

