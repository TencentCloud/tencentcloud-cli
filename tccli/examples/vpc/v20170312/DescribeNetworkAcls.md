**Example 1: Example 1: Querying the network ACL list**



Input: 

```
tccli vpc DescribeNetworkAcls --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "NetworkAclSet": [
            {
                "VpcId": "vpc-12345678",
                "SubnetName": "acl-12345678",
                "NetworkAclName": "test",
                "CreatedTime": "2020-01-01 10:00:00",
                "SubnetSet": [
                    {
                        "SubnetId": "subnet-12345678",
                        "SubnetName": "test",
                        "CidrBlock": "172.16.12.0/24"
                    }
                ],
                "IngressEntries": [
                    {
                        "Protocol": "tcp",
                        "CidrBlock": "172.16.12.123/32",
                        "Action": "Accept",
                        "Description": "test",
                        "Port": 8080
                    },
                    {
                        "Protocol": "all",
                        "CidrBlock": "0.0.0.0/0",
                        "Action": "Drop",
                        "Description": ""
                    }
                ],
                "EgressEntries": [
                    {
                        "Protocol": "tcp",
                        "CidrBlock": "172.16.12.123/32",
                        "Action": "Accept",
                        "Description": "test",
                        "Port": 8080
                    },
                    {
                        "Protocol": "all",
                        "CidrBlock": "0.0.0.0/0",
                        "Action": "Drop",
                        "Description": ""
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "5efe6fa7-6de2-4ce9-911a-f7438bf697d4"
    }
}
```

**Example 2: Example 2: Querying the network ACL list by conditions**



Input: 

```
tccli vpc DescribeNetworkAcls --cli-unfold-argument  \
    --NetworkAclIds acl-12345678 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "NetworkAclSet": [
            {
                "VpcId": "vpc-12345678",
                "NetworkAclId": "acl-12345678",
                "NetworkAclName": "test",
                "CreatedTime": "2020-01-01 10:00:00",
                "SubnetSet": [
                    {
                        "SubnetId": "subnet-12345678",
                        "SubnetName": "test",
                        "CidrBlock": "172.16.12.0/24"
                    }
                ],
                "IngressEntries": [
                    {
                        "Protocol": "tcp",
                        "CidrBlock": "172.16.12.123/32",
                        "Action": "Accept",
                        "Description": "test",
                        "Port": 8080
                    },
                    {
                        "Protocol": "all",
                        "CidrBlock": "0.0.0.0/0",
                        "Action": "Drop",
                        "Description": ""
                    }
                ],
                "EgressEntries": [
                    {
                        "Protocol": "tcp",
                        "CidrBlock": "172.16.12.123/32",
                        "Action": "Accept",
                        "Description": "test",
                        "Port": 8080
                    },
                    {
                        "Protocol": "all",
                        "CidrBlock": "0.0.0.0/0",
                        "Action": "Drop",
                        "Description": ""
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "5efe6fa7-6de2-4ce9-911a-f7438bf697d4"
    }
}
```

