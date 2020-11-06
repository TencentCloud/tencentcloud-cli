**Example 1: 修改拨测任务示例(扩展)**



Input: 

```
tccli cat ModifyTaskEx --cli-unfold-argument  \
    --AgentGroupId 100004185 \
    --CatTypeName http \
    --Url http://www.baidu.com \
    --Period 5 \
    --TaskName HelpToTestBaidu \
    --TaskId 210837 \
    --Type 2
```

Output: 
```
{
    "Response": {
        "TaskId": 210837,
        "RequestId": "b54e51f6-d6bd-4829-9d17-302b0fdd46e7"
    }
}
```

