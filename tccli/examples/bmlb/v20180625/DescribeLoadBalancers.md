**Example 1: 获取黑石负载均衡实例列表**



Input: 

```
tccli bmlb DescribeLoadBalancers --cli-unfold-argument  \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "LoadBalancerSet": [
            {
                "LoadBalancerId": "lb-ltud7t8n",
                "ProjectId": 0,
                "LoadBalancerName": "ami-v6-bak",
                "LoadBalancerType": "open",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "604.bj.251000873.hslb.myqcloud.com",
                "VpcId": "vpc-34cxlz7z",
                "SubnetId": "",
                "Status": 1,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-11-05 20:15:33",
                "StatusTime": "2018-11-06 11:52:13",
                "VpcName": "test",
                "VpcCidrBlock": "10.10.0.0/16",
                "LoadBalancerVips": [
                    "115.159.240.89"
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "lbcfg-5xumxrad",
                "ConfName": "guangda-test",
                "LoadBalancerVipv6s": [
                    "2402:4E00:20:100::2:242"
                ],
                "IpProtocolType": "ipv6",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-84k4a2rp",
                "ProjectId": 0,
                "LoadBalancerName": "ami-v6",
                "LoadBalancerType": "open",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "5fc.bj.251000873.hslb.myqcloud.com",
                "VpcId": "vpc-34cxlz7z",
                "SubnetId": "",
                "Status": 1,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-10-31 11:26:35",
                "StatusTime": "2018-11-06 10:28:30",
                "VpcName": "test",
                "VpcCidrBlock": "10.10.0.0/16",
                "LoadBalancerVips": [
                    "115.159.240.25"
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "lbcfg-5xumxrad",
                "ConfName": "guangda-test",
                "LoadBalancerVipv6s": [
                    "2402:4E00:20:100::2:232"
                ],
                "IpProtocolType": "ipv6",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-f5elebdb",
                "ProjectId": 0,
                "LoadBalancerName": "ami-v4",
                "LoadBalancerType": "open",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "5fb.bj.251000873.hslb.myqcloud.com",
                "VpcId": "vpc-34cxlz7z",
                "SubnetId": "",
                "Status": 1,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-10-31 11:02:24",
                "StatusTime": "2018-11-06 10:28:30",
                "VpcName": "test",
                "VpcCidrBlock": "10.10.0.0/16",
                "LoadBalancerVips": [
                    "115.159.240.53"
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "lbcfg-5xumxrad",
                "ConfName": "guangda-test",
                "LoadBalancerVipv6s": [
                    ""
                ],
                "IpProtocolType": "ipv4",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-cnmtiz1j",
                "ProjectId": 0,
                "LoadBalancerName": "B6hNQSrERg5lxUh-0",
                "LoadBalancerType": "",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "",
                "VpcId": "vpc-34cxlz7z",
                "SubnetId": "",
                "Status": 0,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-10-30 17:19:50",
                "StatusTime": "2018-10-30 17:19:50",
                "VpcName": "",
                "VpcCidrBlock": "",
                "LoadBalancerVips": [
                    ""
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "",
                "ConfName": "",
                "LoadBalancerVipv6s": [
                    ""
                ],
                "IpProtocolType": "ipv4",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-j3fugpgt",
                "ProjectId": 0,
                "LoadBalancerName": "NU2e49l75n2pArr-0",
                "LoadBalancerType": "",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "",
                "VpcId": "vpc-34cxlz7z",
                "SubnetId": "",
                "Status": 0,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-10-30 17:04:01",
                "StatusTime": "2018-10-30 17:04:01",
                "VpcName": "",
                "VpcCidrBlock": "",
                "LoadBalancerVips": [
                    ""
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "",
                "ConfName": "",
                "LoadBalancerVipv6s": [
                    ""
                ],
                "IpProtocolType": "ipv4",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-luvk0ve5",
                "ProjectId": 0,
                "LoadBalancerName": "D4hkBo9lh3rIs5x-0",
                "LoadBalancerType": "",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "",
                "VpcId": "vpc-34cxlz7z",
                "SubnetId": "",
                "Status": 0,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-10-30 16:59:55",
                "StatusTime": "2018-10-30 16:59:55",
                "VpcName": "",
                "VpcCidrBlock": "",
                "LoadBalancerVips": [
                    ""
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "",
                "ConfName": "",
                "LoadBalancerVipv6s": [
                    ""
                ],
                "IpProtocolType": "ipv4",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-9wem1d3f",
                "ProjectId": 0,
                "LoadBalancerName": "0goxvaS9ylRJFuR-0",
                "LoadBalancerType": "",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "",
                "VpcId": "vpc-muinpf9p",
                "SubnetId": "",
                "Status": 0,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-10-30 16:59:05",
                "StatusTime": "2018-10-30 16:59:05",
                "VpcName": "",
                "VpcCidrBlock": "",
                "LoadBalancerVips": [
                    ""
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "",
                "ConfName": "",
                "LoadBalancerVipv6s": [
                    ""
                ],
                "IpProtocolType": "ipv4",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-cxpsclzf",
                "ProjectId": 0,
                "LoadBalancerName": "中文测试",
                "LoadBalancerType": "internal",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "",
                "VpcId": "vpc-muinpf9p",
                "SubnetId": "subnet-c6bzyq4a",
                "Status": 1,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-10-30 16:15:40",
                "StatusTime": "2018-10-30 16:26:16",
                "VpcName": "cassiehe",
                "VpcCidrBlock": "10.1.0.0/16",
                "LoadBalancerVips": [
                    "100.68.210.137"
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "",
                "ConfName": "",
                "LoadBalancerVipv6s": [
                    ""
                ],
                "IpProtocolType": "ipv4",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-m1i50ynj",
                "ProjectId": 0,
                "LoadBalancerName": "5dd-LB",
                "LoadBalancerType": "open",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "5dd.bj.251000873.hslb.myqcloud.com",
                "VpcId": "vpc-34cxlz7z",
                "SubnetId": "",
                "Status": 1,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-10-22 14:47:49",
                "StatusTime": "2018-10-31 16:45:25",
                "VpcName": "test",
                "VpcCidrBlock": "10.10.0.0/16",
                "LoadBalancerVips": [
                    "115.159.240.26"
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "",
                "ConfName": "",
                "LoadBalancerVipv6s": [
                    ""
                ],
                "IpProtocolType": "ipv4",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-m2pg9nev",
                "ProjectId": 0,
                "LoadBalancerName": "5db-LB",
                "LoadBalancerType": "internal",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "",
                "VpcId": "vpc-muinpf9p",
                "SubnetId": "subnet-c6bzyq4a",
                "Status": 1,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-10-18 15:53:47",
                "StatusTime": "2018-10-18 15:55:57",
                "VpcName": "cassiehe",
                "VpcCidrBlock": "10.1.0.0/16",
                "LoadBalancerVips": [
                    "100.68.210.136"
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "",
                "ConfName": "",
                "LoadBalancerVipv6s": [
                    ""
                ],
                "IpProtocolType": "ipv4",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-gdr96fc7",
                "ProjectId": 0,
                "LoadBalancerName": "5c1-LB",
                "LoadBalancerType": "open",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "5c1.bj.251000873.hslb.myqcloud.com",
                "VpcId": "vpc-muinpf9p",
                "SubnetId": "",
                "Status": 1,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-10-11 15:28:56",
                "StatusTime": "2018-10-31 16:42:37",
                "VpcName": "cassiehe",
                "VpcCidrBlock": "10.1.0.0/16",
                "LoadBalancerVips": [
                    "115.159.240.85"
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "",
                "ConfName": "",
                "LoadBalancerVipv6s": [
                    ""
                ],
                "IpProtocolType": "ipv4",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-14gtclwh",
                "ProjectId": 0,
                "LoadBalancerName": "59a-LB",
                "LoadBalancerType": "open",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "59a.bj.251000873.hslb.myqcloud.com",
                "VpcId": "vpc-34cxlz7z",
                "SubnetId": "",
                "Status": 1,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-06-07 20:54:33",
                "StatusTime": "2018-10-31 19:44:12",
                "VpcName": "test",
                "VpcCidrBlock": "10.10.0.0/16",
                "LoadBalancerVips": [
                    "115.159.240.22"
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "",
                "ConfName": "",
                "LoadBalancerVipv6s": [
                    ""
                ],
                "IpProtocolType": "ipv4",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-iz8b4qnf",
                "ProjectId": 0,
                "LoadBalancerName": "bm_ccs_master_lb",
                "LoadBalancerType": "internal",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "",
                "VpcId": "vpc-muinpf9p",
                "SubnetId": "subnet-430cyb94",
                "Status": 1,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-04-08 16:16:12",
                "StatusTime": "2018-08-31 15:05:37",
                "VpcName": "cassiehe",
                "VpcCidrBlock": "10.1.0.0/16",
                "LoadBalancerVips": [
                    "100.68.210.135"
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "",
                "ConfName": "",
                "LoadBalancerVipv6s": [
                    ""
                ],
                "IpProtocolType": "ipv4",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-fxzj6q3x",
                "ProjectId": 0,
                "LoadBalancerName": "l2t6q4pfsswJgoa-0",
                "LoadBalancerType": "",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "",
                "VpcId": "vpc-34cxlz7z",
                "SubnetId": "",
                "Status": 0,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-04-04 16:12:09",
                "StatusTime": "2018-04-04 16:12:09",
                "VpcName": "",
                "VpcCidrBlock": "",
                "LoadBalancerVips": [
                    ""
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "",
                "ConfName": "",
                "LoadBalancerVipv6s": [
                    ""
                ],
                "IpProtocolType": "ipv4",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-9jmpocz3",
                "ProjectId": 0,
                "LoadBalancerName": "wDOmO0OFQjnTowN-0",
                "LoadBalancerType": "",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "",
                "VpcId": "vpc-34cxlz7z",
                "SubnetId": "",
                "Status": 0,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-04-04 16:10:51",
                "StatusTime": "2018-04-04 16:10:51",
                "VpcName": "",
                "VpcCidrBlock": "",
                "LoadBalancerVips": [
                    ""
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "",
                "ConfName": "",
                "LoadBalancerVipv6s": [
                    ""
                ],
                "IpProtocolType": "ipv4",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-hkp82hq9",
                "ProjectId": 0,
                "LoadBalancerName": "rG5HM7y9lhalTXn-0",
                "LoadBalancerType": "",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "",
                "VpcId": "vpc-34cxlz7z",
                "SubnetId": "",
                "Status": 0,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-04-04 16:02:07",
                "StatusTime": "2018-04-04 16:02:07",
                "VpcName": "",
                "VpcCidrBlock": "",
                "LoadBalancerVips": [
                    ""
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "",
                "ConfName": "",
                "LoadBalancerVipv6s": [
                    ""
                ],
                "IpProtocolType": "ipv4",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-2routcy3",
                "ProjectId": 0,
                "LoadBalancerName": "6HAamycPjXcGxDM-0",
                "LoadBalancerType": "",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "",
                "VpcId": "vpc-34cxlz7z",
                "SubnetId": "",
                "Status": 0,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-04-04 15:46:24",
                "StatusTime": "2018-04-04 15:46:24",
                "VpcName": "",
                "VpcCidrBlock": "",
                "LoadBalancerVips": [
                    ""
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "",
                "ConfName": "",
                "LoadBalancerVipv6s": [
                    ""
                ],
                "IpProtocolType": "ipv4",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-qgmbvx57",
                "ProjectId": 0,
                "LoadBalancerName": "3mC9VTP7uQlC2J3-0",
                "LoadBalancerType": "",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "",
                "VpcId": "vpc-34cxlz7z",
                "SubnetId": "",
                "Status": 0,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-04-04 15:46:13",
                "StatusTime": "2018-04-04 15:46:13",
                "VpcName": "",
                "VpcCidrBlock": "",
                "LoadBalancerVips": [
                    ""
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "",
                "ConfName": "",
                "LoadBalancerVipv6s": [
                    ""
                ],
                "IpProtocolType": "ipv4",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-2uuicurr",
                "ProjectId": 0,
                "LoadBalancerName": "ZuCUDyb1GuV3XsS-0",
                "LoadBalancerType": "",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "",
                "VpcId": "vpc-34cxlz7z",
                "SubnetId": "",
                "Status": 0,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-04-04 15:45:52",
                "StatusTime": "2018-04-04 15:45:52",
                "VpcName": "",
                "VpcCidrBlock": "",
                "LoadBalancerVips": [
                    ""
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "",
                "ConfName": "",
                "LoadBalancerVipv6s": [
                    ""
                ],
                "IpProtocolType": "ipv4",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            },
            {
                "LoadBalancerId": "lb-6t7dnny9",
                "ProjectId": 0,
                "LoadBalancerName": "iz88GADpAwbyFu6-0",
                "LoadBalancerType": "",
                "Exclusive": 0,
                "TgwSetType": "fullnat",
                "Domain": "",
                "VpcId": "vpc-34cxlz7z",
                "SubnetId": "",
                "Status": 0,
                "PayMode": "flow",
                "LatestPayMode": "flow",
                "CreateTime": "2018-04-04 15:45:09",
                "StatusTime": "2018-04-04 15:45:09",
                "VpcName": "",
                "VpcCidrBlock": "",
                "LoadBalancerVips": [
                    ""
                ],
                "SupportListenerTypes": [
                    "L4Listener",
                    "L7Listener"
                ],
                "Bandwidth": 0,
                "ConfId": "",
                "ConfName": "",
                "LoadBalancerVipv6s": [
                    ""
                ],
                "IpProtocolType": "ipv4",
                "BzPayMode": "",
                "BzL4Metrics": "",
                "BzL7Metrics": ""
            }
        ],
        "TotalCount": 26,
        "RequestId": "f83cade7-f5ed-432c-952e-23dee4767d9e"
    }
}
```

