**Example 1: Associating multiple instances with one security group**



Input: 

```
tccli cvm AssociateSecurityGroups --cli-unfold-argument  \
    --InstanceIds ins-2zvpghhc ins-915zrb0p \
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

