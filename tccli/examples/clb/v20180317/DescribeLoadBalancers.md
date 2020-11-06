**Example 1: Querying the CLB instance with a specified private IP of the real server bound to it**

This example shows you how to query the CLB instance bound to the real server whose private IP is 172.26.0.11.

Input: 

```
tccli clb DescribeLoadBalancers --cli-unfold-argument  \
    --WithRs 1 \
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

**Example 2: Fuzzy querying CLB instances by name, domain name, and VIP**



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

**Example 3: Querying by CLB instance ID**



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

**Example 4: Querying by CLB instance type, project, name, and VIP**



Input: 

```
tccli clb DescribeLoadBalancers --cli-unfold-argument  \
    --LoadBalancerType OPEN \
    --ProjectId 0 \
    --LoadBalancerName test_LB \
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

