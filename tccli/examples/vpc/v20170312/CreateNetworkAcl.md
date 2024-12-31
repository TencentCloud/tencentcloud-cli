**Example 1: 创建网络ACL**

创建网络ACL

Input: 

```
tccli vpc CreateNetworkAcl --cli-unfold-argument  \
    --VpcId vpc-4tw1bxlq \
    --NetworkAclName demo
```

Output: 
```
{
    "Response": {
        "NetworkAcl": {
            "NetworkAclId": "acl-6zwa44xm",
            "VpcId": "vpc-4tw1bxlq",
            "NetworkAclName": "demo",
            "CreatedTime": "2020-01-01 10:00:00",
            "SubnetSet": [],
            "IngressEntries": [],
            "EgressEntries": [],
            "NetworkAclType": "TRIPLE",
            "TagSet": []
        },
        "RequestId": "5cf1a813-d4f8-4e0c-8f90-c155a84a3ea1"
    }
}
```

