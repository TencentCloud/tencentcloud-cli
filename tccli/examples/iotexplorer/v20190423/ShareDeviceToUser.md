**Example 1: 成功示例**



Input: 

```
tccli iotexplorer ShareDeviceToUser --cli-unfold-argument  \
    --AppKey afpMLiFlGYThFpvJe \
    --ProductId N5DBOST040 \
    --DeviceName nandy_dev3 \
    --OwnerOpenID nandy \
    --ToOpenID zz \
    --ToNickName zz
```

Output: 
```
{
    "Response": {
        "OwnerUserID": "195155279497658759",
        "ToUserID": "195350446737457359",
        "RequestId": "83640ed8-a3a2-44d0-a036-8913d99a3eab"
    }
}
```

