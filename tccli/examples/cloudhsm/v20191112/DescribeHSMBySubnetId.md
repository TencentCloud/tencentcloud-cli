**Example 1: 根据SubnetId查询实例数量**

根据SubnetId查询实例数量

Input: 

```
tccli cloudhsm DescribeHSMBySubnetId --cli-unfold-argument  \
    --SubnetId subnet-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SubnetId": "subnet-xxxxxxxx",
        "RequestId": "6010cd3d-a85a-4e00-b37b-22606d017420"
    }
}
```

