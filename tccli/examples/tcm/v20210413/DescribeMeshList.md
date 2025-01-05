**Example 1: DescribeMeshList**



Input: 

```
tccli tcm DescribeMeshList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "MeshList": [
            {
                "ClusterList": [
                    {
                        "ClusterId": "cls-i3wbzkfl",
                        "Config": {
                            "AutoInjectionNamespaceList": [],
                            "AutoInjectionNamespaceStateList": [],
                            "DeployConfig": {
                                "NodeSelectType": "",
                                "Nodes": []
                            },
                            "EgressGatewayList": [],
                            "IngressGatewayList": [],
                            "Istiod": null
                        },
                        "DisplayName": "cluster-1",
                        "HostedNamespaces": [],
                        "LinkedTime": "2025-01-02T20:18:13+08:00",
                        "Region": "ap-shanghai",
                        "Role": "REMOTE",
                        "State": "RUNNING",
                        "Status": {
                            "LinkErrorDetail": "",
                            "LinkState": "LINKED"
                        },
                        "SubnetId": "subnet-c1nuvmu7",
                        "VpcId": "vpc-5x1y65ok",
                        "Type": "TKE"
                    }
                ],
                "Config": {
                    "AccessLog": {
                        "Address": "http://10.10.10.10",
                        "CLS": {
                            "Enable": true,
                            "NeedDelete": false,
                            "LogSet": "mesh-351lvuec",
                            "Region": "ap-shanghai",
                            "Topic": "mesh-351lvuec-accesslog"
                        },
                        "Enable": true,
                        "EnableServer": false,
                        "EnableStdout": true,
                        "Encoding": "JSON",
                        "Format": "{\n\t\"authority\": \"%REQ(:AUTHORITY)%\",\n\t\"bytes_received\": \"%BYTES_RECEIVED%\",\n\t\"bytes_sent\": \"%BYTES_SENT%\",\n\t\"downstream_local_address\": \"%DOWNSTREAM_LOCAL_ADDRESS%\",\n\t\"downstream_remote_address\": \"%DOWNSTREAM_REMOTE_ADDRESS%\",\n\t\"duration\": \"%DURATION%\",\n\t\"istio_policy_status\": \"%DYNAMIC_METADATA(istio.mixer:status)%\",\n\t\"method\": \"%REQ(:METHOD)%\",\n\t\"path\": \"%REQ(X-ENVOY-ORIGINAL-PATH?:PATH)%\",\n\t\"protocol\": \"%PROTOCOL%\",\n\t\"request_id\": \"%REQ(X-REQUEST-ID)%\",\n\t\"requested_server_name\": \"%REQUESTED_SERVER_NAME%\",\n\t\"response_code\": \"%RESPONSE_CODE%\",\n\t\"response_flags\": \"%RESPONSE_FLAGS%\",\n\t\"route_name\": \"%ROUTE_NAME%\",\n\t\"start_time\": \"%START_TIME%\",\n\t\"upstream_cluster\": \"%UPSTREAM_CLUSTER%\",\n\t\"upstream_host\": \"%UPSTREAM_HOST%\",\n\t\"upstream_local_address\": \"%UPSTREAM_LOCAL_ADDRESS%\",\n\t\"upstream_service_time\": \"%RESP(X-ENVOY-UPSTREAM-SERVICE-TIME)%\",\n\t\"upstream_transport_failure_reason\": \"%UPSTREAM_TRANSPORT_FAILURE_REASON%\",\n\t\"user_agent\": \"%REQ(USER-AGENT)%\",\n\t\"x_forwarded_for\": \"%REQ(X-FORWARDED-FOR)%\"\n}\n",
                        "SelectedRange": {
                            "All": true
                        },
                        "Template": "istio"
                    },
                    "Inject": {
                        "ExcludeIPRanges": [],
                        "HoldApplicationUntilProxyStarts": false,
                        "HoldProxyUntilApplicationEnds": false
                    },
                    "Istio": {
                        "DisableHTTPRetry": false,
                        "DisablePolicyChecks": true,
                        "EnablePilotHTTP": false,
                        "OutboundTrafficPolicy": "ALLOW_ANY",
                        "SmartDNS": {
                            "IstioMetaDNSAutoAllocate": true,
                            "IstioMetaDNSCapture": true
                        },
                        "Tracing": {
                            "Sampling": 0
                        }
                    },
                    "Prometheus": {
                        "InstanceId": "prom-63ad12yj",
                        "Region": "ap-shanghai",
                        "VpcId": "vpc-5x1y65ok",
                        "SubnetId": "subnet-c1nuvmu7",
                        "CustomProm": null
                    },
                    "SidecarResources": {
                        "Limits": [
                            {
                                "Name": "cpu",
                                "Quantity": "2"
                            },
                            {
                                "Name": "memory",
                                "Quantity": "1Gi"
                            }
                        ],
                        "Requests": [
                            {
                                "Name": "cpu",
                                "Quantity": "100m"
                            },
                            {
                                "Name": "memory",
                                "Quantity": "128Mi"
                            }
                        ]
                    },
                    "Tracing": {
                        "APM": {
                            "Region": "ap-shanghai",
                            "InstanceId": "apm-KlX5JAaaq",
                            "Enable": false
                        },
                        "Enable": false
                    }
                },
                "CreatedTime": "2025-01-02T10:50:01+08:00",
                "DisplayName": "mesh-for-test",
                "MeshId": "mesh-351lvuec",
                "Region": "ap-shanghai",
                "State": "RUNNING",
                "Status": {
                    "ActiveOperationList": null,
                    "CanaryVersion": "",
                    "Prometheus": null,
                    "ServiceCount": 43,
                    "StateMessage": "",
                    "TPS": {
                        "DisplayName": "mesh-351lvuec-prom-63ad12yj",
                        "Grafana": {
                            "Enabled": false,
                            "InternalURL": "",
                            "PublicFailedMessage": "",
                            "PublicFailedReason": "",
                            "PublicURL": ""
                        },
                        "InstanceId": "prom-63ad12yj",
                        "PrometheusId": "mesh-351lvuec-prom-63ad12yj",
                        "Region": "ap-shanghai",
                        "State": "RUNNING",
                        "Type": "tmp",
                        "VpcId": "vpc-5x1y65ok"
                    }
                },
                "TagList": [],
                "Type": "HOSTED",
                "UpdatedTime": "2025-01-02T20:50:08+08:00",
                "Version": "1.16.5"
            }
        ],
        "Total": 1
    }
}
```

