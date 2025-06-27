**Example 1: 查看主机资产**

查看主机资产

Input: 

```
tccli ctem DescribeAssets --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "City": "深圳",
                "Country": "中国",
                "DisplayToolCommon": {
                    "CreateAt": "2024-06-06 16:16:16",
                    "CustomerId": 100081,
                    "CustomerName": "5555",
                    "Detail": "",
                    "EnterpriseName": "",
                    "EnterpriseUid": "",
                    "Ignored": false,
                    "JobId": 0,
                    "JobRecordId": 0,
                    "JobStageId": 0,
                    "Md5": "040d6b47e6d1f754992a14752bbb3fe4",
                    "UpdateAt": "2024-06-06 16:16:16"
                },
                "Id": 6880,
                "Ip": "1.1.1.1",
                "Isp": "电信",
                "Os": "",
                "Province": "广东"
            }
        ],
        "RequestId": "c156b846-9f28-4976-a3a4-e9b9683b3b00",
        "Total": 1
    }
}
```

