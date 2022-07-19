**Example 1: 创建数据转发**



Input: 

```
tccli iotvideo CreateDataForward --cli-unfold-argument  \
    --ProductId TOIDHQ3AOQ, \
    --ForwardAddr [{"forward":{"api":"http://127.0.0.1:1080/sub.php"}}] \
    --DataChose 0
```

Output: 
```
{
    "Response": {
        "RequestId": "be69a7a3-7315-40a7-9532-3315e4a3e97e"
    }
}
```

