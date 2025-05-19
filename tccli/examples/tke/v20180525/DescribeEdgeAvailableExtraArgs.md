**Example 1: 查询集群可用的自定义参数**



Input: 

```
tccli tke DescribeEdgeAvailableExtraArgs --cli-unfold-argument  \
    --ClusterVersion 1.12.4
```

Output: 
```
{
    "Response": {
        "ClusterVersion": "1.12.4",
        "AvailableExtraArgs": {
            "KubeAPIServer": [
                {
                    "Name": "enable-admission-plugins",
                    "Type": "string",
                    "Usage": "Comma-delimited list of admission plugins to enable",
                    "Default": "NodeRestriction",
                    "Constraint": "Must be a valid admission plugin name"
                }
            ],
            "KubeControllerManager": [
                {
                    "Name": "node-cidr-mask-size",
                    "Type": "int",
                    "Usage": "Mask size for node CIDR in IPv4 or IPv6 networks",
                    "Default": "24",
                    "Constraint": "Must be a valid CIDR mask size"
                }
            ],
            "KubeScheduler": [
                {
                    "Name": "scheduler-name",
                    "Type": "string",
                    "Usage": "Name of the scheduler to use",
                    "Default": "default-scheduler",
                    "Constraint": "Must be a valid scheduler name"
                }
            ],
            "Kubelet": [
                {
                    "Name": "max-pods",
                    "Type": "int",
                    "Usage": "Maximum number of pods per node",
                    "Default": "110",
                    "Constraint": "Must be a positive integer"
                }
            ]
        },
        "RequestId": "d174dcb6-659b-4ab6-9533-e470a7d91e43"
    }
}
```

