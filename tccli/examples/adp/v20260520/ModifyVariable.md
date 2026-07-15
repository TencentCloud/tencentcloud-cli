**Example 1: ModifyVariable**

修改应用

Input: 

```
tccli adp ModifyVariable --cli-unfold-argument  \
    --AppId 206***********85184 \
    --Variable.DefaultFileName 1.doc \
    --Variable.DefaultValue https://qidian-qbot-test-1251316161.cos.ap-guangzhou.myqcloud.com/public/174454419303809*********2**7********184/ima*****************************751476*******4*d*c* \
    --Variable.Description d**** \
    --Variable.ModuleType 0 \
    --Variable.Name d********cv \
    --Variable.Type 11 \
    --Variable.VariableId b4d5dbd1-f090-4323-bf2b-5b4211df1631
```

Output: 
```
{
    "Response": {
        "RequestId": "ea194623-1b38-423d-944e-61c9daf4a61b"
    }
}
```

