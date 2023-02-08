**Example 1: 示例1**



Input: 

```
tccli keewidb DescribeInstanceReplicas --cli-unfold-argument  \
    --InstanceId kee-9clk****
```

Output: 
```
{
    "Response": {
        "ReplicaGroups": [
            {
                "GroupId": 1081,
                "GroupName": "ng-00",
                "KeeWiDBNodes": [
                    {
                        "NodeId": "fc9d0d4d3f33570320cd2034d75c34521ef1c3ef",
                        "Role": "master",
                        "Status": "Normal"
                    },
                    {
                        "NodeId": "d05b99e5e07b7d3d29a4c6f65d410aada0849797",
                        "Role": "master",
                        "Status": "Normal"
                    },
                    {
                        "NodeId": "be2aba737c920f17e9151266a9ee59a08ca3727e",
                        "Role": "master",
                        "Status": "Normal"
                    }
                ],
                "Role": "master",
                "ZoneId": "ap-guangzhou-2"
            },
            {
                "GroupId": 1082,
                "GroupName": "ng-01",
                "KeeWiDBNodes": [
                    {
                        "NodeId": "af40204e08f25e7848aaaf344cb05c2fb6fd63c6",
                        "Role": "replica",
                        "Status": "Normal"
                    },
                    {
                        "NodeId": "2c0dd8607c8187c45ec6943337fb43e60e3d6add",
                        "Role": "replica",
                        "Status": "Normal"
                    },
                    {
                        "NodeId": "5ddd5a5aa3d4448553fe94d0c0741236f144b9f5",
                        "Role": "replica",
                        "Status": "Normal"
                    }
                ],
                "Role": "replica",
                "ZoneId": "ap-guangzhou-3"
            }
        ],
        "RequestId": "a9575963-23f6-48d7-a1a8-bc31ee861f31",
        "TotalCount": 2
    }
}
```

