**Example 1: 获取报告分类结果**



Input: 

```
tccli cii AddSubStructureTasks --cli-unfold-argument  \
    --MainTaskId Mstiljhgwglc \
    --TaskInfos.0.TaskType MedCheckReport \
    --TaskInfos.0.CustomerId 1 \
    --TaskInfos.0.CustomerName 小明 \
    --TaskInfos.0.FileList xxx.jpg yyy.jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "22dfcc05-1ba1-49b4-a751-f5611cdb3420",
        "SubTaskIds": [
            "Sr595vgwutc1",
            "Sr5fb7zin9xd"
        ]
    }
}
```

