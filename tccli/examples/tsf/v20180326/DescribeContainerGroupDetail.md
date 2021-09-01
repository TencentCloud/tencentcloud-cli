**Example 1: DescribeContainerGroupDetail**



Input: 

```
tccli tsf DescribeContainerGroupDetail --cli-unfold-argument  \
    --GroupId group-xxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "9ae18b81-51b8-461c-816a-b0310461a7e4",
        "Result": {
            "ProtocolPorts": [
                {
                    "Protocol": "TCP",
                    "Port": 30032,
                    "TargetPort": 30032
                }
            ],
            "Server": "ccr.ccs.tencentyun.com",
            "ApplicationType": "C",
            "InstanceNum": 1,
            "MicroserviceType": "N",
            "GroupId": "group-xxxxxxx",
            "UpdateIvl": 10,
            "Envs": [
                {
                    "Name": "tsf_consul_ip",
                    "Value": "169.254.0.77"
                },
                {
                    "Name": "tsf_consul_port",
                    "Value": "8000"
                },
                {
                    "Name": "JAVA_OPTS",
                    "Value": "-Xms128m -Xmx512m -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=512m"
                },
                {
                    "Name": "PATH",
                    "Value": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
                },
                {
                    "Name": "LANG",
                    "Value": "en_US.UTF-8"
                },
                {
                    "Name": "tsf_app_id",
                    "Value": "1256959311"
                },
                {
                    "Name": "tsf_token",
                    "Value": "dx8GUa5yTfSgS4Hk4oy1ru3AFvCDaaD7vwiA_liWcYg="
                },
                {
                    "Name": "tsf_application_id",
                    "Value": "application-by8prkka"
                },
                {
                    "Name": "tsf_cluster_id",
                    "Value": "cls-hvk70jjx"
                },
                {
                    "Name": "tsf_namespace_id",
                    "Value": "namespace-qabqneal"
                },
                {
                    "Name": "tsf_group_id",
                    "Value": "group-gyqpkzda"
                },
                {
                    "Name": "tsf_prog_version",
                    "Value": "jenkins-test-advertisement-admin-1"
                },
                {
                    "Name": "tsf_ratelimit_master_ip",
                    "Value": "169.254.0.77"
                },
                {
                    "Name": "tsf_ratelimit_master_port",
                    "Value": "7000"
                }
            ],
            "ClusterId": "cls-xxxxxxx",
            "NodePort": 30870,
            "CpuRequest": "0.54",
            "LbIp": "",
            "AccessType": 2,
            "MemRequest": "1024",
            "ClusterName": "test",
            "CurrentNum": 1,
            "ApplicationName": "test",
            "NamespaceName": "test",
            "CpuLimit": "1.08",
            "TagName": "test",
            "Message": "",
            "MemLimit": "2048.00",
            "GroupName": "test",
            "Reponame": "tsf_100006xxxxxxx/xxxxxxxx",
            "CreateTime": "2019-05-27 14:58:59",
            "NamespaceId": "namespace-xxxxxxx",
            "InstanceCount": 1,
            "ApplicationId": "application-xxxxxxx",
            "UpdateType": 1,
            "ClusterIp": "172.16.255.29",
            "Status": "Updating"
        }
    }
}
```

