**Example 1: 校验用户是否已经加到TCLake用户列表**

在创建catalog资源前，需要进行校验

Input: 

```
tccli tccatalog CheckUserExists --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Exists": true,
        "RequestId": "0c15128e-74fc-4889-afaf-20697b1a2bce"
    }
}
```

