**Example 1: 获取数据历史**

获取数据历史

Input: 

```
tccli iot GetDataHistory --cli-unfold-argument  \
    --ProductId iot-4e0wsxpi \
    --DeviceNames dev0 dev5 \
    --StartTime '2018-03-30 00:00:00' \
    --EndTime '2018-03-30 23:00:00' \
    --Size 5
```

Output: 
```
{
    "Response": {
        "RequestId": "6280afe8-fe9e-4d8b-b1b4-6084282671ae",
        "DataHistory": [
            {
                "DeviceName": "dev5",
                "Timestamp": 1522413634455,
                "Data": "{\"Temperature\": 1023,  \"Switch\": 1023}"
            },
            {
                "DeviceName": "dev0",
                "Timestamp": 1522413634455,
                "Data": "{\"Temperature\": 1023,  \"Switch\": 1023}"
            }
        ],
        "ScrollId": "DnF1ZXJ5VGhlbkZldGNoAQAAAAAAACOZFkVEYlVxTG1kUlRpdkdDY1RVaFpFZGc=",
        "ScrollTimeout": 300
    }
}
```

