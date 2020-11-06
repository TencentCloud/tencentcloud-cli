**Example 1: 修改实例带宽上限**

修改实例带宽上限

Input: 

```
tccli ecm ResetInstancesMaxBandwidth --cli-unfold-argument  \
    --InstanceIdSet ein-592937kl ein-958392ko \
    --MaxBandwidthOut 50
```

Output: 
```
{
    "Response": {
        "RequestId": "oe333tw8-03g7-4ss0-y7sj-76a0921a2390"
    }
}
```

