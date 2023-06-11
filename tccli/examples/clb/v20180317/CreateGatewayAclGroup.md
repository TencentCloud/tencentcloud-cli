**Example 1: 创建ACL组**

创建ACL组

Input: 

```
tccli clb CreateGatewayAclGroup --cli-unfold-argument  \
    --AclGroupName ACL组名称 \
    --VpcId vpc-b5oj927d
```

Output: 
```
{
    "Response": {
        "AclGroupId": "gwlbacl-0pii****",
        "RequestId": "d5c057bc-fa61-4b86-8c31-0ccdac426c7f"
    }
}
```

