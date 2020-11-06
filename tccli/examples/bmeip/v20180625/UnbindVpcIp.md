**Example 1: 黑石EIP解绑VPCIP**

此接口用于解绑黑石弹性公网IP到黑石私有网络的IP（非黑石物理机IP）

Input: 

```
tccli bmeip UnbindVpcIp --cli-unfold-argument  \
    --EipId eip-fz3yvdzi \
    --VpcId vpc-bjh0qd20 \
    --VpcIp 10.1.0.11
```

Output: 
```
{
    "Response": {
        "TaskId": 2488352,
        "RequestId": "a28288f8-a78c-4b15-8e97-b5b9126819e3"
    }
}
```

