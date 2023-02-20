**Example 1: 事件投递**



Input: 

```
tccli eb PublishEvent --cli-unfold-argument  \
    --EventList.0.Data string \
    --EventList.0.Type string \
    --EventList.0.Source string \
    --EventList.0.Subject qcs::dts:ap-guangzhou:appid12312/uid1250000000:xxx \
    --EventList.1.Data string \
    --EventList.1.Type string \
    --EventList.1.Source string \
    --EventList.1.Subject qcs::dts:ap-guangzhou:appid12312/uid1250000000:xxx \
    --EventBusId string
```

Output: 
```
{
    "Response": {
        "RequestId": "e3d43926-c2cd-49f2-97f0-53db21e6fcea"
    }
}
```

