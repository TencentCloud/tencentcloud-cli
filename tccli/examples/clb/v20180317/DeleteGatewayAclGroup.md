**Example 1: 删除单个网关负载均衡ACL组**

删除单个网关负载均衡ACL组

Input: 

```
tccli clb DeleteGatewayAclGroup --cli-unfold-argument  \
    --AclGroupIds gwlbacl-okhd****
```

Output: 
```
{
    "Response": {
        "RequestId": "31bb359e-317e-49a9-a029-54a958f3a947"
    }
}
```

