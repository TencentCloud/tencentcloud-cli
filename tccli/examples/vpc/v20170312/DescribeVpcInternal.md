**Example 1: 查询VPC列表**



Input: 

```
tccli vpc DescribeVpcInternal --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2 \
    --Filters.0.Name vpc-id \
    --Filters.0.Values vpc-p5sf61yj \
    --Filters.1.Name vpc-name \
    --Filters.1.Values 测试dhcp
```

Output: 
```
{
    "Response": {
        "RequestId": "6a44afb7-0644-4ff9-9761-3502f99d3a15"
    }
}
```

