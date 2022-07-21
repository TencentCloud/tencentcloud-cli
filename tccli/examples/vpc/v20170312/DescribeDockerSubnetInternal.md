**Example 1: 描述Docker subnet**



Input: 

```
tccli vpc DescribeDockerSubnetInternal --cli-unfold-argument  \
    --VpcId 78257 \
    --UniqueVpcId vpc-xxx \
    --Subnet 10.0.0.0 \
    --Mask xxx \
    --IntMask 16
```

Output: 
```
{
    "Response": {
        "DockerSubnet": [
            {
                "Subnet": "10.0.0.0",
                "VpcId": 78257,
                "UniqueVpcId": "vpc-jmaywf6r",
                "Mask": "255.255.0.0",
                "IntMask": 16,
                "CreateTime": "2021-12-28 16:42:40"
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

