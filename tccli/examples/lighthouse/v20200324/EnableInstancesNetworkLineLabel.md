**Example 1: 为实例启用指定的网络线路标签**



Input: 

```
tccli lighthouse EnableInstancesNetworkLineLabel --cli-unfold-argument  \
    --InstanceIds lhins-1fvhioyz \
    --NetworkLineLabel HighQualityReturnBandwidth
```

Output: 
```
{
    "Response": {
        "RequestId": "d244fa0d-9d4d-48b9-8329-6b81db88ee45"
    }
}
```

