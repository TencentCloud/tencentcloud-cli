**Example 1: 查询集群模式Vpc间防火墙开关**

查询集群模式Vpc间防火墙开关

Input: 

```
tccli cfw DescribeClusterVpcFwSwitchs --cli-unfold-argument  \
    --Limit 100 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AssetType": "ccn",
                "AttachIns": [
                    {
                        "InsId": "vpc-msa9dvac",
                        "InsName": "[autotest][勿删]自动化测试B"
                    },
                    {
                        "InsId": "vpc-q9h93ip4",
                        "InsName": "[autotest][勿删]自动化测试A"
                    },
                    {
                        "InsId": "vpc-o2m9s7za",
                        "InsName": "防火墙专用VPC_请勿删改"
                    }
                ],
                "FwType": "ew",
                "InsObj": "ccn-2stwf6cr",
                "IpVersion": 0,
                "NonCluster": 1,
                "ObjName": "[autotest][勿删]自动化测试",
                "Region": "",
                "Status": 0,
                "SwitchMode": 2
            },
            {
                "AssetType": "ccn",
                "AttachIns": [
                    {
                        "InsId": "vpc-7mwvn487",
                        "InsName": "gwlb-vpcfw-test1"
                    },
                    {
                        "InsId": "vpc-60fs07id",
                        "InsName": "gwlb-vpcfw-test2"
                    },
                    {
                        "InsId": "vpc-r1y8myh7",
                        "InsName": "gwlb-fwVpc专用vpc"
                    },
                    {
                        "InsId": "vpc-o06o1mld",
                        "InsName": "防火墙专用VPC_请勿删改"
                    }
                ],
                "FwType": "ew",
                "InsObj": "ccn-6vryyuzr",
                "IpVersion": 0,
                "NonCluster": 1,
                "ObjName": "gwlb-vpcfw使用--勿动",
                "Region": "",
                "Status": 0,
                "SwitchMode": 2
            },
            {
                "AssetType": "ccn",
                "AttachIns": [
                    {
                        "InsId": "vpc-48lxgvje",
                        "InsName": "fengqqian1"
                    },
                    {
                        "InsId": "vpc-ewm7iy2y",
                        "InsName": "fengqqian2"
                    }
                ],
                "FwType": "ew",
                "InsObj": "ccn-pmsxuvgn",
                "IpVersion": 0,
                "NonCluster": 0,
                "ObjName": "test",
                "Region": "",
                "Status": 0,
                "SwitchMode": 2
            }
        ],
        "RequestId": "0fc0816f-e356-49ad-a63c-2bdd8d185b43",
        "Total": 3
    }
}
```

