**Example 1: 设置负载均衡操作保护**

开启负载均衡的操作保护

Input: 

```
tccli clb ModifyLBOperateProtect --cli-unfold-argument  \
    --OperateProtect true \
    --Description on \
    --LoadBalancerId lb-gfz73nj8
```

Output: 
```
{
    "Response": {
        "RequestId": "fc1acfd9-aad5-45cc-9081-8653295e9582"
    }
}
```

