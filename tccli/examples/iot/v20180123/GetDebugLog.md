**Example 1: 获取调试日志**

获取调试日志

Input: 

```
tccli iot GetDebugLog --cli-unfold-argument  \
    --ProductId iot-4e0wsxpi \
    --DeviceNames car \
    --StartTime '2018-05-12 00:00:00' \
    --EndTime '2018-05-12 23:59:59' \
    --Size 5
```

Output: 
```
{
    "Response": {
        "RequestId": "db6a3512-7983-46da-bc6f-d18be937cfff",
        "DebugLog": [
            {
                "Id": "00B6331A2B3A3702A5A05CB7ED20CC54",
                "Event": "connect",
                "LogType": "mqtt",
                "Result": "success",
                "Timestamp": 1526125472000,
                "DeviceName": "car",
                "Data": "",
                "Topic": ""
            },
            {
                "Id": "082CC25A769D3AB496408B26F65FEB45",
                "Event": "connect",
                "LogType": "mqtt",
                "Result": "success",
                "Timestamp": 1526125472000,
                "DeviceName": "car",
                "Data": "",
                "Topic": ""
            },
            {
                "Id": "7BD51645585F31D097730B03272274EB",
                "Event": "connect",
                "LogType": "mqtt",
                "Result": "success",
                "Timestamp": 1526125472000,
                "DeviceName": "car",
                "Data": "",
                "Topic": ""
            },
            {
                "Id": "A6641A9E53683E61B64E78F40A24F782",
                "Event": "connect",
                "LogType": "mqtt",
                "Result": "success",
                "Timestamp": 1526125472000,
                "DeviceName": "car",
                "Data": "",
                "Topic": ""
            },
            {
                "Id": "A694496AA8FA3230A3CFDC8538AA4F7F",
                "Event": "connect",
                "LogType": "mqtt",
                "Result": "success",
                "Timestamp": 1526120670000,
                "DeviceName": "car",
                "Data": "",
                "Topic": ""
            }
        ],
        "ScrollId": "DnF1ZXJ5VGhlbkZldGNoCgAAAAAAAABZFjYzUUxMT211VDVDTXk2X2UtM0tEQ2cAAAAAAAAAWxZDUUs0T2cwR1M4R001OXh6SG96YVRnAAAAAAAAAFoWQ1FLNE9nMEdTOEdNNTl4ekhvemFUZwAAAAAAAABZFkNRSzRPZzBHUzhHTTU5eHpIb3phVGcAAAAAAAAAWxY2M1FMTE9tdVQ1Q015Nl9lLTNLRENnAAAAAAAAAFoWNjNRTExPbXVUNUNNeTZfZS0zS0RDZwAAAAAAAABkFml3djFuZVZGVFM2NnJSb2tFUG9FN3cAAAAAAAAAXBY2M1FMTE9tdVQ1Q015Nl9lLTNLRENnAAAAAAAAAGUWaXd2MW5lVkZUUzY2clJva0VQb0U3dwAAAAAAAABcFkNRSzRPZzBHUzhHTTU5eHpIb3phVGc=",
        "ScrollTimeout": 60
    }
}
```

