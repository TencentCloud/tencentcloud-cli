**Example 1: 检查节点是否可升级**



Input: 

```
tccli tke CheckInstancesUpgradeAble --cli-unfold-argument  \
    --ClusterId cls-xxxxxx \
    --InstanceIds ins-q40fqbso ins-hvldgo6w ins-hrtaxazg
```

Output: 
```
{
    "Response": {
        "ClusterVersion": "1.14.3-tk8s-v1.1-1",
        "LatestVersion": "1.14.3-tk8s-v1.1-1",
        "Total": 3,
        "RequestId": "123",
        "UpgradeAbleInstances": [
            {
                "InstanceId": "ins-q40fqbso",
                "LatestVersion": "xx",
                "Version": "1.14.3-tk8s-v1.0"
            },
            {
                "InstanceId": "ins-hvldgo6w",
                "LatestVersion": "xx",
                "Version": "1.14.3-tk8s-v1.0"
            },
            {
                "InstanceId": "ins-hrtaxazg",
                "LatestVersion": "xx",
                "Version": "1.14.3-tk8s-v1.0"
            }
        ]
    }
}
```

