**Example 1: 网关负载均衡ACL组关联网关负载均衡实例**

网关负载均衡ACL组关联网关负载均衡实例

Input: 

```
tccli gwlb AssociateGatewayAclGroup --cli-unfold-argument  \
    --LoadBalancerId gwlb-4qo**** \
    --AclGroupId gwlbacl-0pii****
```

Output: 
```
{
    "Response": {
        "RequestId": "7daa09a5-f9cd-40f9-9e24-6880aaf4cb2b"
    }
}
```

