**Example 1: demo**

demo

Input: 

```
tccli wedata CreateConnection --cli-unfold-argument  \
    --WorkspaceId aa-zz \
    --Connection.ConnectionName hive_simple \
    --Connection.DisplayName hive_simple \
    --Connection.ConnectionType hive \
    --Connection.AuthType simple \
    --Connection.ConnectionDetail {"url":"jdbc:hive2://30.46.103.13:11784/default","password":"ccc","username":"aa"} \
    --Connection.FileCosInfo.CosRegion ap-beijing \
    --Connection.FileCosInfo.CosBucket abeltest
```

Output: 
```
{
    "Response": {
        "Data": {
            "ConnectionId": "fd7a97df-7019-4962-8a1e-378ebdd95291"
        },
        "RequestId": "963a20fe-3d7d-441e-bf0d-ff46cb904ec1"
    }
}
```

