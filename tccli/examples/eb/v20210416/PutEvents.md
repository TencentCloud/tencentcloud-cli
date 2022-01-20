**Example 1: 事件投递**



Input: 

```
tccli eb PutEvents --cli-unfold-argument  \
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
        "RequestId": "ae684d86-33ec-449e-bc38-9d9552199267"
    }
}
```

