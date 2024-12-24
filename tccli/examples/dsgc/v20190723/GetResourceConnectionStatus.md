**Example 1: 获取授权资源的连接状态**



Input: 

```
tccli dsgc GetResourceConnectionStatus --cli-unfold-argument  \
    --DspaId dspa-6fb60936 \
    --MetaType cdb \
    --ResourceRegion ap-guangzhou \
    --ResourceId cdb-12cd45g7
```

Output: 
```
{
    "Response": {
        "RequestId": "c1b55d08-d956-447e-9852-a93bbb6f5d55",
        "ConnectionStatus": "success",
        "ConnectionDesc": "连接成功"
    }
}
```

