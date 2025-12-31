**Example 1: 修改集群模式VPC防火墙开关**

修改集群模式VPC防火墙开关

Input: 

```
tccli cfw ModifyClusterVpcFwSwitch --cli-unfold-argument  \
    --Enable 1 \
    --CcnSwitch.0.CcnId ccn-a5z72txp \
    --CcnSwitch.0.SwitchMode 2 \
    --CcnSwitch.0.FwVpcCidr auto
```

Output: 
```
{
    "Response": {
        "RequestId": "70ef6201-d73e-4b02-9645-dee6bf00fa66"
    }
}
```

