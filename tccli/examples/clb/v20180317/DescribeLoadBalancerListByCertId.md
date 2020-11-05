**Example 1: Querying CLB instances associated with a specified certificate ID (instances found)**



Input: 

```
tccli clb DescribeLoadBalancerListByCertId --cli-unfold-argument  \
    --CertIds Rrsw4nIA
```

Output: 
```
{
    "Response": {
        "CertSet": [
            {
                "CertId": "Rrsw4nIA",
                "LoadBalancers": [
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
                        "StatusTime": "2019-07-02 21:50:07",
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
                            "VpcId": "vpc-lt9uj4mo"
                        },
                        "SubnetId": "",
                        "SecureGroups": [],
                        "Tags": [],
                        "VipIsp": "BGP",
                        "MasterZone": null,
                        "BackupZoneSet": null,
                        "IsolatedTime": null,
                        "ExpireTime": null,
                        "ChargeType": null,
                        "NetworkAttributes": null,
                        "PrepaidAttributes": null
                    }
                ]
            }
        ],
        "RequestId": "7718d187-7684-4294-954b-1e13009d75f6"
    }
}
```

**Example 2: Querying CLB instances associated with a specified certificate ID (no instances found)**



Input: 

```
tccli clb DescribeLoadBalancerListByCertId --cli-unfold-argument  \
    --CertIds RwFAfr8Y
```

Output: 
```
{
    "Response": {
        "CertSet": [
            {
                "CertId": "RwFAfr8Y",
                "LoadBalancers": []
            }
        ],
        "RequestId": "fe6059b5-faa6-4f21-92a1-0c9ee5df5e54"
    }
}
```

