**Example 1: 关闭数据库代理连接地址**



Input: 

```
tccli cynosdb CloseProxyEndPoint --cli-unfold-argument  \
    --ClusterId cynosdbmysql-j9i41hdd \
    --ProxyGroupId cynosdbmysql-proxy-lti34611
```

Output: 
```
{
    "Response": {
        "FlowId": 147186,
        "TaskId": 148273,
        "RequestId": "51169b54-61d4-4604-a07e-e519a5527923"
    }
}
```

