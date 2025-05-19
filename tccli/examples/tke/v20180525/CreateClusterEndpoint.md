**Example 1: 创建集群访问端口**

创建集群访问端口

Input: 

```
tccli tke CreateClusterEndpoint --cli-unfold-argument  \
    --SubnetId subnet-e55paxnt \
    --ClusterId cls-e55paxnt \
    --IsExtranet True \
    --SecurityGroup sg-e55paxnt \
    --ExtensiveParameters {"InternetAccessible":{"InternetChargeType":"TRAFFIC_POSTPAID_BY_HOUR","InternetMaxBandwidthOut":200}}
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

