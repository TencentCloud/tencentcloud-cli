**Example 1: 使用字段模板批量创建合同智能提取任务**



Input: 

```
tccli ess CreateBatchInformationExtractionTask --cli-unfold-argument  \
    --Operator.UserId yDx************************xxx \
    --ResourceIds yDx************************acc \
    --FieldTemplateId yDx************************yyy
```

Output: 
```
{
    "Response": {
        "TaskIds": [
            "yDx************************ddd"
        ],
        "RequestId": "s1735294966632123121"
    }
}
```

