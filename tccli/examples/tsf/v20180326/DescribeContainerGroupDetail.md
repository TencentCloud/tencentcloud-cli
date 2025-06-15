**Example 1: DescribeContainerGroupDetail**



Input: 

```
tccli tsf DescribeContainerGroupDetail --cli-unfold-argument  \
    --GroupId group-6a79x94v
```

Output: 
```
{
    "Response": {
        "Result": {
            "UpdatedTime": 0,
            "HealthCheckSettings": {
                "ReadinessProbe": {
                    "Type": "tcp",
                    "TimeoutSeconds": 1,
                    "InitialDelaySeconds": 1,
                    "ActionType": "TCP",
                    "Command": [
                        "sh health.sh"
                    ],
                    "PeriodSeconds": 1,
                    "Path": "/health",
                    "SuccessThreshold": 1,
                    "Scheme": "http",
                    "Port": 1,
                    "FailureThreshold": 1
                },
                "LivenessProbe": {
                    "TimeoutSeconds": 1,
                    "InitialDelaySeconds": 1,
                    "ActionType": "TCP",
                    "Command": [
                        "sh health.sh"
                    ],
                    "PeriodSeconds": 1,
                    "Path": "/health",
                    "SuccessThreshold": 1,
                    "Scheme": "http",
                    "Port": 1,
                    "FailureThreshold": 1
                }
            },
            "InstanceNum": 1,
            "NamespaceName": "default",
            "MaxUnavailable": "25%",
            "ApplicationType": "C",
            "CurrentNum": 1,
            "MicroserviceType": "DEF",
            "Status": "Running",
            "LbIp": "10.23.29.11",
            "MemRequest": "0.5",
            "AccessType": 1,
            "UpdateIvl": 10,
            "Envs": [
                {
                    "Name": "consul_ip",
                    "Value": "10.29.26.11"
                },
                {
                    "Name": "host",
                    "Value": "hostName"
                }
            ],
            "TagName": "v1",
            "ClusterIp": "10.29.1.2",
            "MemLimit": "512",
            "CpuLimit": "1",
            "ApplicationId": "application-6a79x94v",
            "ApplicationName": "applicaiton-name",
            "ProtocolPorts": [
                {
                    "TargetPort": 30032,
                    "Protocol": "tcp",
                    "Port": 30032,
                    "NodePort": 0
                }
            ],
            "UpdateType": 1,
            "ClusterId": "cls-6a79x94v",
            "MaxSurge": "25%",
            "Server": "ccr.tencent.com",
            "SubnetId": "subnet-6a79x94v",
            "NodePort": 30870,
            "GroupId": "group-6a79x94v",
            "GroupResourceType": "C",
            "InstanceCount": 1,
            "GroupName": "test-group",
            "ClusterName": "k8s-cluster",
            "CreateTime": "2022-11-22 09:27:11",
            "Reponame": "nginx",
            "CpuRequest": "0.5",
            "Message": "this is a msg",
            "NamespaceId": "namespace-6a79x94v",
            "AllowPlainYamlDeploy": true,
            "IsNotEqualServiceConfig": true,
            "RepoName": "nginx",
            "Alias": "this is a alias"
        },
        "RequestId": "96561cf1-738a-47d6-943b-dec7ebbccabe"
    }
}
```

