**Example 1: 成功调用**



Input: 

```
tccli wedata AddCalcEnginesToProject --cli-unfold-argument  \
    --ProjectId 2916098084817846272 \
    --DLCInfo.0.ComputeResources dlc_linau6d4bu8bd5u52ffu52a8 \
    --DLCInfo.0.Region ap-guangzhou \
    --DLCInfo.0.DefaultDatabase lgx_test_0825
```

Output: 
```
{
    "Response": {
        "RequestId": "eacab638-a5bc-4f23-8284-ac09cde185e5"
    }
}
```

