**Example 1: 示例**



Input: 

```
tccli dsgc GetResourceConnectionStatus --cli-unfold-argument  \
    --DspaId dspa-6fb60936 \
    --MetaType cdb \
    --ResourceRegion ap-guangzhou \
    --ResourceId cdb-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "c1b55d08-d956-447e-9852-a93bbb6f5d55",
        "ConnectionStatus": "success",
        "ConnectionDesc": ""
    }
}
```

