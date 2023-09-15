**Example 1: 指定多个实例绑定一个安全组**



Input: 

```
tccli cvm AssociateSecurityGroups --cli-unfold-argument  \
    --InstanceIds ins-915zrb0p ins-2zvpghhc \
    --SecurityGroupIds sg-9id3l839
```

Output: 
```
{
    "Response": {
        "RequestId": "3385dcf2-e1f0-4ed8-a924-c296721ab65f"
    }
}
```

