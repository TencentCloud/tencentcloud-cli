**Example 1: 检查节点是否可升级**

检查节点是否可升级

Input: 

```
tccli tke CheckInstancesUpgradeAble --cli-unfold-argument  \
    --ClusterId cls-7ph3twqe \
    --InstanceIds ins-q40fqbso ins-hvldgo6w ins-hrtaxazg
```

Output: 
```
{
    "Response": {
        "ClusterVersion": "1.22.5",
        "LatestVersion": "1.22.5",
        "Total": 3,
        "RequestId": "342ea0aa-e45a-41dd-84f5-f7a2929d3fac",
        "UnavailableVersionReason": [
            {
                "InstanceId": "ins-mq0fqbso",
                "Reason": "instance already the master latest version"
            }
        ],
        "UpgradeAbleInstances": [
            {
                "InstanceId": "ins-q40fqbso",
                "LatestVersion": "1.22.5",
                "Version": "1.20.6",
                "RuntimeVersion": "docker-18.9",
                "RuntimeLatestVersion": "docker-18.9"
            },
            {
                "InstanceId": "ins-hvldgo6w",
                "LatestVersion": "1.22.5",
                "Version": "1.20.6",
                "RuntimeVersion": "docker-18.9",
                "RuntimeLatestVersion": "docker-18.9"
            },
            {
                "InstanceId": "ins-hrtaxazg",
                "LatestVersion": "1.22.5",
                "Version": "1.20.6",
                "RuntimeVersion": "docker-18.9",
                "RuntimeLatestVersion": "docker-18.9"
            }
        ]
    }
}
```

