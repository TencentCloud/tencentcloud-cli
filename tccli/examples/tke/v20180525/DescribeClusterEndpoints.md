**Example 1: 获取集群访问地址**

获取集群访问地址

Input: 

```
tccli tke DescribeClusterEndpoints --cli-unfold-argument  \
    --ClusterId cls-65r1c5nu
```

Output: 
```
{
    "Response": {
        "CertificationAuthority": "",
        "ClusterIntranetDomain": "cls.domain",
        "ClusterExternalDomain": "cls.domain",
        "SecurityGroup": "sg-2quou3re",
        "ClusterExternalEndpoint": "12.34.56.78",
        "ClusterIntranetEndpoint": "10.0.0.1",
        "ClusterDomain": "cls-65r1c5nu.ccs.tencent-cloud.com",
        "ClusterExternalACL": [
            "10.0.0.0/24"
        ],
        "RequestId": "33483fde-efec-4d3c-8ff6-340d9dbc2d01"
    }
}
```

