**Example 1: 示例**

示例

Input: 

```
tccli mqtt CreateMessageEnrichmentRule --cli-unfold-argument  \
    --InstanceId mqtt-g4r4wpne \
    --RuleName rule1 \
    --Condition eyJjbGllbnRJZCI6ImNsaWVudC0xIiwidXNlcm5hbWUiOiJjbGllbnQtMSIsInRvcGljIjoiaG9tZS9yb29tMSJ9 \
    --Actions eyJtZXNzYWdlRXhwaXJ5SW50ZXJ2YWwiOjM2MCwicmVzcG9uc2VUb3BpYyI6InJlcGxpZXMvZGV2aWNlcy8ke2NsaWVudGlkfSIsImNvcnJlbGF0aW9uRGF0YSI6IiR7dHJhY2VpZH0iLCJ1c2VyUHJvcGVydHkiOlt7ImtleSI6InRyYWNlLWlkIiwidmFsdWUiOiIke3RyYWNlaWR9In1dfQ== \
    --Priority 2 \
    --Status 1 \
    --Remark remark
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Id": 6,
        "InstanceId": "mqtt-g4r4wpne",
        "RequestId": "63e5ecf1-3d79-4f28-aef3-6e7396f78dcd"
    }
}
```

