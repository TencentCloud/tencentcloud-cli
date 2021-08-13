**Example 1: 开启防火墙路由表开关**

推荐使用场景，针对路由表开启防火墙开关

Input: 

```
tccli cfw ModifyNatFwSwitch --cli-unfold-argument  \
    --Enable 1 \
    --RouteTableIdList rtb-9jbsa559 rtb-dba9eo0f
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 开启防火墙子网开关**

子网参数场景，当前仅支持单一子网开关

Input: 

```
tccli cfw ModifyNatFwSwitch --cli-unfold-argument  \
    --Enable 1 \
    --SubnetIdList subnet-cjxihpy1
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

