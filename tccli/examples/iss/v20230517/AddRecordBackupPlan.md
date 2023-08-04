**Example 1: 成功**

 

Input: 

```
tccli iss AddRecordBackupPlan --cli-unfold-argument  \
    --TemplateId abcdefgh-1234-5678-ijkl-1234567890ab \
    --PlanName test-plan-1 \
    --Describe test1 \
    --LifeCycle.Transition 7 \
    --LifeCycle.Expiration 0 \
    --OrganizationId 191
```

Output: 
```
{
    "Response": {}
}
```

