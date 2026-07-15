**Example 1: CreateVariable**

创建环境变量

Input: 

```
tccli adp CreateVariable --cli-unfold-argument  \
    --AppId 20************85184 \
    --Variable.DefaultFileName *****.docx \
    --Variable.DefaultValue https://qidian-qbot-test-1251316161.cos.ap-guangzhou.myqcloud.co**************441930380**************1*******************************************75147620602304.docx \
    --Variable.Description d*****  \
    --Variable.ModuleType 0 \
    --Variable.Name a*******sad \
    --Variable.Type 11 \
    --Variable.VariableId a23fe75e-76e7-43bd-b198-dc72d6b66131
```

Output: 
```
{
    "Response": {
        "VariableId": "b4d5dbd**************2b-5b4211df1631",
        "RequestId": "b37be014-f5a6-44e7-9e1a-8c4971885928"
    }
}
```

