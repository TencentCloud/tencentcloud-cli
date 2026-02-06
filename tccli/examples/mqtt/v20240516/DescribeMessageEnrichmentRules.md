**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeMessageEnrichmentRules --cli-unfold-argument  \
    --InstanceId mqtt-g4r4wpne
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "Actions": "eyJ1c2VyUHJvcGVydHkiOiBbeyJrZXkiOiAidHJhY2UtaWQiLCAidmFsdWUiOiAiJHt0cmFjZWlkfSJ9XSwgInJlc3BvbnNlVG9waWMiOiAicmVwbGllcy9kZXZpY2VzLyR7Y2xpZW50aWR9IiwgImNvcnJlbGF0aW9uRGF0YSI6ICIke3RyYWNlaWR9IiwgIm1lc3NhZ2VFeHBpcnlJbnRlcnZhbCI6IDM2MH0=",
                "Condition": "eyJ0b3BpYyI6ICJob21lL3Jvb20xIiwgImNsaWVudElkIjogImNsaWVudC0xIiwgInVzZXJuYW1lIjogImNsaWVudC0xIn0=",
                "CreatedTime": 1763347106093,
                "Id": 5,
                "InstanceId": "mqtt-g4r4wpne",
                "Priority": 1,
                "Remark": "remark",
                "RuleName": "rule1",
                "Status": 1,
                "UpdateTime": 1763347106093
            },
            {
                "Actions": "eyJ1c2VyUHJvcGVydHkiOiBbeyJrZXkiOiAidHJhY2UtaWQiLCAidmFsdWUiOiAiJHt0cmFjZWlkfSJ9XSwgInJlc3BvbnNlVG9waWMiOiAicmVwbGllcy9kZXZpY2VzLyR7Y2xpZW50aWR9IiwgImNvcnJlbGF0aW9uRGF0YSI6ICIke3RyYWNlaWR9IiwgIm1lc3NhZ2VFeHBpcnlJbnRlcnZhbCI6IDM2MH0=",
                "Condition": "eyJ0b3BpYyI6ICJob21lL3Jvb20xIiwgImNsaWVudElkIjogImNsaWVudC0xIiwgInVzZXJuYW1lIjogImNsaWVudC0xIn0=",
                "CreatedTime": 1763347249927,
                "Id": 6,
                "InstanceId": "mqtt-g4r4wpne",
                "Priority": 2,
                "Remark": "remark",
                "RuleName": "rule2",
                "Status": 1,
                "UpdateTime": 1763347388148
            }
        ],
        "RequestId": "6e898343-e911-49de-8491-f23108edd157"
    }
}
```

