**Example 1: 集群节点列表**



Input: 

```
tccli cdwpg DescribeInstanceNodes --cli-unfold-argument  \
    --InstanceId cdwpg-xxddd
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "InstanceNodes": [
            {
                "NodeId": 38500,
                "NodeIp": "9.0.175.2",
                "NodeType": "gtm"
            },
            {
                "NodeId": 38501,
                "NodeIp": "9.0.175.5",
                "NodeType": "gtm"
            },
            {
                "NodeId": 38496,
                "NodeIp": "9.0.175.5",
                "NodeType": "cn"
            },
            {
                "NodeId": 38498,
                "NodeIp": "9.0.175.2",
                "NodeType": "cn"
            },
            {
                "NodeId": 38497,
                "NodeIp": "9.0.175.2",
                "NodeType": "cn"
            },
            {
                "NodeId": 38499,
                "NodeIp": "9.0.175.5",
                "NodeType": "cn"
            },
            {
                "NodeId": 38492,
                "NodeIp": "9.0.175.11",
                "NodeType": "dn"
            },
            {
                "NodeId": 38494,
                "NodeIp": "9.0.175.3",
                "NodeType": "dn"
            },
            {
                "NodeId": 38493,
                "NodeIp": "9.0.175.3",
                "NodeType": "dn"
            },
            {
                "NodeId": 38495,
                "NodeIp": "9.0.175.11",
                "NodeType": "dn"
            },
            {
                "NodeId": 38534,
                "NodeIp": "9.0.107.14",
                "NodeType": "gtm"
            },
            {
                "NodeId": 38535,
                "NodeIp": "9.0.107.18",
                "NodeType": "gtm"
            },
            {
                "NodeId": 38530,
                "NodeIp": "9.0.107.18",
                "NodeType": "cn"
            },
            {
                "NodeId": 38532,
                "NodeIp": "9.0.107.14",
                "NodeType": "cn"
            },
            {
                "NodeId": 38531,
                "NodeIp": "9.0.107.14",
                "NodeType": "cn"
            },
            {
                "NodeId": 38533,
                "NodeIp": "9.0.107.18",
                "NodeType": "cn"
            },
            {
                "NodeId": 38526,
                "NodeIp": "9.0.107.9",
                "NodeType": "dn"
            },
            {
                "NodeId": 38528,
                "NodeIp": "9.0.107.24",
                "NodeType": "dn"
            },
            {
                "NodeId": 38527,
                "NodeIp": "9.0.107.24",
                "NodeType": "dn"
            },
            {
                "NodeId": 38529,
                "NodeIp": "9.0.107.9",
                "NodeType": "dn"
            }
        ],
        "RequestId": "2c28a349-8e12-42da-ab31-03478e154c8f"
    }
}
```

