**Example 1: test**



Input: 

```
tccli tdmq CreateClusterOpt --cli-unfold-argument  \
    --ClusterType share \
    --ClusterResource cvm \
    --ClusterName test-cluster \
    --AdminUrl 9.218.28.122:8080 \
    --TracingReport 1.1.1.1:8000 \
    --TracingToken toekn:abcdef \
    --ClbInstanceId lb-abcdefg \
    --BrokerIps 9.139.216.25 9.139.216.29 9.139.216.46 \
    --BookieIps 9.218.28.110 9.218.19.20 9.218.30.124 \
    --BrokerZookeeperIps 9.218.30.58 9.218.18.184 9.218.23.66 \
    --BookieZookeeperIps 9.139.216.47 9.139.216.6 \
    --BrokerSpecification 0 \
    --ProtocolList PULSAR \
    --IsBookieZkTse False \
    --IsBrokerZkTse True \
    --NetworkTypes Public Vpc \
    --MaxBandwidthOut 100
```

Output: 
```
{
    "Response": {
        "RequestId": "029f3725-9dab-4f79-870e-b37d43704b7f"
    }
}
```

