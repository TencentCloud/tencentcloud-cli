**Example 1: 获取prompt任务详情**

获取prompt任务详情

Input: 

```
tccli hai DescribeMuskPrompts --cli-unfold-argument  \
    --WorkgroupId 4a3f3be9-f35b-40bf-b6bb-2af812dd63cb \
    --WorkflowId wf-b9dbb48a-f4cd-40f3-9a68-2af4c78d31a7 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "MuskPromptInfos": [
            {
                "CreateTime": "2024-12-24 12:07:22",
                "OutputResource": [],
                "PromptId": "edc6e6ec-072c-41dd-8672-c956b739fd31",
                "Status": 2,
                "UpdateTime": "2024-12-24 12:09:22",
                "WorkflowId": "wf-b9dbb48a-f4cd-40f3-9a68-2af4c78d31a7",
                "WorkgroupId": "4a3f3be9-f35b-40bf-b6bb-2af812dd63cb"
            }
        ],
        "RequestId": "a8a7930a-b642-4a3e-a3df-2d4a6bd389cc",
        "TotalCount": 1
    }
}
```

