**Example 1: 修改dspm数据识别模板**



Input: 

```
tccli csip ModifyDspmIdentifyComplianceGroup --cli-unfold-argument  \
    --Name kyrie修改 \
    --Id 10001 \
    --MemberId mem-12edwq32 \
    --Description 2 \
    --Status 1
```

Output: 
```
{
    "Response": {
        "RequestId": "1b241fd1-2899-45b1-abb0-289b9af54f95"
    }
}
```

