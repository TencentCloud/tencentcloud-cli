**Example 1: 创建自定义物模型数据类型**



Input: 

```
tccli iotvideo CreateIotDataType --cli-unfold-argument  \
    --IotDataType {"id":"MyStruct1","name":"自定义数据结构","type":[{"name":"aaaa","id":"attr1","type":"int32"},{"name":"bbbb","id":"attr2","type":"string64"},{"name":"eeee","id":"attr3","type":[{"name":"cccc","id":"attr3_1","type":"int32"},{"name":"dddd","id":"attr3_2","type":"int32"}]},{"name":"jjjj","id":"attr4","type":[{"name":"aaaa","id":"attr4_1","type":"int32"},{"name":"bbbb","id":"attr4_2","type":"string64"},{"name":"eeee","id":"attr4_3","type":[{"name":"cccc","id":"attr4_3_1","type":"int32"},{"name":"dddd","id":"attr4_3_2","type":"int32"}]}]}]}
```

Output: 
```
{
    "Response": {
        "RequestId": "8e4a3cb2-6a8e-4858-8c08-062e9f65dca5"
    }
}
```

