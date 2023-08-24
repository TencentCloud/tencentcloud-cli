**Example 1: 升级数据库代理版本**

升级数据库代理版本

Input: 

```
tccli cynosdb UpgradeProxyVersion --cli-unfold-argument  \
    --ClusterId cynosdbmysql-asd \
    --ProxyGroupId cynosdbmysql-proxy-asd \
    --SrcProxyVersion 3.1.0 \
    --DstProxyVersion 3.2.0 \
    --IsInMaintainPeriod yes
```

Output: 
```
{
    "Response": {
        "RequestId": "128046",
        "FlowId": 123,
        "TaskId": 123
    }
}
```

