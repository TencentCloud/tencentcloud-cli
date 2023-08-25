**Example 1: 修改最新评估风险项状态**

修改最新评估风险项状态

Input: 

```
tccli dsgc ModifyDSPAAssessmentRiskLatest --cli-unfold-argument  \
    --DspaId dspa-92aabacd \
    --RiskLatestTableId 1 \
    --Status finished
```

Output: 
```
{
    "Response": {
        "RequestId": "128009ac-7df4-0530-cc92-52f0d945e191"
    }
}
```

