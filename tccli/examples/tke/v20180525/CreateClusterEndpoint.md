**Example 1: 创建集群访问端口**

创建集群访问端口

Input: 

```
tccli tke CreateClusterEndpoint --cli-unfold-argument  \
    --SubnetId subnet-xxxxxx \
    --ClusterId cls-xxxxxxxx \
    --IsExtranet True \
    --SecurityGroup sg-xxxxx \
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

