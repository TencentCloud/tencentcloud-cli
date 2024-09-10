**Example 1: 示例1**

用于安全组批量解绑实例。

Input: 

```
tccli vdb DisassociateSecurityGroups --cli-unfold-argument  \
    --SecurityGroupIds sg-dutt**** \
    --InstanceIds vdb-9clk****
```

Output: 
```
{
    "Response": {
        "RequestId": "c7297527-0e7c-43ad-bdb1-b90fc222d43d"
    }
}
```

