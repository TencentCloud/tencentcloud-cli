**Example 1: 空发回执**



Input: 

```
tccli iottid DeliverTidNotify --cli-unfold-argument  \
    --OrderId 4BI47CqhHQ \
    --Tid 000001035D0C97E3D2A46283D27BC612
```

Output: 
```
{
    "Response": {
        "ProductKey": "testProductKey",
        "RemaindCount": 887,
        "RequestId": "b410542c-b7b1-439f-99b7-6767cbf41f59",
        "Tid": "000001035D0C97E3D2A46283D27BC612"
    }
}
```

