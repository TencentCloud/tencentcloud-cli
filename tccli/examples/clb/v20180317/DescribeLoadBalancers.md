**Example 1: 查询后端绑定了指定内网IP的机器的负载均衡**

查询绑定了内网IP为172.26.0.11的后端服务的负载均衡实例

Input: 

```
tccli clb DescribeLoadBalancers --cli-unfold-argument  \
    --WithRs 1\
    --BackendPrivateIps 172.26.0.11
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "LoadBalancerSet": [
            {
                "LoadBalancerId": "lb-rbw529fz",
                "LoadBalancerName": "test_LB",
                "Forward": 1,
                "Domain": "",
                "LoadBalancerVips": [
                    "129.226.78.67"
                ],
                "LoadBalancerType": "OPEN",
                "Status": 1,
                "CreateTime": "2019-07-02 18:12:52",
                "StatusTime": "2019-07-02 18:12:53",
                "ProjectId": 0,
                "OpenBgp": 0,
                "Snat": false,
                "Isolation": 0,
                "Log": "",
                "AnycastZone": "",
                "AddressIPVersion": "ipv4",
                "VpcId": "vpc-lt9uj4mo",
                "NumericalVpcId": 117008,
                "TargetRegionInfo": {
                    "Region": "ap-hongkong",
                    "VpcId": "vpc-lt9uj12o"
                },
                "SubnetId": "",
                "SecureGroups": [],
                "Tags": [],
                "VipIsp": "BGP",
                "MasterZone": null,
                "BackupZoneSet": null,
                "IsolatedTime": null,
                "ExpireTime": "2019-08-02 18:12:52",
                "ChargeType": "POSTPAID_BY_HOUR",
                "NetworkAttributes": {
                    "InternetChargeType": "BANDWIDTH_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 10
                },
                "PrepaidAttributes": null
            }
        ],
        "RequestId": "eba822a4-67cb-414c-b21d-f98ba3995d12"
    }
}
```

**Example 2: 根据名称、域名、VIP多个字段模糊查询负载均衡实例**



Input: 

```
tccli clb DescribeLoadBalancers --cli-unfold-argument  \
    --SearchKey test_LB
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LoadBalancerSet": [
            {
                "LoadBalancerId": "lb-rbw529fz",
                "LoadBalancerName": "test_LB",
                "Forward": 1,
                "Domain": "",
                "LoadBalancerVips": [
                    "129.226.78.67"
                ],
                "LoadBalancerType": "OPEN",
                "Status": 1,
                "CreateTime": "2019-07-02 18:12:52",
                "StatusTime": "2019-07-02 18:12:53",
                "ProjectId": 0,
                "OpenBgp": 0,
                "Snat": false,
                "Isolation": 0,
                "Log": "",
                "AnycastZone": "",
                "AddressIPVersion": "ipv4",
                "VpcId": "vpc-lt9uj4mo",
                "NumericalVpcId": 117008,
                "TargetRegionInfo": {
                    "Region": "ap-hongkong",
                    "VpcId": "vpc-lt9uj12o"
                },
                "SubnetId": "",
                "SecureGroups": [],
                "Tags": [],
                "VipIsp": "BGP",
                "MasterZone": null,
                "BackupZoneSet": null,
                "IsolatedTime": null,
                "ExpireTime": "2019-08-02 18:12:52",
                "ChargeType": "POSTPAID_BY_HOUR",
                "NetworkAttributes": {
                    "InternetChargeType": "BANDWIDTH_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 10
                },
                "PrepaidAttributes": null
            }
        ],
        "RequestId": "eba822a4-67cb-414c-b21d-f98ba3995d12"
    }
}
```

**Example 3: 根据负载均衡实例ID来查询**



Input: 

```
tccli clb DescribeLoadBalancers --cli-unfold-argument  \
    --LoadBalancerIds lb-rbw529fz
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LoadBalancerSet": [
            {
                "LoadBalancerId": "lb-rbw529fz",
                "LoadBalancerName": "test_LB",
                "Forward": 1,
                "Domain": "",
                "LoadBalancerVips": [
                    "129.226.78.67"
                ],
                "LoadBalancerType": "OPEN",
                "Status": 1,
                "CreateTime": "2019-07-02 18:12:52",
                "StatusTime": "2019-07-02 18:12:53",
                "ProjectId": 0,
                "OpenBgp": 0,
                "Snat": false,
                "Isolation": 0,
                "Log": "",
                "AnycastZone": "",
                "AddressIPVersion": "ipv4",
                "VpcId": "vpc-lt9uj4mo",
                "NumericalVpcId": 117008,
                "TargetRegionInfo": {
                    "Region": "ap-hongkong",
                    "VpcId": "vpc-lt9uj12o"
                },
                "SubnetId": "",
                "SecureGroups": [],
                "Tags": [],
                "VipIsp": "BGP",
                "MasterZone": null,
                "BackupZoneSet": null,
                "IsolatedTime": null,
                "ExpireTime": "2019-08-02 18:12:52",
                "ChargeType": "POSTPAID_BY_HOUR",
                "NetworkAttributes": {
                    "InternetChargeType": "BANDWIDTH_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 10
                },
                "PrepaidAttributes": null
            }
        ],
        "RequestId": "eba822a4-67cb-414c-b21d-f98ba3995d12"
    }
}
```

**Example 4: 根据负载均衡类型、所属项目、负载均衡名称、负载均衡实例的vip来查询**



Input: 

```
tccli clb DescribeLoadBalancers --cli-unfold-argument  \
    --LoadBalancerType OPEN\
    --ProjectId 0\
    --LoadBalancerName test_LB\
    --LoadBalancerVips 129.226.78.67
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LoadBalancerSet": [
            {
                "LoadBalancerId": "lb-rbw529fz",
                "LoadBalancerName": "test_LB",
                "Forward": 1,
                "Domain": "",
                "LoadBalancerVips": [
                    "129.226.78.67"
                ],
                "LoadBalancerType": "OPEN",
                "Status": 1,
                "CreateTime": "2019-07-02 18:12:52",
                "StatusTime": "2019-07-02 18:12:53",
                "ProjectId": 0,
                "OpenBgp": 0,
                "Snat": false,
                "Isolation": 0,
                "Log": "",
                "AnycastZone": "",
                "AddressIPVersion": "ipv4",
                "VpcId": "vpc-lt9uj4mo",
                "NumericalVpcId": 117008,
                "TargetRegionInfo": {
                    "Region": "ap-hongkong",
                    "VpcId": "vpc-lt9uj12o"
                },
                "SubnetId": "",
                "SecureGroups": [],
                "Tags": [],
                "VipIsp": "BGP",
                "MasterZone": null,
                "BackupZoneSet": null,
                "IsolatedTime": null,
                "ExpireTime": "2019-08-02 18:12:52",
                "ChargeType": "POSTPAID_BY_HOUR",
                "NetworkAttributes": {
                    "InternetChargeType": "BANDWIDTH_POSTPAID_BY_HOUR",
                    "InternetMaxBandwidthOut": 10
                },
                "PrepaidAttributes": null
            }
        ],
        "RequestId": "eba822a4-67cb-414c-b21d-f98ba3995d12"
    }
}
```

