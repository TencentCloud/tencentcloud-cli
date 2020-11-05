**Example 1: Querying the cluster list**

This example shows you how to query your list of clusters.

Input: 

```
tccli tcaplusdb DescribeClusters --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Clusters": [
            {
                "ApiAccessId": "8",
                "ApiAccessIp": "10.18.7.15",
                "ApiAccessIpv6": "",
                "ApiAccessPort": 9999,
                "ClusterId": "5462425805",
                "ClusterName": "gz test application",
                "CreatedTime": "2019-12-04 11:28:16",
                "IdlType": "PROTO",
                "NetworkType": "vpc-normal",
                "OldPasswordExpireTime": "",
                "Password": "gz123AppTest56",
                "PasswordStatus": "modifiable",
                "Region": "ap-guangzhou",
                "SubnetId": "subnet-jq2cqev2",
                "VpcId": "vpc-oezt2hwl"
            },
            {
                "ApiAccessId": "2",
                "ApiAccessIp": "10.18.7.9",
                "ApiAccessIpv6": "2001:3CA1:010F:001A:121B:0000:0000:0010",
                "ApiAccessPort": 9999,
                "ClusterId": "6032569361",
                "ClusterName": "Thunder Fighter Test",
                "CreatedTime": "2019-12-25 11:54:02",
                "IdlType": "PROTO",
                "NetworkType": "vpc-normal",
                "OldPasswordExpireTime": "",
                "Password": "ltzj123123X",
                "PasswordStatus": "modifiable",
                "Region": "ap-guangzhou",
                "SubnetId": "subnet-jq2cqev2",
                "VpcId": "vpc-oezt2hwl"
            }
        ],
        "RequestId": "34680b61-9836-44d9-bae9-e231f4b61a48",
        "TotalCount": 2
    }
}
```

