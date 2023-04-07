**Example 1: 修改实例的安全组信息**

修改指定实例的安全组入站规则

Input: 

```
tccli mongodb ModifyDBInstanceSecurityGroup --cli-unfold-argument  \
    --InstanceId cmgo-14i5dgtl' \
    --SecurityGroupIds sg-l7ipccjl
```

Output: 
```
{
    "Response": {
        "RequestId": "bc59fa05-d429-4bcf-863f-1f6f99295485"
    }
}
```

