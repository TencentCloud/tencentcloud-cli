**Example 1: 查询自定义物模型数据类型**



Input: 

```
tccli iotvideo DescribeIotDataType --cli-unfold-argument  \
    --TypeId MyStruct
```

Output: 
```
{
    "Response": {
        "RequestId": "3cfe291c-e6e8-475e-b9c4-bd29abaab262",
        "Data": [
            "{\"id\":\"MyStruct\",\"name\":\"自定义数据结构\",\"type\":[{\"name\":\"aaaa\",\"id\":\"attr1\",\"type\":\"int32\"},{\"name\":\"bbbb\",\"id\":\"attr2\",\"type\":\"string64\"},{\"name\":\"eeee\",\"id\":\"attr3\",\"type\":[{\"name\":\"cccc\",\"id\":\"attr3_1\",\"type\":\"int32\"},{\"name\":\"dddd\",\"id\":\"attr3_2\",\"type\":\"int32\"}]},{\"name\":\"jjjj\",\"id\":\"attr4\",\"type\":[{\"name\":\"aaaa\",\"id\":\"attr4_1\",\"type\":\"int32\"},{\"name\":\"bbbb\",\"id\":\"attr4_2\",\"type\":\"string64\"},{\"name\":\"eeee\",\"id\":\"attr4_3\",\"type\":[{\"name\":\"cccc\",\"id\":\"attr4_3_1\",\"type\":\"int32\"},{\"name\":\"dddd\",\"id\":\"attr4_3_2\",\"type\":\"int32\"}]}]}]}"
        ]
    }
}
```

