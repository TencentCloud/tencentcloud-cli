**Example 1: 查看链路详情**



Input: 

```
tccli ctem DescribeJobRecordDetails --cli-unfold-argument  \
    --Module enterprise \
    --Id 32811
```

Output: 
```
{
    "Response": {
        "EnterpriseEquityPath": [
            {
                "EnterpriseUid": "b12afac95c9ff6c2c3b71618351d61ef",
                "Name": "主体公司",
                "ShareholdingRatio": "55%"
            }
        ],
        "List": [
            {
                "Data": [
                    {
                        "Id": 32811,
                        "Value": "子公司B"
                    }
                ],
                "JobRecordId": 0,
                "Module": "enterprise",
                "ModuleName": "企业架构",
                "TimeAt": "2026-03-04 10:36:10"
            }
        ],
        "Total": 1,
        "RequestId": "e80d7900-eba9-43c7-8b59-d60b74616fc2"
    }
}
```

