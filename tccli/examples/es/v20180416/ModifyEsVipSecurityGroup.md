**Example 1: 修改集群VIP绑定的安全组信息**

修改集群VIP绑定的安全组信息

Input: 

```
tccli es ModifyEsVipSecurityGroup --cli-unfold-argument  \
    --InstanceId es-3p7lkvxx \
    --SecurityGroupIds sg-1 sg-2
```

Output: 
```
{
    "Response": {
        "RequestId": "c96a110c-7493-452d-a99b-683d07xxxxxx"
    }
}
```

