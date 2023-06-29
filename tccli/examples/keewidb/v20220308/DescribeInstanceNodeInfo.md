**Example 1: 示例1**



Input: 

```
tccli keewidb DescribeInstanceNodeInfo --cli-unfold-argument  \
    --InstanceId kee-9clk**** \
    --Limit 100 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "KeeWiDB": [
            {
                "NodeId": "af40204e08f25e7848aaaf344cb05c2fb6fd63c6",
                "NodeRole": "slave"
            },
            {
                "NodeId": "2c0dd8607c8187c45ec6943337fb43e60e3d6add",
                "NodeRole": "slave"
            },
            {
                "NodeId": "5ddd5a5aa3d4448553fe94d0c0741236f144b9f5",
                "NodeRole": "master"
            },
            {
                "NodeId": "d05b99e5e07b7d3d29a4c6f65d410aada0849797",
                "NodeRole": "master"
            },
            {
                "NodeId": "be2aba737c920f17e9151266a9ee59a08ca3727e",
                "NodeRole": "master"
            },
            {
                "NodeId": "fc9d0d4d3f33570320cd2034d75c34521ef1c3ef",
                "NodeRole": "slave"
            }
        ],
        "KeeWiDBCount": 6,
        "Proxy": [
            {
                "NodeId": "3ceae5cc95d9334641447bd315ee46ea8ba39884"
            },
            {
                "NodeId": "cda74b83783be31cbad762d48dd2f5847f866e25"
            },
            {
                "NodeId": "402953672af8b451d9f4b4a55cf4e0c2ad5592f3"
            },
            {
                "NodeId": "f54afc9a2c07b867efa7214eb8da65d2d9e06f34"
            },
            {
                "NodeId": "7fc296b1e7f7e818a9a773f49ba2376ccf2453c0"
            },
            {
                "NodeId": "4cc3cd90864ce50069a05dc02473fb531ac16be6"
            },
            {
                "NodeId": "f43aabbd573d6e2fb36286f5787d81ce89211c80"
            },
            {
                "NodeId": "f09af44dde734efd69e47825483ff4f48de103b0"
            }
        ],
        "ProxyCount": 8,
        "Redis": [],
        "RedisCount": 0,
        "RequestId": "80c6320a-01a3-4fe3-af2a-797e72573732",
        "Tendis": [],
        "TendisCount": 0
    }
}
```

