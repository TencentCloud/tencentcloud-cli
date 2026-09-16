**Example 1: 调用示例**



Input: 

```
tccli faceid ListEKYCWebhooks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Result": "Success",
        "TotalCount": 1,
        "WebhookList": [
            {
                "AddTime": "2026-05-19 19:41:37",
                "ModTime": "2026-05-22 20:40:20",
                "Scene": "AML_SCREENING_RESULT_CHANGE",
                "WebhookId": 49,
                "WebhookName": "webhook",
                "WebhookURL": "https://www.baidu.com"
            }
        ],
        "RequestId": "93699b85-6187-412c-97ba-22868771a63b"
    }
}
```

