**Example 1: 上传合同并新增**

上传合同并新增

Input: 

```
tccli ds CreateContractByUpload --cli-unfold-argument  \
    --Module ContractMng \
    --Operation CreateContractByUpload \
    --ContractFile https://cloud.tencent.com/ \
    --ContractName test \
    --Remarks test \
    --Initiator dcu-c33uil4ap6 \
    --SignInfos.0.AccountResId dcu-c33uil4ap6
```

Output: 
```
{
    "Response": {
        "RequestId": "1cf1946c-5fb1-4eaa-8fdf-49ba755fd798",
        "TaskId": 1
    }
}
```

