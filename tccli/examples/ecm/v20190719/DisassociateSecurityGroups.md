**Example 1: 解绑实例安全组**



Input: 

```
tccli ecm DisassociateSecurityGroups --cli-unfold-argument  \
    --InstanceIds ein-2zvpghhc ein-915zrb0p \
    --SecurityGroupIds esg-9id3l839
```

Output: 
```
{
    "Response": {
        "RequestId": "3385dcf2-e1f0-4ed8-a924-c296721ab65f"
    }
}
```

