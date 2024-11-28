**Example 1: 根据VpcId查询实例数量**

根据VpcId查询实例数量

Input: 

```
tccli cloudhsm DescribeHSMByVpcId --cli-unfold-argument  \
    --VpcId vpc-rhx6fnd7
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "VpcId": "vpc-rhx6fnd7",
        "RequestId": "6010cd3d-a85a-4e00-b37b-22606d017420"
    }
}
```

