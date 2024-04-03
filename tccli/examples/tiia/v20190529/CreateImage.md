**Example 1: 调用成功**



Input: 

```
tccli tiia CreateImage --cli-unfold-argument  \
    --CustomContent custom \
    --ImageUrl http://www.test.com/a.jpg \
    --EntityId 456 \
    --GroupId hello \
    --PicName 456
```

Output: 
```
{
    "Response": {
        "Object": {
            "Box": {
                "Score": 0,
                "Rect": {
                    "Y": 0,
                    "X": 0,
                    "Height": 0,
                    "Width": 0
                }
            },
            "CategoryId": 0
        },
        "RequestId": "da8eedd6-5977-4db8-9334-3b6b190e242b"
    }
}
```

**Example 2: 调用成功示例**



Input: 

```
tccli tiia CreateImage --cli-unfold-argument  \
    --GroupId 123 \
    --EntityId 1 \
    --PicName 1 \
    --ImageUrl http://www.test.com/a.jpg \
    --CustomContent test \
    --Tags {"k": "123"}
```

Output: 
```
{
    "Response": {
        "Object": {
            "Box": {
                "Score": 0,
                "Rect": {
                    "Y": 0,
                    "X": 0,
                    "Height": 0,
                    "Width": 0
                }
            },
            "CategoryId": 0
        },
        "RequestId": "da8eedd6-5977-4db8-9334-3b6b190e242b"
    }
}
```

