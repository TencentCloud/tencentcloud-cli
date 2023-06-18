**Example 1: 升级数据库代理版本**

升级数据库代理版本

Input: 

```
tccli cynosdb UpgradeProxyVersion --cli-unfold-argument  \
    --ClusterId abc \
    --ProxyGroupId abc \
    --SrcProxyVersion abc \
    --DstProxyVersion abc \
    --IsInMaintainPeriod abc
```

Output: 
```
{
    "Response": {
        "RequestId": "128046",
        "FlowId": "123",
        "TaskId": "123"
    }
}
```

