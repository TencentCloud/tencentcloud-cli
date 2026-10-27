**Example 1: 修改业务资源**



Input: 

```
tccli ioa ModifyBusinessResource --cli-unfold-argument  \
    --AreaId 1 \
    --Protocol 2 \
    --ServiceName oa-oss \
    --Levels 5000 \
    --ServiceType domain \
    --ServicePort all \
    --ServiceId 1 \
    --ServiceAddress *.ss.sf-express.com \
    --DirectConn 1
```

Output: 
```
{
    "Response": {
        "RequestId": "75f5b618-59d2-4648-abfd-b90796292265"
    }
}
```

