**Example 1: 更新数据集**



Input: 

```
tccli tsf ModifyProgram --cli-unfold-argument  \
    --ProgramId program-6a79x94v \
    --ProgramName program-mock \
    --ProgramDesc this is a desc \
    --ProgramItemList.0.ProgramItemId prog-item-6a79x94v \
    --ProgramItemList.0.Resource.ResourceId resource-6a79x94v \
    --ProgramItemList.0.Resource.ResourceCode code-mock \
    --ProgramItemList.0.Resource.ResourceName name-mock \
    --ProgramItemList.0.Resource.ServiceCode code-mock \
    --ProgramItemList.0.Resource.ResourceAction Action \
    --ProgramItemList.0.Resource.DeleteFlag True \
    --ProgramItemList.0.Resource.ResourceDesc this is a desc \
    --ProgramItemList.0.Resource.CanSelectAll True \
    --ProgramItemList.0.Resource.SearchWordField programId \
    --ProgramItemList.0.Resource.Index 0 \
    --ProgramItemList.0.ValueList value1 \
    --ProgramItemList.0.IsAll True \
    --ProgramItemList.0.DeleteFlag True \
    --ProgramItemList.0.ProgramId program-6a79x94v \
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

