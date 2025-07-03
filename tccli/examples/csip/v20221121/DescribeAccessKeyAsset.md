**Example 1: 示例1**



Input: 

```
tccli csip DescribeAccessKeyAsset --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [],
        "Total": 0,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 1**



Input: 

```
tccli csip DescribeAccessKeyAsset --cli-unfold-argument  \
    --Filter.Limit 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AccessKeyAlarmList": [
                    {
                        "Count": 7,
                        "Type": 0
                    }
                ],
                "AccessKeyRiskList": [
                    {
                        "Count": 11,
                        "Type": 0
                    }
                ],
                "Advice": 1,
                "AppID": 1256299843,
                "CheckStatus": 0,
                "CreateTime": "2024-09-24 19:21:38",
                "ID": 10092,
                "IPCount": 1,
                "LastAccessTime": "2025-03-12 20:05:59",
                "Name": "AKID***1",
                "Nickname": "飞快的云镜",
                "Remark": "iiiiii",
                "Status": 1,
                "SubNickname": "piperdev",
                "SubUin": "100000415991",
                "Type": 1,
                "Uin": "100004506473"
            }
        ],
        "RequestId": "2b6d0999-a614-41e3-92b8-984c80705275",
        "Total": 37
    }
}
```

