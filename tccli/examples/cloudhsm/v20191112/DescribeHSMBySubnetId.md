**Example 1: 根据SubnetId查询实例数量**

根据SubnetId查询实例数量

Input: 

```
tccli cloudhsm DescribeHSMBySubnetId --cli-unfold-argument  \
    --SubnetId subnet-4vxnrlco
```

Output: 
```
{
    "Response": {
        "RequestId": "67175452-3e94-479a-b28f-c70854d6a34b",
        "SubnetId": "subnet-4vxnrlco",
        "TotalCount": 2
    }
}
```

