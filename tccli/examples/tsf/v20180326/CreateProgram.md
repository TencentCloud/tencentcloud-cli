**Example 1: 创建数据集**



Input: 

```
tccli tsf CreateProgram --cli-unfold-argument  \
    --ProgramName program-test \
    --ProgramDesc this is a description \
    --ProgramItemList.0.ProgramItemId program-6a79x94v \
    --ProgramItemList.0.Resource.ResourceId resource-6a79x94v \
    --ProgramItemList.0.Resource.ResourceCode resourceCode \
    --ProgramItemList.0.Resource.ResourceName name-test \
    --ProgramItemList.0.Resource.ServiceCode mock-service \
    --ProgramItemList.0.Resource.ResourceAction TestAction \
    --ProgramItemList.0.Resource.IdField progaramId \
    --ProgramItemList.0.Resource.NameField programName \
    --ProgramItemList.0.Resource.SelectIdsField programId \
    --ProgramItemList.0.Resource.CreationTime 0 \
    --ProgramItemList.0.Resource.LastUpdateTime 0 \
    --ProgramItemList.0.Resource.DeleteFlag True \
    --ProgramItemList.0.Resource.ResourceDesc this is a desc \
    --ProgramItemList.0.Resource.CanSelectAll True \
    --ProgramItemList.0.Resource.SearchWordField programName \
    --ProgramItemList.0.Resource.Index 0 \
    --ProgramItemList.0.ValueList abc \
    --ProgramItemList.0.IsAll True \
    --ProgramItemList.0.CreationTime 0 \
    --ProgramItemList.0.LastUpdateTime 0 \
    --ProgramItemList.0.DeleteFlag True \
    --ProgramItemList.0.ProgramId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "3b15ccd0-650a-4d9a-96d4-db8a55579d38",
        "Result": true
    }
}
```

