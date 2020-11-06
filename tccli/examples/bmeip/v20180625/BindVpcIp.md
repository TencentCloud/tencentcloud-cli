**Example 1: EIP绑定虚拟IP**

用于绑定黑石弹性公网IP到黑石VPC的IP上（非黑石物理机IP）。区别于BindRs，该接口主要适用于客户使用黑石的半托管服务或者在黑石物理集群中创建自己的云服务器，同时又需要这些半托管的设备或者云服务器出公网的场景。

Input: 

```
tccli bmeip BindVpcIp --cli-unfold-argument  \
    --EipId eip-fz3yvdzi \
    --VpcId vpc-bjh0qd20 \
    --VpcIp 10.1.0.11
```

Output: 
```
{
    "Response": {
        "TaskId": 2488351,
        "RequestId": "6565cb9d-4ded-4af2-967f-e7802ade09d9"
    }
}
```

