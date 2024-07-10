**Example 1: 更新数据集**



Input: 

```
tccli tsf ModifyProgram --cli-unfold-argument  \
    --ProgramId abc \
    --ProgramName abc \
    --ProgramDesc abc \
    --ProgramItemList.0.ProgramItemId abc \
    --ProgramItemList.0.Resource.ResourceId abc \
    --ProgramItemList.0.Resource.ResourceCode abc \
    --ProgramItemList.0.Resource.ResourceName abc \
    --ProgramItemList.0.Resource.ServiceCode abc \
    --ProgramItemList.0.Resource.ResourceAction abc \
    --ProgramItemList.0.Resource.IdField abc \
    --ProgramItemList.0.Resource.NameField abc \
    --ProgramItemList.0.Resource.SelectIdsField abc \
    --ProgramItemList.0.Resource.CreationTime 0 \
    --ProgramItemList.0.Resource.LastUpdateTime 0 \
    --ProgramItemList.0.Resource.DeleteFlag True \
    --ProgramItemList.0.Resource.ResourceDesc abc \
    --ProgramItemList.0.Resource.CanSelectAll True \
    --ProgramItemList.0.Resource.SearchWordField abc \
    --ProgramItemList.0.Resource.Index 0 \
    --ProgramItemList.0.ValueList abc \
    --ProgramItemList.0.IsAll True \
    --ProgramItemList.0.CreationTime 0 \
    --ProgramItemList.0.LastUpdateTime 0 \
    --ProgramItemList.0.DeleteFlag True \
    --ProgramItemList.0.ProgramId abc \
    --EmptyProgramItemList True
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

