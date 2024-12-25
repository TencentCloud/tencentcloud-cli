**Example 1: 部署组列表**



Input: 

```
tccli tsf DescribeContainerGroupAttribute --cli-unfold-argument  \
    --GroupId group-ab958z6y
```

Output: 
```
{
    "Response": {
        "RequestId": "d1b09f98-d331-4de4-8560-d8915775fa37",
        "Result": {
            "ClusterIp": "9.166.255.154",
            "CurrentNum": 1,
            "Envs": [
                {
                    "Name": "JAVA_TOOL_OPTIONS",
                    "Value": " -Xloggc:/data/tsf_apm/monitor/jvm-metrics/gclog.log ",
                    "ValueFrom": null
                },
                {
                    "Name": "SERVICE_AGENT_VERSION",
                    "Value": "none",
                    "ValueFrom": null
                },
                {
                    "Name": "OT_AGENT_VERSION",
                    "Value": "none",
                    "ValueFrom": null
                },
                {
                    "Name": "tsf_app_id",
                    "Value": "1300555551",
                    "ValueFrom": null
                },
                {
                    "Name": "tsf_application_id",
                    "Value": "application-vz6mr4pa",
                    "ValueFrom": null
                },
                {
                    "Name": "tsf_cluster_id",
                    "Value": "cls-n6e3qw5s",
                    "ValueFrom": null
                },
                {
                    "Name": "tsf_namespace_id",
                    "Value": "namespace-vkoezbka",
                    "ValueFrom": null
                },
                {
                    "Name": "tsf_group_id",
                    "Value": "group-ab958z6y",
                    "ValueFrom": null
                },
                {
                    "Name": "tsf_prog_version",
                    "Value": "20230410145308",
                    "ValueFrom": null
                },
                {
                    "Name": "tsf_token",
                    "Value": "MFM-p5wTm0Hj__K_ri4Nui4QV-W51_ETokA1toi_AV8=",
                    "ValueFrom": null
                },
                {
                    "Name": "tsf_region",
                    "Value": "ap-guangzhou",
                    "ValueFrom": null
                },
                {
                    "Name": "tsf_ratelimit_master_ip",
                    "Value": "169.254.0.77",
                    "ValueFrom": null
                },
                {
                    "Name": "tsf_ratelimit_master_port",
                    "Value": "7000",
                    "ValueFrom": null
                },
                {
                    "Name": "tsf_consul_ip",
                    "Value": "169.254.0.77",
                    "ValueFrom": null
                },
                {
                    "Name": "tsf_consul_port",
                    "Value": "8000",
                    "ValueFrom": null
                },
                {
                    "Name": "JAVA_OPTS",
                    "Value": "-Xms128m -Xmx512m -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=512m",
                    "ValueFrom": null
                },
                {
                    "Name": "tsf_event_master_ip",
                    "Value": "169.254.0.77",
                    "ValueFrom": null
                },
                {
                    "Name": "tsf_event_master_port",
                    "Value": "15200",
                    "ValueFrom": null
                }
            ],
            "HealthCheckSettings": {
                "LivenessProbe": null,
                "ReadinessProbe": null
            },
            "InstanceNum": 1,
            "IsNotEqualServiceConfig": false,
            "LbDns": "dns.com",
            "LbIp": "119.29.122.212",
            "Message": "this is a  msg",
            "NodePort": 30111,
            "Status": "Running",
            "SubnetId": ""
        }
    }
}
```

