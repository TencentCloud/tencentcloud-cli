**Example 1: 成功**



Input: 

```
tccli adp SaveWorkflowToolNodeOutput --cli-unfold-argument  \
    --CallbackToken wfr-ee494028-1f91-4cf2-89ab-f04e052b9f52..91b257f7-5145-a013-0b32-0a651ce0b18b.1784201278.be167a5ddddf0779e7b362cef7024771d54c321ae3ba8cbf0eac124616044591 \
    --Result {\"approval_result\":\"approved\",\"approver\":\"张三\",\"comment\":\"同意\"}
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Msg": "ok",
        "RequestId": "a80d6038-9fdd-4df6-967f-6dd3ccc44fc6"
    }
}
```

