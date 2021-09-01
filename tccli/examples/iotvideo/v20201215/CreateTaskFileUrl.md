**Example 1: 获取任务文件上传链接**



Input: 

```
tccli iotvideo CreateTaskFileUrl --cli-unfold-argument  \
    --ProductId ABCDE12345
```

Output: 
```
{
    "Response": {
        "Url": "https://iothub-tasktest-****",
        "FileName": "111111_ABCDE12345_1586228400",
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4a3e97e"
    }
}
```

