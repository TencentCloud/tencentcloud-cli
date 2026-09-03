**Example 1: 绑定IDC集群VPC**

为IDC集群绑定指定的VPC和子网。

Input: 

```
tccli thpc BindClusterVpc --cli-unfold-argument  \
    --ClusterId hpc-12345678 \
    --VpcId vpc-aaaa1234 \
    --SubnetId subnet-bbbb5678
```

Output: 
```
{
    "Response": {
        "ClusterId": "hpc-12345678",
        "VpcId": "vpc-aaaa1234",
        "SubnetId": "subnet-bbbb5678",
        "RequestId": "b2ac2379-6453-4eab-8f63-7ade00cb67b0"
    }
}
```

