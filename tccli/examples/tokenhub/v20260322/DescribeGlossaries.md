**Example 1: DescribeGlossaries**



Input: 

```
tccli tokenhub DescribeGlossaries --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Current": 0,
        "Items": [
            {
                "CreatedTime": "2026-03-01T00:00:00Z",
                "Description": "syytest",
                "GlossaryId": "fc88eea3787c6fb1a7404b65e2c25cac",
                "Name": "syytest-glossary",
                "Source": "zh",
                "Target": "en",
                "UpdatedTime": "2026-03-01T00:00:00Z"
            }
        ],
        "PageSize": 20,
        "RequestId": "381ee90c-4f9a-499f-a1fe-0888593f7337",
        "TotalCount": 1
    }
}
```

