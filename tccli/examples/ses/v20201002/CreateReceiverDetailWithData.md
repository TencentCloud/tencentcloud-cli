**Example 1: 添加收件人地址附带模板参数**

添加收件人地址附带模板参数

Input: 

```
tccli ses CreateReceiverDetailWithData --cli-unfold-argument  \
    --ReceiverId 123 \
    --Datas.0.Email 456@bc.com \
    --Datas.0.TemplateData {"name":"aa","age":"12"}
```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

