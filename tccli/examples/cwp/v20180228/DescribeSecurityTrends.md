**Example 1: 获取安全事件统计数据**

获取安全事件统计数据。

Input: 

```
tccli cwp DescribeSecurityTrends --cli-unfold-argument  \
    --BeginDate 2020-06-20 \
    --EndDate 2020-06-22
```

Output: 
```
{
    "Response": {
        "ReverseShells": [
            {
                "Date": "2020-09-22",
                "EventNum": 1
            }
        ],
        "NonLocalLoginPlaces": [
            {
                "Date": "2020-09-22",
                "EventNum": 1
            }
        ],
        "MaliciousRequests": [
            {
                "Date": "2020-09-22",
                "EventNum": 1
            }
        ],
        "Vuls": [
            {
                "Date": "2020-09-22",
                "EventNum": 1
            }
        ],
        "PrivilegeEscalations": [
            {
                "Date": "2020-09-22",
                "EventNum": 1
            }
        ],
        "Malwares": [
            {
                "Date": "2020-09-22",
                "EventNum": 1
            }
        ],
        "RequestId": "xx",
        "BruteAttacks": [
            {
                "Date": "2020-09-22",
                "EventNum": 1
            }
        ],
        "BaseLines": [
            {
                "Date": "2020-09-22",
                "EventNum": 1
            }
        ],
        "CyberAttacks": [
            {
                "Date": "2020-09-22",
                "EventNum": 1
            }
        ],
        "HighRiskBashs": [
            {
                "Date": "2020-09-22",
                "EventNum": 1
            }
        ]
    }
}
```

