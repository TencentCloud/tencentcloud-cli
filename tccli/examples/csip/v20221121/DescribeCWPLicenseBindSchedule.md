**Example 1: 示例**

查询授权绑定进度

Input: 

```
tccli csip DescribeCWPLicenseBindSchedule --cli-unfold-argument  \
    --TaskId 1135847 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ErrMsg": "",
                "FixMessage": "",
                "MachineExtraInfo": {
                    "HostName": "",
                    "InstanceID": "",
                    "NetworkName": "",
                    "NetworkType": 0,
                    "PrivateIP": "",
                    "WanIP": ""
                },
                "Quuid": "",
                "Status": 0
            }
        ],
        "Schedule": 20,
        "TotalCount": 1,
        "RequestId": "c0c1a82b-ebbf-4b39-b689-0a64decc6b83"
    }
}
```

