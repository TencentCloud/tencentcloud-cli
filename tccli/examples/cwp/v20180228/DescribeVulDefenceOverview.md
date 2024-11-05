**Example 1: 获取漏洞防御概览信息**



Input: 

```
tccli cwp DescribeVulDefenceOverview --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Overview": {
            "Enable": 1,
            "DefendHostCount": 35,
            "ExceptionCount": 1,
            "AttackCounts": [
                0,
                0,
                20,
                0,
                0,
                0,
                0,
                17,
                11,
                2,
                33,
                49,
                105,
                80
            ],
            "DefendCounts": [
                0,
                0,
                20,
                0,
                0,
                0,
                0,
                17,
                11,
                2,
                33,
                49,
                105,
                80
            ],
            "Date": [
                "2024-10-21",
                "2024-10-22",
                "2024-10-23",
                "2024-10-24",
                "2024-10-25",
                "2024-10-26",
                "2024-10-27",
                "2024-10-28",
                "2024-10-29",
                "2024-10-30",
                "2024-10-31",
                "2024-11-01",
                "2024-11-02",
                "2024-11-03"
            ]
        },
        "RequestId": "29fa069b-b83e-4e88-944f-456de8bfffcd"
    }
}
```

