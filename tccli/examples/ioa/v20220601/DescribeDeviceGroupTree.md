**Example 1: 测试**

测试

Input: 

```
tccli ioa DescribeDeviceGroupTree --cli-unfold-argument  \
    --DeviceGroupId 93 \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Devices": [
                {
                    "GroupId": 93,
                    "GroupName": "未分组终端",
                    "Id": 56,
                    "Ip": "113.108.77.68",
                    "Locked": 0,
                    "Mac": "00:0C:29:20:19:FE",
                    "Mid": "A8A8DB0AF29D36613529617CF363F118657D4243",
                    "Name": "DESKTOP-1A85MRH"
                },
                {
                    "GroupId": 93,
                    "GroupName": "未分组终端",
                    "Id": 121,
                    "Ip": "119.147.10.184",
                    "Locked": 0,
                    "Mac": "",
                    "Mid": "75129D715480905B6A9C4569893C763466947ECE",
                    "Name": "DESKTOP-AL8RU6H"
                },
                {
                    "GroupId": 93,
                    "GroupName": "未分组终端",
                    "Id": 7,
                    "Ip": "113.108.77.72",
                    "Locked": 0,
                    "Mac": "00:0C:29:10:00:5C",
                    "Mid": "75129D715480905B6A9C4569893C76346503D808",
                    "Name": "DESKTOP-AL8RU6H"
                },
                {
                    "GroupId": 93,
                    "GroupName": "未分组终端",
                    "Id": 113,
                    "Ip": "119.147.10.195",
                    "Locked": 0,
                    "Mac": "C8:5A:CF:00:E8:14",
                    "Mid": "6E27B4133DA1B7CAA88C038BB67D8BF962749547",
                    "Name": "seedsnie-PC3"
                },
                {
                    "GroupId": 93,
                    "GroupName": "未分组终端",
                    "Id": 131,
                    "Ip": "113.108.77.63",
                    "Locked": 0,
                    "Mac": "",
                    "Mid": "rickey8fbdd6329229125333f72dbfd85fd81966AC47F7",
                    "Name": "超级里奇测试"
                },
                {
                    "GroupId": 93,
                    "GroupName": "未分组终端",
                    "Id": 135,
                    "Ip": "14.22.11.164",
                    "Locked": 0,
                    "Mac": "52:54:00:BA:30:90",
                    "Mid": "EBA3878F3ED998E724F798787774312766C5982A",
                    "Name": "devcloud11355"
                },
                {
                    "GroupId": 93,
                    "GroupName": "未分组终端",
                    "Id": 57,
                    "Ip": "113.108.77.50",
                    "Locked": 0,
                    "Mac": "F0:77:C3:94:75:A5",
                    "Mid": "8A613EEADF244D223FB45E045D10FC1E657D4F09",
                    "Name": "JOHNQQIAO-NB0"
                },
                {
                    "GroupId": 93,
                    "GroupName": "未分组终端",
                    "Id": 52,
                    "Ip": "113.108.77.51",
                    "Locked": 0,
                    "Mac": "00:0C:29:10:00:5C",
                    "Mid": "75129D715480905B6A9C4569893C763465681A9B",
                    "Name": "DESKTOP-AL8RU6H"
                },
                {
                    "GroupId": 93,
                    "GroupName": "未分组终端",
                    "Id": 133,
                    "Ip": "119.147.10.207",
                    "Locked": 0,
                    "Mac": "00:0C:29:10:00:5C",
                    "Mid": "75129D715480905B6A9C4569893C763466BCC2BA",
                    "Name": "DESKTOP-AL8RU6H"
                },
                {
                    "GroupId": 93,
                    "GroupName": "未分组终端",
                    "Id": 12,
                    "Ip": "119.147.10.202",
                    "Locked": 0,
                    "Mac": "00:0C:29:10:00:5C",
                    "Mid": "75129D715480905B6A9C4569893C7634650D06FD",
                    "Name": "DESKTOP-AL8RU6H"
                },
                {
                    "GroupId": 93,
                    "GroupName": "未分组终端",
                    "Id": 50,
                    "Ip": "119.147.10.199",
                    "Locked": 0,
                    "Mac": "",
                    "Mid": "1958d4fd2dbdaf5ccd0fdb6a5fa5e8336531E1EC01655F182C",
                    "Name": "pikachu mac postman"
                }
            ],
            "Groups": []
        },
        "RequestId": "4f76a517-49c1-47eb-9336-b4dce2fc29f4"
    }
}
```

