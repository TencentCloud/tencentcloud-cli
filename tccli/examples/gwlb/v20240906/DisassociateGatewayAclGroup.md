**Example 1: 网关负载均衡ACL组解关联网关负载均衡实例**

网关负载均衡ACL组解关联网关负载均衡实例

Input: 

```
tccli gwlb DisassociateGatewayAclGroup --cli-unfold-argument  \
    --LoadBalancerId gwlb-4qoy**** \
    --AclGroupId gwlbacl-0pii****
```

Output: 
```
{
    "Response": {
        "RequestId": "e52be01e-a2d3-483e-a227-3506eb5c1cd0"
    }
}
```

