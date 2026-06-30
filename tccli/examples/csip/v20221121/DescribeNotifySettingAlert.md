**Example 1: 示例**



Input: 

```
tccli csip DescribeNotifySettingAlert --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Settings": [
            {
                "AssetRange": 2,
                "BeginTime": "00:00:00",
                "EndTime": "23:59:59",
                "Item": [],
                "Mode": 1,
                "Module": "Alert",
                "Option": [
                    "HIGH"
                ],
                "Status": 1,
                "SubModule": "BRUTE_FORCE"
            }
        ],
        "RequestId": "c5785954-2e97-4927-94de-e567399c0305"
    }
}
```

