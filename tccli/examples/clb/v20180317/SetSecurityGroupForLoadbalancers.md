**Example 1: Binding one security group to multiple CLB instances**



Input: 

```
tccli clb SetSecurityGroupForLoadbalancers --cli-unfold-argument  \
    --SecurityGroup sg-12345678 \
    --OperationType ADD \
    --LoadBalancerIds lb-0936o712 lb-tttt5555
```

Output: 
```
{
    "Response": {
        "RequestId": "00ca7fca-90f1-47fe-a724-5d7e96d04633"
    }
}
```

