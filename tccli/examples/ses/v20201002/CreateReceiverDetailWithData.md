**Example 1: 添加收件人地址附带模板参数**

添加收件人地址附带模板参数

Input: 

```
tccli ses CreateReceiverDetailWithData --cli-unfold-argument  \
    --ReceiverId 123 \
    --Datas.0.Email example@gmail.com \
    --Datas.0.TemplateData {"name":"john","age":"12"}
```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

