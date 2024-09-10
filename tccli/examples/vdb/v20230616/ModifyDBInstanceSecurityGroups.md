**Example 1: 示例1**

修改实例绑定的安全组

Input: 

```
tccli vdb ModifyDBInstanceSecurityGroups --cli-unfold-argument  \
    --InstanceIds vdb-9clk**** \
    --SecurityGroupIds sg-iqxw**** sg-dutt**** sg-eudo****
```

Output: 
```
{
    "Response": {
        "RequestId": "b3a86195-eee7-4e17-8405-e1fc5810c55b"
    }
}
```

