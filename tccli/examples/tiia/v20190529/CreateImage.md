**Example 1: 调用成功示例**



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
        "RequestId": "cac925c7-c939-4eb6-8db5-d642f7385c30"
    }
}
```

**Example 2: 调用成功**



Input: 

```
tccli tiia CreateImage --cli-unfold-argument  \
    --CustomContent custom \
    --ImageUrl https://img1.gtimg.com/chinanba/pics/hv1/86/220/2312/150393986.jpg \
    --EntityId 456 \
    --GroupId hello \
    --PicName 456
```

Output: 
```
{
    "Response": {
        "RequestId": "da8eedd6-5977-4db8-9334-3b6b190e242b"
    }
}
```

